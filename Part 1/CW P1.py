import time

#Creating Empty Lists
Progress = []
Trailer = []
Retriever = []
Exclude = []

#Function For Display Out of Range
def OutOfRange(Credits):
    if Credits not in range(0, 140, 20):
        print('Out of Range')

#Function for take Outcome of the Progress
#At the Same time append any element for the list to increase the length
def ProgressOutcome(Pass, Defer, Fail):
    Total = Pass + Defer + Fail
    if Total != 120:
        print('Total incorrect')        #Total
    elif Pass == 120 and Defer == 0 and Fail == 0:
        print('Progress')
        Progress.append("*")    #Appending a * to increase the Length of the List
    elif Pass == 100 and (Defer == 20 or Defer == 0) and (Fail == 0 or Fail == 20):
        print('Progress (module trailer)')
        Trailer.append("*")
    elif (Pass == 40 or Pass == 20 or Pass == 0 or Pass == 60 or Pass == 80) and (
        Defer == 40 or Defer == 20 or Defer == 0 or Defer == 60 or Defer == 80 or Defer == 100 or Defer == 120) and (
        Fail == 0 or Fail == 20 or Fail == 40 or Fail == 60):
        print('Module retriever')
        Retriever.append("*")
    elif (Pass == 40 or Pass == 20 or Pass == 0) and (Defer == 40 or Defer == 20 or Defer == 0) and (
            Fail == 80 or Fail == 120 or Fail == 100):
        print('Exclude')
        Exclude.append("*")

#Creating a Function to print the Horizontal Histogram
def Histogram(Progress, Trailer, Retriever, Exclude):
    print('-' * 70)
    time.sleep(0.5)
    print('Horizontal Histogram')
    #Printing '*'s according to the Length of Lists created
    print('Progress ', len(Progress), '   : ', '*' * len(Progress))
    print('Trailer ', len(Trailer), '    : ', '*' * len(Trailer))
    print('Retriever ', len(Retriever), '  : ', '*' * len(Retriever))
    print('Excluded ', len(Exclude), '   : ', '*' * len(Exclude))
    print()
    Outcomes = len(Progress) + len(Trailer) + len(Retriever) + len(Exclude)
    time.sleep(0.5)
    if Outcomes == 1:
        print('Only 1 Outcome in Total')
    else:   
        print(Outcomes,'Outcomes in Total')
    print('-' * 70)


#------------------------------------Main Code------------------------------------------

print('-' * 25, 'WELCOME to the Program', '-' * 25)
print()

while True:         #Main Loop To the Program
    while True:     #Loop To get the correct input for PASS
        try:
            PASS = int(input('Please enter your credits at PASS : '))
            OutOfRange(PASS)        #Checking the Range with Function
            if PASS in range(0, 140, 20):
                break
        except ValueError:
            print('Integer required')

    while True:
        try:
            DEFER = int(input('Please enter your credits at DEFER : '))
            OutOfRange(DEFER)
            if DEFER in range(0, 140, 20):
                break
        except ValueError:
            print('Integer required')

    while True:
        try:
            FAIL = int(input('Please enter your credits at FAIL : '))
            OutOfRange(FAIL)
            if FAIL in range(0, 140, 20):
                ProgressOutcome(PASS, DEFER, FAIL)
                break
        except ValueError:
            print('Integer required')

    print()         #Printing Empty Line
    print('Would you like to enter another set of data?')
    Response = input("Enter 'y' for yes or 'q' to quit and view results : ").lower()
    print()     #Asking the user to continue or quiet

    if Response == 'y':
        continue
    elif Response == 'q':
        Histogram(Progress, Trailer, Retriever, Exclude)
        print()
        print('-' * 25, 'End of the Program', '-' * 25)
        break
    else:
        print('Wrong Command; Program will Continue')
        print()

#End of the Program
