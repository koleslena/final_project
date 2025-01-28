import unittest
from parser import *
from service import Student, Group, Curator

class TestParse(unittest.TestCase):

    def test_parse_value(self):
        val_name = parse_value("add curator name='curator name' role='curator role'", 'name')
        val_role = parse_value("add curator name='curator name' role='curator role'", 'role')
        
        self.assertTrue(val_name == 'curator name')
        self.assertTrue(val_role == 'curator role')

    def test_parse_fields(self):
        fs, vls = parse_fields("add curator name='curator name' role='curator role'", Curator.fields)
        
        self.assertTrue(len(vls) == 2)
        self.assertTrue(len(fs) == 2)  

        fs, vls = parse_fields("add student name='student name' sex='student sex: М/Ж' birth_date='date of birth: 1991-04-29' group_id='group id' year='education year'", Student.fields)
        
        self.assertTrue(len(vls) == 5)
        self.assertTrue(len(fs) == 5) 

        fs, vls = parse_fields("add group name='group name' curator_id='curator id' speciality='speciality of group'", Group.fields)
        
        self.assertTrue(len(vls) == 3)
        self.assertTrue(len(fs) == 3)               

   
if __name__ == '__main__':
    unittest.main()