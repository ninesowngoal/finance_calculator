def simple_interest(deposit, rate, invest_years):
        simple_interest = deposit*(1 + (rate / 100)*invest_years)
        simple_answer = "This will be your interest after {} years: £{}".format(str(invest_years), str(simple_interest))
        print(simple_answer)