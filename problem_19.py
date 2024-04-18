import datetime

def firstSundays(start_year, end_year):
    count = 0
    # Iterate over years from start_year to end_year
    for year in range(start_year, end_year + 1):
        # Iterate over months from January to December
        for month in range(1, 13):
            # Create a datetime object for the first day of the month
            day = datetime.datetime(year, month, 1)
            # Check if the day is a Sunday (weekday() returns 6 for Sunday)
            if day.weekday() == 6:
                count += 1
    return count

# Get user input for the start and end years
start_year = int(input("Enter the start year: "))
end_year = int(input("Enter the end year: "))

# Call the function to get the count of Sundays falling on the first of the month
sundays_count = firstSundays(start_year, end_year)
print("Number of Sundays falling on the first of the month from {} to {}: {}".format(start_year, end_year, sundays_count))
