import sqlite3
from datetime import datetime
import pandas as pd

DB_PATH = "database/final_project_database.db"


def get_connection():
    return sqlite3.connect(DB_PATH)


def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        recording_id TEXT,
        filename TEXT,
        prediction TEXT,
        risk_level TEXT,
        confidence REAL,
        real_probability REAL,
        fake_probability REAL,
        model_name TEXT,
        processing_time REAL,
        created_at TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_prediction(recording_id, filename, prediction, risk_level, confidence,
                      real_probability, fake_probability, model_name, processing_time):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO predictions (
        recording_id, filename, prediction, risk_level, confidence,
        real_probability, fake_probability, model_name, processing_time, created_at
    )
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        recording_id,
        filename,
        prediction,
        risk_level,
        confidence,
        real_probability,
        fake_probability,
        model_name,
        processing_time,
        datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def get_history():
    conn = get_connection()

    df = pd.read_sql_query("""
        SELECT
            recording_id AS "Recording ID",
            filename AS "File Name",
            prediction AS "Prediction",
            risk_level AS "Risk Level",
            confidence AS "Confidence",
            model_name AS "Model",
            processing_time AS "Processing Time",
            created_at AS "Date"
        FROM predictions
        ORDER BY id DESC
    """, conn)

    conn.close()
    return df


def get_statistics():
    conn = get_connection()
    df = pd.read_sql_query("SELECT * FROM predictions", conn)
    conn.close()

    if df.empty:
        return {
            "total": 0,
            "real": 0,
            "fake": 0,
            "avg_confidence": 0,
            "avg_processing_time": 0
        }

    return {
        "total": len(df),
        "real": len(df[df["prediction"] == "Real"]),
        "fake": len(df[df["prediction"] == "Spoof Detected"]),
        "avg_confidence": round(df["confidence"].mean(), 2),
        "avg_processing_time": round(df["processing_time"].mean(), 3)
    }


def clear_history():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM predictions")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='predictions'")
    conn.commit()
    conn.close()