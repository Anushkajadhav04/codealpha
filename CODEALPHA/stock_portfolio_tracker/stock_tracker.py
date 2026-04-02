# Predefined stock prices
stock_prices = {
    "CRYPT": 180,
    "JIO": 250,
    "GOOG": 2700,
    "AMZN": 3300,
    "MSFT": 300
}

portfolio = {}
total_investment = 0

print("📊 Stock Portfolio Tracker")
print("Available stocks:", list(stock_prices.keys()))

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("⚠️ Stock not available!")
        continue

    try:
        quantity = int(input("Enter quantity: "))
    except ValueError:
        print("⚠️ Enter a valid number!")
        continue

    portfolio[stock] = portfolio.get(stock, 0) + quantity

# Calculate total investment
print("\n📁 Your Portfolio:")
for stock, quantity in portfolio.items():
    price = stock_prices[stock]
    investment = price * quantity
    total_investment += investment
    print(f"{stock} → {quantity} shares × ${price} = ${investment}")

print("\n💰 Total Investment Value: $", total_investment)

# Save to file
with open("portfolio.txt", "w") as file:
    file.write("Stock Portfolio Summary\n")
    for stock, quantity in portfolio.items():
        file.write(f"{stock}: {quantity} shares\n")
    file.write(f"\nTotal Investment: ${total_investment}")

print("✅ Portfolio saved to 'portfolio.txt'")