
# Week 4, Session 2: Countdown

# Recursive countdown function
def countdown(n):
    """
    This recursive function prints numbers from n down to 0.

    Args:
        n : int, positive integer representing the starting number.

    Returns:
        None, prints the countdown sequence from n to 0.
    """

    # Base case
    if n < 0:
        return

    print(n)

    # Recursive case
    countdown(n - 1)


# Check if correct output is produced
countdown(30)
countdown(5)


# Equivalent function using a loop
def countdown_loop(n):
    """
    This function prints numbers from n down to 0 using a loop.

    Args:
        n : int, positive integer representing the starting number.

    Returns:
        None, prints the countdown sequence from n to 0.
    """

    for number in range(n, -1, -1):
        print(number)


# Check the loop version
countdown_loop(30)
countdown_loop(5)
