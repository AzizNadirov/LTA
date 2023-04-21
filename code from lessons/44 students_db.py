from student_mgmt_44 import students_db as db
from student_mgmt_44 import create_student, retrieve_student, update_student, delete_student
from student_mgmt_44 import get_student_age as get_age


# initially db is like:
print(f"DB INITIALLY:")
print(db)
print("-"* 100)


# 1. Create student Yagub
yagub_id = 9
new_student = {'id': yagub_id, 'name': 'Yagub', 'surname': 'Yagublu', 'bith_year': '1999', 'birth_city': 'Sumgayit'}
db = create_student(student_dict=new_student, students_db=db)
print(f"DB AFTER CREATING 'Yagub':")
print(db)
print("-"* 100)


# 2. Retrieve student Yagub
yagub = retrieve_student(id=yagub_id, students_db=db)
print(f"RETRIEVE 'Yagub':")
print(yagub)
print("-"* 100)


# 3. Update student Yagub
to_change = {'name': 'Yaqub', 'surname': 'Yaqublu', 'birth_city': 'Sumqayit'}
db = update_student(id=yagub_id, students_db=db, value_dict=to_change)
print(f"DB AFTER UPDATING 'Yagub':")
print(db)
print("-"* 100)


# 4. Delete student Yagub
db = delete_student(id=yagub_id, students_db=db)
print(f"DB AFTER DELETING 'Yagub':")
print(db)
print("-"* 100)


# 5. Get Fazil's age:
fazil_id = 2
age = get_age(id=fazil_id, students_db=db)
print(f"Fazil's Age: {age}")