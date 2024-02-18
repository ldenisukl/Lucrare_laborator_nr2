class Faculty:
    def __init__(self, name, field):
        self.name = name
        self.field = field
        self.students = []

    def assign_student(self, student):
        self.students.append(student)

    def graduate_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def enrolled_students(self):
        return [student for student in self.students if not student.graduate_status]

    def graduates(self):
        return [student for student in self.students if student.graduate_status]


class Student:
    def __init__(self, name, unique_identifier, email):
        self.name = name
        self.unique_identifier = unique_identifier
        self.email = email
        self.graduate_status = False

    def graduate(self):
        self.graduate_status = True


class University:
    def __init__(self):
        self.faculties = []

    def create_faculty(self, name, field):
        faculty = Faculty(name, field)
        self.faculties.append(faculty)

    def search_faculty(self, unique_identifier):
        for faculty in self.faculties:
            for student in faculty.students:
                if student.unique_identifier == unique_identifier:
                    return faculty
        return None

    def display_all_faculties(self):
        return [faculty.name for faculty in self.faculties]

    def display_faculties_by_field(self, field):
        return [faculty.name for faculty in self.faculties if faculty.field == field]

university = University()

while True:
    print("\nMenu:")
    print("1. Faculty Operations")
    print("2. General Operations")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nFaculty Operations:")
        print("1. Create and assign a student to a faculty")
        print("2. Graduate a student from a faculty")
        print("3. Display current enrolled students")
        print("4. Display graduates")
        print("5. Check if a student belongs to a faculty")

        faculty_choice = input("Enter your choice: ")

        if faculty_choice == "1":
            faculty_name = input("Enter faculty name: ")
            faculty_field = input("Enter faculty field: ")
            student_name = input("Enter student name: ")
            student_id = input("Enter student unique identifier: ")
            student_email = input("Enter student email: ")

            student = Student(student_name, student_id, student_email)
            university.create_faculty(faculty_name, faculty_field)
            faculty = university.faculties[-1]
            faculty.assign_student(student)
            print("Student assigned to faculty.")

        elif faculty_choice == "2":
    student_id = input("Enter student unique identifier: ")
    faculty_name = input("Enter faculty name: ")

    # Cautăm facultatea căreia îi aparține studentul
    faculty = university.search_faculty(student_id)

    if faculty and faculty.name == faculty_name:
        for student in faculty.students:
            if student.unique_identifier == student_id:
                student.graduate()
                faculty.graduate_student(student)
                print("Student graduated from faculty.")
                break
        else:
            print("Student not found in the specified faculty.")
    else:
        print("Student not found or not assigned to the specified faculty.")

       elif faculty_choice == "3":
    faculty_name = input("Enter faculty name: ")

    for faculty in university.faculties:
        if faculty.name == faculty_name:
            enrolled_students = faculty.enrolled_students()
            if enrolled_students:
                print("Enrolled students:")
                for student in enrolled_students:
                    print(f"- {student.name}")
            else:
                print("No enrolled students in the specified faculty.")
            break
    else:
        print("Faculty not found.")

        elif faculty_choice == "4":
    faculty_name = input("Enter faculty name: ")

    for faculty in university.faculties:
        if faculty.name == faculty_name:
            graduates = faculty.graduates()
            if graduates:
                print("Graduates:")
                for student in graduates:
                    print(f"- {student.name}")
            else:
                print("No graduates in the specified faculty.")
            break
    else:
        print("Faculty not found.")


        elif faculty_choice == "5":
    student_id = input("Enter student unique identifier: ")
    faculty_name = input("Enter faculty name: ")

    faculty = university.search_faculty(student_id)

    if faculty and faculty.name == faculty_name:
        print(f"The student belongs to {faculty.name} faculty.")
    else:
        print("Student not found or not assigned to the specified faculty.")


    elif choice == "2":
        print("\nGeneral Operations:")
        print("1. Create a new faculty")
        print("2. Search what faculty a student belongs to")
        print("3. Display University faculties")
        print("4. Display all faculties belonging to a field")

        general_choice = input("Enter your choice: ")

        if general_choice == "1":
            faculty_name = input("Enter faculty name: ")
            faculty_field = input("Enter faculty field: ")
            university.create_faculty(faculty_name, faculty_field)
            print("Faculty created.")

        elif general_choice == "2":
            student_id = input("Enter student unique identifier: ")
            faculty = university.search_faculty(student_id)
            if faculty:
                print(f"The student belongs to {faculty.name} faculty.")
            else:
                print("Student not found or not assigned to any faculty.")

        elif general_choice == "3":
            print("University faculties:")
            print(university.display_all_faculties())
        elif general_choice == "4":
            field = input("Enter field: ")
            faculties = university.display_faculties_by_field(field)
            if faculties:
                print(f"Faculties belonging to {field}:")
                print(faculties)
            else:
                print("No faculties found for this field.")

    elif choice == "3":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a valid option.")
