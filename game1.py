student_grade = {}

def add_student(name,grade):
    student_grade[name] = grade
    print(f'Data of {name} is added')

def update_student(name,grade):
    if name in student_grade:

        student_grade[name] = grade
        print(f'Data of {name} has been updated')  
    else:
        print(f'Student not found')
    
def delete_student(name,grade):
    if name in student_grade:

        del student_grade[name] 
        print(f'Data of {name} has been deleted')

def display_student():
    if student_grade:
        for name, grade in student_grade.items():
            print(f'{name} : {grade}')
    else:
        print(f'No Student found! ')


def main():

    while True:
        
        print("\n WELCOME TO STUDENT MARKS MANAGEMENT SYSTEM!")
        print("\n PRESS THE NUMBERS TO DO THE FOLLOWING TASK")
        print("\n 1. Add a student")
        print("2. Update a student")
        print("3. Delete a student data")
        print("4. Display all the student data")
        print("5. Exit the program")

        a = int(input("Enter the task(1-5) to perform: "))
        if a == 1:
            name = input("Enter the student name: ")
            grade = int(input("Enter the marks: "))
            add_student(name,grade)

        elif a == 2:
            name = input("Enter the student name: ")
            grade = int(input("Enter the marks: "))
            update_student(name,grade)
        elif a == 3:
            name = input("Enter the student name: ")
            grade = int(input("Enter the marks: "))
            delete_student(name,grade)

        elif a == 4:
            display_student()
        
        elif a == 5:

            print("Exiting the program")
            break
        else:
            print("Invalid choice")
        


if __name__ == "__main__":
    main()
