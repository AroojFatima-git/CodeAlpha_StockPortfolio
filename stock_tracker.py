import csv


# Manually defined stock prices
STOCK_PRICES = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}


def display_available_stocks():
    print("\nAvailable Stocks:")
    
    for stock, price in STOCK_PRICES.items():
        print(f"{stock}: ${price}")


def get_portfolio():
    portfolio = {}

    while True:

        stock = input(
            "\nEnter stock symbol (or 'done' to finish): "
        ).upper().strip()

        if stock == "DONE":
            break

        if stock not in STOCK_PRICES:
            print(" Stock not available.")
            continue

        try:
            quantity = int(input("Enter quantity: "))

            if quantity <= 0:
                print(" Quantity must be greater than 0.")
                continue

            portfolio[stock] = portfolio.get(stock, 0) + quantity

        except ValueError:
            print(" Please enter a valid number.")

    return portfolio


def calculate_investment(portfolio):
    total = 0

    for stock, quantity in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = price * quantity

        total += investment

    return total


def display_portfolio(portfolio):
    print("\n" + "=" * 50)
    print("             YOUR PORTFOLIO")
    print("=" * 50)

    print(f"{'Stock':<10}{'Quantity':<12}{'Price':<12}{'Investment'}")
    print("-" * 50)

    for stock, quantity in portfolio.items():

        price = STOCK_PRICES[stock]
        investment = price * quantity

        print(
            f"{stock:<10}"
            f"{quantity:<12}"
            f"${price:<11}"
            f"${investment}"
        )


def save_to_csv(portfolio, filename="portfolio.csv"):

    with open(filename, "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(
            ["Stock", "Quantity", "Price", "Investment"]
        )

        for stock, quantity in portfolio.items():

            price = STOCK_PRICES[stock]
            investment = price * quantity

            writer.writerow(
                [stock, quantity, price, investment]
            )

    print(f"\n Portfolio saved to {filename}")


def main():

    print("=" * 50)
    print("        STOCK PORTFOLIO TRACKER")
    print("=" * 50)

    display_available_stocks()

    portfolio = get_portfolio()

    if not portfolio:
        print("\nNo stocks added.")
        return

    display_portfolio(portfolio)

    total = calculate_investment(portfolio)

    print("\n" + "=" * 50)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 50)

    choice = input("\nSave portfolio to CSV? (y/n): ").lower()

    if choice == "y":
        save_to_csv(portfolio)


if __name__ == "__main__":
    main()
