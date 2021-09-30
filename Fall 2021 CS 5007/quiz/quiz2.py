def f1(minutes):
    # Convert Minutes to Seconds
    return minutes * 60


def f2(hours):
    # Convert Hours to Minutes
    return hours * 60


def f3(days):
    # Convert Days to Hours
    return days * 24


def f4(weeks):
    # Convert Weeks to Days
    return weeks * 7


def main():
    # Prompt the user for required inputs
    weeks = int(input("Please enter the number of weeks: "))
    days = int(input("Please enter the number of days: "))
    hours = int(input("Please enter the number of hours: "))
    minutes = int(input("Please enter the number of minutes: "))

    # convert weeks to days and add to user entered days
    days += f4(weeks)

    # convert days to hours and add to user entered hours
    hours += f3(days)

    # convert hours to minutes and add to user entered minutes
    minutes += f2(hours)

    # convert total minutes to seconds
    seconds = f1(minutes)

    # output result
    print("The total number of seconds is ", seconds)


if __name__ == "__main__":
    main()
