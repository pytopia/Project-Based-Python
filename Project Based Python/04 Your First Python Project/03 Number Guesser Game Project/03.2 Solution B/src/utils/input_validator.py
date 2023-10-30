def get_valid_input(prompt, start, end):
    """Get a valid integer input from the user between start and end (inclusive)."""
    while True:
        try:
            user_input = int(input(prompt))
            if start <= user_input <= end:
                return user_input
            else:
                print(f"Please enter a number between {start} and {end}.")
        except ValueError:
            print("Invalid input. Please enter a number.")
