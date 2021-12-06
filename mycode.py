"""
Ethan Porter
Assignment 8.1: Loadable contact list - Now As aA Class
mycode.py
This code acts as a form of practicing different functions in an ATM list using classes that I created.
I used the PowerPoint provided and taught by instructor Harikrishna Kuttivelil taught through the 9.1 - 10.1 lecturre notes as well as help from Sanjay Shrikanth
"""
#creates a class atm
class atm:
    def __init__(self,name, balance, PIN):
        self.machine[name] = (balance, PIN)
    #Provides the user with a choice to see the balance of the program by putting in a PIN
    def get_balance(self, name,PIN):
        if name in self.balance:
                depo, pin = self.balance[name]
                if pin == PIN:
                    return f"Balance Set: {depo}"
        return "Invalid Account"
    def set_balance (self, name, PIN, deposit):
        if name in self.balance:
                depo, pin = self.balance[name]
                if pin == PIN:
                    self.balance[name]= (depo, pin)
                    return f"Balance Set: {self.balance}"
        return "Invalid Account" 
    #a function that is used to allow the user to input an amount they wish to withdraw and does it
    def withdraw(self, name, PIN):
        withdraw = float(input("How much would you like to withdrawal?"))
        if name in self.balance:
                depo, pin = self.balance[name]
                if pin == PIN:
                    depo-=withdraw
                    self.balance[name]= (depo, pin)
                    return f"Withdrew: {withdraw}. Current Balance: {depo}"
        return "Invalid Account" 
    #a function that i used to allow a user to put in a set amount of money as a deposit
    def deposit(self, name, PIN):
        deposit = float(input("Please insert cash to deposit:"))
        if name in self.balance:
                depo, pin = self.balance[name]
                if pin == PIN:
                    depo += deposit
                    self.balance[name]= (depo, pin)
                    return f"Withdrew: {deposit}. Current Balance: {depo}"