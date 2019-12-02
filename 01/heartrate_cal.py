#Target Heart Rate Calculator
age=21
your_Maximum_Heart_Rate=220-age
print(your_Maximum_Heart_Rate,'Beats per minute')
Lower_end_of_your_Target_Heart_Rate= int(70/100*(your_Maximum_Heart_Rate))
print(Lower_end_of_your_Target_Heart_Rate,'Beats per minute')
Higher_end_of_your_Target_Heart_Rate=int(85/100*(your_Maximum_Heart_Rate))
print(Higher_end_of_your_Target_Heart_Rate,'Beats per minute')

