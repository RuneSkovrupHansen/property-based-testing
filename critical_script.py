#!/bin/python3

import awesome_math
import awesome_sort

def main():
    
    stock_prices = [2000, 200, 1500, 900, 5000, 600]
    awesome_sort.bubble_sort(stock_prices)
    print(f"The highest value of a stock is: {stock_prices[-1]}")
    # 5000

    stock_prices = [2000, 200, 1500, 900, 5000, 600]
    total_value = 0
    for stock_price in stock_prices:
        total_value = awesome_math.add(stock_price, total_value)
    print(f"The total value of stocks is: {total_value}")
    # 10200


if __name__ == "__main__":
    main()
