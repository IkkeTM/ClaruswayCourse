income = float(input("What is your yearly income? "))

if income < 67000:
    after_tax = income * 0.76
elif income < 97000:
    after_tax = income * 0.69
else:
    after_tax = income * 0.66

print(f"After taxes you have {after_tax} left.")