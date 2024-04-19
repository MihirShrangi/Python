x = int(input("Enter Any number:"))

match x:
    case 0:
        print("Case 1 is running")
    case 1:
        print("case 2 is running")
    case _:
        print("Defualt id Running")
