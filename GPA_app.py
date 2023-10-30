#Nicholas Schuhmacher
#GPA App
#Progam gathers student info and GPA and gives a response based on input

#This will ask for your last name and if its ZZZ it ends
last_name = input("What is your last name: ")
if last_name == "ZZZ":
    print("Grades not available for user")
#This asks for your first name and GPA and if it above a certain number you get a specific response
else:
    first_name =input("What is your first name: ")
    GPA = float(input("What is your GPA: "))
    if GPA >= 3.5:
        print("You have made the Dean's List!")
    elif GPA >= 3.25:
        print("You have made the Honor Roll!")


