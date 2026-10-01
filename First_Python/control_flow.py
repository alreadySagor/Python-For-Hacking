# age = int(input("Enter your age: "))

# if age > 18:
#     print("You're Adult!")
# elif age == 18:
#     print("You're 18 years old")
# else:
#     print("You are Minor!")

score = int(input("Enter your score: "))

if score >= 80 and score <= 100:
    print("A+")
elif score >= 70 and score < 80:
    print("A")
elif score >= 60 and score <= 69:
    print("A-")
elif score >= 50 and score < 60:
    print("B")
elif score >= 40 and score <= 49:
    print("C")
elif score > 32 and score < 40:
    print("D")
elif score > 100:
    print("Invalid score!!!!\nTry again....")
else:
    print("Failed!!!")