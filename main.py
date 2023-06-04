# Python
# Password Enter Limitation Code

my_password = "Anurag1234"
attempt = 10
while True:
    password = input("Enter Your Password :\n>>")
    if attempt == 1:
        print("Maximum Limit Over, Try Again After 60 minute")
        break
    if password == my_password:
        print("You Have Successfully Logged In !")
        print(f"Your Password is : {password}")
        break
    else:
        attempt -= 1
    print(f"{password} | is not correct Password")
    print("Remaining Attempt is", attempt)
