import pickle

def AddRec():
    pass

def DisplayRec():
    pass

def SearchRec():
    pass

while True:
    print("Main_Menu")
    print("1-AddRec")
    print("2-DisplayRec")
    print("3-SearchRec")
    print("Enter Your choice ")
    choice = int(input("Enter your choice "))
    if choice == 1:
        AddRec()
    elif choice == 2:
        DisplayRec()
    elif choice == 3:
        SearchRec()
    elif choice == 4:
        print("Thanks.. Visit Again!")
        exit()
    else:
        print("Error!")
    