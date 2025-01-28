from DB import initialize_database
from service import Student, Group, Curator
from parser import *

def main():
    initialize_database('initDB.sql')

    while True:
        print("\nStudent Management System")
        print("\nCommands: ")
        print("\nTo add curator:")
        print("\nadd curator name='curator name' role='curator role' ")
        print("\nTo add group:")
        print("\nadd group name='group name' curator_id='curator id' speciality='speciality of group'")
        print("\nTo add student:")
        print("\nadd student name='student name' sex='student sex: М/Ж' birth_date='date of birth: 1991-04-29' group_id='group id' year='education year'")

        print("\nTo view curators/groups/students:")
        print("\nlist curators / list groups / list students")

        print("\nTo change student: <student_id is mandatory other are not>")
        print("\nchange student student_id='student id' name='student name' sex='student sex: М/Ж' birth_date='date of birth: 1991-04-29' group_id='group id' year='education year'")
        
        print("\nTo remove curators/groups/students: <id is mandatory>")
        print("\nremove student id='student id' / remove group id='group id' / remove curator id='curator id'")

        print("\nTo exit type exit")

        command = input("\n\nChoose an option: ")

        if command.startswith('add'):
            lst = command.split()
            if (lst[1] == 'curator'):
                args, values = parse_fields(command, Curator.fields)
                Curator.add_curator(args, values)
            elif (lst[1] == 'student'):
                args, values = parse_fields(command, Student.fields)
                Student.add_student()
            elif (lst[1] == 'group'):
                args, values = parse_fields(command, Group.fields)
                Group.add_group()
            else: 
                print("Invalid command. Try again.")

        elif command.startswith('list'):
            lst = command.split()
            if (lst[1] == 'curator'):
                Curator.list_curator()
            elif (lst[1] == 'student'):
                Student.list_student()
            elif (lst[1] == 'group'):
                Group.list_group()
            else: 
                print("Invalid command. Try again.")

        elif command.startswith('change'):
            lst = command.split()
            id = parse_value(command, id)
            if id:
                if (lst[1] == 'curator'):
                    args, values = parse_fields(command, Curator.fields)
                    Curator.change_curator(id, args, values)
                elif (lst[1] == 'student'):
                    args, values = parse_fields(command, Student.fields)
                    Student.change_student(id, args, values)
                elif (lst[1] == 'group'):
                    args, values = parse_fields(command, Group.fields)
                    Group.change_group(id, args, values)
                else: 
                    print("Invalid command. Try again.")
            else:
                print("Invalid command. Try again.")                    

        elif command.startswith('remove'):
            lst = command.split()
            id = parse_value(command, id)
            if id:
                if (lst[1] == 'curator'):
                    Curator.remove_curator(id)
                elif (lst[1] == 'student'):
                    Student.remove_student(id)
                elif (lst[1] == 'group'):
                    Group.remove_group(id)
                else: 
                    print("Invalid command. Try again.")
            else:
                print("Invalid command. Try again.")

        elif command.startswith('exit'):
            break

        else:
            print("Invalid command. Try again.")

if __name__ == '__main__':
    main()
