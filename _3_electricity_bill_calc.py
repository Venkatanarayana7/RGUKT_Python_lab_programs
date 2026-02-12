def electricity_bill():
    units = float(input("Enter units consumed: "))

    if units <= 50:
        bill = units * 0.50
    elif units <= 150:
        bill = 50 * 0.50 + (units - 50) * 0.75
    elif units <= 250:
        bill = 50 * 0.50 + 100 * 0.75 + (units - 150) * 1.00
    else:
        bill = 50 * 0.50 + 100 * 0.75 + 100 * 1 + (units - 250) * 1.25


    print(f"Electricity Bill: {bill:.2f}")

electricity_bill()


# input --> 300
# output --> 262.50