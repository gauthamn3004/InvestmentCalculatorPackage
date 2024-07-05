from investment_calculator_package import *
sip = SIP_Calculator()
location = 'D:/Documents/Code/Github/InvestmentCalculatorPackage/test/sip_sample.csv'
sip.update_investments(csv_location = location)
print("SIP final investment: {0}".format(str(sip.final_investment_amount)))

# lumpsum = Lumpsum_Calculator(amount = sip.final_investment_amount, rate_of_interest = 5, investment_term_in_years = 40)
# print("Lumpsum final investment: {0}".format(str(lumpsum.final_investment_amount)))