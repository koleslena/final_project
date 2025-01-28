from crud import add, get_list, update, delete

class Student:
    table_name = 'ST_STUDENT'
    fields = ['name', 'sex', 'birth_date', 'group_id', 'year']

    def add_student(self, args, values):
      add(self.table_name, args, values)
    
    def list_student(self):
      get_list(self.table_name)

    def change_student(self, id, args, values):
      update(self.table_name, id, args, values)

    def remove_student(self, id):
      delete(self.table_name, id)

class Group:
    table_name = 'ST_GROUP'
    fields = ['name', 'curator_id', 'speciality']
    
    def add_group(self, args, values):
      add(self.table_name, args, values)

    def list_group(self):
      get_list(self.table_name)

    def change_group(self, id, args, values):
      update(self.table_name, id, args, values)

    def remove_group(self, id):
      delete(self.table_name, id)

class Curator:
    table_name = 'ST_CURATOR'
    fields = ['name', 'role']

    def add_curator(self, args, values):
      add(self.table_name, args, values)
    
    def list_curator(self):
      get_list(self.table_name)

    def change_curator(self, id, args, values):
      update(self.table_name, id, args, values)

    def remove_curator(self, id):
      delete(self.table_name, id)