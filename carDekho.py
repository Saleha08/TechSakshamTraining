cars = [
    {"name": "Maruti Swift", "brand": "Maruti", "price": 700000, "details": ("Petrol", 5)},
    {"name": "Hyundai Creta", "brand": "Hyundai", "price": 1200000, "details": ("Diesel", 5)},
    {"name": "Honda City", "brand": "Honda", "price": 1500000, "details": ("Petrol", 5)},
    {"name": "Toyota Fortuner", "brand": "Toyota", "price": 3500000, "details": ("Diesel", 7)},
]

def search_by_price_range(min_price, max_price):
    try:
        print(f"\nCars in range ₹{min_price} - ₹{max_price}:")
        found = False
        for car in cars:
            if min_price <= car["price"] <= max_price:
                print(f"- {car['name']} ({car['brand']}) - ₹{car['price']} - {car['details'][0]} - {car['details'][1]} Seater")
                found = True
        if not found:
            print("No cars found in this range.")
    except Exception as e:
        print("An error occurred:", e)

try:
    min_price = int(input("Enter minimum price: "))
    max_price = int(input("Enter maximum price: "))

    if min_price < 0 or max_price < 0:
        raise ValueError("Price cannot be negative.")
    if min_price > max_price:
        raise ValueError("Minimum price cannot be greater than maximum price.")

    search_by_price_range(min_price, max_price)
except ValueError as ve:
    print("Invalid input:", ve)
except Exception as e:
    print("An unexpected error occurred:", e)