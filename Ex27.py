mor=float(input("Kg morango: "))
mac=float(input("Kg maçã: "))

pm=2.5 if mor<=5 else 2.2
pa=1.8 if mac<=5 else 1.5

total=mor*pm+mac*pa

if mor+mac>8 or total>25:
    total*=0.9

print("Total:",total)
