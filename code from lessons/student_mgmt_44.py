# [ CRUD - Create, Retrieve, Update, Delete] Student



# a small dblike...
students_db = [{'id': 1, 'name': 'Anar', 'surname': 'Mammadli', 'bith_year': '1998', 'birth_city': 'Baku'},
            {'id': 2, 'name': 'Fazil', 'surname': 'Mehdi', 'bith_year': '2001', 'birth_city': 'Gence'},
            {'id': 3, 'name': 'Aynur', 'surname': 'Salmanli', 'bith_year': '2002', 'birth_city': 'Tovuz'},
            ]



# CREATE
def create_student(student_dict, students_db):
    students_db = students_db.copy()
    students_db.append(student_dict)
    return students_db


# RETRIEVE
def retrieve_student(id, students_db):
    for index, student in enumerate(students_db):
        if student['id'] == id:
            return student, index
        
    raise ValueError(f"Student with id: {id} not found!")




# UPDATE
def update_student(id, students_db, value_dict):
    students_db = students_db.copy()
    # get student
    student, i = retrieve_student(id, students_db=students_db)
    # update student
    for k, v in value_dict.items():
        student[k] = v
    # replace in students_db
    students_db[i] = student

    return students_db


# DELETE
def delete_student(id, students_db):
    students_db = students_db.copy()
    student, i = retrieve_student(id=id, students_db=students_db)
    resp = input(f"Are you sure that want to delete student:\n{student}: ")
    if resp.lower() in ('y', 'yes'):
        # delete student
        deleted = students_db.pop(i)
        print(f"{deleted}\t deleted")
        return students_db
    else:
        return None


# SOME ADDITION
def get_student_age(id, students_db):
    current_year = 2023
    student, _ = retrieve_student(id, students_db)
    age = current_year - int(student['bith_year'])
    return age