from functions import *

#User chooses what they would like to calculate: bond or investment - case insensitive.
#Based on their choice, the user will input the necessary information (deposit, interest rate and time taken).
#Program will calculate the investment or home loan repayment.
print("This program is an investment and home loan repayment calculator.")
print("To choose which you would like, please type 'Investment' or 'Bond'.")

while True:
    calc_choice = input("What would you like to calculate? Investment or Bond?: ")

    if calc_choice == "investment" or calc_choice.lower() == "investment" or calc_choice.upper() == "investment": #Checks for investment in the user input. Case insensitive.
        print("You have chosen investment.")
        try:
            deposit = int(input("Enter the amount of money you are depositing: "))
            rate = float(input("Enter the interest rate (number only, without '%'): "))
            invest_years = int(input("Enter the number of years you plan on investing: "))
            interest = input("Would you like to calculate simple or compound interest?: ") #User chooses whether to calculate simple or compound interest.
        except ValueError:
            print("That didn't quite work. Please try again. Note: You may have entered a letter instead of a number.")
            continue
    if interest == "simple" or interest.lower() == "simple" or interest.upper() == "simple": #Simple interest will be calculated and the result returned.
        simple.simple_interest(deposit, rate, invest_years)
    elif interest == "compound" or interest.lower() == "compound" or interest.upper() == "compound": #Compound interest will be calculated and the result returned.
        print("Compound interest will now be calculated.")
        compound.compound_interest(deposit, rate, invest_years)
    elif interest != "simple" or interest != "compound":
        print("Invalid input.")

    if calc_choice == "bond" or calc_choice.lower() == "bond" or calc_choice.upper() == "bond": #Checks for bond in the user input. Case insensitive.
        print("You have chosen bond.")
        try:
            house_value = int(input("What is the current value of the house?: "))
            house_rate = float(input("Enter the interest rate (number only, without '%'): "))
            invest_months = int(input("Enter the number of months you plan to take to repay the bond: "))
        except ValueError:
            print("That didn't quite work. Please try again. Note: You may have entered a letter instead of a number.")
            continue
        print("The bond repayment will now be calculated.")
        bond.bond_repayment(house_rate, house_value, invest_months)

    elif calc_choice != "bond" or calc_choice != "investment":
        print("Invalid input.")

    user_continue = input("Would you like to continue?: ")
    
    if user_continue == "y" or user_continue == "yes":
        continue
    elif user_continue == "n" or user_continue == "no":
        break