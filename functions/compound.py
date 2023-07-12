import math

def compound_interest(deposit, rate, invest_years):
    compound_interest = deposit*math.pow((1 + (rate / 100)),invest_years)
    compound_answer = "This will be your interest after {} years: £{}".format(str(invest_years), str(compound_interest))
    print(compound_answer)