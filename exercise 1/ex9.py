import random

def day_profit(price, cups_sold, cost_per_cup):
    return (price - cost_per_cup) * cups_sold


def main():
    cost_per_cup = 0.30
    price = 0.75
    best_profit = 0
    total_profit = 0
    best_day = 0
    best_weather = ""

    for day in range(1, 8):

        cups_sold = int(input(f"day {day} cups solds: "))
        weather = random.choice(["sunny", "rainy", "cloudy"])

        if weather == "rainy":
            cups_sold = int(cups_sold * 0.5)

        elif weather == "cloudy":
            cups_sold = int(cups_sold * 0.8)

        profit = day_profit(price, cups_sold, cost_per_cup)
        print(f"Day {day}: {weather}, Profit = {profit:.2f}")

        if profit < 0:
            print("Rough day — consider lowering the price.")

        if best_profit < profit:
            best_profit = profit
            best_day = day
            best_weather = weather
            print("New best day!")


        total_profit += profit
        print(total_profit)




    price = 0.10
    best_profit = 0
    best_price = 0

    while price <= 2.00:

        cups_sold = max(0, 50 - 40 * price)

        profit = day_profit(price, cups_sold, cost_per_cup)

        if profit > best_profit:
            best_profit = profit
            best_price = price
            print(f"New best price: {best_price:.2f} with profit: {best_profit:.2f}")

        price = round(price + 0.05, 2)


    print(f"Total Profit: {total_profit:.2f}")
    print(f"Best Day: {best_day}")
    print(f"Best Weather: {best_weather}")
    print(f"Best Day Profit: {best_profit:.2f}")
    print(f"Best Price: {best_price:.2f}")




if __name__ == "__main__":
    main()