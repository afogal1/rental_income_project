class RentProbCalc:
    
    def __init__(self):
        self.rent = []
        self.totalMonthlyIncome = []
        self.totalExpenses = []
        self.totalMonthlyCashFlow = []
        self.propertyCost = []
        
        
        
    def expenses(self):
        tax = int(input("Enter the amount of property taxes you will have to pay: "))
        insurance = int(input("Enter the insurance amount: "))
        vacancyPercent = int(input("Enter the percentage of rental income that will be deducted in case of vacancy: ")) 
        vacancyExpense = vacancyPercent / self.rent
        self.totalExpenses = tax + insurance + vacancyExpense
        print(f"vacancyExpense is {vacancyExpense}")
        
    def initialRentalCalc(self):
        self.propertyCost = int(input("Please enter in the listing price for the property: "))
        self.rent = int(input("Enter the monthly income you receive in rent from your tenants: "))
        otherIncome = int(input("Enter the amount of any other income you'll receive from tenants: "))
        self.totalMonthlyIncome = self.rent + otherIncome
        print(f"The total monthly income you will receive from this property is: {self.totalMonthlyIncome}")

        
    def mortgageCalc(self):
        lifeOfLoan = int(input("Enter how long the loan contract is set for: "))
        mortgage = self.propertyCost / lifeOfLoan 
        print(f"The monthly mortgage on this property is {mortgage}")
    

    def cashFlow(self):
        self.totalMonthlyCashFlow = self.totalMonthlyIncome - self.totalExpenses
        print(f"your total monthly cash flow after deducting monthly expenses is {self.totalMonthlyCashFlow}")
    

    def returnOnInvestment(self):
        downPayment = int(input("How much did you put down on your property: "))
        closingCost = int(input("Enter your closing cost: "))
        rehabBudget = int(input("Did you make any fixes to your property if so enter the total amount spent on rehabilitation: "))
        totalInvestment = downPayment + closingCost + rehabBudget
        print(f"Your total investment into this property is {totalInvestment}")
        annualCashFlow = self.totalMonthlyCashFlow * 12
        roi = annualCashFlow / totalInvestment
        print(f"Your return on investment is {roi}")


newHome = RentProbCalc()


def run():
    while True:
        calculating = input("What would you like to calculate or visualize: initial investment(1), expenses(2), mortgage(3), cash flow(4) or your return on investment(5) or 'quit' to end. ")
        if calculating == "1":
            print(newHome.initialRentalCalc())
        elif calculating == "2":
            print(newHome.expenses())
        elif calculating == "3":
            print(newHome.initialRentalCalc())
            print(newHome.mortgageCalc())
        elif calculating == "4":
            print(newHome.cashFlow())
        elif calculating == "5":
            print(newHome.initialRentalCalc())
            print(newHome.returnOnInvestment())
        elif calculating == "quit":
            break
        else: 
            print("Error: Please try again.")
            
run()

