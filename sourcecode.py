# Student Record and Academic Management System
# Data Organization using Python Collections
students = {}
def add_student():
    roll = input("Enter Roll Number: ")
    if roll in students:
        print("Student with this roll number already exists!")
        return
    name = input("Enter Student Name: ")
    department = input("Enter Department: ")
    registration_no = input("Enter Registration Number: ")
    dob = input("Enter Date of Birth (DD/MM/YYYY): ")
    subjects = []
    marks = []
    n = int(input("Enter number of subjects: "))
    for i in range(n):
        subject = input(f"Enter Subject {i + 1}: ")
        mark = float(input(f"Enter Marks in {subject}: "))
        subjects.append(subject)
        marks.append(mark)
    attendance = []
    for subject in subjects:
        att = float(input(f"Enter attendance percentage for {subject}: "))
        attendance.append(att)
    email = input("Enter Email ID: ")
    phone = input("Enter Phone Number: ")
    address = input("Enter Address: ")
    students[roll] = {
        "name": name,
        "department": department,
        "registration": (registration_no, dob),
        "subjects": subjects,
        "marks": marks,
        "attendance": attendance,
        "contact": {"email": email, "phone": phone, "address": address}
    }
    print("\nStudent added successfully!")
def display_student(student):
    print("\n------------------------------")
    print("Roll Number :", student["roll"])
    print("Name        :", student["name"])
    print("Department  :", student["department"])
    print("Registration Number :", student["registration"][0])
    print("Date of Birth       :", student["registration"][1])
    print("\nSubjects and Marks:")
    for i in range(len(student["subjects"])):
        print(student["subjects"][i], ":", student["marks"][i],
              "| Attendance:", student["attendance"][i], "%")
    print("\nContact Information")
    print("Email   :", student["contact"]["email"])
    print("Phone   :", student["contact"]["phone"])
    print("Address :", student["contact"]["address"])
    average = sum(student["marks"]) / len(student["marks"])
    print("Average Marks :", round(average, 2))
    print("------------------------------")
def search_student():
    roll = input("Enter Roll Number to search: ")
    if roll in students:
        student = students[roll].copy()
        student["roll"] = roll
        display_student(student)
    else:
        print("Student not found!")
def update_student():
    roll = input("Enter Roll Number to update: ")
    if roll not in students:
        print("Student not found!")
        return
    print("\n1. Update Name")
    print("2. Update Department")
    print("3. Update Email")
    print("4. Update Phone")
    print("5. Update Address")
    choice = input("Enter your choice: ")
    if choice == "1":
        students[roll]["name"] = input("Enter new name: ")
    elif choice == "2":
        students[roll]["department"] = input("Enter new department: ")
    elif choice == "3":
        students[roll]["contact"]["email"] = input("Enter new email: ")
    elif choice == "4":
        students[roll]["contact"]["phone"] = input("Enter new phone: ")
    elif choice == "5":
        students[roll]["contact"]["address"] = input("Enter new address: ")
    else:
        print("Invalid choice!")
        return
    print("Student record updated successfully!")
def delete_student():
    roll = input("Enter Roll Number to delete: ")
    if roll in students:
        del students[roll]
        print("Student record deleted successfully!")
    else:
        print("Student not found!")
def display_all():
    if len(students) == 0:
        print("No student records available.")
        return
    for roll, data in students.items():
        student = data.copy()
        student["roll"] = roll
        display_student(student)
def calculate_average():
    roll = input("Enter Roll Number: ")
    if roll not in students:
        print("Student not found!")
        return
    marks = students[roll]["marks"]
    if len(marks) == 0:
        print("No marks available.")
        return
    average = sum(marks) / len(marks)
    print("Average Marks =", round(average, 2))
def highest_scorer():
    if len(students) == 0:
        print("No student records available.")
        return
    highest_roll = None
    highest_average = -1
    for roll, student in students.items():
        if len(student["marks"]) > 0:
            average = sum(student["marks"]) / len(student["marks"])
            if average > highest_average:
                highest_average = average
                highest_roll = roll
    if highest_roll is not None:
        print("\nHighest Scorer")
        print("Roll Number :", highest_roll)
        print("Name        :", students[highest_roll]["name"])
        print("Department  :", students[highest_roll]["department"])
        print("Average     :", round(highest_average, 2))
def students_by_department():
    department = input("Enter Department: ")
    found = False
    print("\nStudents in", department, "Department:")
    for roll, student in students.items():
        if student["department"].lower() == department.lower():
            print("Roll:", roll, "| Name:", student["name"])
            found = True
    if not found:
        print("No students found in this department.")
def count_students():
    print("Total Number of Students:", len(students))
def show_departments_and_subjects():
    departments = set()
    subjects = set()
    for student in students.values():
        departments.add(student["department"])
        for subject in student["subjects"]:
            subjects.add(subject)
    print("\nDepartments:")
    print(departments)
    print("\nSubjects:")
    print(subjects)
while True:
    print("\n======================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Calculate Average Marks")
    print("7. Find Highest Scorer")
    print("8. List Students by Department")
    print("9. Count Students")
    print("10. Display Departments and Subjects")
    print("11. Exit")
    choice = input("\nEnter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        search_student()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        display_all()
    elif choice == "6":
        calculate_average()
    elif choice == "7":
        highest_scorer()
    elif choice == "8":
        students_by_department()
    elif choice == "9":
        count_students()
    elif choice == "10":
        show_departments_and_subjects()
    elif choice == "11":
        print("Thank you for using Student Management System!")
        break
    else:
        print("Invalid choice! Please try again.")