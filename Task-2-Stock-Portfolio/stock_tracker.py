# CodeAlpha Internship - Task 2
# Stock Portfolio Tracker

print("=" * 40)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 40)

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420,
    "AMZN": 180
}

total_investment = 0

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you have finished.\n")

while True:
    stock = input("Enter stock name: ").upper()

    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not available. Please choose from the list.")
        continue

    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0.")
            continue

        investment = stock_prices[stock] * quantity
        total_investment += investment

        print(f"{stock} x {quantity} = ${investment}")
        print(f"Current total investment: ${total_investment}\n")

    except ValueError:
        print("Please enter a valid number for quantity.\n")

print("\n" + "=" * 40)
print(f"TOTAL INVESTMENT VALUE: ${total_investment}")
print("=" * 40)

print("\nThank you for using Stock Portfolio Tracker!")