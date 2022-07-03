''' S01Q03 - Multiplication table as per user choice '''

def multi_table(table, limit):
    for i in range (1, limit+1):
        print(i, "*", table, "=", i * table)
        
def get_value():
    m_table = int(input("Enter the multiplication table:"))
    t_limit = int(input("Enter the Limit of Multiplication table:"))
    multi_table(m_table, t_limit)

def main():
    get_value()

#Main starts from here
main()
