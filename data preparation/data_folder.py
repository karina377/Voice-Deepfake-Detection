import pandas as pd
from pathlib import Path
import shutil

# =======================
# נתיבים שלך
# =======================
CSV_PATH = "labeling_data.csv"
AUDIO_DIR = Path("ASVspoof2021_DF_eval/flac")  # תיקיית ה-FLAC
OUT_DIR = Path("balanced_from_eval")           # יצירת דאטה חדש כאן
#balanced data <-
# =======================
# הגדרות איזון
# =======================
RANDOM = 42

# אם אצלך יש בדיוק 5 סוגים כמו שהראית:
ATTACK_TYPES = [
    "traditional_vocoder",
    "neural_vocoder_autoregressive",
    "neural_vocoder_nonautoregressive",
    "waveform_concatenation",
    "unknown"
]

# =======================
# 1) טעינת ה-CSV
# =======================
df = pd.read_csv(CSV_PATH)

# ודאות טיפוסים
df["recording_id"] = df["recording_id"].astype(str)
df["label"] = df["label"].astype(str)

# =======================
# 2) בניית רשימת קבצים שקיימים בתיקיית AUDIO_DIR
# =======================
existing = {p.stem: p for p in AUDIO_DIR.rglob("*.flac")}

print("Audio files found in AUDIO_DIR:", len(existing))

# =======================
# 3) סינון ל-IDs שקיימים בפועל בתיקייה
# =======================
df_in_dir = df[df["recording_id"].isin(existing.keys())].copy()

print("Rows in CSV that exist in AUDIO_DIR:", len(df_in_dir))
print("\nLabel distribution BEFORE balancing:")
print(df_in_dir["label"].value_counts())

# =======================
# 4) איזון bonafide/spoof + איזון attack_type בתוך spoof
# =======================
bon = df_in_dir[df_in_dir["label"] == "bonafide"].copy()
spo = df_in_dir[df_in_dir["label"] == "spoof"].copy()

# לוודא שיש attack_type לזיופים
if "attack_type" not in df_in_dir.columns:
    raise ValueError("CSV חייב להכיל עמודה attack_type כדי לאזן לפי סוגי תקיפה.")

# כמה יש לכל attack_type בתוך הסינון
spo_counts = spo["attack_type"].value_counts()
print("\nSpoof attack counts available (in AUDIO_DIR):")
print(spo_counts)

# המגבלה: מינימום מכל סוג תקיפה (כדי להיות שווה)
min_attack = min(int(spo_counts.get(a, 0)) for a in ATTACK_TYPES)

if min_attack == 0:
    missing = [a for a in ATTACK_TYPES if int(spo_counts.get(a, 0)) == 0]
    raise ValueError(f"חסרים אצלך בתיקייה סוגי תקיפה: {missing}. אי אפשר לאזן באופן שווה בלי הדוגמאות הללו.")

max_spoof_balanced = min_attack * len(ATTACK_TYPES)

# כדי להיות 50-50, N מוגבל גם ע"י bonafide וגם ע"י spoof המאוזן
N = min(len(bon), max_spoof_balanced)

# כמה מכל attack_type
per_attack = N // len(ATTACK_TYPES)

print("\nChosen N per label (bonafide & spoof):", N)
print("Per attack_type in spoof:", per_attack)
print("Total balanced size:", 2 * N)

# דגימה שווה מכל attack_type
spo_parts = []
for i, atk in enumerate(ATTACK_TYPES):
    sub = spo[spo["attack_type"] == atk]
    spo_parts.append(sub.sample(n=per_attack, random_state=RANDOM + i))

spo_bal = pd.concat(spo_parts)

# השלמה אם חסר בגלל חלוקה שלמה
need = N - len(spo_bal)
if need > 0:
    extra_pool = spo.drop(spo_bal.index, errors="ignore")
    extra = extra_pool.sample(n=need, random_state=999)
    spo_bal = pd.concat([spo_bal, extra])

# bonafide דוגמים N
bon_bal = bon.sample(n=N, random_state=RANDOM)

# איחוד ושמירה ל-CSV
balanced = pd.concat([bon_bal, spo_bal]).sample(frac=1, random_state=RANDOM).copy()

print("\nLabel distribution AFTER balancing:")
print(balanced["label"].value_counts())

print("\nSpoof attack distribution AFTER balancing:")
print(balanced[balanced["label"] == "spoof"]["attack_type"].value_counts())

OUT_DIR.mkdir(parents=True, exist_ok=True)
balanced_csv_path = OUT_DIR / "balanced_dataset.csv"
balanced.to_csv(balanced_csv_path, index=False)
print("\nSaved CSV:", balanced_csv_path)

# =======================
# 5) העתקת הקבצים לתיקייה חדשה לפי תיוג
#    מבנה מוצע:
#    balanced_from_eval/
#       real/
#       fake/<attack_type>/
# =======================
real_dir = OUT_DIR / "real"
fake_dir = OUT_DIR / "fake"

real_dir.mkdir(parents=True, exist_ok=True)
fake_dir.mkdir(parents=True, exist_ok=True)

missing_files = []

for _, row in balanced.iterrows():
    rid = str(row["recording_id"])
    src = existing.get(rid)

    if src is None:
        missing_files.append(rid)
        continue

    if row["label"] == "bonafide":
        dst = real_dir / src.name
    else:
        atk = str(row["attack_type"])
        atk_dir = fake_dir / atk
        atk_dir.mkdir(parents=True, exist_ok=True)
        dst = atk_dir / src.name

    shutil.copy2(src, dst)

print("\nDone copying files.")
print("Missing files (should be 0):", len(missing_files))
if missing_files:
    print("Example missing IDs:", missing_files[:10])

print("\nOutput folder created at:", OUT_DIR.resolve())
