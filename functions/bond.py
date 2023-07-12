def bond_repayment(house_rate, house_value, invest_months):
    repayment = (((house_rate / 100) / 12) * house_value) / (1 - (1 + ((house_rate / 100) / 12))**(-invest_months)) #Bond repayment calculation.
    repayment_answer = "This is the amount you will have to pay each month over {} months: £{}".format(str(invest_months), str(repayment))
    return(repayment_answer)