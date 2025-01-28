from crud import add, get_list, update, delete

class Student:
    table_name = 'ST_STUDENT'
    fields = ['name', 'sex', 'birth_date', 'group_id', 'year']
    id_field = 'STUDENT_ID'
    columns= {
      'name': 'STUDENT_NAME',
      'sex': 'STUDENT_SEX', 
      'birth_date': 'STUDENT_BIRTH_DATE', 
      'group_id': 'STUDENT_GROUP_ID', 
      'year': 'STUDENT_EDUCATION_YEAR'
    }

    def add_student(args, values):
      add(Student.table_name, [Student.columns[a] for a in args], values)
    
    def list_student():
      return get_list(Student.table_name)

    def change_student(id, args, values):
      update(Student.table_name, Student.id_field, id, [Student.columns[a] for a in args], values)

    def remove_student(id):
      delete(Student.table_name, Student.id_field, id)

class Group:
    table_name = 'ST_GROUP'
    fields = ['name', 'curator_id', 'speciality']
    id_field = 'GROUP_ID'
    columns= {
      'name': 'GROUP_NAME',
      'curator_id': 'GROUP_CURATOR_ID', 
      'speciality': 'GROUP_SPECIALITY'
    }
    
    def add_group(args, values):
      add(Group.table_name, [Group.columns[a] for a in args], values)

    def list_group():
      return get_list(Group.table_name)

    def change_group(id, args, values):
      update(Group.table_name, Group.id_field, id, [Group.columns[a] for a in args], values)

    def remove_group(id):
      delete(Group.table_name, Group.id_field, id)

class Curator:
    table_name = 'ST_CURATOR'
    fields = ['name', 'role']
    id_field = 'CURATOR_ID'
    columns= {
      'name': 'CURATOR_NAME',
      'role': 'CURATOR_ROLE'
    }

    def add_curator(args, values):
      add(Curator.table_name, [Curator.columns[a] for a in args], values)
    
    def list_curator():
      return get_list(Curator.table_name)

    def change_curator(id, args, values):
      update(Curator.table_name, Curator.id_field, id, [Curator.columns[a] for a in args], values)

    def remove_curator(id):
      delete(Curator.table_name, Curator.id_field, id)