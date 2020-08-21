
name = input("Enter the email address: ")
try:
    companyName = (name.split("@")[1]).split(".")[0]
    print("Your company name is: " + companyName)
except:
    print("Invalid Input!")

