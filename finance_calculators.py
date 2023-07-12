import math
#User chooses what they would like to calculate: bond or investment - case insensitive.
#Based on their choice, the user will input the necessary information (deposit, interest rate and time taken).
#Program will calculate the investment or home loan repayment.
print("This program is an investment and home loan repayment calculator.")
print("To choose which you would like, please type 'Investment' or 'Bond'.")

calc_choice = input("What would you like to calculate? Investment or Bond?: ")

if calc_choice == "investment" or calc_choice.lower() == "investment" or calc_choice.upper() == "investment": #Checks for investment in the user input. Case insensitive.
    print("You have chosen investment.")
    deposit = int(input("Enter the amount of money you are depositing: "))
    rate = float(input("Enter the interest rate (number only, without '%'): "))
    invest_years = int(input("Enter the number of years you plan on investing: "))
    interest = input("Would you like to calculate simple or compound interest?") #User chooses whether to calculate simple or compound interest.
    if interest == "simple" or interest.lower() == "simple" or interest.upper() == "simple": #Simple interest will be calculated and the result returned.
        print("Simple interest will now be calculated.")
        simple_interest = deposit*(1 + (rate / 100)*invest_years)
        simple_answer = "This will be your interest after {} years: £{}".format(str(invest_years), str(simple_interest))
        print(simple_answer)
    elif interest == "compound" or interest.lower() == "compound" or interest.upper() == "compound": #Compound interest will be calculated and the result returned.
        print("Compound interest will now be calculated.")
        compound_interest = deposit*math.pow((1 + (rate / 100)),invest_years)
        compound_answer = "This will be your interest after {} years: £{}".format(str(invest_years), str(compound_interest))
        print(compound_answer)
    else:
        print("Invalid input.")

elif calc_choice == "bond" or calc_choice.lower() == "bond" or calc_choice.upper() == "bond": #Checks for bond in the user input. Case insensitive.
    print("You have chosen bond.")
    house_value = int(input("What is the current value of the house?: "))
    house_rate = float(input("Enter the interest rate (number only, without '%'): "))
    invest_months = int(input("Enter the number of months you plan to take to repay the bond: "))
    print("The bond repayment will now be calculated.")
    repayment = (((house_rate / 100) / 12) * house_value) / (1 - (1 + ((house_rate / 100) / 12))**(-invest_months)) #Bond repayment calculation.
    repayment_answer = "This is the amount you will have to pay each month over {} months: £{}".format(str(invest_months), str(repayment))
    print(repayment_answer)

elif calc_choice != "bond" or calc_choice != "investment":
    print("Invalid input.")