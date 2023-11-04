password = input("Enter your password : ")
i = 0
try:
    while password == "Spathiphyllum" or password == "spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
        print("No, I want a big Spathiphyllum!")

except:
    print("Enter correct password")

password = input("Enter your password : ")

try:
    if password == "Spathiphyllum":
        print("Yes - Spathiphyllum is the best plant ever!")
    elif password == "spathiphyllum":
        print("No, I like big Spathiphyllum")
    else:
        print("Spathiphyllum! Not input!")
except:
    print("Entered wrong password")