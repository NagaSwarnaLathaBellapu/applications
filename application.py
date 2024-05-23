#ATM application
'''while True:
           account=10000
           pwd=1234
           card=input("insert the card")
           if card=='c':
              print("welcome swarna")
              passward=int(input("enter the passward"))
              if passward==pwd:
        
                 option=int(input(choose the options
                                            1 balanceenq
                                            2 withdraw))
                 if option==1:
                     print("your account balance",account)
                 elif option==2:
                       money=int(input("enter the money"))
                       print(money)
                       bal=account-money
                       print("your rem bal is",bal)
              else:
                   print("incorct passward")
           else:
                 print("invalid card")'''
'''                                          
account=10000
while True:
pwd=1234
        card=input("insert the card")
        if card=='c':
            print("welcome swarna")
            passward=int(input("enter the passward"))
            if passward==pwd:
                option=int(input(choose the options
                      1.balenq
                      2.withdraw))
                if option==1:
                    print("your account balance",account)
                elif option==2:
                    money=int(input("enter the money"))
                    print(money)
                    bal=accont-money
                    account=bal
                    print("your rem bal is",bal)
            else:
                  print("incorrect passward")
        else:
            print("invalid card")
                                  '''   
                                    
#RAILWAY TICKET APPLICATION
'''while True:
            ticket_price=1000
            gender=input(choose the options 1.male 2.female
            age=int(input("enter the age"))
            if gender==1 or age>=60:
                l=(ticket_price*30)/100
                print("the ticket price for senior citizen is",l)
            elif gender==1 or age<60:
                
                print("the ticket price is",ticket_price)

            elif gender==2 or age>=60:
                 m=(ticket_price*50)/100
                 print("the ticket price for senior citizen is",m)

            elif gender==2 or  age<60 :
                 n=(ticket_price*20)/100
                 print("the ticket price is",n)'''
            

#flight tickets application


while True:
    time=input("enter the time")
    airways_price=int(input("enter the price"))
    airways_name=input("enter the flight name")
    option=int(input('''choose the options
                                1.usa-india 2.vij-ban 3.ganv-mum'''))
    if option==1:
        print("your ticket is conformed")
        seets=input('''enter the option a.window seet b.away fromwindow seet''')
        if seets=='a':
            print("you have a window seet")
            print("happy journey")
            if seets=='b':
                print("sorry you dont have window seet")
                print("do you want to change your seet")
                change=int(input('''change your seet 1.please change 2.no thanks'''))
                if change==1:
                    print("yah,we will change your seet")
                elif change==2:
                         print("yah no thanks ,iam fine")
            elif option==2:
                 print("no tickets available")



