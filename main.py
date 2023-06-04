# Python
# Password Enter Limitation Code

__welcome__ = """
x----------------------------x
| Password Limitation Python |
x----------------------------x
"""

print(__welcome__)
my_password = "AnuragNagar"
attempts = 10
while True:
    password = input("Enter Your Password :\n>>")
    if attempts == 1:
        print("Maximum Limit Over, Try Again After 60 minute")
        break
    if password == my_password:
        print("Congratulation, You Have Successfully Logged In !")
        print(f"Password : {password}")
        break
    else:
        attempts -= 1
    print(f"| X | '{password}' is not correct Password.")
    print("Remaining Attempt is", attempts, "\n")
