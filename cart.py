foods = []

total_prices = 0

print("Welcome to the Food Cart!")

while True:
    food = input("Enter the name of your food item: ")
    
    try:
        
        price = float(input(f"Enter price for {food}: R"))
    except ValueError:
        print("Invalid price. Please enter a numeric value.")
        continue
    
    foods.append((food, price))
    total_prices += price
    
    another = input("Do you want to add another food item? (yes/no): ").strip().lower()
    if another != 'yes':
        break
    
    print("\nCurrent food items in the cart:")
    for item, price in foods:
        print(f"{item}: R{price:.2f}")
        
        print(f"\nTotal price of all food items: R{total_prices:.2f}")

