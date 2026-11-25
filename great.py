marks=int(input("enter your marks: "))
if marks>100 or marks<0:
    print("Invalid marks")
elif marks>=90 and marks<=100:
    print("Grade A")
elif marks>=80 and marks<90:
    print("Grade B")
else:
    print("Grade C")
elif marks>=70 and marks<80:
    print("Grade D")
else: