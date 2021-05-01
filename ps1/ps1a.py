annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

down_payment = 0.25 * total_cost
monthly_salary = annual_salary / 12
current_saving = 0
months = 0

while current_saving < down_payment:
    months += 1
    current_saving += current_saving * 0.04 / 12 + monthly_salary * portion_saved
    

print(f"Number of months: {months}")