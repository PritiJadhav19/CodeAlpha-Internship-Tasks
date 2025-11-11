stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 130,
    "MSFT": 310
}

print("Welcome to the Stock Portfolio Tracker!\n")
print("Available Stocks and Prices (USD):")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")
print("\nEnter your stock portfolio details.\n")

portfolio = {}
total_investment = 0

while True:
    stock_name = input("Enter stock symbol (or 'done' to finish): ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("Invalid stock symbol! Please choose from the list above.")
        continue

    try:
        quantity = int(input(f"Enter quantity of {stock_name}: "))
    except ValueError:
        print("Please enter a valid number for quantity.")
        continue

    investment_value = stock_prices[stock_name] * quantity
    portfolio[stock_name] = quantity
    total_investment += investment_value

    print(f"Added {quantity} shares of {stock_name} worth ${investment_value}\n")

print("Portfolio Summary:")
for stock, quantity in portfolio.items():
    print(f"{stock}: {quantity} shares @ ${stock_prices[stock]} each = ${stock_prices[stock] * quantity}")

print(f"\nTotal Investment Value: ${total_investment}")

save_choice = input("\nDo you want to save this result to a file? (yes/no): ").lower()

if save_choice == "yes":
    with open("portfolio_summary.txt", "w") as file:
        file.write("Portfolio Summary:\n")
        for stock, quantity in portfolio.items():
            file.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]} = ${stock_prices[stock] * quantity}\n")
        file.write(f"\nTotal Investment Value: ${total_investment}\n")
    print("Portfolio summary saved to 'portfolio_summary.txt'.")

print("\nThank you for using the Stock Portfolio Tracker!")
