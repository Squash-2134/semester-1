
# Week 1.3, Session 2: Write User Information to a File

# Prompt the user for their name, age, and favorite colour
name = input("Enter your name: ")
age = input("Enter your age: ")
colour = input("Enter your favourite colour: ")

# Open user_info.txt for writing
with open("user_info.txt", "w") as file:

    # Write each piece of information on a new line
    file.write(name + "\n")
    file.write(age + "\n")
    file.write(colour + "\n")
