import random
import csv


def writefh():
    with open("bot.txt", "a")as fh:
        fh.write(name1.upper() + "," + id + "\n")
        fh.close()
    cont()


def readfh():
    def main():
        with open("bot.txt", "r") as file:
            file_reader = csv.reader(file)
            user_find(file_reader)
            file.close()

    def user_find(file):
        for row in file:
            if row[0] == fullname:
                print("username found", fullname)
                user_found = [row[0], row[1]]
                poli_check(user_found)
                print(bot(), "Do you want your Details? Y/N")
                yn = input(user(), )
                if yn == "y" or yn == "Y" or yn == "Yes" or yn == "yes":
                    filename=fullname+".txt"
                    with open(filename, "w") as f:
                        print(bot(), fullname + ".txt")
                        f.write("Hi " + fullname.upper())
                        f.close()
                cont()
                break
            else:
                pass

    def poli_check(user_found):
        if user_found[1] == polnum:
            return "Policy Number Match"
        else:
            pass

    main()


def enternameandpoli():
    global fullname, polnum
    print(bot(), "enter your full name:")
    print(user(), end="")
    fullname = input()
    print(bot(), "enter your policy number:")
    print(user(), end="")
    polnum = input()
    readfh()


def bot():
    return "Bot :"


def user():
    return "user :"


def username():
    print(user(), "I am ", end="")
    username = input()
    return username


def new():
    global num, id, name1
    name1 = input("Enter your full name:")
    first = name1.split()

    alpha = random.sample(range(65, 90), 1)
    for i in alpha:
        ch = chr(i)

    randomlist = random.sample(range(11111, 99999), 1)
    for i in randomlist:
        num = i

    id = first[0].lower() + "-" + ch + "-" + str(num)
    print(id)

    writefh()



def buy():
    enternameandpoli()


def renew():
    enternameandpoli()


def looking():
    enternameandpoli()


def interact():
    print("-------------------------------------------------------")
    print(bot(), end="")
    print("\t1.Get a new Quote")
    print("\t2.Buy a policy(has a Zion Quote)")
    print("\t3.Renew his Existing Policy")
    print("\t4.Looking for documents for his Existing Policy")
    print("-------------------------------------------------------")
    ch = int(input("Choose your status: "))
    if ch == 1:
        new()

    elif ch == 2:
        buy()

    elif ch == 3:
        renew()

    elif ch == 4:
        looking()

    else:
        print(bot(), "Please choose a valid option:")
        interact()


def botwrite():
    global name
    print(bot(), "Hi!!Great to meet u!! your full name?")
    name = str(username())
    print(bot(), name.upper(), ",zion is a great insurance provider for automoblies,You car/bike?")
    vechicle = input(user(), )
    interact()


def cont():
    print("Are you sure you want to continue? Y/N")
    temp = str(input(user()))
    if temp == "Y" or temp == "y" or temp == "yes" or temp == "YES":
        interact()
    else:
        print(bot(), "Thank You")


botwrite()