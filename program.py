# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:42:07 2021

@author: Nimisha
"""
carbon_footprint = 0
def member():
    global carbon_footprint
    while True:  
        try: 
            n_member = int(input("Enter the no of members in your household (including yourself) : ")) 
        except ValueError: 
            print("Please enter an integer value!") 
            continue
        else: 
            if(n_member == 1):
                carbon_footprint += 14
            elif(n_member == 2):
                carbon_footprint += 12
            elif(n_member == 3):
                carbon_footprint += 10
            elif(n_member == 4):
                carbon_footprint = 8
            elif(n_member == 5):
                carbon_footprint = 6
            elif(n_member == 6):
                carbon_footprint = 4
            elif(n_member > 6):
                carbon_footprint = 2
            else:
                print("Invalid option. Try Again!\n")
                member()
        break
def house():
    global carbon_footprint
    while True:  
        try: 
            n_house = int(input("Choose the size of your house :\n1.Large house\n2.Medium house\n3.Small house\n4.Apartment\nYour choice : ")) 
        except ValueError: 
            print("Please enter an integer value!") 
            continue
        else:      
            if(n_house == 1):
             carbon_footprint += 10
            elif(n_house == 2):
                carbon_footprint += 7
            elif(n_house == 3):
                carbon_footprint += 4
            elif(n_house == 4):
                carbon_footprint += 2
            else:
                print("Invalid option. Try Again!\n")
                house()
        break
def food():
    global carbon_footprint
    while True:
        try:
            n_food = int(input("What are your food choices ?\n1.Most of your food is pre-packaged\n2.You eat domestic meat on a daily basis\n3.You eat domestic meat a few times a week\n4.You are a vegetarian\n5.You are vegan or eat only wild meat\nYour choice : "))
        except ValueError:
            print("Please enter an integer value!")
            continue
        else:
            if(n_food == 1):
                carbon_footprint += 12
            elif(n_food == 2):
                carbon_footprint += 10
            elif(n_food == 3):
                carbon_footprint += 8
            elif(n_food == 4):
                carbon_footprint += 4
            elif(n_food == 5):
                carbon_footprint += 2
            else:
                print("Invalid Option. Try Again!! ")
                food()
            break
def water():
    global carbon_footprint
    while True:
        try:
            n_water = int(input("Do you own/use any of the following items:\n1.Dishwasher\n2.Washing Machine\n3.Both Dishwasher and Washing Machine\n4.Don't own any of the two\nYour Choice: "))
        except ValueError:
            print("Please enter an integer value!")
            continue
        else:
            if(n_water == 1):
                def dishwasher():
                    global carbon_footprint
                    while True:
                        try:
                            n_dishwasher = int(input("How long do you run your dishwasher ? :\n1.more than 9 times per week\n2.4 to 9 times a week\n3.1 to 3 times a week\nYour Choice : "))
                        except ValueError:
                            print("Please enter an integer value!")
                            continue
                        else:
                            if(n_dishwasher == 1):
                              carbon_footprint += 3
                            elif(n_dishwasher == 2):
                                carbon_footprint += 2
                            elif(n_dishwasher == 3):
                                carbon_footprint += 1
                            else:
                                print("Invalid Option. Try Again!! ")
                                dishwasher()
                            break
                dishwasher()
            elif(n_water == 2):
                def WashingMachine():
                    global carbon_footprint
                    while True:
                        try:
                            n_Washing = int(input("How long do you run your washing machine ? :\n1.more than 9 times per week\n2.4 to 9 times a week\n3.1 to 3 times a week\nYour Choice : "))
                        except ValueError:
                            print("Please enter an integer value!")
                            continue
                        else:
                            if(n_Washing == 1):
                              carbon_footprint += 3
                            elif(n_Washing == 2):
                                carbon_footprint += 2
                            elif(n_Washing == 3):
                                carbon_footprint += 1
                            else:
                                print("Invalid Option. Try Again!! ")
                                WashingMachine()
                        break
                WashingMachine()
            elif(n_water == 3):
                dishwasher()
                WashingMachine()
            else:
                print("Invalid Option. Try Again!! ")
                water()
            break
def purchase():
    global carbon_footprint
    while True:
        try:
            n_purchase = int(input("How many new pieces of furniture, electronics, or other household gadgets do you purchase per year\n1.More than 7\n2.Between 5 - 7\n3.between 3 and 5 items\n4.less than 3 items\n5.Almost nothing or only secondhand items\nYourChoice : "))
        except ValueError:
            print("Please enter an integer value!")
            continue
        else:
            if(n_purchase == 1):
                carbon_footprint += 10
            elif(n_purchase == 2):
                carbon_footprint += 8
            elif(n_purchase == 3):
                carbon_footprint += 6
            elif(n_purchase == 4):
                carbon_footprint += 4
            elif(n_purchase == 5):
                carbon_footprint += 2
            else:
                print("Invalid Option. Try Again!! ")
                purchase()
        break
def garbage():
    global carbon_footprint
    while True:
        try:
            n_garbage = int(input("How many garbage cans do you fill per week\n1.4 garbage cans each week\n2.3 garbage cans each week\n3.2 garbage cans each week\n4.1 garbage cans each week\n5.half of a garbage can or less per week\nYourChoice : "))
        except ValueError:
            print("Please enter an integer value!")
            continue
        else:
            if(n_garbage == 1):
                carbon_footprint += 50
            elif(n_garbage == 2):
                carbon_footprint += 40
            elif(n_garbage == 3):
                carbon_footprint += 30
            elif(n_garbage == 4):
                carbon_footprint += 20
            elif(n_garbage == 5):
                carbon_footprint += 5
            else:
                print("Invalid Option. Try Again!! ")
                garbage()
        break
def recycle():
    global carbon_footprint
    while True:
        try:
            n_recycle = int(input("Select the applicable option\n1.I don't recycle\n2.I recycle\nYour Choice : "))
        except ValueError:
            print("Please enter an integer value!")
            continue
        else:
            if(n_recycle == 1):
                carbon_footprint += 24
            elif(n_recycle == 2):
                carbon_footprint += 24
                def opt():
                  global carbon_footprint
                  while True:
                      try:
                          n_1recycle = int(input("How many of the following items do you recycle - \n->Glass  ->Pastic  ->Paper  ->Aluminium  ->Steel  ->Food Waste\n1.Only 1\n2.Two\n3.Three\n4.Four\n5.five\n6.All Of the items \nYour Choice : "))
                      except ValueError:
                          print("Please enter an integer value!\n")
                          continue
                      else:  
                          if(n_1recycle == 1):
                              carbon_footprint -= 4
                          elif(n_1recycle == 2):
                              carbon_footprint -= 8
                          elif(n_1recycle == 3):
                              carbon_footprint -= 12
                          elif(n_1recycle == 4):
                              carbon_footprint -= 16
                          elif(n_1recycle == 5):
                              carbon_footprint -= 20
                          elif(n_1recycle == 6):
                              carbon_footprint -= 24
                          else:
                              print("Invalid Option. Try Again!!\n")
                              opt()
                      break
                opt()
            else:
                print("Invalid Option. Try Again!! \n")
                garbage() 
        break
print("Carbon Footprint (household) Point Calculator\nNOTE: The lower the points the better")                               
member()
food()
house()
water()
purchase()
garbage()
recycle()
print("Your Points are : "+ str(carbon_footprint))
if carbon_footprint<=50:
    print("You are making a small impact on the environment")
else:
    print("You are making a big impact on the environment")
