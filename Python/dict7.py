"""Consider following dictionary that contains marks of 6 students. Write main script to print the name 
of students containing maximum and minimum marks from it.
marks = {“Vinay”:61, “Tushar”:52, “Vishal”:55, “Tanmay”:71, “Amey”:70, “Amit”:65}"""

marks = {"Vinay": 61, "Tushar": 52, "Vishal": 55,
         "Tanmay": 71, "Amey": 70, "Amit": 65}

max = max(marks, key=marks.get)
print("Student with maximum marks:", max)

min = min(marks, key=marks.get)
print("Student with minimum marks:", min)
