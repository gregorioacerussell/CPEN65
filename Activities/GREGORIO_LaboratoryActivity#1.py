import sys

class Phonebook():
    def __init__(self): # this is where data are stored
        self.student_numbers, self.surnames, self.first_names, self.occupations, self.genders, self.country_codes, self.area_codes, self.numbers = [], [], [], [], [], [], [], []
        self.genderConvert = {'M': 'His', 'F': 'Her'}
        self.choiceConvert = {1: 'Philippines', 2: 'Thailand', 3: 'Singapore', 4: 'Indonesia', 5: 'Malaysia', 6: '', 0: ''}

    def int_inputValidation(self, prompt):
        while True:
            try:
                return int(input(prompt))
            except ValueError:
                print("Please input a number")
    def str_inputValidation(self, prompt):
        while True:
            user_input = input(prompt)
            if user_input.replace(" ", "").isalpha():
                return user_input
            else:
                print("Input a valid option")
                continue
    def mainMenu(self):  # Main Menu
        print("""
| ASEAN Phonebook Interface |

[1] Store to ASEAN Phonebook
[2] Edit entry in ASEAN Phonebook
[3] Search ASEAN Phonebook by Country
[4] Exit
""")
        while True:
            mainmenu_choice = self.int_inputValidation("Enter choice: ")
            if mainmenu_choice > 4 or mainmenu_choice < 1:
                print("Not in Range")
                continue
            elif mainmenu_choice == 1:
                self.storeInfo()
            elif mainmenu_choice == 2:
                self.editInfo()
            elif mainmenu_choice == 3:
                self.checkCountry()
            elif mainmenu_choice == 4:
                sys.exit()

    def storeInfo(self):  # 1 - Store to ASEAN Phonebook

        student_number = self.int_inputValidation("Enter student number: ")
        self.student_numbers.append(student_number)

        surname = self.str_inputValidation("Enter surname: ").title()
        self.surnames.append(surname)

        first_name = self.str_inputValidation("Enter first name: ").title()
        self.first_names.append(first_name)

        occupation = self.str_inputValidation("Enter occupation: ").title()
        self.occupations.append(occupation)

        while True:
            gender = self.str_inputValidation("Enter M for Male or F for Female: ").upper()
            if gender not in ['M', 'F']:
                print("Error, not in choices")
            else:
                self.genders.append(gender)
                break

        country_code = self.int_inputValidation("Enter country code: ")
        self.country_codes.append(country_code)

        area_code = self.int_inputValidation("Enter area code: ")
        self.area_codes.append(area_code)

        number = self.int_inputValidation("Enter number: ")
        self.numbers.append(number)

        while True:
            entry = self.str_inputValidation("Do you want to enter another entry [Y/N]? ").upper()
            if entry == 'Y':
                self.storeInfo()
            elif entry == 'N':
                self.mainMenu()
            else:
                print("Error, only input Y or N")
                continue

    def editInfo(self):  # 2 - Edit entry in ASEAN Phonebook
        found = False
        while True:
            student_numberEDIT = self.int_inputValidation("Enter student number: ")
            for i in range(len(self.student_numbers)):
                if self.student_numbers[i] == student_numberEDIT:
                    found = True
                    print(f"""
Here is the existing information about {self.student_numbers[i]}
{self.first_names[i]} {self.surnames[i]} is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} number is {self.numbers[i]}

Which of the following information do you wish to change?
[1] Student Number    [4] Occupation      [7] Phone Number
[2] Surname           [5] Country Code    [8] None - Back to Main Menu
[3] Gender            [6] Area Code
""")
                    while True:
                        choice = self.int_inputValidation("Enter choice: ")
                        if choice == 1:
                            self.student_numbers[i] = self.int_inputValidation("Enter new student number: ")
                            print("Done")
                            self.mainMenu()
                        if choice == 2:
                            self.surnames[i] = self.str_inputValidation("Enter new surname: ")
                            print("Done")
                            self.mainMenu()
                        if choice == 3:
                            while True:
                                self.genders[i] = self.str_inputValidation("Enter new gender: ").upper()
                                if self.genders[i] not in ['M', 'F']:
                                    print("Invalidation")
                                    continue
                                else:
                                    print("Done")
                                    self.mainMenu()
                        if choice == 4:
                            self.occupations[i] = self.str_inputValidation("Enter new occupation: ")
                            print("Done")
                            self.mainMenu()
                        if choice == 5:
                            self.country_codes[i] = self.int_inputValidation("Enter new country code:")
                            print("Done")
                            self.mainMenu()
                        if choice == 6:
                            self.area_codes[i] = self.int_inputValidation("Enter new area code: ")
                            print("Done")
                            self.mainMenu()
                        if choice == 7:
                            self.numbers[i] = self.int_inputValidation("Enter new number: ")
                            print("Done")
                            self.mainMenu()
                        if choice == 8:
                            self.mainMenu()
                        if choice > 8 or choice <= 0:
                            print("Not in Range")

    def checkCountry(self): # 3 - Search ASEAN Phonebook by Country
        print("""
From which country:
[1] Philippines     [4] Indonesia       [0] No More
[2] Thailand        [5] Malaysia
[3] Singapore       [6] ALL
""")
        choice1 = self.int_inputValidation("Enter choice 1: ")
        choice2 = self.int_inputValidation("Enter choice 2: ")
        choice3 = self.int_inputValidation("Enter choice 3: ")
        print()

        all_checker = False
        choice1_1_checker = False
        choice1_2_checker = False
        choice1_3_checker = False
        choice1_4_checker = False
        choice1_5_checker = False
        choice2_checker = False
        choice3_checker = False
        choice2_1_checker = False
        choice2_2_checker = False
        choice2_3_checker = False
        choice2_4_checker = False
        choice2_5_checker = False

        if choice1 == choice2 == choice3:
            if choice1 == 0:
                return
            elif choice1 == 6:
                print("Here are all of the students:")
            else:
                print(f"Here are the students from {self.choiceConvert[choice1]}:")
        elif choice1 == choice2:
            if choice1 == 6:
                print("Here are all the students:")
            elif choice3 == 6:
                print("Here are all the students:")
            elif choice1 == 0:
                print(f"Here are the students from {self.choiceConvert[choice3]}")
            else:
                print(f"Here are the students from {self.choiceConvert[choice3]} and {self.choiceConvert[choice1]}:")
        elif choice1 == choice3:
            if choice1 == 6:
                print("Here are all the students:")
            elif choice2 == 6:
                print("Here are all the students")
            elif choice1 == 0:
                print(f"Here are the students from {self.choiceConvert[choice2]}")
            else:
                print(f"Here are the students from {self.choiceConvert[choice1]} and {self.choiceConvert[choice2]}:")
        elif choice2 == choice3:
            if choice1 == 6:
                print("Here are all the students:")
            elif choice2 == 6:
                print("Here are all the students")
            elif choice1 == 0:
                print(f"Here are the students from {self.choiceConvert[choice2]}")
            else:
                print(f"Here are the students from {self.choiceConvert[choice1]} and {self.choiceConvert[choice2]}:")
        elif choice1 or choice2 or choice3 == 6:
            print(f"Here are all students:")
        else:
            print(f"Here are the students from {self.choiceConvert[choice1]}, {self.choiceConvert[choice2]}, and {self.choiceConvert[choice3]}:")

        if choice1 == 1:
            choice1_1_checker = True
            if choice2 == 6:
                print()
            elif choice3 == 6:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '63':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice1 == 2:
            if choice2 == 6:
                print()
            elif choice3 == 6:
                print()
            else:
                choice1_2_checker = True
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '66':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice1 == 3:
            if choice2 == 6:
                print()
            elif choice3 == 6:
                print()
            else:
                choice1_3_checker = True
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '65':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice1 == 4:
            if choice2 == 6:
                print()
            elif choice3 == 6:
                print()
            else:
                choice1_4_checker = True
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '62':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice1 == 5:
            if choice2 == 6:
                print()
            elif choice3 == 6:
                print()
            else:
                choice1_5_checker = True
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '60':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice1 == 6:
            all_checker = True
            for i in range(len(self.numbers)):
                    print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")
            self.mainMenu()

        if choice1 == 0:
            print()

        if choice2 == 1:
            if choice3 == 6:
                print()
            else:
                choice2_1_checker = True
                if choice1_1_checker == False:
                    for i in range(len(self.numbers)):
                        if str(self.numbers[i])[0:2] == '63':
                            print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice2 == 2:
            if choice3 == 6:
                print()
            else:
                if choice1_2_checker:
                    print()
                else:
                    choice2_2_checker = True
                    for i in range(len(self.numbers)):
                        if str(self.numbers[i])[0:2] == '66':
                            print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice2 == 3:
            if choice3 == 6:
                print()
            else:
                choice2_3_checker = True
                if choice1_3_checker == False:
                    for i in range(len(self.numbers)):
                        if str(self.numbers[i])[0:2] == '65':
                            print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice2 == 4:
            if choice3 == 6:
                print()
            else:
                choice2_4_checker = True
                if choice1_4_checker == False:
                    for i in range(len(self.numbers)):
                        if str(self.numbers[i])[0:2] == '62':
                            print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice2 == 5:
            if choice3 == 6:
                print()
            else:
                choice2_5_checker = True
                if choice1_5_checker == False:
                    for i in range(len(self.numbers)):
                        if str(self.numbers[i])[0:2] == '60':
                            print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice2 == 6:
            for i in range(len(self.numbers)):
                if all_checker == False:
                    print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")
            self.mainMenu()

        if choice2 == 0:
            print()

        if choice3 == 1:
            if choice1_1_checker:
                if choice2_1_checker:
                    print()
            elif choice2_1_checker:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '63':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice3 == 2:
            if choice1_2_checker:
                if choice2_2_checker:
                    print()
            elif choice2_2_checker:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '66':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice3 == 3:
            if choice1_3_checker:
                if choice2_3_checker:
                    print()
            elif choice2_3_checker:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '65':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice3 == 4:
            if choice1_4_checker:
                if choice2_4_checker:
                    print()
            elif choice2_4_checker:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '62':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice3 == 5:
            if choice1_5_checker:
                if choice2_5_checker:
                    print()
            elif choice2_5_checker:
                print()
            else:
                for i in range(len(self.numbers)):
                    if str(self.numbers[i])[0:2] == '60':
                        print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")

        if choice3 == 6:
            for i in range(len(self.numbers)):
                if all_checker == False:
                    print(f"{self.surnames[i]}, {self.first_names[i]}, with student number {self.student_numbers[i]}, is a {self.occupations[i]}. {self.genderConvert[self.genders[i]]} phone number is {self.numbers[i]}")
            self.mainMenu()
        if choice3 == 7:
            print()

        self.mainMenu()
run = Phonebook()
run.mainMenu()