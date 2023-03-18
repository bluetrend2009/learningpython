basic = float(input("What is Ramesh's basic salary? "))
# dearness allowance is 40%
da = 0.4 * basic
# house rent allowance is 20%
hra = 0.2 * basic
# professional tax is 200
prof_tax = 200
# provident fund is 4300
prov_fund = 4300
# gross amount is basic + allowances - deductions
gross = basic + da + hra - prof_tax - prov_fund
# print the gross amount
print(f"Ramesh's gross salary is: {gross}")