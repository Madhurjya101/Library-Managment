# 📚 Saraswati Library Management System (CLI)

A menu-driven **Library Management System** built using **Python**, focused on **Object-Oriented Programming (OOP)** and **JSON-based persistent storage**.

This command-line application allows users to manage library books efficiently while permanently storing data in a structured JSON format.

---

## ✨ Features

- Add new books with a unique Book ID  
- Prevent duplicate Book IDs  
- Search books by Book ID  
- View all available books  
- Update book title and author  
- Delete books by Book ID  
- Persistent data storage using `books.json`  
- Input validation and exception handling  

---

## 🧠 Concepts Used

- Object-Oriented Programming (OOP)
- Classes and Objects
- Constructors (`__init__`)
- Class methods (`@classmethod`)
- Data serialization using `to_dict()`
- Data deserialization using `from_dict()`
- JSON file handling (`json.load`, `json.dump`)
- Exception handling
- Menu-driven CLI application logic

---

## 🗂 Project Structure

```
Library-Management/
│
├── library.py
├── books.json  (auto-generated after first run)
└── README.md
```

---

## ▶️ How to Run

1. Make sure Python 3 is installed on your system  
2. Clone this repository:

```bash
git clone https://github.com/your-username/Library-Management.git
```

3. Navigate into the project folder:

```bash
cd Library-Management
```

4. Run the program:

```bash
python library.py
```

---

## 💾 Data Storage

All book data is stored in `books.json` using structured JSON format.

- Objects are converted to dictionaries before saving.
- Dictionaries are converted back to objects when loading.

This ensures clean separation between:
- **Storage format (JSON)**
- **Program objects (Book class instances)**

---

## 🔄 Future Improvements

- Add book borrowing system
- Add student/user management
- Add due date tracking
- Convert CLI to GUI
- Integrate SQLite database
- Add logging system

---

## 📌 Notes

- `books.json` is automatically created after the first book is added.
- It is recommended to add `books.json` to `.gitignore` to avoid committing data files.

Example `.gitignore`:

```
books.json
__pycache__/
```

---

## 👨‍💻 Author

**Madhurjya Mandit Nath**  
Class 9 | Python Learner  

---

⭐ If you like this project, feel free to fork, improve, or suggest enhancements!


