#Ride Cost Calculator

distance_travelled=int(input('enter your distance:'))
cost=int(input('cost of diesel per litre:'))
fuel=int(input('Fuel Average'))
cost_of_driving_per_day_to_office=(distance_travelled/fuel)*cost
print(cost_of_driving_per_day_to_office,'Ride Cost')

