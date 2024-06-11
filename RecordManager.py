import pickle

def AddRec():
    ch = "Y"
    while ch == "Y" or ch == "y":
        i=int(input("Enter Student_id "))
        n=input("Enter Student_name ")
        m=int(input("Enter Student_marks "))
        rec=[i,n,m]
        f=open("Student.dat",'ab')
        pickle.dump(rec,f)
        ch = input("Do You wish to Enter more Records (Y/N) ")
        if ch == "Nn":
            break
        f.close()
        

def DisplayRec():
    f=open("Student.dat" , "rb")
    while True:
        try:
            rec=pickle.load(f)
            for i in rec:
                print(i,end=" ")
            print()
        except EOFError:
            break
    f.close()

def SearchRec(): 
    r=int(input("Enter Student_id to search "))
    f=open("Student.dat" , "rb")
    flag = False
    while True:
        try:
            rec=pickle.load(f)
            for i in rec:
                if i[0]==r:
                    print("Record Found-> ", i)
                    flag = True
        except EOFError:
            break
    if flag == False:
        print("No File Found!")
    f.close()
    

while True:
    print("Main_Menu")
    print("1-AddRec")
    print("2-DisplayRec")
    print("3-SearchRec")
    print("4-Exit")
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
    