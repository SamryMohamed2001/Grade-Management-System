# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1956190, 20221534
# Date: 2022.11.16

#Declaring 
Progress=0
Trailer=0
Retriever=0
Exclude=0
total_count=0
credit_list=[]
condition=True
file = open('store.txt','w')
file.close()

#Defining the list
def credit():
    for k in credit_list:
        print(k)

#Defining the file
def file_store():
    print('Part 3')
    print('----------------------------------------------------------------------------')
    try:
        file=open('store.txt', 'r')
        outcome=file.read()
        print(outcome.rstrip())
        file.close()
    except FileNotFoundError:
        print('File not found, please check!')

#Condition for inputs
while condition==True:
    while True:
        #Getting pass credit
        credit_pass = input('Please enter your credits at PASS: ')
        try:
            credit_pass = int(credit_pass)
        except ValueError:
            #Validation
            print('Integer required.')
            continue
        while 120<credit_pass<0 or credit_pass%20!=0:
            print('Out of range.')
            break
        else:
            break

    while True:
        #Getting defer credit
        credit_defer = input('Please enter your credits at DEFER: ')
        try:
            credit_defer = int(credit_defer)
        except ValueError:
            #Validation
            print('Integer required.')
            continue
        while 120<credit_defer<0 or credit_defer%20!=0:
            print('Out of range.')
            break
        else:
            break
        
    while True:
        #Getting fail credit
        credit_fail = input('Please enter your credits at FAIL: ')
        try:
            credit_fail = int(credit_fail)
        except ValueError:
            #Validation
            print('Integer required.')
            continue
        while 120<credit_fail<0 or credit_fail%20!=0:
            print('Out of range.')
            break
        else:
            break
    
    #Calculating the total credits
    total=credit_pass+credit_defer+credit_fail
    if total!=120:
        print('Total incorrect!\n')
    else:
        if credit_pass==120:
            print('Progress\n')
            Progress=Progress+1
            grade='Progress'
        elif credit_pass==100:
            print('Progress (Module Trailer)\n')
            Trailer=Trailer+1
            grade='Module Trailer'
        elif credit_fail==80 or credit_fail==100 or credit_fail==120:
            print('Exclude\n')
            Exclude=Exclude+1
            grade='Exclude'
        else:
            print('Module Retriever\n')
            Retriever=Retriever+1
            grade='Module Retriever'
        total_count=total_count+1

        #Using f string and appending the list
        credit_list.append(f'{grade} : {credit_pass}, {credit_defer}, {credit_fail}')

        #Opening file
        file=open('store.txt','a')
        file.write(f'{grade} : {credit_pass}, {credit_defer}, {credit_fail}\n')
        #Closing file
        file.close()
        
    while True:
         #Asking for option
         print('Do you want to add another one?')
         choice=input('Press "y" to enter again or "q" to quit and see the results: ')
         choice=choice.lower() #Identify both lower case and upper case output as one.
         
         if choice == "y":
             print('----------------------------------------------------------------------------')
             break
         elif choice=="q":
             #Histogram
             print('\n')
             print('Histogram')
             print('----------------------------------------------------------------------------')
             print('Progress ', Progress, ':',  "*"*Progress)
             print('Trailer ', Trailer, ':',  "*"*Trailer)
             print('Retriever ', Retriever, ':', "*"*Retriever)
             print('Exclude ', Exclude, ':',  "*"*Exclude)
             print(total_count, 'outcomes in total.')
             print('\n')
             print('Part 2')
             print('----------------------------------------------------------------------------')
             #Calling list
             credit()
             print('----------------------------------------------------------------------------')
             print('\n')
             #Calling file
             file_store()
             print('----------------------------------------------------------------------------')
             condition=False
             break
         elif choice!="y" or choice!="q":
             print('Try again!')
    
    
                

            
            
            


        



        










        


            
            
            


        



        










        


