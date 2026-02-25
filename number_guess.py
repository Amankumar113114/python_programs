import random
def result():
    guess=int(input("guess the number :"))
    if guess>num:
     print("too high")
    elif guess<num:
     print("too low")
    else:
     print("your guess is correct ")
     return True

difficulty=input("enter difficulty level:\n"
                 "1.easy ==> the range of number is between 1 to 50 with 10 attempt\n"
                 "2.medium ==> the range of number is between 1 to 100 with 7 attempt\n"
                 "3.hard ==> the range of number is between 1 to 200 with 5 attempt\n")

if difficulty in ["1","easy"]:
  num =random.randint(1,50)
  attempt=10

  
elif difficulty in ["2","medium"]:
  num =random.randint(1,100)
  attempt=7
  
elif difficulty in ["3","hard"]:
  num =random.randint(1,200)
  attempt=5
else:
  print("please choose correct difficulty")
  exit()
for i in range(attempt):
  if result():
     break
else:
    print(f"out of attempts the number is {num}")

  

  
   

