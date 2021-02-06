from time import sleep

class Computer():
    def __init__(self, userName="computer", isAdmin="No", OS="Unknown", graphicCard="Unknown", status="off", sound=0,
                 language="ENG", diskMemory=256, notes=[], inch=15):

        self.userName = userName
        self.isAdmin = isAdmin
        self.OS = OS
        self.graphicCard = graphicCard
        self.status = status
        self.sound = sound
        self.language = language
        self.diskMemory = diskMemory
        self.notes = notes
        self.inch = inch

    def giveError(self):
        print("Your computer is offline. You need to turn it on in order to perform this operation.\n")

    def change_userName(self):
        if self.status == "off":
            self.giveError()
        else:
            self.userName = input("Enter new user name = ")
            print("Computer's user name has been changed.\n")

    def manage_admins(self):
        if self.status == "off":
            self.giveError()
        else:
            if self.isAdmin == "No":
                print("Do you want to promote this user to 'admin'?, (Yes, No)")
                user_input = input("Your input = ")
                if user_input.lower() == "yes":
                    self.isAdmin = "Yes"
                elif user_input.lower() == "no":
                    pass
                else:
                    print("Invalid input, please try again.")
            else:
                print("Do you want to demote this admin to 'normal user'?, (Yes, No)")
                user_input = input("Your input = ")
                if user_input.lower() == "yes":
                    self.isAdmin = "No"
                elif user_input.lower() == "no":
                    pass
                else:
                    print("Invalid input, please try again.")

    def change_OS(self):
        if self.status == "off":
            self.giveError()
        else:
            if self.OS == "Unknown":
                print("Your current Operating System is 'Unknown'. Do you want to identify your OS?, (Yes, No)")
                yn_input = input("Your input = ")
                if yn_input.lower() == "yes":
                    self.OS = input("Enter your OS = ")
                    print("Your OS is identified as", self.OS)
                elif yn_input.lower() == "no":
                    pass
                else:
                    print("Invalid input, please try again.")
            else:
                OS_input = input("Enter your new Operating System = ")
                old_OS = self.OS
                self.OS = OS_input
                print("Your OS changed successfully from {} to {}. You will be using {} from now on.".format(old_OS,
                                                                                                             self.OS,
                                                                                                             self.OS))

    def change_GraphicCard(self):
        if self.status == "off":
            self.giveError()
        else:
            if self.graphicCard == "Unknown":
                print("Your current Graphic Card is 'Unknown'. Do you want to identify your Graphic Card?, (Yes, No)")
                user_input = input("Your input = ")
                if user_input.lower() == "yes":
                    self.graphicCard = input("Enter your first Graphic Card = ")
                    print("Your Graphic Card is identified as", self.graphicCard)
                elif user_input.lower() == "no":
                    pass
                else:
                    print("Invalid input, please try again.")
            else:
                user_input2 = input("Enter your new Graphic Card = ")
                old_GC = self.graphicCard
                self.graphicCard = user_input2
                print("Your Graphic Card changed successfully from {} to {}. You will be using {} from now on.".format(
                    old_GC, user_input2, user_input2))

    def changeStatus(self):
        if self.status == "off":
            print("Your computer is off. Do you want to turn it on?, (Yes, No)")
            user_input = input("Enter = ")
            if user_input.lower() == "yes":
                self.status = "on"
                print("Your computer is turning on...")
                sleep(2)
                print("Your computer is on.")
            elif user_input.lower() == "no":
                pass
            else:
                print("Invalid input, please try again.")
        else:
            print("Your computer is on. Do you want to turn it off?, (Yes, No)")
            user_input = input("Enter = ")
            if user_input.lower() == "no":
                pass
            elif user_input.lower() == "yes":
                self.status = "off"
                print("Your computer is turning off...")
                sleep(2)
                print("Your computer is off")
            else:
                print("Invalid input, please try again.")

    def soundOptions(self):
        if self.status == "off":
            self.giveError()
        else:
            while True:
                print("""
                Sound level is currently = {}/100. 
                To increase enter '>' (+1) or '>>' (+10). 
                To decrease enter '<' (-1) or '<<' (-10). 
                To mute enter 'x'
                To exit press 'q'
                """.format(self.sound))

                sound_opt = input("Enter your option = ")
                if sound_opt == ">":
                    if self.sound + 1 <= 100:
                        self.sound += 1

                    else:
                        print("Sound level is already maximum 100/100.\n")
                elif sound_opt == ">>":
                    if self.sound + 10 >= 100:
                        self.sound = 100

                    else:
                        self.sound += 10
                elif sound_opt == "<":
                    if self.sound == 0:
                        print("Sound level is already minimum 0/100\n")
                    else:
                        self.sound -= 1

                elif sound_opt == "<<":
                    if (self.sound - 10) < 0:
                        self.sound = 0

                    else:
                        self.sound -= 10

                elif sound_opt == "x":
                    self.sound = 0

                elif sound_opt == "q":
                    break

                else:
                    print("Invalid input, please try again.")

    def changeLanguage(self):
        if self.status == "off":
            self.giveError()
        else:
            print(
                """Your computer language is currently {}. Other supported languages: 
                English (ENG) 
                German (GER) 
                Turkish (TR) 
                Spanish(SPA) 
                Italian(ITA) 
                Russian(RU)""".format(self.language))

            while True:
                language_opt = input("Enter your new language (to exit press q) = ")
                if language_opt == "q":
                    break
                elif language_opt in ["TR", "ENG", "GER", "SPA", "ITA", "RU"]:
                    self.language = language_opt
                    break
                else:
                    language_opt = input("Enter a valid language (to exit press q) = ")

    def __str__(self):
        return ("""                    
                    User's name = {}
                    Admin status = {}
                    Operating System = {}
                    Graphic Card = {}
                    Status = {}
                    Sound Level = {}/100
                    Language = {}
                    Memory Available = {} GB
                    Monitor's inch =  {}
                    
              """).format(self.userName, self.isAdmin, self.OS, self.graphicCard, self.status, self.sound,
                          self.language, self.diskMemory, self.inch)

    def __len__(self):
        return self.inch

    def check_diskMemory(self):
        if self.status == "off":
            self.giveError()
        else:
            print(myFirst.diskMemory, "GB Available")

    def addNotes(self):
        if self.status == "off":
            self.giveError()
        else:
            while True:
                if self.diskMemory == 0:
                    print("There is no space available, please clear your disk.")
                note = input("Enter what you want to save as note (to exit press 'q') = ")
                if note == "q":
                    break
                else:
                    temp = self.diskMemory
                    temp -= len(str(note))
                    if temp >= 0:
                        self.notes.append(note)
                        self.diskMemory -= len(str(note))
                    else:
                        print("There is no space available for this note, please clear your disk or try to add "
                              "shorter notes.")

    def deleteNotes(self):
        print("\nYour saved notes: \n")
        print(*self.notes, sep='\n')
        print("""
        
        To delete all the notes enter 'x'
        To delete a specific note, enter that note 
        To delete from index, enter 'i'
        To exit press 'q'
        
        """)
        while True:
            n_input = input("Enter your input = ")

            if n_input in self.notes:
                print("{} has been deleted from your notes.".format(n_input))
                self.notes.remove(n_input)

            elif n_input == "x":
                print("All of your notes are deleted.")
                self.notes = []
                break

            elif n_input == "i":
                while True:

                    if not self.notes:
                        print("There are no available notes.")
                        break

                    else:
                        index_input = int(input("Enter your index to delete (to cancel enter 'q') = "))

                        if not self.notes[index_input] == []:
                            print("{}. index ({}) has been deleted.".format(index_input, self.notes[index_input]))
                            self.notes.pop(index_input)
                        elif index_input == "q":
                            break
                        else:
                            print("Invalid input, please try again.")

            elif n_input == "q":
                break

            else:
                print("Invalid input, please try again.")

    def viewNotes(self):
        if self.status == "off":
            self.giveError()
        else:
            print("\nYour saved notes: \n")
            print(*self.notes, sep='\n')

myFirst = Computer()

if myFirst.status == "off":
    print("Your computer is currently off. You should turn it on in order to perform tasks.")

print("          Tasks are listed.")

while True:
    print("""
          To exit menu press 'q'

          0. Turn on/off your computer
          1. Show my computer's properties
          2. Change computer's user name
          3. Change computer's' operation system
          4. Change computer's graphic card
          5. Change computer's language
          6. Manage admin users
          7. Sound options
          8. Add notes
          9. Delete notes
          10. View notes
          11. Check your disk capacity

      """)

    task_no = input("Enter your task number = ")

    if task_no == "q":
        break

    if task_no == "0":
        myFirst.changeStatus()

    elif task_no == "1":
        print(myFirst)

    elif task_no == "2":
        myFirst.change_userName()

    elif task_no == "3":
        myFirst.change_OS()

    elif task_no == "4":
        myFirst.change_GraphicCard()

    elif task_no == "5":
        myFirst.changeLanguage()

    elif task_no == "6":
        myFirst.manage_admins()

    elif task_no == "7":
        myFirst.soundOptions()

    elif task_no == "8":
        myFirst.addNotes()

    elif task_no == "9":
        myFirst.deleteNotes()

    elif task_no == "10":
        myFirst.viewNotes()

    elif task_no == "11":
        myFirst.check_diskMemory()

    else:
        print("Invalid input, please try again.")
