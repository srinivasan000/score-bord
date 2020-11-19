name=input("enter your name: ")
print('hello '+name)
your_score = input("enter your score: ")
opponent_score = input("enter your opponent score: ")
if your_score > opponent_score:
    print("you won the match")
elif your_score == opponent_score:
    print("match draw")
else:
    print("you lose the match")
    print("your opponent won the match")