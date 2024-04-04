# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:47:30 2024

@author: GideonLaz
"""

# this is an app technicals viewer#

def PersonalPortal(): #this is the personal login area screen
    print ("Logging in to your Personal Portal ... ")
    
    
def PassW():# managuser password
    PassWord = input("Enter your Password : ")
    ConfirmPassword = input("Confirm your Password")
    if ConfirmPassword == PassWord:
        PersonalPortal()
    else:
        print ("the password you enterd does not match please enter the correct password")
        PassW()
def entrance():# entrance to the main body of the app
    print ("loading .......")
    print ("Welcome onboard the libravast portal, please enter your details below")
    FirstName = input("Enter your First Name : ")
    LastName = input("Enter your Last Name : ")
    MiddleName = input("Enter your Middle Name : ")
    UserName = input ("choos a Ussername")
    print("creat a password to access your account")
    PassW()
    print("Hi", UserName , " you are welcome to your personal portal on LibravastApp")
    print("......................................................................")
    print("......................................................................")
    print("W       W      EEEEE      L        CCCCC      OOO    M       M    EEEEE")
    print("W       W      E          L       C          O   O   MM     MM    E     ")
    print("W   W   W      EEEE       L      C          O   O   M M   M M    EEEE  ")
    print("W  W W  W      E          L       C          O   O   M  M M  M    E     ")
    print(" W W W W       EEEEE      LLLLL    CCCyCC      OOO    M   M   M    EEEEE")
        
        
    
def outlog():#logging off function
    print ("Logging off.....")
    
def mainV():#initial function of the app
    print ("you are Now on the LibravastApp Portal")
    print ("enter Y to continue and N to abort")
    keyn = input("")
    if keyn =="Y" or keyn == "y":
        entrance()
    elif keyn == "N" or keyn =="n":
        outlog()
mainV()# app starting point
    