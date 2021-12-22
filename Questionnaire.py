Roles = []
Films = []
Name = ""
Chosen_priority = ""
role_list = ['Director of Photography', 'Camera Operator', 'Producer', 'Editor/Sound', 'Production Designer'] #Edit This array for number of Roles you have.
film_list = ['Protected' , 'Merry Christmas', 'The Cadillac', 'Birthday Party', 'Turn Over', 'Draw Now'] #Edit THis array for number of Films you have.
from os import X_OK
import time
print("----------------------------------------------------------------------------------------")
Name = input("Name: ")

def role_priority_q(role_list, Roles, accumulator_number):
    th_term = "th "
    while True:
        if str(accumulator_number)[len(str(accumulator_number)) - 2:] != str(11) or str(accumulator_number)[len(str(accumulator_number)) - 2:] != str(12):
            if int(str(accumulator_number)[-1]) == 0:
                th_term = "st "
            if int(str(accumulator_number)[-1]) == 1:
                th_term = "nd "
            if int(str(accumulator_number)[-1]) == 2:
                th_term = "rd "
            accumulator_number = len(Roles) + 1
        if accumulator_number == len(role_list):
            role_question = "Last Choice Role? "
        else:       
            role_question = str(accumulator_number) + th_term + "Choice Role? "
            accumulator_number = int(accumulator_number)
        answer = input(role_question)
        try:
            answer = int(answer)
            if answer in range(1, len(role_list) + 1):
                answer = answer - 1
                if answer in Roles:
                    print("You have already chosen this role.")
                else:
                    Roles.append(answer)
                    break
            else:
                print("Please Enter a number between 1 and " + str(int(len(role_list)) + 1) + ".")
        except:
            print("Error! Please enter a number.")

def role_q(role_list, Roles):  
    accumulator_number = 0
    for x in range(0, len(role_list)):
        role_priority_q(role_list, Roles, accumulator_number)
        accumulator_number += 1
    print("")
    print("----------------------------------------------------------------------------------------")
    for x in range(0, len(Roles)):
        th_term = "th "
        if str(x)[len(str(x)) - 2:] != str(11) or str(x)[len(str(x)) - 2:] != str(12):
            if int(str(x)[-1]) == 0:
                th_term = "st "
            if int(str(x)[-1]) == 1:
                th_term = "nd "
            if int(str(x)[-1]) == 2:
                th_term = "rd "
        if int(x) == int(len(Roles) - 1):
            print("Last Choice is: " + role_list[Roles[x]])
        else:
            print(str(int(x) + 1) + th_term + "Choice: " + role_list[Roles[x]])
    print("")
    while True:
        print("Is this correct? (Y/N) ")
        confirmation = input()
        if confirmation == "y" or confirmation == "Y":
            break
        if confirmation == "n" or confirmation == "N":
            Roles = []
            role_q(role_list, Roles)
            break
        else:
            print("Please enter Y or N ONLY")
            
def Role_priority(role_list):
    print("----------------------------------------------------------------------------------------")
    print("Here is your Role you can choose from:")
    for x in range(0, len(role_list)):
        print(str(int(x) + 1) + ") " + role_list[x])
    print("")  
    print("----------------------------------------------------------------------------------------")
    role_q(role_list, Roles)

def Film_priority(film_list, Films):
    print("")
    print("----------------------------------------------------------------------------------------")
    print("Here are the films you can choose from:")

    for x in range(0, len(film_list)):
        print(str(int(x + 1)) + ") " + film_list[x])
    
    print("")
    for x in range(0, len(film_list)):
        th_term = "th "
        if str(x)[len(str(x)) - 2:] != str(11) or str(x)[len(str(x)) - 2:] != str(12):
            if int(str(x)[-1]) == 0:
                th_term = "st "
            if int(str(x)[-1]) == 1:
                th_term = "nd "
            if int(str(x)[-1]) == 2:
                th_term = "rd "
        while True:
            if x == int(len(film_list) - 1):
                answer = input("Last Choice Film: ")
            else:
                answer = input(str(int(x + 1)) + th_term + " Choice Film: ")
            try:
                answer = int(answer)
                if answer in range(0, int(len(film_list) + 1)):
                    answer = int(answer) - 1
                    if answer in Films:
                        print("You have already chosen this one.")
                    else:
                        Films.append(answer)
                        break
                else:
                    print("Error! Try to input a number from 1 to " + str(int(len(film_list))) + ".")
            except:
                print("Error! Try to input a number from 1 to " + str(int(len(film_list))) + ".")

    print("")
    print("----------------------------------------------------------------------------------------")
    print("Here is your Film choices:")
    for x in range(0, len(Films)):
        th_term = "th "
        if str(x)[len(str(x)) - 2:] != str(11) or str(x)[len(str(x)) - 2:] != str(12):
            if int(str(x)[-1]) == 0:
                th_term = "st "
            if int(str(x)[-1]) == 1:
                th_term = "nd "
            if int(str(x)[-1]) == 2:
                th_term = "rd "
        if int(x) == int(len(Films) - 1):
            print("Last Choice is: " + film_list[Films[x]])
        else:
            print(str(int(x) + 1) + th_term + "Choice is: " + film_list[Films[x]])
    print("")
    print("Is this correct? (Y/N) ")
    while True:
        answer = input()
        if answer == "Y" or answer == "y":
            break
        if answer == "N" or answer == "n":
            Films = []
            Film_priority(film_list, Films)
            break
        else:
            print("Please Enter (Y/N) ONLY.")

def Menu(Films, film_list, Roles, role_list, Name):
    print("")
    print('''Which one is your prefered priority? 
    1) Role Priority
    2) Film Priority
    ''')
    while True:
        priority = input("Type Here: ")
        if priority == str('1'):
            Chosen_priority = "Role"
            print("")
            Role_priority(role_list)
            Film_priority(film_list, Films)
            break
        if priority == str('2'):
            Chosen_priority = "Film"
            print("")
            Film_priority(film_list, Films)
            Role_priority(role_list)
            break
        else:
            print("You can only enter 1 or 2.")

    print("")
    print("----------------------------------------------------------------------------------------")
    print("Summery:")
    print("")
    print("Name: " + Name)
    print("")
    print("Priority: " + Chosen_priority)
    print("")

    def print_Role(Roles, role_list):
        print("Role Order:")
        for x in range(0, int(len(Roles))):
            print(str(int(x) + 1) + ") " + role_list[Roles[x]])
        print("")

    def print_Film(Films, film_list):
        print("Film Order:")
        for x in range(0, int(len(Films))):
            print(str(int(x) + 1) + ") " + film_list[Films[x]])
        print("")

    if Chosen_priority == "Role":
        print_Role(Roles, role_list)
        print_Film(Films, film_list)

    if Chosen_priority == "Film":
        print_Film(Films, film_list)
        print_Role(Roles, role_list)
    print("Is this Correct? (Y/N)")
    while True:
        answer = input()
        if answer == "Y" or answer == "y":
            break
        if answer == "N" or answer == "n":
            Roles.clear()
            Films.clear()
            Menu(Films, film_list, Roles, role_list, Name)
        else:
            print("Please Enter (Y/N) ONLY.")
    print("")
    print("----------------------------------------------------------------------------------------")
    print("Printing...")
    time.sleep(1)
    filepath = 'C:\Python\Choices/' + Name + ".txt"
    print(filepath)
    with open(str(filepath), 'w') as f:
        f.write('Name: ')
        f.write('\n')
        f.write(str(Name))
        f.write('\n')
        f.write('Priority: ')
        f.write('\n')
        f.write(str(Chosen_priority))
        f.write('\n')
        f.write('Role Order: ')
        f.write('\n')
        for x in Roles:
            if x == int(int(len(Roles)) - 1):
                f.write(str(x))
            else:
                f.write(str(str(x) + ', '))
        f.write('\n')
        f.write('Film Order: ')
        f.write('\n')
        for x in Films:
            if x == int(int(len(Films)) - 1):
                f.write(str(x))
            else:
                f.write(str(str(x) + ', '))

    for x in range(3, 0, -1):
        print(str(x) + "...")
        time.sleep(1)
    print("DONE!")
    print("")
    print("----------------------------------------------------------------------------------------")
    time.sleep(1)
    print("Shutting Down...")
    print("----------------------------------------------------------------------------------------")
    time.sleep(1)
    exit()
Menu(Films, film_list, Roles, role_list, Name)