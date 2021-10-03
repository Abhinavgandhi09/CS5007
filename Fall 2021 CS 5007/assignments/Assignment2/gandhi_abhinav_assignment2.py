

def get_data_list():
    pass


def get_monthly_average():
    pass

def find_six_highest_lowest_monthly_average_price():
    pass

def reformat_max_res():
    pass


def min_reformat_list():
    pass


def print_info():
    pass


def main():
    # Read GOOGL.csv and return 2D list
    stock_data = get_data_list()

    # compute monthly average prices for each year
    mothly_avg_prices = get_monthly_average()

    # find the 6 highest and lowest monthly avg prices
    min_max = find_six_highest_lowest_monthly_average_price()

    # reformat the highest monthly avg prices
    max_reformat_list = reformat_max_res()

    # reformat the lowest monthle avg prices
    min_reformat_list = reformat_min_res()

    # print output
    print_info()

if __name__ == "__main__":
    main()
