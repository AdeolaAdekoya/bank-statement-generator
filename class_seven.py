# import time

import random
from datetime import datetime




# filter takes in a functiona and an
# filter is usually yes or no
# the firt arguement shoukd always remain true or false


# dictionary pops by the key............lists pops by the index.



#  filter

# making use of range, print out all  the odd numbers betwwwen 10 and 50



# n = range(10,50)
# my_filter = list(filter(lambda x: x %2 !=0,n))
# print(my_filter)


# option = "Www.HackerRank.com"

# print(option.swapcase())


# or 

# a = "".join([i.upper() if i.islower() else i.lower() for i in option])

# built in modules


# time modules


# print("hello there!")
# time.sleep(2.5)
# print("done!")

# random.seed(2)
# my_num = range(1,11)


# random.shuffle(my_num) #shuffles the list
# data = random.sample(my_num, 10)  # gets a sample of k items from our overall population
# print(my_num)


# print(datetime.today().date())

# today = datetime.today()
# print(type(today))


# today = datetime.today().month()
# print(today)

# today = datetime.today().weekday()
# print(today)

# today = datetime.today().isoweekday()  #iso starts counting from 1 thats why it returns 2
# print(today)

# to get the date in full form
# today = datetime.today()
# print(datetime.strftime(today, "%b, %d %Y"))




# add date to the bank app.. creating a new user and adding a transaction. adding a statisctical summary of the. get the account statement by date



# get a date then get it in the following format 


# today = datetime.today()
# print(datetime.strftime(today, "%A, %d of %B, %Y"))
# tomorrow = datetime.today()
# print(datetime.strftime(tomorrow, "%A-%d-%b-%Y"))
# next2 = datetime.today()
# print(datetime.strftime(next2, "%a,%b %d %Y."))
# time1 = datetime.today()
# print(datetime.strftime(time1, "Today is the %dth day of %b. %Y"))


# strp comes from string to date time object
# time3 = datetime.today()
# print(datetime.strptime("21-Jan-22 8:10:40",  "%d-%b-%y %H:%M:%S"))


#  a function is a named sequence of statements that performs a computation.
# write a function that takes in an intiger and returns true of false if if the intiger is a prime number

# fruitful function can return something

#friutless retuns none 

# some functions can take in arguments but not all
# parametier is used when making the function. but not always




# git hub


# # text = "Www.HackerRank.com"
# # print(text.swapcase())


# # a = "".join([i.upper() if i.islower() else i.lower() for i in text])
# # print(a)


# # import time
# import random
# from datetime import datetime

# # print("Hello there!")   
# # time.sleep(2.5) 
# # print("Done!")
# # random.seed(2)
# # my_num = list(range(1,11))

# # random.shuffle(my_num) #shuffles the list
# # print(my_num)
# # data = random.sample(my_num, 3 ) #get a sample of k items from our overall population
# # print(data)

# today = datetime.today()

# print(datetime.strptime("21-Jan-22 8:10:40", "%d-%b-%y %H:%M:%S"))

import random


data = {}
trans_data = {}

print("Welcome to the AstroBank App")
while True:
    print("Enter s to signup or l to login:")
    print("Enter any other key to close")
    choice = input(">").lower()

    if choice == 'l':
        acc_num = input("Enter your account num:\n>")
        pin = input("Enter your pin:\n>")

        user = data.get(acc_num)

        if user and user['pin'] == pin:
            print(f"Welcome {user['name']}.\nYour account balance is ${user['bal']}")

            while True:
                print("""\nWhat would you like to do?
                    Press 1 to withdraw
                    Press 2 to deposit
                    Press 3 to transfer
                    Press any other key to quit.""")

                user_input = input(">")

                if user_input == '1':
                    amount = int(input("How much?\n>"))
                    if amount >= user['bal']:
                        print("Insufficient Funds")
                    else:
                        user['bal']-=amount

                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "withdrawal"
                        }

                        trans_data[acc_num].append(detail)


                        print("Please take your cash")
                        print(f"Balance is {user['bal']}")

                elif user_input == '2':
                    amount = int(input("How much?\n>"))

                    user['bal']+=amount

                    #log transaction data
                    detail = {
                        "amount":amount,
                        "type": "credit",
                        "action" : "deposit"
                    }

                    trans_data[acc_num].append(detail)

                    print("Successful")
                    print(f"Balance is {user['bal']}")
                elif user_input == '3':
                    recepient_ = input("Enter recepient account\n>")
                    amount = int(input("How much?\n>"))

                    if user['bal'] < amount:
                        print("Insufficient Funds")

                    recepient = data.get(recepient_)
                    if recepient:
                        recepient['bal'] += amount
                        user['bal'] -=amount

                        #log transaction data
                        detail = {
                            "amount":amount,
                            "type": "debit",
                            "action" : "transfer"
                        }

                        trans_data[acc_num].append(detail)

                        detail_recepient = {
                            "amount":amount,
                            "type": "credit",
                            "action" : "transfer"
                        }

                        trans_data[recepient_].append(detail_recepient)

                        print("Successful")
                        print(f"Balance is {user['bal']}")
                    else:
                        print(f"Unable to fetch customer with account {recepient_}")

                else:
                    print("Good bye")
                    break
        else:
            print("Invalid Login")

    elif choice == 's':
        name = input("Enter your name:\n>")
        dob= input("Enter your date of birth:\n>")
        bvn= input("Enter your BVN:\n>")
        pin = input("Enter your PIN:\n>")
        details = [('name', name), 
                ('dob', dob), 
                ('bvn', bvn), 
                ('pin', pin), 
                ('bal',0) 
                ]

        #generate account number
        num = [1,2,3,4,5,6,7,8,9,0]
        acc_num_list = ["3"]
        acc_num_list.extend([str(random.choice(num)) for _ in range(9)])


        acc_num = "".join(acc_num_list)

        data[acc_num] = dict(details)
        trans_data[acc_num] = []

        print(f"\nYour account has been created. You account number is {acc_num}\n")

    else:
        break



print(data)
print(trans_data)

