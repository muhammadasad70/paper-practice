import random
num=random.randint(0,10)
print(num)
guess=-1
while True:
# while guess!=num:
    guess=eval(input("enter a number"))
    if guess<num:
        print("low")
    elif guess>num:
        print("high")
    elif guess==num:
        print("equal")
        break
        print("good bye")
    else:
        continue
