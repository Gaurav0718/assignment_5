student_list = {
    'Gaurav': 18,
    'Shashank': 45,
    'Prajwal': 69,
    'Yashas': 88,
    'Anirudh': 99,
    'Pranav': 77,
    'Poorab': 100
}

name_input = input("Enter the student's name: ")
name_input = name_input.capitalize()

if name_input in student_list:
    print(f"{name_input}\'s marks: {student_list[name_input]}")
else:
    print("Student not found")
