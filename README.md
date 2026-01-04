# Expense Tracker v6

A command-line Expense Tracker built in **pure Python**, focused on **logic, clarity, and real practice** rather than frameworks or tutorials.

This project was written **from scratch**, using a procedural approach, and serves as the final version before a clean OOP redesign in v7.

---

## 🎯 Project Goals

* Practice real-world Python logic
* Design a multi-feature CLI program
* Handle user input safely and consistently
* Separate concerns across multiple modules
* Build confidence without tutorial dependency

---

## 🧠 Key Learning Focus

* Input validation and normalization
* Data aggregation and statistics
* Modular program design
* Debugging through reasoning, not copying
* Designing functions based on real usage (main-driven refactoring)

---

## 📂 Project Structure

```
expense_tracker_v6/
│
├── main.py              # Program entry point & menu
├── expense_input.py     # All user input & validation
├── calculations.py      # Price calculations & statistics
├── storage.py           # JSON save/load logic
├── utility.py           # Search tools & helpers
└── expense_tracker_v6.json  # Saved expense history
```

---

## ⚙️ Features

### 1️⃣ Add Expenses

* Enter product name
* Choose category from a fixed list
* Enter price
* Repeat until finished

Automatically calculates:

* Total price
* Average price
* Most expensive product
* Least expensive product
* Total spending per category
* Highest & lowest spending categories

Data is saved to a JSON file with timestamps.

---

### 2️⃣ Search Product

* Search for a product name in saved history
* Returns all matches with timestamps
* Input is normalized (case-insensitive)

---

### 3️⃣ Load Old Data

* Loads and displays previously saved expense data from JSON

---

### 4️⃣ Exit Program

* Clean exit from the CLI

---

## 🛡️ Input Validation Rules

* Product names:

  * Cannot be empty
  * Cannot contain numbers
  * Supports `done` and `exit`

* Categories:

  * Must match predefined category list
  * Case-insensitive input

* Prices:

  * Must be a non-negative float

---

## 🧩 Design Philosophy

* Input layer guarantees valid data
* Calculation layer assumes valid input
* Minimal defensive programming inside core logic
* Known limitations are accepted in v6
* Code clarity is prioritized over over-engineering

## 🚀 Next Version (v7)

* Full rewrite using Object-Oriented Programming
* Classes such as:

  * `Expense`
  * `ExpenseTracker`
  * `StorageManager`
* Cleaner state management
* Improved extensibility

---

## 🧠 Author Notes

This project was built through **practice, debugging, and reasoning**, not tutorials.

Mistakes were treated as learning tools, and each version reflects deeper understanding.

---

## 📌 Version

**Expense Tracker v6** — Final Procedural Version
