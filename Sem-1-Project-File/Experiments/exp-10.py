students = [("Mahin", 17), ("Aditya", 19), ("Ishaan", 18), ("Ishika", 19), ("Ayush", 17)]
sorted_students = sorted(students, key=lambda x: (-x[1], x[0]))
for student in sorted_students:
    print(student)