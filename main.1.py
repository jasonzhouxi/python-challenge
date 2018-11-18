import csv

PyBank_csv = ('C:/Users/user/Desktop/DataClass-/UCIRV201810DATA4/Homeworks/HW03-Python/PyBank/Resources/budget_data.csv')

with open(PyBank_csv) as revenue_data:
    csvreader = csv.DictReader(revenue_data, delimiter=",")
    csv_header = next(csvreader)
    Total_months = 0
    Total_revenue = 0
    prev_Revenue = 0
    greatest_decrease = ["", 99999999999999999999]
    greatest_increase = ["", 0]

    for row in csvreader:
        Total_months += 1
        Total_revenue += int(row['Revenue'])

    Changes = []
    for row in csvreader:
        Change = int(row['Revenue']) - prev_Revenue
        prev_Revenue = int(row['Revenue'])
        Changes.append(Change)
    Average_Change = sum(Changes) / len(Changes)

    for row in csvreader:
        if Changes > greatest_increase[1]:
            greatest_increase[1] = Changes
            greatest_increase[0] = row("Date")
        if Changes < greatest_decrease[1]:
            greatest_decrease[1] = Changes
            greatest_decrease[0] = row("Date")

print(f"Total Months: {Total_months}")
print(f"Total: {Total_revenue}")
print(f'Changes are : {Changes}')
print(f'Average Change is: {Average_Change}')
print(f'The Greatest Increase occurs at: {greatest_increase[0]} , amount: {greatest_increase[1]}')
print(f'The Greatest Decrease occurs at: {greatest_decrease[0]} , amount: {greatest_decrease[1]}')
