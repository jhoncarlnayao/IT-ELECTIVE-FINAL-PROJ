import random
import time
import os


dogs = {}
cats = {}
puppies = {}
kittens = {}
hamster = {}


def colorcoding():

    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    # Bold text colors
    BOLD_BLACK = '\033[1;30m'
    BOLD_RED = '\033[1;31m'
    BOLD_GREEN = '\033[1;32m'
    BOLD_YELLOW = '\033[1;33m'
    BOLD_BLUE = '\033[1;34m'
    BOLD_MAGENTA = '\033[1;35m'
    BOLD_CYAN = '\033[1;36m'
    BOLD_WHITE = '\033[1;37m'

    # Background colors

    BRIGHT_BACKGROUND_BLACK = '\033[100m'
    BRIGHT_BACKGROUND_RED = '\033[101m'
    BRIGHT_BACKGROUND_GREEN = '\033[102m'
    BRIGHT_BACKGROUND_YELLOW = '\033[103m'
    BRIGHT_BACKGROUND_BLUE = '\033[104m'
    BRIGHT_BACKGROUND_MAGENTA = '\033[105m'
    BRIGHT_BACKGROUND_CYAN = '\033[106m'
    BRIGHT_BACKGROUND_WHITE = '\033[107m'

    # Reset color to default
    ENDC = '\033[0m'


def clearconsole():
    os.system('cls' if os.name == 'nt' else 'clear')

# ==============================================PET COMPANION LOG==============================
clearfileadopt=(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt")
clearfilepet = r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt"
def petcompanionlog(clearfileadopt,clearfilepet):
    while True:
        print("╔══════════════════════════════╗")
        print("\033[102m\033[1;37m║       PET COMPANION LOG      ║\033[0m")
        print("╠══════════════════════════════╣")
        choice = input(
            "[1]:Pet History\n[2]:Adopt History\n[3]:Return Main Menu \nEnter your choice here: ")
        print("╚══════════════════════════════╝")
        clearconsole()
        if choice == "1":
            print("╔══════════════════════════════╗")
            print("\033[102m║        PET HISTORY           ║\033[0m")
            print("╠══════════════════════════════╣")
            choice = input(
                "[1]: See History\n[2]: Return \nEnter your choice here: ")
            print("╚══════════════════════════════╝")
            print("\n")
            clearconsole()
            if choice == "1":
                print("╔══════════════════════════╗")
                print("\033[103m║   CURRENT PET HISTORY    ║\033[0m")
                print("╚══════════════════════════╝")
                with open (r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "r") as file:
                    content = file.read()
                    print(content)
                choice=input("[1]: Clear history\n[2]: Return\nEnter your choice here:")
                if choice=="1":
                    
                    clearfilepet = r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt"
                    with open(clearfilepet, "w") as file:
                        file.truncate()
                    print("\033[1;32mHistory in PET HISTORY has been cleared.\033[0m")
                    input("\033[1;32mPress enter to continue.\033[0m")
                    clearconsole()
                elif choice=="2":
                    clearconsole()
                    return petcompanionlog(clearfileadopt,clearfilepet)
                else:
                 print("\033[1;31mInvalid Choice. Please try again\033[0m")
                
            elif choice=="2":
                clearconsole()
                return petcompanionlog(clearfileadopt,clearfilepet)
            
            else:
                print("\033[1;31mInvalid Choice. Please try again\033[0m")
           
        elif choice == "2":
            print("╔══════════════════════════╗")
            print("\033[105m║      ADOPT HISTORY       ║\033[0m")
            print("╠══════════════════════════╣")
            choice = input(
                "[1]: See History\n[2]: Return\nEnter your choice here: ")
            print("╚══════════════════════════╝")
            print("\n")
            clearconsole()
            if choice == "1":
                print("╔══════════════════════════╗")
                print("\033[106m║  CURRENT ADOPT HISTORY   ║\033[0m")
                print("╚══════════════════════════╝")
                with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "r") as file:
                    content = file.read()
                    print(content)
                choice=input("[1]: Clear history\n[2]: Return\nEnter your choice here:")
                if choice=="1":
                    clearfileadopt = r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt"
                    with open(clearfileadopt, "w") as file:
                        file.truncate()
                    print("\033[1;32mHistory in ADOPT HISTORY has been cleared.\033[0m")
                    input("\033[1;32mPress enter to continue.\033[0m")
                    clearconsole()
                    
                elif choice=="2":
                    clearconsole()
                    return petcompanionlog(clearfileadopt,clearfilepet)
                else:
                 print("\033[1;31mInvalid Choice. Please try again\033[0m")
                    
                
            elif choice=="2":
                clearconsole()
                return petcompanionlog(clearfileadopt,clearfilepet)
        elif choice=="3":
            return main()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")
                    
           

# ============================================END PET COMPANION LOG=================================
# ===================================================EDIT PET DETAILS======================================


def edit():

    while True:
        print("╔══════════════════════════╗")
        print("\033[104m║     EDIT PET DETAILS     ║\033[0m")
        print("╠══════════════════════════╣")
        print("     [1]:Dogs               ")
        print("     [2]:Cats               ")
        print("     [3]:Kittens            ")
        print("     [4]:Puppies            ")
        print("     [5]:Hamster            ")
        print("     [6]:Return Main Menu   ")
        print("╚══════════════════════════╝")
        edit = input("Enter your choice here: ")
        if edit == "1":
            editdogs()
        elif edit == "2":
            editcats()
        elif edit == "3":
            editkittens()
        elif edit == "4":
            editpuppies()
        elif edit == "5":
            edithamsters()
        elif edit == "6":
            clearconsole()
            return main()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")
# =======================================================END EDIT PET DETAILS===================================
# ===============================================ADD PET MENU==========================================


def addpet():
    while True:
        print("╔══════════════════════════╗")
        print("\033[103m\033[1;37m║        ADD A PET         ║\033[0m")
        print("╠══════════════════════════╣")
        print("        [1]: Dogs")
        print("        [2]: Cats")
        print("        [3]: Kittens")
        print("        [4]: Puppies")
        print("        [5]: Hamster")
        print("        [6]: Return Main Menu")
        print("╚══════════════════════════╝")
        choice = input("Enter your choice here: ")

        if choice == "1":
            addpetdogs()
        elif choice == "2":
            addpetcats()
        elif choice == "3":
            addpetkittens()
        elif choice == "4":
            addpetpuppies()
        elif choice == "5":
            addpethamsters()
        elif choice == "6":
            clearconsole()
            return main()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")

# ==================================================END ADD PET MENU========================================

# ===========================================ADD PET===============================================


def addpetdogs():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[107m\033[44m║         DOGS AREA        ║\033[0m")
    print("╠══════════════════════════╣")

    while True:
        cont = input(
            "[1]: Continue Filling up Information\n[2]: Return\nEnter you choice here: ")
        print("╚══════════════════════════╝")
        print()
        if cont == "1":
            print("\033[1;34mDogs Information\033[0m")
            name = input("Name: ")
            breed = input("Breed: ")
            gender = input("Male or Female: ")
            size = input("Size: ")
            age = input("Age: ")
            dogs[name] = breed, gender, size, age
            print()
            print(
                f"\033[1;34m{name} \033[1;32mhas been added to the list of dogs successfully.\033[0m")
            input("\033[1;32mPress enter to continue.\033[0m")
            clearconsole()
            print()

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "w") as file:
                file.write("Dog Information:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")

            break

        elif cont == "2":
            clearconsole()
            return addpet()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


def addpetcats():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[105m║         CATS AREA        ║\033[0m")
    print("╠══════════════════════════╣")
    while True:
        cont = input(
            "[1]: Continue Filling up Information\n[2]: Return\nEnter you choice here: ")
        print("╚══════════════════════════╝")
        print()
        if cont == "1":
            print("\033[1;35mCats Information\033[0m")
            name = input("Name: ")
            breed = input("Breed: ")
            gender = input("Male or Female: ")
            size = input("Size: ")
            age = input("Age: ")
            cats[name] = breed, gender, size, age
            print()
            print(
                f"\033[1;35m{name}\033[0m \033[1;32mhas been added to the list of cats successfully.\033[0m")
            input("\033[1;32mPress enter to continue.\033[0m")
            clearconsole()
            print()

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "w") as file:
                file.write("Cat Information:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
            break
        elif cont == "2":
            clearconsole()
            return addpet()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


def addpetkittens():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[103m'\033[1;33m║       KITTENS AREA       ║\033[0m")
    print("╠══════════════════════════╣")
    while True:
        cont = input(
            "[1]: Continue Filling up Information\n[2]: Return\nEnter you choice here: ")
        print("╚══════════════════════════╝")
        print()
        if cont == "1":
            print("\033[1;33mKitten Information\033[0m")
            name = input("Name: ")
            breed = input("Breed: ")
            gender = input("Male or Female: ")
            size = input("Size: ")
            age = input("Age: ")
            kittens[name] = breed, gender, size, age
            print()
            print(
                f"\033[1;33m{name}\033[0m \033[1;32mhas been added to the list of kittens successfully.\033[0m")
            input("\033[1;32mPress enter to continue.\033[0m")
            clearconsole()
            print()

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "w") as file:
                file.write("Kitten Information:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
            break
        elif cont == "2":
            clearconsole()
            return addpet()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


def addpetpuppies():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[102m║       PUPPIES AREA       ║\033[0m")
    print("╠══════════════════════════╣")
    while True:
        cont = input(
            "[1]: Continue Filling up Information\n[2]: Return\nEnter you choice here: ")
        print("╚══════════════════════════╝")
        print()

        if cont == "1":
            print("\033[1;32mPuppie Information\033[0m")
            name = input("Name: ")
            breed = input("Breed: ")
            gender = input("Male or Female: ")
            size = input("Size: ")
            age = input("Age: ")
            puppies[name] = breed, gender, size, age
            print()
            print(
                f"\033[1;32m{name} has been added to the list of puppies successfully.\033[0m")
            input("\033[1;32mPress enter to continue.\033[0m")
            clearconsole()

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "w") as file:
                file.write("Puppie Information:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
            break
        elif cont == "2":
            clearconsole()
            return addpet()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


def addpethamsters():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[106m║       HAMSTERS AREA      ║\033[0m")
    print("╠══════════════════════════╣")
    while True:
        cont = input(
            "[1]: Continue Filling up Information\n[2]: Return\nEnter you choice here: ")
        print("╚══════════════════════════╝")
        print()
        if cont == "1":
            print("\033[1;34mHamster Information\033[0m")
            name = input("Name: ")
            breed = input("Breed: ")
            gender = input("Male or Female: ")
            size = input("Size: ")
            age = input("Age: ")
            hamster[name] = breed, gender, size, age
            print()
            print(
                f"\033[1;34m{name}\033[0m \033[1;32mhas been added to the list of hamsters successfully.\033[0m")
            input("\033[1;32mPress enter to continue.\033[0m")
            clearconsole()
            print()

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\history.txt", "w") as file:
                file.write("Hamster Information:\n")
                file.write(f"Name: {name}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
            break
        elif cont == "2":
            clearconsole()
            return addpet()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


# ==============================================END ADD PET ============================================

# ============================================BROWSE PETS================================================

def browsepetdogs():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[107m\033[44m║        CURRENT DOGS:     ║\033[0m")
    print("╚══════════════════════════╝")
    if not dogs:
        print("\033[1;31mNo dogs available\033[0m\n")
    for name, (breed, gender, size, age) in dogs.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size    : {size}")
        print(f"Age     : {age}")
        print()

        print("Press enter to continue")
        input()
        clearconsole()
        main()


def browsepetcats():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[105m║        CURRENT CATS:     ║\033[0m")
    print("╚══════════════════════════╝")
    if not cats:
        print("\033[1;31mNo cats available\033[0m\n")
    for name, (breed, gender, size, age) in cats.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size    : {size}")
        print(f"Age     : {age}")
        print()

        print("Press enter to continue")
        clearconsole()
        input()
        main()


def browsepetpuppies():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[102m║      CURRENT PUPPIES:    ║\033[0m")
    print("╚══════════════════════════╝")
    if not puppies:
        print("\033[1;31mNo puppies available\033[0m\n")
    for name, (breed, gender, size, age) in puppies.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size    : {size}")
        print(f"Age     : {age}")
        print()

        print("Press enter to continue")
        clearconsole()
        input()
        main()


def browsepetkittens():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[103m'\033[1;33m║      CURRENT KITTENS:    ║\033[0m")
    print("╚══════════════════════════╝")
    if not kittens:
        print("\033[1;31mNo kittens available\033[0m\n")
    for name, (breed, gender, size, age) in kittens.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size    : {size}")
        print(f"Age     : {age}")
        print()
        
        print("Press enter to continue")
        clearconsole()
        input()
        main()



def browsepethamsters():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[106m║      CURRENT HAMSTERS:   ║\033[0m")
    print("╚══════════════════════════╝")
    if not hamster:
        print("\033[1;31mNo hamsters available\033[0m\n")
    for name, (breed, gender, size, age) in hamster.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size    : {size}")
        print(f"Age     : {age}")
        print()

        print("Press enter to continue")
        clearconsole()
        input()
        main()


# =============================================END BROWSE PETS=================================================

# ================================================EDIT PET DETAILS=================================================


def editdogs():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[107m\033[44m║    CURRENT DOGS LIST     ║\033[0m")
    print("╚══════════════════════════╝")
    if not dogs:
        print(
            "\033[1;31mSorry, there are no dogs available for editing at the moment.\033[0m\n")
        input(
            "\033[1;31mPress enter to return to the menu for editing pet information.\033[0m")
        clearconsole()
        return edit()
    for name, (breed, gender, size, age) in dogs.items():
        print(f"Dog Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size  : {size}")
        print(f"Age   : {age}")
        print()

    selected_name = input("Enter the name of the dog you want to update: ")

    if selected_name in dogs:
        print(f"Editing details for {selected_name}:\n")

        # Display current details
        print(f"Dog Name: {selected_name}")
        print(f"Breed   : {dogs[selected_name][0]}")
        print(f"Gender  : {dogs[selected_name][1]}")
        print(f"Size  : {dogs[selected_name][2]}")
        print(f"Age   : {dogs[selected_name][3]}")
        print()

        new_breed = input("Update Breed: ")
        new_gender = input("Update Gender: ")
        new_size = input("Update Size: ")
        new_age = input("Update Age: ")

        dogs[selected_name] = (new_breed, new_gender, new_size, new_age)

        print(f"{selected_name}'s details updated successfully.")
    else:
        print(f"Dog with name {selected_name} not found.")


def editcats():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[105m║    CURRENT CATS LIST     ║\033[0m")
    print("╚══════════════════════════╝")
    if not cats:
        print(
            "\033[1;31mSorry, there are no cats available for editing at the moment.\033[0m\n")
        input(
            "\033[1;31mPress enter to return to the menu for editing pet information.\033[0m")
        clearconsole()
        return edit()
    for name, (breed, gender, size, age) in cats.items():
        print(f"Cat Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size  : {size}")
        print(f"Age   : {age}")
        print()

    selected_name = input("Enter the name of the cat you want to update: ")

    if selected_name in cats:
        print(f"Editing details for {selected_name}:\n")

        # Display current details
        print(f"Cat Name: {selected_name}")
        print(f"Breed   : {cats[selected_name][0]}")
        print(f"Gender  : {cats[selected_name][1]}")
        print(f"Size  : {cats[selected_name][2]}")
        print(f"Age   : {cats[selected_name][3]}")
        print()

        new_breed = input("Update Breed: ")
        new_gender = input("Update Gender: ")
        new_size = input("Update Size: ")
        new_age = input("Update Age: ")

        cats[selected_name] = (new_breed, new_gender, new_size, new_age)

        print(f"{selected_name}'s details updated successfully.")
    else:
        print(f"Dog with name {selected_name} not found.")


def editpuppies():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[102m║  CURRENT PUPPIES LIST    ║\033[0m")
    print("╚══════════════════════════╝")
    if not puppies:
        print(
            "\033[1;31mSorry, there are no puppies available for editing at the moment.\033[0m\n")
        input(
            "\033[1;31mPress enter to return to the menu for editing pet information.\033[0m")
        clearconsole()
        return edit()
    for name, (breed, gender, size, age) in puppies.items():
        print(f"Puppie Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size  : {size}")
        print(f"Age   : {age}")
        print()

    selected_name = input("Enter the name of the Puppie you want to update: ")

    if selected_name in dogs:
        print(f"Editing details for {selected_name}:\n")

        # Display current details
        print(f"Puppie Name: {selected_name}")
        print(f"Breed   : {puppies[selected_name][0]}")
        print(f"Gender  : {puppies[selected_name][1]}")
        print(f"Size  : {puppies[selected_name][2]}")
        print(f"Age   : {puppies[selected_name][3]}")
        print()

        new_breed = input("Update Breed: ")
        new_gender = input("Update Gender: ")
        new_size = input("Update Size: ")
        new_age = input("Update Age: ")

        puppies[selected_name] = (new_breed, new_gender, new_size, new_age)

        print(f"{selected_name}'s details updated successfully.")
    else:
        print(f"Dog with name {selected_name} not found.")


def editkittens():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[103m'\033[1;33m║   CURRENT KITTENS LIST   ║\033[0m")
    print("╚══════════════════════════╝")
    if not kittens:
        print(
            "\033[1;31mSorry, there are no kittens available for editing at the moment.\033[0m\n")
        input(
            "\033[1;31mPress enter to return to the menu for editing pet information.\033[0m")
        clearconsole()
        return edit()
    for name, (breed, gender, size, age) in kittens.items():
        print(f"Puppie Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size  : {size}")
        print(f"Age   : {age}")
        print()

    selected_name = input("Enter the name of the kittens you want to update: ")

    if selected_name in dogs:
        print(f"Editing details for {selected_name}:\n")

        # Display current details
        print(f"Puppie Name: {selected_name}")
        print(f"Breed   : {kittens[selected_name][0]}")
        print(f"Gender  : {kittens[selected_name][1]}")
        print(f"Size  : {kittens[selected_name][2]}")
        print(f"Age   : {kittens[selected_name][3]}")
        print()

        new_breed = input("Update Breed: ")
        new_gender = input("Update Gender: ")
        new_size = input("Update Size: ")
        new_age = input("Update Age: ")

        kittens[selected_name] = (new_breed, new_gender, new_size, new_age)

        print(f"{selected_name}'s details updated successfully.")
    else:
        print(f"Dog with name {selected_name} not found.")


def edithamsters():
    clearconsole()
    print("╔══════════════════════════╗")
    print("\033[47m\033[106m║   CURRENT HAMSTERS LIST  ║\033[0m")
    print("╚══════════════════════════╝")
    if not hamster:
        print(
            "\033[1;31mSorry, there are no hamsters available for editing at the moment.\033[0m\n")
        input(
            "\033[1;31mPress enter to return to the menu for editing pet information.\033[0m")
        clearconsole()
        return edit()
    for name, (breed, gender, size, age) in hamster.items():
        print(f"Hamster Name: {name} ")
        print(f"Breed   : {breed}")
        print(f"Gender  : {gender}")
        print(f"Size  : {size}")
        print(f"Age   : {age}")
        print()

    selected_name = input("Enter the name of the Hamster you want to update: ")

    if selected_name in dogs:
        print(f"Editing details for {selected_name}:\n")

        # Display current details
        print(f"Puppie Name: {selected_name}")
        print(f"Breed   : {hamster[selected_name][0]}")
        print(f"Gender  : {hamster[selected_name][1]}")
        print(f"Size  : {hamster[selected_name][2]}")
        print(f"Age   : {hamster[selected_name][3]}")
        print()

        new_breed = input("Update Breed: ")
        new_gender = input("Update Gender: ")
        new_size = input("Update Size: ")
        new_age = input("Update Age: ")

        hamster[selected_name] = (new_breed, new_gender, new_size, new_age)

        print(f"{selected_name}'s details updated successfully.")
    else:
        print(f"Dog with name {selected_name} not found.")


# =================================================END PET DETAILS====================================================

# ==================================================ADOPT PET===========================================================


def adoptpet():
    clearconsole()
    while True:
        print("╔══════════════════════════╗")
        print(f"\033[103m║        BROWSE PETS       ║\033[0m")
        print("╚══════════════════════════╝")
        print("       [1]: Dogs")
        print("       [2]: Cats")
        print("       [3]: Kittens")
        print("       [4]: Puppies")
        print("       [5]: Hamster")
        print("       [6]: Return Main menu")
        print("╚══════════════════════════╝")
        choice = input("Enter your choice here: ")
        clearconsole()
        print()

        if choice == "1":
            print("╔══════════════════════════╗")
            print("\033[107m\033[44m║    CURRENT DOGS LIST     ║\033[0m")
            print("╚══════════════════════════╝")
            if not dogs:
                print(
                    "\033[1;31mSorry, there are no dogs available for adoption at the moment.\033[0m\n")
                input(
                    "\033[1;31mPress enter to return to the adoption menu.\033[0m")
                return adoptpet()
            for name, (breed, gender, size, age) in dogs.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size    : {size}")
                print(f"Age     : {age}")
                print()

            print()
            print("Adoption Paper ")
            print("Fill up this Form: ")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            typepet = input("Dog's Name: ")
            breed = input("Breed: ")
            age = input("Age: ")
            size = input("Size: ")
            gender = input("Gender: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            nameperson = input("Name of Person: ")
            contactnum = input("Contact Number: ")
            address = input("Residential Address: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            exp = input("Previous experience with pets y/n: ")
            petowned = input("Any other pets currently owned y/n: ")
            print("╚════════════════════════╝")
            print("\n")
            clearconsole()
            input("Press Enter to submit your information and complete the details.")

            input("You can now view all the information you've provided.")

            print(f"{nameperson} ADOPTION PAPER")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            print(f"Type of Pet: {typepet}")
            print(f"Breed: {breed}")
            print(f"Age: {age}")
            print(f"Size: {size}")
            print(f"Gender: {gender}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            print(f"Name of Person: {nameperson}")
            print(f"Contact Number: {contactnum}")
            print(f"Residential Address: {address}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            print(f"Previous experience with pets: {exp}")
            print(f"Any other pets currently owned: {petowned}")
            print("╚════════════════════════╝")
            print("\n")

            print("Press Enter to complete the adoption process.")
            if typepet in dogs:
                adoptpett = dogs.pop(typepet)
                print(f"You have successfully adopted {typepet}")
            else:
                print(f"Sorry, {typepet} is not available for adoption.")

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "w") as file:
                file.write("Dog Information:\n")
                file.write(f"Name: {typepet}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
                file.write("\n")
                file.write(f"{nameperson} Information:\n")
                file.write(f"Fullname: {nameperson}\n")
                file.write(f"Contac Number: {contactnum}\n")
                file.write(f"Residential Address: {address}\n")
                file.write(f"Previous experience with pets: {exp}\n")
                file.write(f"Any other pets currently owned: {petowned}\n")
            input("")
            clearconsole()
            main()

        elif choice == "2":
            print("╔══════════════════════════╗")
            print("\033[47m\033[105m║    CURRENT CATS LIST     ║\033[0m")
            print("╚══════════════════════════╝")
            if not cats:
                print(
                    "\033[1;31mSorry, there are no cats available for adoption at the moment.\033[0m\n")
                input(
                    "\033[1;31mPress enter to return to the adoption menu.\033[0m")
                return adoptpet()
            for name, (breed, gender, size, age) in cats.items():
                print(f"Cat Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size    : {size}")
                print(f"Age     : {age}")

                print()
            print("Adoption Paper ")
            print("Fill up this Form: ")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            typepet = input("Cat's Name: ")
            breed = input("Breed: ")
            age = input("Age: ")
            size = input("Size: ")
            gender = input("Gender: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            nameperson = input("Name of Person: ")
            contactnum = input("Contact Number: ")
            address = input("Residential Address: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            exp = input("Previous experience with pets y/n: ")
            petowned = input("Any other pets currently owned y/n: ")
            print("╚════════════════════════╝")
            print("\n")
            clearconsole()
            input("Press Enter to submit your information and complete the details.")

            input("You can now view all the information you've provided.")

            print(f"{nameperson} ADOPTION PAPER")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            print(f"Type of Pet: {typepet}")
            print(f"Breed: {breed}")
            print(f"Age: {age}")
            print(f"Size: {size}")
            print(f"Gender: {gender}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            print(f"Name of Person: {nameperson}")
            print(f"Contact Number: {contactnum}")
            print(f"Residential Address: {address}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            print(f"Previous experience with pets: {exp}")
            print(f"Any other pets currently owned: {petowned}")
            print("╚════════════════════════╝")
            print("\n")

            print("Press Enter to complete the adoption process.")
            if typepet in cats:
                adoptpett = cats.pop(typepet)
                print(f"You have successfully adopted {typepet}")
            else:
                print(f"Sorry, {typepet} is not available for adoption.")

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "w") as file:
                file.write("Cat Information:\n")
                file.write(f"Name: {typepet}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
                file.write("\n")
                file.write(f"{nameperson} Information:\n")
                file.write(f"Fullname: {nameperson}\n")
                file.write(f"Contac Number: {contactnum}\n")
                file.write(f"Residential Address: {address}\n")
                file.write(f"Previous experience with pets: {exp}\n")
                file.write(f"Any other pets currently owned: {petowned}\n")
            input("")
            clearconsole()
            main()

        elif choice == "3":
            print("╔══════════════════════════╗")
            print("\033[103m'\033[1;33m║   CURRENT KITTENS LIST   ║\033[0m")
            print("╚══════════════════════════╝")
            if not kittens:
                print(
                    "\033[1;31mSorry, there are no kittens available for adoption at the moment.\033[0m\n")
                input(
                    "\033[1;31mPress enter to return to the adoption menu.\033[0m")
                return adoptpet()
            for name, (breed, gender, size, age) in kittens.items():
                print(f"Kitten Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size    : {size}")
                print(f"Age     : {age}")
                print()
            print("Adoption Paper ")
            print("Fill up this Form: ")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            typepet = input("Kitten's Name: ")
            breed = input("Breed: ")
            age = input("Age: ")
            size = input("Size: ")
            gender = input("Gender: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            nameperson = input("Name of Person: ")
            contactnum = input("Contact Number: ")
            address = input("Residential Address: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            exp = input("Previous experience with pets y/n: ")
            petowned = input("Any other pets currently owned y/n: ")
            print("╚════════════════════════╝")
            print("\n")
            clearconsole()
            input("Press Enter to submit your information and complete the details.")

            input("You can now view all the information you've provided.")

            print(f"{nameperson} ADOPTION PAPER")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            print(f"Type of Pet: {typepet}")
            print(f"Breed: {breed}")
            print(f"Age: {age}")
            print(f"Size: {size}")
            print(f"Gender: {gender}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            print(f"Name of Person: {nameperson}")
            print(f"Contact Number: {contactnum}")
            print(f"Residential Address: {address}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            print(f"Previous experience with pets: {exp}")
            print(f"Any other pets currently owned: {petowned}")
            print("╚════════════════════════╝")
            print("\n")

            print("Press Enter to complete the adoption process.")
            if typepet in kittens:
                adoptpett = kittens.pop(typepet)
                print(f"You have successfully adopted {typepet}")
            else:
                print(f"Sorry, {typepet} is not available for adoption.")

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "w") as file:
                file.write("Kitten Information:\n")
                file.write(f"Name: {typepet}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
                file.write("\n")
                file.write(f"{nameperson} Information:\n")
                file.write(f"Fullname: {nameperson}\n")
                file.write(f"Contac Number: {contactnum}\n")
                file.write(f"Residential Address: {address}\n")
                file.write(f"Previous experience with pets: {exp}\n")
                file.write(f"Any other pets currently owned: {petowned}\n")
            input("")
            clearconsole()
            main()

        elif choice == "4":
            print("╔══════════════════════════╗")
            print("\033[47m\033[102m║  CURRENT PUPPIES LIST    ║\033[0m")
            print("╚══════════════════════════╝")
            if not puppies:
                print(
                    "\033[1;31mSorry, there are no puppies available for adoption at the moment.\033[0m\n")
                input(
                    "\033[1;31mPress enter to return to the adoption menu.\033[0m")
                return adoptpet()
            for name, (breed, gender, size, age) in puppies.items():
                print(f"Puppie Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size    : {size}")
                print(f"Age     : {age}")

                print()
            print("Adoption Paper ")
            print("Fill up this Form: ")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            typepet = input("Puppie's Name: ")
            breed = input("Breed: ")
            age = input("Age: ")
            size = input("Size: ")
            gender = input("Gender: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            nameperson = input("Name of Person: ")
            contactnum = input("Contact Number: ")
            address = input("Residential Address: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            exp = input("Previous experience with pets y/n: ")
            petowned = input("Any other pets currently owned y/n: ")
            print("╚════════════════════════╝")
            print("\n")
            clearconsole()
            input("Press Enter to submit your information and complete the details.")

            input("You can now view all the information you've provided.")

            print(f"{nameperson} ADOPTION PAPER")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            print(f"Type of Pet: {typepet}")
            print(f"Breed: {breed}")
            print(f"Age: {age}")
            print(f"Size: {size}")
            print(f"Gender: {gender}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            print(f"Name of Person: {nameperson}")
            print(f"Contact Number: {contactnum}")
            print(f"Residential Address: {address}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            print(f"Previous experience with pets: {exp}")
            print(f"Any other pets currently owned: {petowned}")
            print("╚════════════════════════╝")
            print("\n")

            print("Press Enter to complete the adoption process.")
            if typepet in puppies:
                adoptpett = puppies.pop(typepet)
                print(f"You have successfully adopted {typepet}")
            else:
                print(f"Sorry, {typepet} is not available for adoption.")

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "w") as file:
                file.write("Puppie Information:\n")
                file.write(f"Name: {typepet}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
                file.write("\n")
                file.write(f"{nameperson} Information:\n")
                file.write(f"Fullname: {nameperson}\n")
                file.write(f"Contac Number: {contactnum}\n")
                file.write(f"Residential Address: {address}\n")
                file.write(f"Previous experience with pets: {exp}\n")
                file.write(f"Any other pets currently owned: {petowned}\n")
            input("")
            clearconsole()
            main()

        elif choice == "5":
            print("╔══════════════════════════╗")
            print("\033[47m\033[106m║   CURRENT HAMSTERS LIST  ║\033[0m")
            print("╚══════════════════════════╝")
            if not hamster:
                print(
                    "\033[1;31mSorry, there are no hamsters available for adoption at the moment.\033[0m\n")
                input(
                    "\033[1;31mPress enter to return to the adoption menu.\033[0m")
                return adoptpet()
            for name, (breed, gender, size, age) in hamster.items():
                print(f"Hamster Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size    : {size}")
                print(f"Age     : {age}")

                print()
            print("Adoption Paper ")
            print("Fill up this Form: ")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            typepet = input("Hamster's Name: ")
            breed = input("Breed: ")
            age = input("Age: ")
            size = input("Size: ")
            gender = input("Gender: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            nameperson = input("Name of Person: ")
            contactnum = input("Contact Number: ")
            address = input("Residential Address: ")
            print("╚════════════════════════╝")
            print("\n")
            input("Press enter to continue.")
            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            exp = input("Previous experience with pets y/n: ")
            petowned = input("Any other pets currently owned y/n: ")
            print("╚════════════════════════╝")
            print("\n")
            clearconsole()
            input("Press Enter to submit your information and complete the details.")

            input("You can now view all the information you've provided.")

            print(f"{nameperson} ADOPTION PAPER")
            print("╔══════════════════════════╗")
            print("║      PET INFORMATION     ║")
            print("╠══════════════════════════╣")
            print(f"Type of Pet: {typepet}")
            print(f"Breed: {breed}")
            print(f"Age: {age}")
            print(f"Size: {size}")
            print(f"Gender: {gender}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║   PERSONAL INFORMATION   ║")
            print("╠══════════════════════════╣")
            print(f"Name of Person: {nameperson}")
            print(f"Contact Number: {contactnum}")
            print(f"Residential Address: {address}")
            print("╚════════════════════════╝")
            print("\n")

            print("╔══════════════════════════╗")
            print("║  EXPERIENCE WITH PETS    ║")
            print("╠══════════════════════════╣")
            print(f"Previous experience with pets: {exp}")
            print(f"Any other pets currently owned: {petowned}")
            print("╚════════════════════════╝")
            print("\n")

            print("Press Enter to complete the adoption process.")
            if typepet in hamster:
                adoptpett = hamster.pop(typepet)
                print(f"You have successfully adopted {typepet}")
            else:
                print(f"Sorry, {typepet} is not available for adoption.")

            with open(r"C:\PYTHON2NDYEAR\PYTHONFINALPROJ\adoptedpet.txt", "w") as file:
                file.write("Cat Information:\n")
                file.write(f"Name: {typepet}\n")
                file.write(f"Breed: {breed}\n")
                file.write(f"Gender: {gender}\n")
                file.write(f"Size: {size}\n")
                file.write(f"Age: {age}\n")
                file.write("\n")
                file.write(f"{nameperson} Information:\n")
                file.write(f"Fullname: {nameperson}\n")
                file.write(f"Contac Number: {contactnum}\n")
                file.write(f"Residential Address: {address}\n")
                file.write(f"Previous experience with pets: {exp}\n")
                file.write(f"Any other pets currently owned: {petowned}\n")
            input("")
            clearconsole()
            main()

        elif choice == "6":
            return main()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


# ===================================================END ADOPT PET=========================================================

# ======================================================REMOVE PET===========================================================

def removepet():
    while True:
        print("╔══════════════════════════╗")
        print("\033[106m║  REMOVE PET LISTING AREA ║\033[0m")
        print("╠══════════════════════════╣")
        print("       [1]: Dogs")
        print("       [2]: Cats")
        print("       [3]: Kittens")
        print("       [4]: Puppies")
        print("       [5]: Hamster")
        print("       [6]: Return Main Menu")
        print("╚══════════════════════════╝")
        remove = input("Enter your choice here: ")
        clearconsole()

        if remove == "1":
            print("╔══════════════════════════╗")
            print("\033[107m\033[44m║        CURRENT DOGS:     ║\033[0m")
            print("╚══════════════════════════╝")
            if not dogs:
                print("\033[1;31mNo dogs available\033[0m\n")
            for name, (breed, gender, size, age) in dogs.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size  : {size}")
                print(f"Age   : {age}")
                print()

            removedog = input("Enter Dog name to remove: ")
            removedvalue = dogs.pop(removedog, None)
            if removedvalue is not None:
                print(f"Removed details for dog '{removedog}': {removedvalue}")
            else:
                print(f"Dog '{removedog}' not found in the dictionary.")
            return main()

        elif remove == "2":
            print("╔══════════════════════════╗")
            print("\033[47m\033[105m║        CURRENT CATS:     ║\033[0m")
            print("╚══════════════════════════╝")
            if not cats:
              print("\033[1;31mNo cats available\033[0m\n")
            for name, (breed, gender, size, age) in cats.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size  : {size}")
                print(f"Age   : {age}")
                print()

            removecats = input("Enter Cat name to remove: ")
            removedvalue = cats.pop(removecats, None)
            if removedvalue is not None:
                print(
                    f"Removed details for cat '{removecats}': {removedvalue}")
            else:
                print(f"Cat '{removecats}' not found in the dictionary.")
                return main()

        elif remove == "3":
            print("╔══════════════════════════╗")
            print("\033[103m'\033[1;33m║   CURRENT KITTENS LIST   ║\033[0m")
            print("╚══════════════════════════╝")
            if not kittens:
             print("\033[1;31mNo dogs available\033[0m\n")
            for name, (breed, gender, size, age) in kittens.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size  : {size}")
                print(f"Age   : {age}")
                print()

            removekittens = input("Enter Kitten name to remove: ")
            removedvalue = kittens.pop(removekittens, None)
            if removedvalue is not None:
                print(
                    f"Removed details for kitten '{removekittens}': {removedvalue}")
            else:
                print(f"Kitten '{removekittens}' not found in the dictionary.")
                return main()

        elif remove == "4":
            print("╔══════════════════════════╗")
            print("\033[47m\033[102m║      CURRENT PUPPIES:    ║\033[0m")
            print("╚══════════════════════════╝")
            if not puppies:
             print("\033[1;31mNo puppies available\033[0m\n")
            for name, (breed, gender, size, age) in puppies.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size  : {size}")
                print(f"Age   : {age}")
                print()

            removepuppies = input("Enter Puppie name to remove: ")
            removedvalue = puppies.pop(removepuppies, None)
            if removedvalue is not None:
                print(
                    f"Removed details for puppie '{removepuppies}': {removedvalue}")
            else:
                print(f"Puppie '{removepuppies}' not found in the dictionary.")
                return main()

        elif remove == "5":
            print("╔══════════════════════════╗")
            print("\033[47m\033[106m║   CURRENT HAMSTERS LIST  ║\033[0m")
            print("╚══════════════════════════╝")
            if not hamster:
             print("\033[1;31mNo hamsters available\033[0m\n")
            for name, (breed, gender, size, age) in hamster.items():
                print(f"Dog Name: {name} ")
                print(f"Breed   : {breed}")
                print(f"Gender  : {gender}")
                print(f"Size  : {size}")
                print(f"Age   : {age}")
                print()

            removehamster = input("Enter Hamster name to remove: ")
            removedvalue = hamster.pop(removehamster, None)
            if removedvalue is not None:
                print(
                    f"Removed details for hamster '{removehamster}': {removedvalue}")
            else:
                print(
                    f"Hamster '{removehamster}' not found in the dictionary.")
                return main()
        elif remove == "6":
            return main()
        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


# ========================================================END REMOVE PET==========================================================

# =====================================================ABOUT US=================================================================

def aboutus():
    clearconsole()
    print("╔══════════════════════════╗")
    print("║  ABOUT PET COMPANION HUB ║")
    print("╚══════════════════════════╝")

    print("Our Mission:\nTo create a community that celebrates the joy and\ncompanionship that pets bring into our lives ")
    print()
    print("Special Thank you:\nA big thank you goes to my wife, Kylie Kate J. Carpio, \nfor the contributions and support to Pet Companion Hub.")
    print()
    print("Contact information:\nEmail:jhoncarlnayaoxx@gmail.com\nPhone:09494072274")
    print()
    print("Follow us on Social Media:\nFacebook:https://web.facebook.com/Jownas21\nFacebook:https://web.facebook.com/francinekate.leones\nFacebook:https://web.facebook.com/jhoncarl.nayao/")
    print()

    print("Press enter to return in main menu")
    input()
    clearconsole()
    return main()


# ========================================================END ABOUT US=============================================================
def main():
    while True:
        print()
        print("\033[31m██████  ███████ ████████      ██████  ██████  ███    ███ ██████   █████  ███    ██ ██  ██████  ███    ██\033[0m")
        print("\033[32m██   ██ ██         ██        ██      ██    ██ ████  ████ ██   ██ ██   ██ ████   ██ ██ ██    ██ ████   ██\033[0m")
        print("\033[33m██████  █████      ██        ██      ██    ██ ██ ████ ██ ██████  ███████ ██ ██  ██ ██ ██    ██ ██ ██  ██\033[0m")
        print("\033[34m██      ██         ██        ██      ██    ██ ██  ██  ██ ██      ██   ██ ██  ██ ██ ██ ██    ██ ██  ██ ██\033[0m")
        print("\033[35m██      ███████    ██         ██████  ██████  ██      ██ ██      ██   ██ ██   ████ ██  ██████  ██   ████\033[0m")
        print("\033[36m                                                                                                                       \033[0m")
        print("\033[1;32m                                                     PET COMPANION HUB\033[0m \033[1;33m- Connecting Hearts, One Paw at a Time!\033[0m")

        print("\n\n\n\n")

        print("╔══════════════════════════════╗")
        print("\033[102m\033[1;37m║  MAIN MENU PET COMPANION HUB ║\033[0m")
        print("╠══════════════════════════════╣")
        print("[1]: Browse Pets")
        print("[2]: Adopt Pet")
        print("[3]: Add a Pet")
        print("[4]: Edit Pet Details")
        print("[5]: Remove Pet Listing")
        print("[6]: About us")
        print("[7]: Pet Companion Log")
        print("[8]: Log out / Exit")
        print("╚══════════════════════════════╝")
        choice = input("Enter your choice here: ")
        clearconsole()
        print()

        if choice == "1":
            while True:
                print("╔══════════════════════════╗")
                print(f"\033[103m║        BROWSE PETS       ║\033[0m")
                print("╠══════════════════════════╣")
                print("      [1]: Dogs")
                print("      [2]: Cats")
                print("      [3]: Kittens")
                print("      [4]: Puppies")
                print("      [5]: Hamster")
                print("      [6]: Return Main Menu")
                print("╚══════════════════════════╝")
                choice2 = input("Enter your choice here: ")
                print()

                if choice2 == "1":
                    browsepetdogs()
                elif choice2 == "2":
                    browsepetcats()
                elif choice2 == "3":
                    browsepetkittens()
                elif choice2 == "4":
                    browsepetpuppies()
                elif choice2 == "5":
                    browsepethamsters()
                elif choice2 == "6":
                    clearconsole()
                    return main()
                else:
                    print("\033[1;31mInvalid Choice. Please try again\033[0m")

        elif choice == "2":
            adoptpet()
        elif choice == "3":
            addpet()
        elif choice == "4":
            edit()
        elif choice == "5":
            removepet()
            clearconsole()
        elif choice == "6":
            aboutus()
        elif choice == "7":
            petcompanionlog(clearfileadopt,clearfilepet)

        elif choice == "8":
            seconds = 4
            print("╔══════════════════════════════════════════════╗")
            print("║  Thank you for exploring Pet Companion Hub!  ║")
            print("║       Wagging tails await your return.       ║")
            print("╚══════════════════════════════════════════════╝")
            seconds = 5
            print("Farewell, Pet Lover! Exiting gracefully...")
            for i in range(seconds):
                print(f".\n", end='')
                time.sleep(1)
            clearconsole()
            import login
            break

        else:
            print("\033[1;31mInvalid Choice. Please try again\033[0m")


main()
