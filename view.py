#!/usr/bin/env python3

import os

def shared_banner():
    os.system("clear")
    print("\n#############################"
          "\n#############################"
          "\n###                       ###"
          "\n###    Terminal Trader    ###"
          "\n###                       ###"
          "\n#############################"
          "\n#############################")



def main_menu():
    shared_banner()
    print(  "\n MAIN MENU"
            "\n   [b] Buy"
            "\n   [s] Sell"
            "\n   [l] Look-up"
            "\n   [q] Quote"
            "\n   [e] Exit")
    return input("\n   What would you like to do? ")

def login_menu():
    shared_banner()
    print ("\n    LOGIN MENU")
    return input("\n    Your Username: "),\
            input("\n    Your Password: ")



def buy_menu():
    shared_banner()
    print ("    BUY MENU")
    return input("\n    Ticker Symbol:  "),\
            input("\n    Trade Volume:   ")

def sell_menu():
    shared_banner()
    print ("   SELL MENU")
    return input("\n    Ticker Symbol:  "),\
            input("\n    Trade Volume:   ")

if __name__ == "__main__":
    print(login_menu())
