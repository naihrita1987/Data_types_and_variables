n = int(input("How many times you want to pour water: "))
capacity=255
total=0

for i in range(n):
    qty = int(input("How many liters you want to pour: "))
    if total + qty <= capacity:
        total +=qty    
    else:
        print("Invalid input")
print(f"The litre equals: {total}")