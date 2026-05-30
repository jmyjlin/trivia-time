print("Quiz")
score = 0
answer = input("What is 2 + 2? ")
if answer == "4":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What is the capital of California? ").lower()
if answer == "sacramento":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
answer = input("What does the colors red and blue make? ").lower()
if answer == "purple":
    print("Correct!")
    score += 1
else:
    print("Wrong!")
print(f"\n{score}/3 correct")
