#1. Writing a program for personal information
Name = input('Enter your name: ') #name is entered and Variable name created
Address = input('Enter city, state, and zip code: ') #Address entered and variable created
Phone = input('Enter your phone number: ') #Phone number entered and variable created
Major = input('Enter your College major: ') #College majore entered and variable created 

#Writing a code for the information to be displayed
print('Name:', Name, '\nAddress:', Address, '\nPhone number:', Phone,
       '\nCollege major:', Major)
#-----------------------------------------------------------------------------------------

#2. writing a program for sales prediction
total_sales = float(input('Enter total sales here: ')) #total sales defined 
profit = total_sales * .23 #profit of sales is defined and calculated

#Total profit is displayed
print(f'Total profit is $:, {profit:,.2f}.')
#-----------------------------------------------------------------------------------------

#3. writing a program for land calculation
total_land = int(input('Enter total square ft in your tract of land: ')) #total land defined
acres = total_land / 43560 #calculation for total land to acres

#land calculation displayed
print(f'The amount of acres in your land is, {acres:,}.')
#------------------------------------------------------------------------------------------

#4. Program for total purchase
SALES_TAX_RATE = .07
item1 = float(input('Enter the price of item1:')) #list of items and determining their prices
item2 = float(input('Enter the price of item2:'))
item3 = float(input('Enter the price of item3:'))
item4 = float(input('Enter the price of item4:'))
item5 = float(input('Enter the price of item5:'))
subtotal = item1 + item2 + item3 + item4 + item5 #Calculating the subtotal
sales_tax = SALES_TAX_RATE * subtotal #defining the sales tax
total_price = subtotal + sales_tax 

#Displaying grand total 
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Sales Tax: ${sales_tax:,.2f}")
print(f"Total: ${total_price:,.2f}")
#------------------------------------------------------------------------------------------------

#5. distance traveled program 
speed = 70
distance1 = 70 * 6
distance2 = 70 * 10
distance3 = 70 * 15
print(f'The car will travel {distance1} miles in 6 hours.')
print(f'The car will travel {distance2} miles in 10 hours.')
print(f'The car will travel {distance3} miles in 15 hours.')
#-----------------------------------------------------------------------------------------------

#6. sales tax program 
STATE_TAX = 0.05
COUNTY_TAX = 0.025
TOTAL_SALES_TAX = STATE_TAX + COUNTY_TAX 
purchase_amount = float(input('enter the total of your purchase: '))
county_tax = COUNTY_TAX * purchase_amount
state_tax = STATE_TAX * purchase_amount 
total_sales_tax = TOTAL_SALES_TAX * purchase_amount
final_sale = purchase_amount + total_sales_tax

#Display for every value
print(f'purchase amount: ${purchase_amount:,.2f}')
print(f'state sales tax: ${state_tax:,.2f}')
print(f'county sales tax: ${county_tax:,.2f}')
print(f'sales tax: $ {total_sales_tax:,.2f}')
print(f'total of sale: ${final_sale:,.2f}')
#-----------------------------------------------------------------------------------------------------

#7. calculating MPG
miles_driven = int(input('Enter the amount of miles driven: '))
gallons_used = int(input('Enter the amount of gallons used: '))
MPG = miles_driven / gallons_used

#displaying result
print('Your cars MPG this trip were', MPG)
#--------------------------------------------------------------------------------------------------------

#8. tip, tax, and total
TIP = .18
Sales_Tax = 0.07
TOTAL_MEAL_TAX = TIP + Sales_Tax #from here down calculating meal tax and prices
meal_purchased = float(input('enter the charge for the food: '))
tip_ammount = meal_purchased * TIP
Sales_Ammount = meal_purchased * Sales_Tax
entire_meal_tax = TOTAL_MEAL_TAX * meal_purchased
final_meal_price = entire_meal_tax + meal_purchased

#displaying results
print(f'Meal Total: ${meal_purchased:.2f}')
print(f'18% Tip: ${tip_ammount:.2f}')
print(f'Sales Tax: ${Sales_Ammount:.2f}')
print(f'Total of sale: ${final_meal_price:.2f}')
#----------------------------------------------------------------------------------------------------------
#9. Celcius to Farenheit Converter 
celcius = int(input('Enter a temperature in Celcius: '))
farenheit = ((9/5)*celcius) + 32

#displaying results
print('The tempreature converted from celcius to farenheit is', farenheit)
#-------------------------------------------------------------------------------------------------------------

#10. ingredient adjuster
#calculating how much of each ingredient per cookie 
Sugar = 1.5 / 48
butter = 1 / 48
flour = 2.75 / 48
num_cookies = int(input('how many cookies do you want to make? '))
#calculating ingredients per cookie 
sugar_needed = Sugar * num_cookies
butter_needed = butter * num_cookies 
flour_needed = flour * num_cookies

#displaying results 
print(f'For {num_cookies} cookies you will need:')
print(f'Cups of sugar: {sugar_needed}')
print(f'Cups of butter: {butter_needed}')
print(f'Cups of flour:{flour_needed}')
#------------------------------------------------------------------------------------------------------------

#11. Lion and Tiger percentages
num_lions = int(input('Enter the number of lions: '))
num_tigers = int(input('Enter the number of tigers: '))
total_cats = num_lions + num_tigers
#calculate percentages of lions and tigers
percent_lions = (num_lions / total_cats) * 100 
percent_tigers = (num_tigers / total_cats) * 100

#display results
print(f'The exhibit has {percent_lions:.2f}% lions and {percent_tigers}% tigers.')
#------------------------------------------------------------------------------------------------------------

#12. Stock transaction program
Joe_shares = 2000
Joe_shares_price = Joe_shares * 40.00
stock_broker_comission = Joe_shares_price * 0.03
#2 weeks later
Joe_shares_sold = 2000
Joe_shares_sold_price = Joe_shares_sold * 42.75
Stockbroker_2ndcomission = Joe_shares_price * .03
Joes_profit = Joe_shares_sold_price - (Joe_shares_price + stock_broker_comission + Stockbroker_2ndcomission)

#display results
print(f'Joe paid ${Joe_shares_price:,.2f} for his shares')
print(f'Joe paid his stockbroker ${stock_broker_comission:,.2f} for his 3% comission')
print(f'Joe sold his shares for ${Joe_shares_sold_price:,.2f} his stockbroker earned${Stockbroker_2ndcomission:,.2f}.')
print(f'Joes profit was ${Joes_profit:,.2f}.')
#-----------------------------------------------------------------------------------------------------------------------

#I did not understand number 13 and 14 even after reading through the entire book 