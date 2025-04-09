import funcs
import main
import admin

while True:
    print("\n=== Banking System Menu ===")
    print("1. Create Account")
    print("2. Login and Access Account")
    print("3. Admin Login")
    print("4. Exit")
    ch = input("Enter your choice: ")

    if ch == '1':
        main.createAccount()
    elif ch == '2':
        data = funcs.login()
        if data:
            funcs.success(data)
    elif ch == '3':
        admin.adminLogin()
    elif ch == '4':
        print("Thank you for using the banking system.")
        break
    else:
        print("Invalid choice.")
