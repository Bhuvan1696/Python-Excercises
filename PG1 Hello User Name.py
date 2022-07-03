''' S01Q01 - Hello World Program with User Name '''

'''Method 1 '''

def print_name(name):
    print("Hello", name)
    
def get_name():
    name = input("Enter Your Name:")
    print_name(name)

def main():
    get_name()

#Main starts from here
main()
