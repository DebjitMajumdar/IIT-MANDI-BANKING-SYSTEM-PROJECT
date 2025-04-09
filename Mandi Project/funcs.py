import os
from datetime import datetime

def login():
    print("=== Login ===")
    accNo = input("Enter account number: ")
    pin = input("Enter 4-digit PIN: ")

    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            for line in f:
                details = line.strip().split(",")
                if details[0] == accNo and details[2] == pin:
                    print("Login successful")
                    print("\nWelcome", details[1])
                    return details
    except FileNotFoundError:
        pass

    print("Invalid account number or PIN.")
    return None

def checkBalance(data):
    print("=== Account Balance ===")
    print("Account Holder:", data[1])
    print("Account Number:", data[0])
    print("Current Balance: ₹", data[3])


def success(data):
    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Change PIN")
        print("6. Transfer Money")
        print("7. Logout")

        ch2 = input("Enter your choice: ")

        if ch2 == '1':
            checkBalance(data)
        elif ch2 == '2':
            depositMoney(data)
        elif ch2 == '3':
            withdrawMoney(data)
        elif ch2 == '4':
            viewHistory(data[0])
        elif ch2 == '5':
            changePIN(data)
        elif ch2 == '6':
            transferMoney(data)
        elif ch2 == '7':
            break
        else:
            print("Invalid choice.")


def depositMoney(data):
    print("=== Deposit Money ===")
    amount = input("Enter amount to deposit: ")

    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount")
        return

    newBalance = int(data[3]) + int(amount)
    data[3] = str(newBalance)

    updateAccount(data)
    logTransaction(data[0], "Deposit", amount, data[3])
    print("Deposit successful. New Balance: ₹", data[3])

def withdrawMoney(data):
    print("=== Withdraw Money ===")
    amount = input("Enter amount to withdraw: ")

    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount.")
        return

    if int(amount) > int(data[3]):
        print("Insufficient balance.")
        return

    newBalance = int(data[3]) - int(amount)
    data[3] = str(newBalance)

    updateAccount(data)
    logTransaction(data[0], "Withdrawal", amount, data[3])
    print("Withdrawal successful. New Balance: ₹", data[3])

def updateAccount(data):
    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Account file not found.")
        return

    with open("accounts.txt", "w", encoding="utf-8") as f:
        for line in lines:
            details = line.strip().split(",")
            if details[0] == data[0]:
                f.write(data[0] + "," + data[1] + "," + data[2] + "," + data[3] + "\n")
            else:
                f.write(line)

def logTransaction(accNo, action, amount, balance):
    folder = "history"
    if not os.path.exists(folder):
        os.makedirs(folder)

    filename = os.path.join(folder, "acc_" + accNo + "_history.txt")
    time = datetime.now().strftime("%d-%m-%Y %H:%M")
    log = time + " - " + action + ": " + amount + " | Balance: ₹" + balance + "\n"

    with open(filename, "a", encoding="utf-8") as f:
        f.write(log)

def viewHistory(accNo):
    folder = "history"
    filename = os.path.join(folder, "acc_" + accNo + "_history.txt")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            print("\n--- Transaction History ---")
            print(f.read())
    except FileNotFoundError:
        print("No transaction history found.")

def changePIN(data):
    print("=== Change PIN ===")
    oldPin = input("Enter current PIN: ")
    if oldPin != data[2]:
        print("Incorrect PIN.")
        return

    newPin = input("Enter new 4-digit PIN: ")
    if not newPin.isdigit() or len(newPin) != 4:
        print("PIN must be 4 digits.")
        return

    confirmPin = input("Confirm new PIN: ")
    if newPin != confirmPin:
        print("PINs do not match.")
        return

    data[2] = newPin
    updateAccount(data)
    print("PIN changed successfully.")

def transferMoney(data):
    print("=== Transfer Money ===")
    toAcc = input("Enter recipient's account number: ")
    amount = input("Enter amount to transfer: ")

    if not amount.isdigit() or int(amount) <= 0:
        print("Invalid amount.")
        return

    amount = int(amount)

    if amount > int(data[3]):
        print("Insufficient balance.")
        return

    senderAcc = data[0]
    try:
        with open("accounts.txt", "r", encoding="utf-8") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print("Account file not found.")
        return

    recipientFound = False

    for i in range(len(lines)):
        accData = lines[i].strip().split(",")
        if accData[0] == toAcc:
            accData[3] = str(int(accData[3]) + amount)
            lines[i] = ",".join(accData) + "\n"
            logTransaction(toAcc, "Received from " + senderAcc, str(amount), accData[3])
            recipientFound = True
            break

    if not recipientFound:
        print("Recipient account not found.")
        return

    for i in range(len(lines)):
        accData = lines[i].strip().split(",")
        if accData[0] == senderAcc:
            accData[3] = str(int(accData[3]) - amount)
            lines[i] = ",".join(accData) + "\n"
            data[3] = accData[3]
            logTransaction(senderAcc, "Transferred to " + toAcc, str(amount), accData[3])
            break

    with open("accounts.txt", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print("Transfer successful. New Balance: ₹", data[3])
