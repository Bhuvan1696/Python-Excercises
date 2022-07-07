''' S03Q02 -

- Ask the user to enter a number.
            - If the number is a single digit number,
                 add 7 to it, and print the number in its unit’s place
            - If the number is a two digit number,
                raise the number to the power of 5, 
                and print the number in its unit’s place
            - If the number is a three digit number, 
                ask the user to enter another number. 
                Add the 2 numbers and print the number in its unit’s place'''

def triple(num):
    print(num, "is Triple Digit")
    num2 = int(input("Enter another number to add:"))
    print("Added two numbers:", num+num2)
    
def double(num):
    print(num, "is Double Digit")
    print("Power of 5:", pow(num, 5))
    
def single(num):
    print(num, "is single Digit")
    print ("Added 7: ", num+7)

def digit(num):
    if num < 10:
        single(num)
    elif num < 100:
        double(num)
    elif num < 1000:
        triple(num)
    else:
        print("More than 3 Digit..", num)

def get_number(limit):
    
    for i in range (1, limit+1): 
        nums = []
        num = int(input("Enter the number:"))
        nums = nums + [num]
        digit(num)

def main():
    limit = int(input("enter the limit:"))
    get_number(limit)

#Main starts from here
main()
