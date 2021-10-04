

def get_data_list():
    data_list = []  # list to store stock data
    file = open("GOOGL.csv", "r")  # open the file to read

    for line in file:
        data_list.append(line.split(','))  # read each line in file, split the string, and append to data_list

    return data_list  # return the list with stored stock data


def get_monthly_average(stock_data):
    avg_list = []  # list to store the average stock prices
    year_list = ['2016', '2017', '2018', '2019', '2020']
    month_list = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
    sum_of_prices = 0
    sum_of_vol = 0
    # print(stock_data[int(1259)][0])
    for year in range(int(len(year_list))):
        for month in range(int(len(month_list))):
            for row in range(int(len(stock_data))):
                if year_list[year] + '-' + month_list[month] in stock_data[row][0]:
                    sum_of_prices += float(stock_data[row][5]) * float(stock_data[row][6])
                    sum_of_vol += float(stock_data[row][6])
            if int(month) < 9:
                monthly_avg = [month_list[month].replace('0', '') + '/' + year_list[year], str(sum_of_prices/sum_of_vol)]
            else:
                monthly_avg = [month_list[month] + '/' + year_list[year], str(sum_of_prices / sum_of_vol)]
            avg_list.append(monthly_avg)
            sum_of_prices = 0
            sum_of_vol = 0

    # for day in stock_data:
    #     print(stock_data[row][0])
        # row += 1
    return avg_list


def find_six_highest_lowest_monthly_average_price(monthly_avg_prices):
    max_list = []
    min_list = []

    max_price = float(monthly_avg_prices[0][1])
    min_price = float(monthly_avg_prices[len(monthly_avg_prices)-1][1])

    while len(max_list) < 6:
        for row in range(len(monthly_avg_prices)):
            # print(float(monthly_avg_prices[row][1]))
            if max_price < float(monthly_avg_prices[row][1]):
                max_price = float(monthly_avg_prices[row][1])
                index = row
        max_list.append([monthly_avg_prices[index][0], str(max_price)])
        monthly_avg_prices.pop(index)
        max_price = float(monthly_avg_prices[0][1])

    i = 0
    while i < len(max_list):
        monthly_avg_prices.append(max_list[i])
        i += 1

    while len(min_list) < 6:
        for row in range(len(monthly_avg_prices)):
            if min_price > float(monthly_avg_prices[row][1]):
                min_price = float(monthly_avg_prices[row][1])
                index = row
        min_list.append([monthly_avg_prices[index][0], monthly_avg_prices[index][1]])
        monthly_avg_prices.pop(index)
        min_price = float(max_list[0][1])

    return max_list, min_list


def reformat_max_res():
    max_reformat_list = None
    return max_reformat_list


def reformat_min_res():
    min_reformat_list = None
    return min_reformat_list


def print_info():
    pass


def main():
    # Read GOOGL.csv and return 2D list
    stock_data = get_data_list()

    # compute monthly average prices for each year
    monthly_avg_prices = get_monthly_average(stock_data)

    # find the 6 highest and lowest monthly avg prices
    max_prices, min_prices = find_six_highest_lowest_monthly_average_price(monthly_avg_prices)

    # reformat the highest monthly avg prices
    max_reformat_list = reformat_max_res()

    # reformat the lowest monthly avg prices
    min_reformat_list = reformat_min_res()

    # print output
    print_info()


if __name__ == "__main__":
    main()
