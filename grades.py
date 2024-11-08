student_mark = int(input("Enter the student's mark: "))

if 70 <= student_mark <= 100:
        print ("The Grade of the student is A")

elif 60 <= student_mark <= 69:
        print ("The Grade of the student is B")
    
elif 50 <= student_mark <= 59:
        print ("The Grade of the student is C")
elif 40 <= student_mark <= 49:
        print ("The Grade of the student is D")
elif 30 <= student_mark <= 39:
        print ("The Grade of the student is E")
    
elif 20 <= student_mark <= 29:
        print ("The Grade of the student is F")
    
else:
    grade = "Invalid student mark"
    print ("Invalid student's mark")
