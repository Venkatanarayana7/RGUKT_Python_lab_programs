def interest_calculator():
    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter rate of interest: "))
    time = float(input("Enter time in years: "))

    si = (principal * rate * time) / 100
    ci = principal * ((1 + rate / 100) ** time) - principal

    print(f"Simple Interest: {si:.2f}")
    print(f"Compound Interest: {ci:2f}")

interest_calculator()
