annual_salary = float(input("Enter your starting salary: "))

down_payment = 0.25 * 1000000

left = 0
right = 10000
steps = 0 

while True:
    mid = (left + right) / 2
    steps += 1
    portion_saved = mid / float(10000)
    current_saving = 0
    months = 0
    monthly_salary = annual_salary / 12

    for i in range(36):
        months += 1
        current_saving += current_saving * 0.04 / 12 + monthly_salary * portion_saved
        if months % 6 == 0:
            monthly_salary *= 1.07

    if steps > 13:
        print("It is not possible to pay the down payment in three years.")    
        break
    elif current_saving >= down_payment-100 and current_saving <= down_payment+100:
        print(f"Best saving rate: {portion_saved}\n")
        print(f"Steps in besection search: {steps}")
        break
    elif current_saving < down_payment-100:
        left = mid
    else:
        right = mid 


