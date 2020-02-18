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
        """ Buys a stock given its variable and the number of shares (>0). """
        
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
        """ Sells a stock given its symbol and the number of shares (>0). """
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
        else:
            print("This stock is not in the portfolio!")

    def buyMutualFund(self, shares, mfund):
        """ Buys a mutual fund given its variable and the number of shares (>0). """
        
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
        """ Sells a mutual fund given its symbol and the number of shares (>0). """
        
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
                    
                    # rounding the number of shares for mutual fund
                    if round(mfund.quantity, 2) == 0.00:
                        mfund.quantity = 0
                        self.mfunds.remove(mfund)
                else:
                    print("The maximum available amount of shares is exceeded!")                
                break
        else:
            print("This mutual fund is not in the portfolio!")
                
    def buyBond(self, shares, bond):
        """ Buys a bond given its variable and the number of shares (>0). """
        
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
        """ Sells a bond given its symbol and the number of shares (>0). """
        
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
        else:
            print("This bond is not in the portfolio!")
    
    def history(self):
        """ Prints the list of transactions (audit log) of the portfolio. """
        
        print("\n".join(self.log))
        
    def __str__(self):
        """ Prints the balance of the portfolio. """
        
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
        """ Prints the balance of the portfolio. """
        
        return self.__str__()

# a common class for stock, mfund, and bond used for the inheritance
class FinInstrument(object):
    def __init__(self, price, symbol):
        self.symbol = symbol
        self.price = price
        self.quantity = 0
        print("A %s with price $%.2f and symbol %s is created." % (self.type, price, symbol))
        
    def __str__(self):
        """ Prints the attributes of the financial instrument used. """
        
        return "%s %s: price = %.2f, quantity = %d." % (self.type, self.symbol, self.price, self.quantity)
    
    def __repr__(self):
        """ Prints the attributes of the financial instrument used. """
        
        return self.__str__()
        
class Stock(FinInstrument):
    def __init__(self, price, symbol):
        self.type = "stock"
        super().__init__(price, symbol)
        
class MutualFund(FinInstrument):
    def __init__(self, symbol):
        self.type = "mutual fund"
        super().__init__(1, symbol)
    def __str__(self):
         # rewritten to output the quantity of mfund correctly (float):
        return "%s %s: price = %.2f, quantity = %.2f." % (self.type, self.symbol, self.price, self.quantity)
 
class Bond(FinInstrument):
    def __init__(self, price, symbol):
        self.type = "bond"
        super().__init__(price, symbol)

if __name__ == '__main__':
    
    try:
        #given commands from HW description:
        portfolio = Portfolio() 
        portfolio.addCash(300.50) 
        s = Stock(20, "HFH") 
        portfolio.buyStock(5, s) 
        mf1 = MutualFund("BRT") 
        mf2 = MutualFund("GHT") 
        portfolio.buyMutualFund(10.3, mf1) 
        portfolio.buyMutualFund(2, mf2)
        print(portfolio)
        #Given output of cash in the HW description is wrong ($140.50), I think.
        #It has to be (300.5 - 100 - 10.3 - 2) = $188.20 here.
        
        portfolio.sellMutualFund("BRT", 3) 
        portfolio.sellStock("HFH", 1) 
        portfolio.withdrawCash(50) 
        portfolio.history()
        
        #additional commands for bonds:
        b = Bond(10, "STD") #Creates Bond with price 10 and symbol "STD"
        portfolio.buyBond(10, b) #Buys 10 shares of bond b
        print(portfolio)
        portfolio.sellBond("STD", 5) #Sells 5 shares of STD
        portfolio.history()
        
        #commands checking whether eveything except cash clears from the balance:
        portfolio.sellStock("HFH", 4)
        print(portfolio)
        portfolio.sellBond("STD", 5)
        print(portfolio)
        portfolio.sellMutualFund("BRT", 7.3)
        print(portfolio)
        portfolio.sellMutualFund("GHT", 2)
        print(portfolio)
        portfolio.history()
        
        #commands checking some error messages
        u = Bond(10, "QWE")
        portfolio.buyBond(30, u)
        portfolio.sellBond("QWR", 40)
        portfolio.sellStock("RTY", 20)
        print(portfolio)
        portfolio.history()

    except:
        print("Wrong input!")
    
# The end.