mark = int(input("Enter the student's mark: "))

if 70 <= mark <= 100:
        print ("A")

elif 60 <= mark <= 69:
        print ("B")
    
elif 50 <= mark <= 59:
        print ("C")
elif 40 <= mark <= 49:
        print ("D")
elif 30 <= mark <= 39:
        print ("E")
    
elif 20 <= mark <= 29:
        print ("F")
    
else:
    grade = "Invalid mark"
    print ("Invalid mark")
