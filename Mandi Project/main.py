import random

def createAccount():
    print("=== Create New Account ===")
    name = input("Enter account holder's name: ")
    pin = input("Set a 4-digit PIN: ")
    balance = input("Enter initial deposit amount: ₹")

    while True:
        accNo = str(random.randint(10**9, 10**10 - 1))
        exists = False
        try:
            with open("accounts.txt", "r", encoding="utf-8") as f:
                for line in f:
                    details = line.strip().split(",")
                    if details[0] == accNo:
                        exists = True
                        break
        except FileNotFoundError:
            break

        if not exists:
            break

    with open("accounts.txt", "a", encoding="utf-8") as f:
        f.write(accNo + "," + name + "," + pin + "," + balance + "\n")

    print("Account created successfully!")
    print("Your Account Number is:", accNo)


