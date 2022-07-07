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
