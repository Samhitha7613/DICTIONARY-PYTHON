# Info.
print("Attempt 5 rounds and in each round\n random quiz questions will be displayed to you.")
print("Each Question carry 1 marks.")


#Q1
print("Q1)   Who developed Python Programming Language?")
print(" 1)Wick van Rossum   2)Guido van Rossum    ")
q1=int(input("Ans. Q1: "))

#Q2
print("Q2)  Is Python case sensitive when dealing with identifiers?")
print(" 1)Yes   2)No")
q2=int(input("Ans. Q2: "))

#Q3
print("Q3)   What will be the value of the following Python expression?")
print(" 4 + 3 % 5")
print("1)7  2)2")
q3=int(input("Ans. Q3: "))

#4
print("Q4)  .Which of the following is used to define a block of code in Python language?")
print("1)Indentation    2) key")
q4=int(input("Ans. Q4: "))

#5
print("Which of the following character is used to give single-line comments in Python?")
print("1)// 2)#")
q5=int(input("Ans. Q5: "))

# calculating marks
marks=0
if q1==2:
    marks+=1
if q2==1:
    marks+=1
if q3==1:
    marks+=1
if q4==1:
    marks+=1
if q5==2:
    marks+=1

# final statement
if marks==5:
    print("Congratulations! You done it. You have got",marks,"out of 5.")
elif marks==4:
    print("Congratulations! You have got",marks,"out of 5.")
elif marks<=3:
    print("You have got",marks,"out of 5.")
    print("Best wishes for next time.")
