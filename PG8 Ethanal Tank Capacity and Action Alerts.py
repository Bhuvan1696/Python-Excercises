''' S04Q01 - Ethanal tank capacity calculation in percentage with required action alert

Requirement:
A Chemical plant has a tank for storing ethanol
When the tank is more than 80% full,
it should raise an alarm to close the valve.
When the tank is less than 20% full,
it should send an SMS to buy more liquid.
The total tank capacity is 900 litres '''

''' Formula: Percentage = (number you want to find the percentage for ÷ total) × 100'''

def action_alert(percentage):

    if percentage < 20:
        print("Please buy more liquid...")
    elif percentage > 80:
        print("Tank is full.. Close the valve!!!")
    else:
        print("Enough liquid to use...")
        
def percentage_calc(value):
    tot_capacity = 900
    percentage = (value/900) * 100
    percentage = int(percentage)
    print("Current Capacity level", percentage,"%")
    action_alert(percentage)
    
def get_current_value():
    current_level = int(input("Enter the current level of ethanal tank:"))
    percentage_calc(current_level)

def main():
    get_current_value()

#Main starts from here
main()
