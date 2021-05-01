annual_salary = float(input("Enter your starting salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
current_saving = 0
months = 0

while current_saving < down_payment:
    months += 1
    current_saving += current_saving * 0.04 / 12 + monthly_salary * portion_saved
    if months % 6 == 0:
        monthly_salary *= 1 + semi_annual_raise
    
print(f"Number of months: {months}")