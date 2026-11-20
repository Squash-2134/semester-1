
# Week 1.3, Session 2: Calculate Average Grade and Write to a File

# Open student_data.csv and read the data
with open("student_data.csv", "r") as file:
    data = file.readlines()

# Skip the header row
data = data[1:]

# Open report.txt for writing
with open("report.txt", "w") as report:

    # Read each student's grades and calculate their average
    for row in data:
        columns = row.strip().split(",")

        student_name = columns[1]
        mathematics = int(columns[2])
        science = int(columns[3])
        history = int(columns[4])

        average = (mathematics + science + history) / 3

        # Write the student's name and average to the report
        report.write(f"{student_name}: {average:.2f}\n")
