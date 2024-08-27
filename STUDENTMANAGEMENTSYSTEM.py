class Student:
    def __init__(self, id, first_name, last_name, age, major):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.major = major

    def update(self, first_name=None, last_name=None, age=None, major=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if age:
            self.age = age
        if major:
            self.major = major

    def display(self):
        print(f"\033[1mSTUDENT ID: {self.id}, First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, Major: {self.major}\033[0m")

class StudentDatabase:
    def __init__(self):
        self.students = []

    def add(self, student):
        self.students.append(student)

    def remove(self, student_id):
        self.students = [student for student in self.students if student.id != student_id]

    def find(self, student_id):
        for student in self.students:
            if student.id == student_id:
                return student
        return None

    def display_all(self):
        if not self.students:
            print("\033[1mNo students in the database.\033[0m")
        else:
            for student in self.students:
                student.display()

class StudentManagementSystem:
    def __init__(self, database):
        self.database = database

    def add_student(self, id, first_name, last_name, age, major):
        student = Student(id, first_name, last_name, age, major)
        self.database.add(student)

    def delete_student(self, student_id):
        if not self.database.students:
            print("\033[1mCannot delete. The database is empty.\033[0m")
        else:
            self.database.remove(student_id)

    def update_student(self, student_id, first_name=None, last_name=None, age=None, major=None):
        if not self.database.students:
            print("\033[1mCannot update. The database is empty.\033[0m")
        else:
            student = self.database.find(student_id)
            if student:
                student.update(first_name, last_name, age, major)
            else:
                print("\033[1mStudent not found.\033[0m")

    def show_all_students(self):
        self.database.display_all()

def menu():
    database = StudentDatabase()
    system = StudentManagementSystem(database)

    while True:
        print("\n1. Add Student")
        print("2. Delete Student")
        print("3. Update Student")
        print("4. Show All Students")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            while True:
                id = input("Enter STUDENT ID (7 characters): ")
                if len(id) == 7:
                    break
                else:
                    print("Try again. Enter 7 characters.")
            
            while True:
                first_name = input("Enter First Name: ")
                if first_name.isalpha():
                    break
                else:
                    print("Invalid name. Please enter only letters.")
            
            while True:
                last_name = input("Enter Last Name: ")
                if last_name.isalpha():
                    break
                else:
                    print("Invalid name. Please enter only letters.")
            
            while True:
                try:
                    age = int(input("Enter Age (greater than 16): "))
                    if age > 16:
                        break
                    else:
                        print("Age must be greater than 16.")
                except ValueError:
                    print("Invalid age. Please enter a whole number.")
            
            major = input("Enter Major: ")
            system.add_student(id, first_name, last_name, age, major)
        
        elif choice == '2':
            if not database.students:
                print("\033[1mCannot delete. The database is empty.\033[0m")
            else:
                id = input("Enter ID to delete: ")
                system.delete_student(id)
        
        elif choice == '3':
            if not database.students:
                print("\033[1mCannot update. The database is empty.\033[0m")
            else:
                id = input("Enter STUDENT ID to update: ")
                first_name = input("Enter First Name (leave blank to skip): ")
                last_name = input("Enter Last Name (leave blank to skip): ")
                age = input("Enter Age (leave blank to skip): ")
                major = input("Enter Major (leave blank to skip): ")
                system.update_student(id, first_name or None, last_name or None, int(age) if age.isdigit() and int(age) > 16 else None, major or None)
        
        elif choice == '4':
            system.show_all_students()
        
        elif choice == '5':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()


