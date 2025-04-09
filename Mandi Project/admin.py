import os

def adminLogin():
    print("=== Admin Login ===")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    if username == "admin" and password == "1234":
        print("Admin login successful.")
        adminMenu()
    else:
        print("Invalid credentials.")

def adminMenu():
    while True:
        print("\n=== Admin Menu ===")
        print("1. View All Accounts")
        print("2. View Total Bank Balance")
        print("3. Delete an Account")
        print("4. Search for an Account")
        print("5. Logout")
        ch = input("Enter your choice: ")

        if ch == '1':
            viewAllAccounts()
        elif ch == '2':
            viewTotalBalance()
        elif ch == '3':
            deleteAccount()
        elif ch == '4':
            searchAccount()
        elif ch == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def viewAllAccounts():
    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            print("\n--- All Accounts ---")
            print("Acc No".ljust(12), "Name".ljust(20), "Balance")
            print("-" * 40)
            for line in f:
                details = line.strip().split(",")
                print(details[0].ljust(12), details[1].ljust(20), "₹", details[3])
    except FileNotFoundError:
        print("No accounts found.")

def searchAccount():
    accNo = input("Enter account number to search: ")
    found = False

    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                details = line.strip().split(",")
                if details[0] == accNo:
                    print("\n--- Account Found ---")
                    print("Acc No   :", details[0])
                    print("Name     :", details[1])
                    print("PIN      :", details[2])
                    print("Balance  : ₹", details[3])
                    found = True
                    break
        if not found:
            print("Account not found.")
    except FileNotFoundError:
        print("No accounts found.")

def viewTotalBalance():
    total = 0
    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                details = line.strip().split(",")
                total += int(details[3])
        print("Total Bank Balance: ₹", total)
    except FileNotFoundError:
        print("No accounts found.")

def deleteAccount():
    accNo = input("Enter account number to delete: ")
    found = False
    updatedLines = []

    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                details = line.strip().split(",")
                if details[0] != accNo:
                    updatedLines.append(line)
                else:
                    found = True

        if found:
            with open("accounts.txt", "w", encoding="utf-8") as f:
                f.writelines(updatedLines)

            # Remove transaction history if exists
            historyFile = os.path.join("history", "acc_" + accNo + "_history.txt")
            if os.path.exists(historyFile):
                os.remove(historyFile)

            print("Account", accNo, "deleted successfully.")
        else:
            print("Account not found.")
    except FileNotFoundError:
        print("No accounts found.")
