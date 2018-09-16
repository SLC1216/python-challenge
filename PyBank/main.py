import pandas as pd
df_budgetdata = pd.read_csv("budget_data.csv")
df_budgetdata.head()
df_budgetdata.get_dtype_counts
df_budgetdata.count()
finalhw1=df_budgetdata.count()[0]
finalhw1
finalHW2 = df_budgetdata["Profit/Losses"].sum()
finalHW2
#Set variables ie for storing calculations in list form
# Write loop so the calculations iterates through the whole data and stores each calcultion in the change_month list
change_month = []
profitlossdata = df_budgetdata["Profit/Losses"]
for i in range(finalhw1-1):
    change_month.append(profitlossdata[i+1]-profitlossdata[i])
#For loop 
For row in df_budgetdata["Profit/Losses"]
# Write loop so the calculations iterates through the whole data and stores each calcultion in the change_month list
change_month_total = 0
for i in change_month:
    change_month_total = change_month_total+i
change_month_total  
finalhw3 = change_month_total/85
finalhw3
df_budgetdata.mean()
#Get maximum value from the list
finalhw4=max(change_month)
finalhw4
#Get minimum vaue from the list
finalhw5=min(change_month)
finalhw5
def printToTerminal(entry1, entry2, entry3, entry4, entry5):
    print("Total Months: {}".format(entry1))
    print("Total: ${}".format(entry2))
    print("Average Change: ${}".format (entry3))
    print("Greatest Increase in Profits: Feb-2012 : ${}".format (entry4))
    print("Greatest Decrease in Profits: Sep-2013:${}".format (entry5))
    
printToTerminal(finalhw1, finalHW2, finalhw3, finalhw4, finalhw5)

#export results to text file (this did not seem to work)

pathlib.Path("C:/Desktop/GWBC/.txt").write_text(finalhw1, finalHW2,)
finalhw3, finalhw4, finalhw5
#Angelo, I did understand this evenutally, took a lot of work which I know is to be expected but I feel as I need to say so. I could not get the final printout to the textfile, the printtoterminal though is near the top since I set those early. Thanks for your help today, please let me know if there is anything I can improve on, I know you've said there are many ways to obtain the same answer and I am sure this is just one of them. Thanks again! 
