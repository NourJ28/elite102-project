import time

users = {
    "admin": {"pin": "1328", "balance": 999},
    "customer": {"pin": "1111", "balance": 111}
}

def show_menu():
    print("\nWelcome to nour's banking system")
    print("1. login")
    print("2. create account")
    print("3. exit")
    choice = input("enter your choice please: ")
    return choice

def login():
    username = input("enter your username: ")
    pin = input("enter your PIN: ")
    
    if username in users and users[username]["pin"] == pin:
        print(f"login successful, welcome {username}")
        return username
    else:
        print("invalid username or pin")
        return None

def show_dashboard(username):
    while True:
        print(f"\nWelcome {username}")
        print(f"your current balance is: ${users[username]["balance"]}")
        print("1. check balance")
        print("2. deposit")
        print("3. withdraw")
        print("4. log out")
        
        choice = input("enter your choice: ")
        
        if choice == '1':
            check_balance(username)
        elif choice == '2':
            deposit_money(username)
        elif choice == '3':
            withdraw_money(username)
        elif choice == '4':
            print("logging out...")
            break
        else:
            print("sorry I dont understand")

def check_balance(username):
    print(f"your balance is: ${users[username]["balance"]}")

def deposit_money(username):
    try:
        amount = float(input("enter amount to deposit: $"))
        if amount > 0:
            users[username]['balance'] += amount
            print(f"successfully deposited ${amount}. new balance: ${users[username]['balance']}")
        else:
            print("amount must be greater than zero.")
    except ValueError:
        print("invalid input")
def withdraw_money(username):
    try:
        amount = float(input("enter amount to withdraw: $"))
        if amount <= 0:
            print("amount must be greater than zero.")
        elif amount > users[username]['balance']:
            print("Not enough in your balance")
        else:
            users[username]["balance"] -= amount
            print(f"successfully withdrew ${amount}, new balance: ${users[username]["balance"]}")
    except ValueError:
        print("invalid input")

def create_account():
    username = input("enter a new username: ")
    if username in users:
        print("username already exists")
    else:
        pin = input("enter a new pin: ")
        users[username] = {"pin": pin, "balance": 0}
        print(f"account created")

def main():
    while True:
        choice = show_menu()
        
        if choice == '1':
            username = login()
            if username:
                show_dashboard(username)
        elif choice == '2':  
            create_account()
        elif choice == '3':  
            print("Bye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
