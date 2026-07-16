import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# 1. טעינת הנתונים
# ==============================
df = pd.read_csv("labeling_data.csv")


df = df[df["source_dataset"] == "asvspoof"]

print("Total samples after filtering (asvspoof):", len(df))

# ==============================
# 2. התפלגות מחלקות
# ==============================
print("\n=== Label Distribution ===")
counts = df["label"].value_counts()
print(counts)

print("\nPercentages:")
print(df["label"].value_counts(normalize=True) * 100)

# גרף
counts.plot(kind='bar')
plt.title("Label Distribution (vcc2021)")
plt.xlabel("Label")
plt.ylabel("Count")
plt.show()

# ==============================
# 3. כפילויות
# ==============================
duplicate_ids = df[df.duplicated(subset="recording_id")]
print("\nNumber of duplicate recording_id:", len(duplicate_ids))

# בדיקת סתירות (אותו ID עם real + fake)
conflicts = df.groupby("recording_id")["label"].nunique()
conflicts = conflicts[conflicts > 1]

print("Conflicting labels:", len(conflicts))

# ==============================
# 4. סוגי התקפות
# ==============================
print("\n=== Attack Types ===")
print(df["attack_type"].value_counts())

print("\nUnique attack types:")
print(df["attack_type"].unique())

# גרף
df["attack_type"].value_counts().plot(kind='bar')
plt.title("Attack Types Distribution")
plt.xticks(rotation=45)
plt.show()

# ==============================
# 5. התפלגות זיופים בלבד
# ==============================
spoof_df = df[df["label"] == "spoof"]

attack_distribution = spoof_df["attack_type"].value_counts(normalize=True) * 100

print("\n=== Attack Distribution (Spoof Only) ===")
print(attack_distribution)

# ==============================
# 6. unknown analysis
# ==============================
print("\n=== Unknown attack_type ===")
print(df[df["attack_type"] == "unknown"]["label"].value_counts())

# ==============================
# 7. מקור הדאטה 
# ==============================
print("\n=== Source Dataset Check ===")
print(df["source_dataset"].value_counts())

# ==============================
# 8. סוג דחיסה
# ==============================
if "compression_type" in df.columns:
    print("\n=== Compression Types ===")
    print(df["compression_type"].value_counts())

    df["compression_type"].value_counts().plot(kind='bar')
    plt.title("Compression Types")
    plt.show()

# ==============================
# 9. בדיקת ערכים חסרים
# ==============================
print("\n=== Missing Values ===")
print(df.isnull().sum())

# ==============================
# 10.  אורך הקלטות
# ==============================
import librosa

durations = []


if "file_path" in df.columns:
    sample_df = df.sample(min(200, len(df))) 

    for path in sample_df["file_path"]:
        try:
            y, sr = librosa.load(path, sr=None)
            durations.append(len(y) / sr)
        except:
            continue

    if len(durations) > 0:
        print("\n=== Audio Duration Stats ===")
        print(pd.Series(durations).describe())

        plt.hist(durations, bins=30)
        plt.title("Audio Duration Distribution")
        plt.xlabel("Seconds")
        plt.ylabel("Count")
        plt.show()
