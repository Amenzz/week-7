
import os
import json
import psycopg2
from dotenv import load_dotenv
from glob import glob

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD"),
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT")
)

cursor = conn.cursor()

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)
        for msg in data:
            cursor.execute("""
                INSERT INTO raw.telegram_messages (data, filename)
                VALUES (%s, %s)
            """, [json.dumps(msg), os.path.basename(path)])

    conn.commit()

def main():
    files = glob("data/raw/telegram_messages/**/*.json", recursive=True)
    for f in files:
        print(f"Loading {f}")
        load_file(f)

    print("Done.")

if __name__ == "__main__":
    main()
