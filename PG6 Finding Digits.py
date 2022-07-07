''' S03Q01 - finding digits of the given numbers '''

def digit(num):

    if num < 10:
        print(num, ": Single digit.")
    elif num < 100:
        print(num, ": Double digit..")
    else:
        print(num)
            
def get_number():

    num = int(input("Enter the number:"))
    digit(num)

def main():

    limit = int(input("Enter the limit:"))
    
    for i in range(1, limit+1):
        num = get_number()
        
#Main starts from here
main()
    
