''' S02Q02 - Using the starting and ending values of your car’s odometer, 
            and the measure of fuel consumed, 
            calculate the number of stops one should make for refuelling 
            while travelling from Bangalore to Goa, 
            a distance of 560 kms '''

def no_of_stops(travelled):

    to_goa = 560
    fuel_travel = travelled
    count = 0
    while (travelled <= to_goa):
        count += 1
        travelled = travelled + fuel_travel
    print("No.of fuel stopping:", count)
    print("Reached Goa...")
        
def milege(start, current, fuel):

    travelled = current - start
    milege = travelled / fuel
    print("Travelled:", travelled)
    print("Milege:", milege)

    no_of_stops(travelled)
    
def get_value():

    start_km = int(input("Enter the starting KM of Odometer:"))
    current_km = int(input("Enter the current KM of Odometer:"))
    fuel_capacity = float(input("Enter the fuel tank capacity:"))
    milege(start_km, current_km, fuel_capacity)

def main():

    get_value()

#Main starts from here
main()
