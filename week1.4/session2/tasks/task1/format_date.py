
# Week 4, Session 2: Task 1

# Write a function format_date that takes 4 arguments: day, month,
# year, separator. The separator is an optional argument with a default
# value of "-". The function returns the formatted date as a string.


def format_date(day, month, year, separator="-"):
    formatted_date = f"{day}{separator}{month}{separator}{year}"

    return formatted_date


# Test the function with different separators
print(format_date(20, 11, 2026))
print(format_date(20, 11, 2026, "/"))
print(format_date(20, 11, 2026, ":"))
print(format_date(20, 11, 2026, "."))
