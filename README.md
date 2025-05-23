# 📝 Simple Tasks App

**Simple Tasks App** is a command-line task manager built with Python and PostgreSQL. It allows users to add, list, update, and delete tasks — all stored in a database with persistent status control.

---

## 📦 Features

- ✅ Add new tasks  
- 📋 List all tasks sorted by ID  
- 🔄 Change task status (`Active`, `Inactive`, `Completed`)  
- ❌ Delete tasks by ID  
- 🔃 Automatically reorder IDs after deletion  
- 🕐 Timestamp when a task is created  

---

## ⚙️ Technologies

- Python 3
- PostgreSQL
- `psycopg2` library for database connection
- ANSI color codes for terminal output
- Custom terminal screen clearer (`Clear` module)

---

## 🛠️ Requirements

- Python 3 installed
- PostgreSQL installed and running
- A database with the following table:

```sql
CREATE TABLE to_do_list (
    id SERIAL PRIMARY KEY,
    to_do TEXT NOT NULL,
    status TEXT NOT NULL,
    entry_time TEXT
);

🚀 How to Run

    Clone this repository:

git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

    Install dependencies:

pip install psycopg2

    Update the database credentials in the script:

conn = psycopg2.connect(
    dbname="project",
    user="postgres",
    password="YOUR_PASSWORD",
    host="localhost",
    port="5432"
)

    Run the app:

python3 main.py

📷 Example Output

--- Simple Tasks App ---
[1] Add Task
[2] List all tasks
[3] Exit

Select an option: 2

List of tasks
--------
[1] Wash dishes / Active / 10:02:14
[2] Study Python / Completed / 10:05:40
[3] Send resume / Inactive / 11:00:02

🧹 Screen Clear Module

The app uses a small utility module (clear.py) to clean the terminal screen:

import os

class Clear:
    def __init__(self):
        os.system('cls' if os.name == 'nt' else 'clear')

🔧 Possible Improvements

Support for tags or categories

Filter tasks by status

Web interface using Flask or FastAPI

    Add task priority levels

Feel free to fork and improve this project! 🚀