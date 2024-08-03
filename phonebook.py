def show_menu():
    menu_text=""
    menu_text+=("-"*5)+"Menu"+("-"*5)
    menu_text+="""
1. Insert
2. Delete
3. Search
4. Print All
5. Show This Menu
6. Exit"""
    print menu_text

def insert():
    f=open("phonebook.dat", "a")

    name = raw_input("name: ")
    pnum = raw_input("phone num: ")

    f.write(name+"|"+pnum+"\n")
    f.close()

def delete():
    print "Check the exact name by searching or printing all."
    name = raw_input("name to delete: ")
    if name == "":
        print "nothing is put in"
        return

    listLines = open("phonebook.dat", "r").readlines()
    i=0
    while i < len(listLines):
        if listLines[i].lower().find(name.lower()) != -1:
            splitedList = listLines[i].split("|")
            print splitedList[0], (splitedList[-1])[:-1]
            if raw_input("Are you sure you want to delete this?") == "yes":
                del listLines[i]
        i+=1

    open("phonebook.dat", "w").writelines(listLines)

def search():
    searchList = []
    name = raw_input("name to find: ")
    if name == "":
        print "nothing is put in."
        return

    f = open("phonebook.dat", "r")
    while True:
        line = f.readline()
        if not line:
            break

        if line.lower().find(name.lower()) != -1:
            searchList.append(line)

    f.close()
    if searchList != []:
        for x in range(0, len(searchList)):
            splitedList = searchList[x].split("|")
            print splitedList[0], (splitedList[-1])[:-1]

def print_all():
    listLines = open("phonebook.dat", "r").readlines()

    if listLines != []:
        for x in range(0, len(listLines)):
            splitedList = listLines[x].split("|")
            print splitedList[0], (splitedList[-1])[:-1]

def select_menu():
    choice = input("Choice: ")
    if choice==1:
        insert()
    elif choice==2:
        delete()
    elif choice==3:
        search()
    elif choice==4:
        print_all()
    elif choice==5:
        show_menu()
    elif choice==6:
        exit(0)
    else:
        print choice, "<- Unsupported Choice"

### __main__ ###
show_menu()
while True:
    select_menu()
