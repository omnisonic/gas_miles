# function to calculate cost of miles traveled
def cost_of_miles(miles,gas_price,mpg):
    return miles/mpg*gas_price


miles = int(input("How far are you going? "))
gas_price = float(input("How much does gas cost per gallon? "))
mpg = int(input("How many miles do you get per gallon? "))

print('The cost of driving',miles,'miles is',cost_of_miles(miles,gas_price,mpg))

