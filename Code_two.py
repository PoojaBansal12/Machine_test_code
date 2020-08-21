name = input("Enter the email address: ")
name = (name.split("@")[1]).split(".")[0]

print(name)