import os
import csv
csvpath = os.path.join('..', 'Python-Challenge', 'budget_data.csv')

csv_header= [] 

with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print(csvreader)
    next(csvreader)
    #print(csv_header)
    #csv_list=[csvreader]

    #months = 0
    #for row in range(len(csv_list)):
        #if ((csv_list[row]=="Jan") or "Feb" or "Mar" or "Apr" or "May" or "Jun" or "Jul" or "Aug" or "Sep" or "Oct" or "Nov" or "Dec":
            #months+=1
    #print(months)
    row_counter=0
    net_profit = 0
    month_list=[]
    profit_list=[]

    for row in csvreader:
        net_profit+= int(row[1])
        row_counter+= 1
        month_list.append(row[0])
        profit_list.append(row[1])

    #print(net_profit)
    #print(row_counter)
    #print(month_list)
    #print(profit_list)

    increaseList=[]

    for i in range(len(profit_list)):
        if(i==0):
            increaseList.append(i)
        else:
            increaseList.append(int(profit_list[i])-int(profit_list[i-1]))
    #print(increaseList)
        
    bigIncrease=increaseList.index(max(increaseList))

    #print(bigIncrease)
    #print(month_list[bigIncrease],increaseList[bigIncrease])
        
        #if item at profit_list[2]-profit_list[1] is > profit_list[1]-profit_list[0]
    bigDecrease=increaseList.index(min(increaseList))
    #print(bigDecrease)
    #print(month_list[bigDecrease],increaseList[bigDecrease])

    def average(increaseList):
        return sum(increaseList) / len(increaseList)
    averageChange=average(increaseList)
    #print(round(averageChange))

    print("Financial Analysis")
    print("Total Months ="+ str(row_counter))
    print("Total ="+ str(net_profit))
    print("Average Change ="+ str(round(averageChange)))
    print("Greatest Increase in Profits ="+ month_list[bigIncrease],increaseList[bigIncrease])
    print("Greatest Decrease in Profits ="+ month_list[bigDecrease],increaseList[bigDecrease])
 # row[0] => column 1
# row[1] => column 2
        

#print("row[0]", row[0])
#print("row[1]", row[1])
#sum everything in column2
        




        


       
       


        








