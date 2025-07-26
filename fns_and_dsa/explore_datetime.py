from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format and print
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    print("Current date and time:", formatted_date)

def calculate_future_date():
    try:
        # Prompt user for input
        days_to_add = int(input("Enter number of days to add: "))
        # Calculate future date
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        # Format and print
        print("Future date after", days_to_add, "days will be:", future_date.strftime('%Y-%m-%d'))
    except ValueError:
        print("Please enter a valid integer number of days.")

# Call the functions
display_current_datetime()
calculate_future_date()
