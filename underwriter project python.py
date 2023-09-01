print('''
  Mortgage Underwriter Project
  ============================
''')
print('''This program determines a customers eligibility for a home loan based on the following risk factors
''')
print('''For credit score, debt to income ratio and appraised loan to value enter numbers instead of characters
''')
restart = "y"
def uw_model():
    credit_score = input('''Enter Customers Credit Score:
      ''')
    credit_score = float(credit_score)
    debt_to_income_ratio = input('''Enter Debt to Income Ratio Percentage:
      ''')
    debt_to_income_ratio = float(debt_to_income_ratio)
    Approved_loan_to_value = input('''Enter Appraised Loan to Value Percentage:
      ''')
    Approved_loan_to_value = float(Approved_loan_to_value)
    bank_col = input('''Bankruptcy or collections in the past 7 years? Y/N: ''').lower()
    
    if credit_score >= 620 and debt_to_income_ratio < 43 and Approved_loan_to_value <+ 80 and bank_col ==("n"):
        print('''
                APPROVED
    ''')
    else:
        print('''
                DECLINED
    ''')
    #620 minimum credit score
    #43% maximum debt to income ratio
    #80% maximum loan to value ratio
    if credit_score < 620:
        print('''*Low Credit Score
    ''')
    if debt_to_income_ratio >= 43:
        print('''*Debt to Income ratio is too high
    ''')
    if Approved_loan_to_value > 80:
        print('''*Loan to value is too high
    ''')
    if bank_col == ("y"):
        print('''*Negative credit record
    ''')
        
while restart == "y":
    uw_model()
    continue_question = input ("Do you want to continue Y/N?: ").lower()
    restart = continue_question
