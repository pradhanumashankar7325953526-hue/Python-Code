tm = 0
for i in range(1, 6):
    marks = float(input("Enter marks for subject{i} (out of 50): "))
    tm += marks
    mm = 5 * 50
    per = (tm / mm) * 100
    print("Total marks:", tm)
    print("Percentage:", per)
    if per >= 90 and per < 100:
        print("Grade: O")
    elif per >= 80 and per < 90:
        print("Grade: A")
    elif per >= 70 and per < 80:        
        print("Grade: B")
    elif per >= 60 and per < 70:
        print("Grade: C")
    elif per >= 50 and per < 60:
        print("Grade: D")
    elif per >= 0 and per < 50:
        print("Grade: F")
    else:
        print("Invalid Percentage") 