''' S02Q01 - Car Milege '''

''' Formula: Car mileage = No. of Kms/ Quantity Of Fuel Used '''

def milege(start, current, fuel):

    travelled = current - start
    milege = travelled / fuel
    print("Travelled KM:", travelled)
    print("Milege:", milege)
    
def get_value():
    
    start_km = int(input("Enter the Odometer Start Value:"))
    current_km = int(input("Enter the Odometer current Value:"))
    fuel = float(input("Enter how much fuel you have filled:"))

    milege(start_km, current_km, fuel)
   
def main():
    get_value()

#Main starts from here
main()
