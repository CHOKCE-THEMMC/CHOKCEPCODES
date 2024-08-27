# Student Management System
This is a refactored version of the Student Management System.
The system allows users to add, delete, update, and view student records. 
The code has been refactored to follow SOLID principles, eliminate redundancy (DRY), simplify the design (KISS), and avoid unnecessary features (YAGNI).

## Table of Contents
 Features
- Installation
- Usage
- Code Structure
- Example Usage


  ## Features
- Add a new student
- Delete a student
- Update student information
- View all students

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/CHOKCE-THEMMC/student-management-system.git
   cd student-management-system
2.Run the system:
python student_management_system.py

## Usage
Follow the menu options to add, delete, update, and view students.

## Code Structure
student_management_system.py
Classes:
  1.Student: Handles student data and updating student information.
  2.StudentDatabase: Manages the collection of students.
  3.StudentManagementSystem: Provides high-level operations for managing students.
Menu Function:
  menu(): Implements a simple text-based menu for user interaction.

  ## Example Usage
    system = StudentManagementSystem(StudentDatabase())
    system.add_student(1, "John Doe", 20, "Computer Science")
    system.add_student(2, "Jane Smith", 22, "Mathematics")
    system.show_all_students()
    system.update_student(1, first_name="Johnathan")
    system.show_all_students()
    system.delete_student(2)
    system.show_all_students()

