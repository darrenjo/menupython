#-------------------------------------------------------------------------------
# Name:        Structural Programming Modules
# Purpose:     Praktikum Pengantar Teknologi Informasi I (2020/2021)
#
# Author:      Darren Jo
#
# Created:     2020/10/15
# Copyright:   (c) Jo Darren Adriel 2020
# Licence:     VK8MA-NPHZQ-H77JM-XXXXX-XXXXX
#-------------------------------------------------------------------------------

global appetizerCount 
global mainCourseCount 
global dessertCount 
global drinksCount

global appt
global mainc
global dessert
global drinks

global totitem
global totprice
global countQuantity



#Main Menu
def displayMenu():
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("Do you want to order something delicious? (y/n)\n")
    print("***********************************************\n") 


#Menu Appetizer
def appetizerMenu():
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("")
    print("MIT & MT Restaurant Appetizer Menu: ")
    print("1. Mussels Marinara - Rp. 80.000")
    print("2. Garlic Bread with Cheese - Rp. 45.000")
    print("3. Grilled Asparagus in Prosciutto - Rp. 100.000")
    print("")
    print("99. Next to Main Course")
    print("Enter your order (1-3 or 99): ")


#Harga Appetizer
def appetizerPrice(no_appt):
    global appetizerCount
    global appt
    if no_appt == 1 :
        appetizerCount = 1
        appt = 80000 
    elif no_appt == 2 :
        appetizerCount = 1
        appt = 45000
    elif no_appt == 3 :
        appetizerCount = 1
        appt = 100000
    elif no_appt == 99 :
        appetizerCount = 0
        appt = 0
    else :
        appetizerCount = 0
        appt = 0
        print("Input Salah")
    return


#Menu Main Course
def mainCourseMenu():
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("")
    print("MIT & MT Restaurant Main Course Menu:")
    print("1. Seafood Risotto - Rp. 150.000")
    print("2. Vegetable Lasagna - Rp. 90.000")
    print("3. Grilled Chicken - Rp. 120.000")
    print("")
    print("99. Next to Dessert")
    print("Enter your order (1-3 or 99):")


#Harga Main Course
def mainCoursePrice(no_mainc):
    global mainCourseCount
    global mainc
    if no_mainc == 1 :
        mainCourseCount = 1
        mainc = 150000
    elif no_mainc == 2 :
        mainCourseCount = 1
        mainc = 90000
    elif no_mainc == 3 :
        mainCourseCount = 1
        mainc = 120000
    elif no_mainc == 99 :
        mainCourseCount = 0
        mainc = 0
    else :
        mainCourseCount = 0
        mainc = 0
        print("Input Salah")
    return


#Menu Dessert
def dessertMenu():
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("")
    print("MIT & MT Restaurant Dessert Menu:")
    print("1. Raspberry Panna Cotta - Rp. 70.000")
    print("2. Classic Chocolate Cake - Rp. 80.000")
    print("3. Signature Tiramisu - Rp. 60.000")
    print("")
    print("99. Next to Drinks")
    print("Enter your order (1-3 or 99): ")


#Harga Dessert
def dessertPrice(no_dessert):
    global dessertCount
    global dessert
    if no_dessert == 1 :
        dessertCount = 1
        dessert = 70000
    elif no_dessert == 2 :
        dessertCount = 1
        dessert = 80000
    elif no_dessert == 3 :
        dessertCount = 1
        dessert = 60000
    elif no_dessert == 99 :
        dessertCount = 0
        dessert = 0
    else :
        dessertCount = 0
        dessert = 0
        print("Input Salah")
    return


#Menu Drinks
def drinksMenu():
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("")
    print("MIT & MT Restaurant Drinks Option:")
    print("1. Mineral Water - Rp. 50.000")
    print("2. Coke - Rp. 80.000")
    print("3. Sparkling Water - Rp. 70.000")
    print("")
    print("99. Finish Order")
    print("Enter your order (1-3 or 99):")


#Harga Minuman
def drinksPrice(no_drinks):
    global drinksCount
    global drinks
    if no_drinks == 1 :
        drinksCount = 1
        drinks = 50000
    elif no_drinks == 2 :
        drinksCount = 1
        drinks = 80000
    elif no_drinks == 3 :
        drinksCount = 1
        drinks = 70000
    elif no_drinks == 99 :
        drinksCount = 0
        drinks = 0
    else :
        drinksCount = 0
        drinks = 0
        print("Input Salah")
    return


#Invoice
def invoiceDisplay(totitem,totprice):
    print("************************************************")
    print("*  Thank you for visiting MIT & MT Restaurant  *")
    print("************************************************")
    print("Total Item :",totitem)
    print("Total Price: Rp ",format(totprice, ",.2f"), sep="")
    print("")
    print("************************************************")
    print("*  Please review us on any website that exists *")
    print("************************************************")


#Menghitung Total Item
def countQuantity(appetizerCount, mainCourseCount, dessertCount , drinksCount):
    totitem = 0
    totitem = appetizerCount + mainCourseCount + dessertCount + drinksCount
    return totitem

def totalPrice(appt, mainc, dessert, drinks):#fungsi harga total harga
    totprice = 0
    totprice = appt + mainc + dessert + drinks
    return totprice


# Show the display menu here
displayMenu()
# User choose the decision
y_n = str(input("y/n? = "))

# Condition if True
if(y_n == "y" or y_n == "Y"):
    #Appetizer
    appetizerMenu()
    no_appt = 0
    no_appt = int(input("Masukkan input yang anda inginkan : "))
    appetizerPrice(no_appt)

    #Main Course
    mainCourseMenu()
    no_mainc = 0
    no_mainc = int(input("Masukkan input yang anda inginkan : "))
    mainCoursePrice(no_mainc)

    #Dessert
    dessertMenu()
    no_dessert = 0
    no_dessert = int(input("Masukkan input yang anda inginkan : "))
    dessertPrice(no_dessert)

    #Drinks
    drinksMenu()
    no_drinks = 0
    no_drinks = int(input("Masukkan input yang anda inginkan : "))
    drinksPrice(no_drinks)

    #Total item
    totitem = countQuantity(appetizerCount, mainCourseCount, dessertCount, drinksCount)

    #Total Price
    totprice = totalPrice(appt, mainc, dessert, drinks)

    #Manggil Invoice
    invoiceDisplay(totitem,totprice)

elif(y_n == "n" or y_n == "N"):
    print("*****************************************")
    print("*  Thank you and see you again later!   *")
    print("*    Created  by Darren using Python    *")
    print("*****************************************")

# Condition if false
    # Write your code
else:
    print("***********************************************")
    print("*        Welcome to MIT & MT Restaurant       *")
    print("*        Created by Darren using Python       *")
    print("***********************************************\n")
    print("Do you want to order something delicious? (y/n)\n")
    print("***********************************************\n")
    print("ERROR UNKNOWN INPUT")
