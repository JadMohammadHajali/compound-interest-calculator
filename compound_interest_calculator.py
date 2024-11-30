""" Compound Interest Calculator Project

The program will display the user's new balance after accruing interest over the specified number of years.
"""

principle = 0
time = 0
rate = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than or equal to zero.")
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("Interest rate can't be less than or equal to zero.")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("The time can't be less than or equal to zero.")
    else:
        break

total = principle * pow((1 + rate/100), time)
print(f"Balance after {time} years/s: {total:.2f}")
