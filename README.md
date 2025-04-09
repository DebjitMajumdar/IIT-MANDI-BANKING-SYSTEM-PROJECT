# 🏦 Python Banking System Project

A modular, console-based banking system in Python that simulates basic banking operations for users and administrative functionalities for the bank manager. All data is securely stored using file handling techniques with transaction logs maintained in a dedicated folder.

---

## 📌 Features

### 👤 User Functions
- ✅ Create new account (auto-generates 10-digit account number).
- ✅ Login using account number and PIN.
- ✅ Check balance.
- ✅ Deposit money.
- ✅ Withdraw money.
- ✅ Transfer money to other accounts.
- ✅ View transaction history.
- ✅ Change PIN.

### 👨‍💼 Admin Functions
- ✅ Secure login with admin credentials.
- ✅ View all account details.
- ✅ View total bank balance.
- ✅ Search account by account number.
- ✅ Delete user accounts and their transaction history.

---

## 🗂️ Folder Structure

```
Mandi Project/
├── accounts.txt                  # Stores all user account details
├── history/                      # Folder for storing transaction logs
│   ├── acc_<accountNo>_history.txt
├── main.py                       # Entry point and account creation
├── menu.py                       # User interface and program flow
├── funcs.py                      # Contains all user operations
├── admin.py                      # Admin login and functionalities
└── README.md                     # This file (project documentation)
```

---

## ▶️ How to Run

### 🧰 Requirements
- Python 3.x installed

### 🚀 Run the Program

open menu.py
click on run or 'F5'

## 📌 Sample Credentials

### Admin Login:
```
Username: admin
Password: 1234
```

### User Login:
You will be shown your 10-digit account number after account creation. Use that with your chosen PIN.

---

## 💡 How It Works

- Each account stores:
  - Account Number
  - Name
  - 4-digit PIN
  - Current Balance
- All account info is saved in `accounts.txt`.
- Transaction logs are saved per user in the `history/` folder.
- Admin operations access and modify the same data file.

---

## 📊 Sample Transaction Log

Example content of a `history/acc_1234567890_history.txt`:

```
08-04-2025 14:21 - Deposit: 2000 | Balance: ₹5000
08-04-2025 15:10 - Transferred to 9876543210: 1000 | Balance: ₹4000
```

---

## 🛠 Technologies Used

- Python 3.x
- File I/O (`open`, `readlines`, `write`)
- Standard libraries (`os`, `datetime`, `random`)
- Modular programming
- Console-based UI

---
## 👨‍💻 Software Used 
- Visual Studio Code
- IDLE 3.12.0
- OBS 31.0.2

## 🎯 Project Goals Achieved

- ✔️ Data persistence through text files
- ✔️ Console menu system with clear options
- ✔️ Transaction tracking and security
- ✔️ Admin and user separation
- ✔️ Clean and modular code

---

## 📽️ Demo Video

👉 

---

