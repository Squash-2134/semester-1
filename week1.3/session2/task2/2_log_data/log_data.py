# Week 1.3, Session 2: Log Data Filtering

try:
    # Open and read the file
    with open("log_data.csv", "r") as file:
        data = file.readlines()

    # Skip the header row
    for row in data[1:]:
        columns = row.strip().split(",")

        date = columns[0]
        time = columns[1]
        ip_address = columns[2]
        request = columns[4]
        status_code = columns[5]

        # Find failed login attempts
        if request == "POST /login" and status_code == "401":
            print(f"IP address {ip_address} failed to login at {time} on {date}")

except FileNotFoundError:
    print("Error: File not found.")



# Hints:
# - Remember to handle file errors
# - The first row is headers - you'll need to skip it
# - Each row has: Date, Time, IP_Address, User_Agent, Request, Status_Code
# - You need to find rows where Request = "POST /login" AND Status_Code = "401"
# - You can use list comprehension or loops to filter the data
