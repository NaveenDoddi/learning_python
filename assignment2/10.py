pre_username = "admin"
pre_password = "password123"
username = input("Enter username: ")
password = input("Enter password: ")
if username == pre_username and password == pre_password:
    print("Access Granted")
else:
    print("Access Denied")
