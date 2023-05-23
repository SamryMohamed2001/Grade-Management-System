#Declaring
Progress=0
Trailer=0
Retriever=0
Exclude=0
total_count=0
condition=True
credit_dict={}
id_list=[]

#Defining the dictionary
def dict_():
    print('-'*60)
    print('Part 04')
    for (k,v) in credit_dict.items():
        print(k, v)

while condition == True:
    #Getting student ID
    number=input('Enter the student ID: ')
    if number not in id_list:
        #Appending the list of student ID
        id_list.append(number)
        #Getting pass credit
        credit_pass=input('Please enter your credits at PASS: ')
        try:
            credit_pass=int(credit_pass)
        except ValueError:
            print('Integer Required!\n')
            print('Enter again!')
            continue
        while 0>credit_pass>120 or credit_pass%20!=0:
            print('Out of range!\n')
            print('Enter again!')
            break

        #Getting defer credit
        credit_defer=input('Please enter your credits at DEFER: ')
        try:
            credit_defer=int(credit_defer)
        except ValueError:
            print('Integer Required!\n')
            print('Enter again!')
            continue
        while 0>credit_defer>120 or credit_defer%20!=0:
            print('Out of range!\n')
            print('Enter again!')
            break

        #Getting fail credit
        credit_fail=input('Please enter your credits at FAIL: ')
        try:
            credit_fail=int(credit_fail)
        except ValueError:
            print('Integer Required!\n')
            print('Enter again!')
            continue
        while 0>credit_fail>120 or credit_fail%20!=0:
            print('Out of range!\n')
            print('Enter again!')
            break

        #Getting total of credits
        total=credit_pass+credit_defer+credit_fail
        if total!=120: #Condition for total
            print('Total incorrect!\n')
        else:
            #Conditions for credits
            if credit_pass==120:
                print('Progress\n')
                Progress=Progress+1
                grade='Progress'
                credit_dict[number]= ': ' + (grade) + ' - ' + str(credit_pass)+ ', ' + str(credit_defer) + ', ' + str(credit_fail)
            elif credit_pass==100:
                print('Progress (Module Trailer)\n')
                Trailer=Trailer+1
                grade='Module Trailer'
                credit_dict[number]= ': ' + (grade) + ' - ' + str(credit_pass)+ ', ' + str(credit_defer) + ', ' + str(credit_fail)
            elif credit_fail==80 or credit_fail==100 or credit_fail==120:
                print('Exclude\n')
                Exclude=Exclude+1
                grade='Exclude'
                credit_dict[number]= ': ' + (grade) + ' - ' + str(credit_pass)+ ', ' + str(credit_defer) + ', ' + str(credit_fail)
            else:
                print('Do not Progress - Module Retriever\n')
                Retriever=Retriever+1
                grade='Module Retriever'
                credit_dict[number]= ': ' + (grade) + ' - ' + str(credit_pass)+ ', ' + str(credit_defer) + ', ' + str(credit_fail)
            total_count=total_count+1
    else:
        #Printing existing messages
        print('Student ID already exists!')
    
    while True:
         #Asking for choices
         print('Do you want to add another one?')
         choice=input('Press "y" to enter again or "q" to quit and see the results: ')
         if choice == "y":
             print('----------------------------------------------------------------------------')
             break
         elif choice=="q":
             #Calling the dictionary
             dict_()
             condition=False
             break
         elif choice!="y" or choice!="q":
             #Printing message for invalid inputs 
             print('Try again')
             
             
    
    
    








        


