import os
import random
import shutil

# תיקיית מקור עם כל ההקלטות
source_folder = "/Users/karinapisarenko/Desktop/Karina/project/dataset_hebrew/he/clips"

# תיקיית יעד
target_folder = "/Users/karinapisarenko/Desktop/Karina/project/dataset_hebrew/he/selected"

# כמות הקבצים 
N = 1108

# יצירת תיקיית יעד אם לא קיימת
os.makedirs(target_folder, exist_ok=True)

# רשימת כל הקבצים
files = [f for f in os.listdir(source_folder) if f.endswith(".wav") or f.endswith(".flac") or f.endswith(".mp3")]

print("סה״כ קבצים בתיקייה:", len(files))

# בחירה אקראית
selected_files = random.sample(files, N)

# העתקה
for file in selected_files:
    src = os.path.join(source_folder, file)
    dst = os.path.join(target_folder, file)
    shutil.copy(src, dst)

print("הועתקו", len(selected_files), "קבצים")
