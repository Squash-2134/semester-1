
# Week 4, Session 2: Task 1

import calendar

# Original example
print(calendar.month(2025, 10))

# Two additional month() calls with different w and l values
print(calendar.month(2025, 10, w=4, l=2))
print(calendar.month(2025, 10, w=6, l=3))


# Original example of a full year calendar
print(calendar.calendar(2025))

# Three additional calendar() calls with different optional arguments
print(calendar.calendar(2025, w=3, l=1, c=4, m=3))
print(calendar.calendar(2025, w=4, l=2, c=8, m=4))
print(calendar.calendar(2025, w=5, l=3, c=10, m=2))
