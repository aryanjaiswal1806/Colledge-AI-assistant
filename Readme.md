# 🎓 College AI Assistant

An AI-powered College Student Information Assistant built using Python, SQLite, and Hugging Face. It helps users access student information, check attendance, view academic marks, and ask questions to an AI assistant.

## ✨ Features

- 👨‍🎓 **Student Information:** Search students by roll number.
- 📊 **Attendance Management:** Check student attendance percentages.
- 📝 **Academic Marks:** View students' marks.
- 🤖 **AI Assistant:** Ask questions using a Hugging Face language model.
- 🗄️ **SQLite Database:** Store student records locally.
- 🔐 **Environment Variables:** Keep API tokens in a `.env` file.
- 🖥️ **Simple Interface:** Use an easy-to-understand terminal menu.

## 🛠️ Technologies Used

- Python
- SQLite
- Hugging Face Inference API
- `huggingface_hub`
- `python-dotenv`

## 📁 Project Structure

```text
College-AI-Assistant/
│
├── app.py
├── .env
├── .gitignore
├── college.db
└── README.md
```

**Note:** The `.env` and `college.db` files are local files and should not be uploaded to GitHub.

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd College-AI-Assistant
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on