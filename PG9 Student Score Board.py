''' S04Q02 - Students Results

Requirement:

Brilliant School sets an exam wherein, 
    English exam is for 80 marks, 
    Science for 90 marks and 
    Mathematics for 100 mark

First Class if score is more than or equal to 90 %
Second Class if score is more than or equal to 75%
Average if student has not failed
Failed if score is less than or equal to 35 % '''

def rank(percentage):

    if percentage >= 90:
        print("Rank: First Class...")
    elif percentage >= 75 and percentage < 90:
        print("Rank: Second Class...")
    elif percentage <= 35:
        print("Rank: Failed...!")
    else:
        print("Rank: Average")
        
def tot_calc(eng, sci, mat):

    total = eng + sci + mat
    print("Total Marks:", total)

    percentage = (total / 270) * 100
    print("Percentge:", percentage)
    rank(percentage)
    
def get_marks():

    eng = int(input("Enter English Mark out of 80:"))
    sci = int(input("Enter Science Marl out of 90:"))
    mat = int(input("Enter Maths Mark out of 100:"))

    tot_calc(eng, sci, mat)

def main():
    get_marks()

#Main starts from here
main()
