#Weighted Score Calculator
A1=float(input('enter your marks in A1'))
A2=float(input('enter your marks in A2'))
A3=float(input('enter your marks in A3'))
E1=float(input('enter your marks in E1'))
E2=float(input('enter your marks in E2'))
weighted_score = float(( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35)
print('weighted_score_based_on_individual_assignment_scores',weighted_score)
