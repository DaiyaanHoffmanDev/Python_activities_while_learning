# this is a compound interest calculator

principal = 0
rate = 0
time = 0

while principal <= 0:
    print("Principal must be grater than 0 ")
    principal = float(input("Enter the principal amount: "))
    if principal <= 0:
        print("Principal must be grater than 0 ")

while rate <= 0:
    print("Rate must be grater than 0 ")
    rate = float(input("Enter the interest rate (in %): "))
    if rate <= 0:
        print("Rate must be grater than 0 ")

while time <= 0:
    print("Time must be grater than 0 ")
    time = int(input("Enter the time (in years): "))
    if time <= 0:
        print("Time must be grater than 0 ")

print(principal, rate, time)

total = principal * pow(1 + rate / 100, time)
print(f"total amount after {time} years = R{total:.2f}")