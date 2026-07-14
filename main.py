"""
Student Management System

A simple Python + MySQL application to manage student records.
Features:
- Add Student
- Update Student
- Delete Student
- Search Student
- View Students
- Generate Report

Author: Ravi Kumawat
"""


import mysql.connector
from  mysql.connector import Error

# -------------------------------
# Add a new student
# -------------------------------

def add_student():
    name=input("enter student name: ")
    branch=input("enter student branch:")
    try:
        semester = int(input("Enter semester: "))
    except ValueError:
        print("Invalid semester.")
        return
    address=input("enter student address : ")
    
    query=''' INSERT INTO student(name,semester,branch,address) values(%s,%s,%s,%s) '''
    values=(name,semester,branch,address)
    try:
        cursor.execute(query,values)
        conn.commit()
        print("\nStudent Added successfully")
    except Exception as e :
        print(f"Error : {e}")

# -------------------------------
# Update existing student details
# -------------------------------

def update_student():
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    name = input("Enter new name: ")
    try:
        semester = int(input("Enter new semester: "))
    except ValueError:
        print("Invalid semester.")
        return
    branch = input("Enter new branch: ")
    address = input("Enter new address: ")

    query = """
    UPDATE student
    SET NAME = %s,
        SEMESTER = %s,
        BRANCH = %s,
        ADDRESS = %s
    WHERE ID = %s
    """

    values = (name, semester, branch, address, student_id)
    try:
        cursor.execute(query, values)
        conn.commit()
    

        if cursor.rowcount > 0:
            print("\nStudent updated successfully!")
        else:
            print("\nStudent not found.")
    except Exception as e :
        print(f"Error : {e}")

# -------------------------------
# Delete student by ID
# -------------------------------

def delete_student():
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID.")
        return

    query = "DELETE FROM student WHERE ID = %s"
    try:
        cursor.execute(query, (student_id,))
        conn.commit()

        if cursor.rowcount > 0:
            print("\nStudent deleted successfully!")
        else:
            print("\nStudent not found.")
    except Exception as e :
        print(f"Error : {e}")

# -------------------------------
# Display all students
# -------------------------------

def view_student():
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    if not students:
        print("No students found.")
        return

    print("\n===================== STUDENT LIST =====================")
    print(f"{'ID':<5}{'NAME':<20}{'SEM':<10}{'BRANCH':<30}{'ADDRESS'}")
    print("-" * 80)

    for student in students:
        print(f"{student[0]:<5}{student[1]:<20}{student[2]:<10}{student[3]:<30}{student[4]}")

    print("-" * 80)
        

# -------------------------------
# Search student using ID
# -------------------------------   
    
def search_student():
    try:
        student_id = int(input("Enter Student ID: "))
    except ValueError:
        print("Invalid ID.")
        return
    query='''SELECT * FROM student where id =%s'''
    try:
        cursor.execute(query,(student_id,))
        student = cursor.fetchone()

        if student:
            print("\nStudent Details")
            print("-" * 30)
            print("ID       :", student[0])
            print("Name     :", student[1])
            print("Semester :", student[2])
            print("Branch   :", student[3])
            print("Address  :", student[4])
        else:
            print("Student not found.")
    except Exception as e :
        print(f"Error : {e}")

# -------------------------------
# Generate student report
# -------------------------------

def generate_report():
    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    print("\n========== STUDENT REPORT ==========")
    print(f"{'ID':<5}{'NAME':<15}{'SEM':<8}{'BRANCH':<30}{'ADDRESS'}")
    print("-" * 80)

    for student in students:
        print(f"{student[0]:<5}{student[1]:<15}{student[2]:<8}{student[3]:<30}{student[4]}")

    print("-" * 80)
    print(f"Total Students: {len(students)}")



# -------------------------------
# Connect to MySQL Database
# -------------------------------

try:

    conn = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password=input("Enter MySQL password :"),
        database="student_management"   # Replace with your database name
    )

    

    # Check database connection 
        
    if conn.is_connected() :
        print ("\nconnect successfully to student_management  ")
    cursor=conn.cursor()

except Error as e:
    if e.errno == 1045:
        print("\n❌ Incorrect MySQL username or password.")
    elif e.errno == 1049:
        print("\n❌ Database 'student_management' does not exist.")
    else:
        print("\n❌ Error:", e)
    exit()



#------------------------------------
#   Main Menu
#------------------------------------



while True:

    # Display menu options

    print("\nChoose a option\n ")
    print("1. Add Student ")
    print("2. Update Student Detail ")
    print("3. Delete Student ")
    print("4. View Students ")
    print("5. Search Student ")
    print("6. Generate Report ")
    print("7. Exit ")

    # Take user input

    try:
        choice = int(input("\nEnter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    # Perform selected operation

    if (choice==1):
        add_student()
    elif(choice==2):
        update_student()
    elif(choice==3):
        delete_student()
    elif(choice==4):
        view_student()
    elif(choice==5):
        search_student()
    elif(choice==6):
        generate_report()
    elif(choice==7):
        print("\nThank You")

        # Close database resources

        cursor.close()
        conn.close()
        break
    else:
        print("\nEnter valid choice")