def main():
    birth_rate = 8
    death_rate = 12
    migrant_rate = 670
    number_of_seconds_per_day = 24*60*60

    date_of_population = int(input("Please enter the population on 08/29/2020"))
    total_no_of_days = int(input("Enter number of days since last count"))

    net_rate = 1/birth_rate + 1/migrant_rate - 1/death_rate

    net_rate_per_day = net_rate * number_of_seconds_per_day

    estimated_population = net_rate_per_day * total_no_of_days

    print(estimated_population)


if __name__ == "__main__":
    main()