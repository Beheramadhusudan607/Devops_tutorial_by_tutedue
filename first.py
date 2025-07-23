score = int(input("Enter your score: "))
if score >= 90:
    print("grade: A")
elif score >= 80:
    print("grade: B")
elif score >= 70:
    print("grade: C")
elif score >= 60:
    print("grade: D")   
else:
    print("grade: F")
    
    
# Student Grades Program

# Initialize empty dictionary
student_grades = {}

while True:
    print("\n--- Student Grade Menu ---")
    print("1. Add a new student and grade")
    print("2. Update an existing student’s grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        if name in student_grades:
            print(f"{name} already exists. Use option 2 to update the grade.")
        else:
            grade = input("Enter grade: ")
            student_grades[name] = grade
            print(f"{name} added with grade {grade}.")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in student_grades:
            grade = input("Enter new grade: ")
            student_grades[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"{name} not found. Use option 1 to add the student.")

    elif choice == "3":
        if not student_grades:
            print("No student data available.")
        else:
            print("\n--- Student Grades ---")
            for name, grade in student_grades.items():
                print(f"{name}: {grade}")

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
# End of Student Grades Program

file = open("grades.txt", "w")
for name, grade in student_grades.items():
    file.write(f"{name}: {grade}\n")
file.close()
# This code snippet is for a simple grading system and a student grades management program.
# It allows users to input scores, determine grades, and manage student grades with options to add, update, and print grades.
# The file "grades.txt" is opened for writing and stores the student grades.
