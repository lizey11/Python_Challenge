import os
import csv
PyBank= os.path.join('budget_data.csv')

#open and read csv file

with open(PyBank, newline='') as csvfile:

    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)

    # create lists to hold profit and months
    Profit = []
    months = []

    #read through each row of data after header
    for rows in csvreader:
        Profit.append(int(rows[1]))
        months.append(rows[0])

    # find revenue change
    revenue_change = []

    for number in range(1, len(Profit)):
        revenue_change.append((int(Profit[number]) - int(Profit[number-1])))
    
    # calculate average revenue change
    revenue_average = sum(revenue_change) / len(revenue_change)
    
    # calculate total length of months
    total_months = len(months)

    # greatest increase in revenue
    greatest_increase = max(revenue_change)
    # greatest decrease in revenue
    greatest_decrease = min(revenue_change)


    # print the Results
    print("Financial Analysis")
    print("....................................................................................")
    print("total months: " + str(total_months))
    print("Total: " + "$" + str(sum(Profit)))
    print("Average change: " + "$" + str(revenue_average))
    print("Greatest Increase in Profits: " + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
    print("Greatest Decrease in Profits: " + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))




