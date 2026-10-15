

import os
import sqlite3
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

# Database setup
con = sqlite3.connect("college.db")
con.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll INTEGER PRIMARY KEY,
    name TEXT,
    branch TEXT,
    attendance REAL,
    marks REAL
)
""")

con.executemany("""
INSERT OR IGNORE INTO students VALUES(?,?,?,?,?)
""", [
    (101, "Abhishek", "CSE", 85, 90),
    (102, "Rahul", "CSE", 70, 75),
])
con.commit()


def search_student(roll):
    return con.execute(
        "SELECT * FROM students WHERE roll=?", (roll,)
    ).fetchone()


def ask_ai(question):
    token = os.getenv("HF_TOKEN")

    if not token:
        print("Please add HF_TOKEN to your .env file.")
        return

    try:
        client = InferenceClient(
            api_key=token,
            provider="auto"
        )

        response = client.chat.completions.create(
            model="Qwen/Qwen2.5-7B-Instruct",
            messages=[
                {
                    "role": "system",
                    "content": (
                        "You are a helpful college assistant. "
                        "Never invent student records."
                    )
                },
                {"role": "user", "content": question}
            ],
            max_tokens=300
        )

        print("\nAI:", response.choices[0].message.content)

    except Exception as e:
        print("AI Error:", e)


# Main menu
while True:
    print("\n===== COLLEGE AI ASSISTANT =====")
    print("1. Search Student")
    print("2. Check Attendance")
    print("3. Check Marks")
    print("4. Ask AI")
    print("5. Exit")

    choice = input("Enter choice: ").strip()

    if choice in ("1", "2", "3"):
        try:
            roll = int(input("Enter roll number: "))
            student = search_student(roll)

            if not student:
                print("Student not found!")
                continue

            if choice == "1":
                print("Roll Number:", student[0])
                print("Name:", student[1])
                print("Branch:", student[2])

            elif choice == "2":
                print("Attendance:", student[3], "%")

            elif choice == "3":
                print("Marks:", student[4])

        except ValueError:
            print("Please enter a valid roll number.")

    elif choice == "4":
        question = input("Ask your question: ")
        ask_ai(question)

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")

con.close()