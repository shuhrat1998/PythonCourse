#   INTL 550 - HW1
#   Name : Shukhrat Khuseynov
#   ID   : 0070495

class Portfolio():
    def __init__(self):
        self.cash = 0
        self.stocks = []
        self.mfunds = []
        self.history = ["Transactions:\n"]
    def addCash(self, cash):
        self.cash += cash
        transaction = str(cash) + "$ of cash are added to the portfolio.\n"
        print(transaction)
        self.history.append(str(len(self.history)-1)+". "+transaction)
        
    def buyStock(self, shares, symbol):
        pass
    def buyMutualFund(self, shares, symbol):
        pass
    def sellMutualFund(self, symbol, shares):
        pass
    def sellStock(self, symbol, shares):
        pass
    def withdrawCash(self, cash):
        pass
    def history(self):
        pass
    def __str__(self):
        return "%s" %self.firstname

class FinInstrument(object):
    pass
class Stock(FinInstrument):
    pass
class MutualFund(FinInstrument):
    pass
class Bond(FinInstrument):
    pass
