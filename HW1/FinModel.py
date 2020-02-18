"""
INTL 550 - HW1
Name : Shukhrat Khuseynov
ID   : 0070495
"""
from random import uniform

class Portfolio():
    def __init__(self):
        self.cash = 0.0
        self.stocks = []
        self.mfunds = []
        self.bonds = []
        self.log = ["Transactions:"]
        print("A portfolio is created.")
        
    def addCash(self, cash):
        """ Adds cash to the portfolio. """

        if cash >= 0:
            self.cash += cash
            
            # printing and saving transaction for the audit log
            transaction = "$%.2f are added to the portfolio." % cash
            self.log.append("%d. " % len(self.log) + transaction)
            print(transaction)

        else: print("Wrong input!")
    def withdrawCash(self, cash):
        """ Withdraws cash from the portfolio. """
        
        if cash >= 0:
            self.cash -= cash
                
            # printing and saving transaction for the audit log
            transaction = "$%.2f are withdrawn from the portfolio." % cash
            self.log.append("%d. " % len(self.log) + transaction)
            print(transaction)
                
        else: print("Wrong input!")
        
    def buyStock(self, shares, stock):
        """ Buys a stock given its variable and the number of shares. """
        
        cost = stock.price * shares
        if cost <= self.cash:
            self.cash -= cost
            self.stocks.append(stock)
            stock.quantity += shares
            
            # printing and saving transaction for the audit log
            transaction = "$%.2f are used to buy %d shares of %s stock." % (cost, shares, stock.symbol)
            self.log.append("%d. " % len(self.log) + transaction)
            print(transaction)
                
        else:
            print("There is no enough cash for this transaction!")
    def sellStock(self, symbol, shares):
        for stock in self.stocks:
            # no stocks with same symbols is assumed
            if stock.symbol == symbol:
                if shares <= stock.quantity:
                    price = round(uniform(0.5 * stock.price, 1.5 * stock.price), 2)
                    print("price =", price)
                    gain = price * shares
                    self.cash += gain
                    stock.quantity -= shares
                                        
                    # printing and saving transaction for the audit log
                    transaction = "$%.2f are earned after selling %d shares of %s stock." % (gain, shares, stock.symbol)
                    self.log.append("%d. " % len(self.log) + transaction)
                    print(transaction)
                    
                    if stock.quantity == 0:
                        self.stocks.remove(stock)
                else:
                    print("The maximum available amount of shares is exceeded!")                
                break
            elif stock == self.stocks[-1]:
                print("This stock is not in the portfolio!")

    def buyMutualFund(self, shares, mfund):
        """ Buys a mutual fund given its variable and the number of shares. """
        
        cost = 1 * shares
        if cost <= self.cash:
            self.cash -= cost
            self.mfunds.append(mfund)
            mfund.quantity += shares
            
            # printing and saving transaction for the audit log
            transaction = "$%.2f are used to buy %.2f shares of %s mutual fund." % (cost, shares, mfund.symbol)
            self.log.append("%d. " % len(self.log) + transaction)
            print(transaction)
            
        else:
            print("There is no enough cash for this transaction!")
    def sellMutualFund(self, symbol, shares):
        for mfund in self.mfunds:
            # no mutual funds with same symbols is assumed
            if mfund.symbol == symbol:
                if shares <= mfund.quantity:
                    price = round(uniform(0.9, 1.2), 2)
                    print("price =", price)
                    gain = price * shares
                    self.cash += gain
                    mfund.quantity -= shares
                                        
                    # printing and saving transaction for the audit log
                    transaction = "$%.2f are earned after selling %.2f shares of %s mutual fund." % (gain, shares, mfund.symbol)
                    self.log.append("%d. " % len(self.log) + transaction)
                    print(transaction)
                    
                    if mfund.quantity == 0.00:
                        self.mfunds.remove(mfund)
                else:
                    print("The maximum available amount of shares is exceeded!")                
                break
            elif mfund == self.mfunds[-1]:
                print("This mutual fund is not in the portfolio!")
                
    def buyBond(self, shares, bond):
        """ Buys a bond given its variable and the number of shares. """
        
        cost = bond.price * shares
        if cost <= self.cash:
            self.cash -= cost
            self.bonds.append(bond)
            bond.quantity += shares
            
            # printing and saving transaction for the audit log
            transaction = "$%.2f are used to buy %.2f shares of %s mutual fund." % (cost, shares, bond.symbol)
            self.log.append("%d. " % len(self.log) + transaction)
            print(transaction)

        else:
            print("There is no enough cash for this transaction!")
    def sellBond(self, symbol, shares):
        for bond in self.bonds:
            # no bonds with same symbols is assumed
            if bond.symbol == symbol:
                if shares <= bond.quantity:
                    price = round(uniform(1 * bond.price, 1.05 * bond.price), 2)
                    print("price =", price)
                    gain = price * shares
                    self.cash += gain
                    bond.quantity -= shares
                                        
                    # printing and saving transaction for the audit log
                    transaction = "$%.2f are earned after selling %d shares of %s bond." % (gain, shares, bond.symbol)
                    self.log.append("%d. " % len(self.log) + transaction)
                    print(transaction)
                    
                    if bond.quantity == 0:
                        self.bonds.remove(bond)
                else:
                    print("The maximum available amount of shares is exceeded!")                
                break
            elif bond == self.bonds[-1]:
                print("This bond is not in the portfolio!")
    
    def history(self):
        print("\n".join(self.log))
    def __str__(self):
        balance = "Portfolio.\n* cash: $%.2f" % self.cash + "\n"
        if len(self.stocks) != 0:
            balance += "-> stock(s):\n"
            for stock in self.stocks:
                balance += "%d %s\n" % (stock.quantity, stock.symbol)
        if len(self.mfunds) != 0:
            balance += "-> mutual fund(s):\n"
            for mfund in self.mfunds:
                balance += "%.2f %s\n" % (mfund.quantity, mfund.symbol)
        if len(self.bonds) != 0:
            balance += "-> bond(s):\n"
            for bond in self.bonds:
                balance += "%d %s\n" % (bond.quantity, bond.symbol)
        return "%s" %balance
    def __repr__(self):
        return self.__str__()

# a common class for stock, mfund, and bond used for the inheritance
class FinInstrument(object):
    def __init__(self, price, symbol):
        self.symbol = symbol
        self.price = price
        self.quantity = 0
    def __str__(self):
        return ("%s %s: price = %.2f, quantity = " % (self.type, self.price) + self.quantity + ".\n")
    def __repr__(self):
        return self.__str__()
        
class Stock(FinInstrument):
    def __init__(self, price, symbol):
        super().__init__(price, symbol)
        self.type = "stock"
        print("A stock with price $%.2f and symbol %s is created." % (price, symbol))
        
class MutualFund(FinInstrument):
    def __init__(self, symbol):
        super().__init__(1, symbol)
        self.quantity = 0.0
        self.type = "mfund"
        print("A mutual fund with symbol %s is created." % symbol)
        
class Bond(FinInstrument):
    def __init__(self, price, symbol):
        super().__init__(price, symbol)
        self.type = "bond"
        print("A bond with price $%.2f and symbol %s is created." % (price, symbol))

if __name__ == '__main__':
    
    try:
        portfolio = Portfolio() #Creates a new portfolio
        portfolio.addCash(300.50) #Adds cash to the portfolio
        s = Stock(20, "HFH") #Create Stock with price 20 and symbol "HFH"
        portfolio.buyStock(5, s) #Buys 5 shares of stock s
        mf1 = MutualFund("BRT") #Create MF with symbol "BRT"
        mf2 = MutualFund("GHT") #Create MF with symbol "GHT"
        portfolio.buyMutualFund(10.3, mf1) #Buys 10.3 shares of "BRT"
        portfolio.buyMutualFund(2, mf2) #Buys 2 shares of "GHT"
        print(portfolio) #Prints portfolio
        portfolio.sellMutualFund("BRT", 3) #Sells 3 shares of BRT
        portfolio.sellStock("HFH", 1) #Sells 1 share of HFH
        portfolio.withdrawCash(50) #Removes $50
        portfolio.history() #Prints a list of all transactions ordered by time
        
        #additionally for bonds
        b = Bond(10, "STD") #Create Bond with price 10 and symbol "STD"
        portfolio.buyBond(10, b) #Buys 10 shares of bond b
        print(portfolio) #Prints portfolio
        portfolio.sellBond("STD", 5) #Sells 5 shares of STD
        portfolio.history() #Prints a list of all transactions ordered by time
    except:
        print("Wrong input!")
    
# The end.