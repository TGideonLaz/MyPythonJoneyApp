# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 22:47:30 2024

@author: GideonLaz
"""

# this is an app technicals viewer#

def PersonalPortal(): #this is the personal login area screen //Flow 4 function Flow 4
    print ("Logging in to your Personal Portal ... ")
    
    
def PassW():# managuser password // Flow 3 Function Flow 3
    PassWord = input("Enter your Password : ")
    ConfirmPassword = input("Confirm your Password")
    if ConfirmPassword == PassWord:
        PersonalPortal() #Flow4 Function call
    else:
        print ("the password you enterd does not match please enter the correct password")
        PassW() #Flow4 if Password does not match
def entrance():# entrance to the main body of the app //Flow 2 if yes
    print ("loading .......")
    print ("Welcome onboard the libravast portal, please enter your details below")
    FirstName = input("Enter your First Name : ")
    LastName = input("Enter your Last Name : ")
    MiddleName = input("Enter your Middle Name : ")
    UserName = input ("choos a Ussername")
    print("creat a password to access your account")
    PassW() # Flow 3 function call
    def WelcomeScreen(): # flow5 function
        print("Hi", UserName , " you are welcome to your personal portal on LibravastApp")
        print("......................................................................")
        print("......................................................................")
        print("W       W      EEEEE      L        CCCCC      OOO    M       M    EEEEE")
        print("W       W      E          L       C          O   O   MM     MM    E     ")
        print("W   W   W      EEEE       L      C          O   O   M M   M M    EEEE  ")
        print("W  W W  W      E          L       C          O   O   M  M M  M    E     ")
        print(" W W W W       EEEEE      LLLLL    CCCyCC      OOO    M   M   M    EEEEE")
        print("")  
        print("") 
        print("") 
        print("") 
        print(" In this portal you have access to a pool of sub-applications ranging from utilities , productivities and more.")
        print(" and note that they are all commandline applications as this portal would keep increasing in applications")
        print(" bellow are categories of applications you can access.")
        print("..........................................................................") 
        print("..........................................................................") 
        print("..........................................................................") 
    #.#########################################################################################################################################################
    # this is were the functions start and every orther function must go under here
    #edit only from this part of the app to contain the varieous categories of the available apps in the program. the main apps would be within each categories
    def ProductivityApps():
        print("Loading Productivity apps... ", UserName)
        
    def EducationApps():
        print("Loading Education apps... ", UserName)
    def BussinessApps():
        print("Loding Bussiness Apps...", UserName)
    # all app categories must not go bellow this line>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    #############################################################################################################################################################
    WelcomeScreen()# flow 5 function call
    #from below is the function that tells the user what categories of apps are there in this program.>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    def AppCategory(): #Flow 6 Function
        AppCat = input(""" enter the keyword of the categories you which to explore
                            Productivity,Education,Bussiness""")# this is were you should add prompt of any category as string aperaring on the screen to the user. just add your own category
    ###############################################################################################################################################################################################
    # from this pont is were you define your category and point it to the category function above. do no create above this line nor beneat the following line
        if AppCat == "productivity" or AppCat == "Productivity" or AppCat == "PRODUCTIVITY":
            ProductivityApps()
        elif AppCat == "education" or AppCat == "Education" or AppCat == "EDUCATION":
            EducationApps()
        elif AppCat == "bussiness" or AppCat == "Bussiness" or AppCat == "BUSSINESS":
            BussinessApps()
        else:
           print(" you have not enterd any available app category ", UserName , "please enter an available one")
           AppCategory()
    # all definition of category functions must be within and above the "else" keyword and should star with an "elif" also must not cross this line<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
    ####################################################################################################################################################################################################
    AppCategory()# flow 6 Function call
    
def outlog():#logging off function // Flow2 if no
    print ("Logging off.....")
    
    print ("logged off.")
    print("if you whish you can enter 'L' to Log back in or 'C' to continue logoff")
    
    def logback():
        print("you are logged off enter key 'L' to log back in")
        Log = input("")
        if Log == "L" or Log == "l":
            mainV()
        else:
            logg()
        
    def logg():
        print("you are logged off enter key 'L' to log back in")
        Log = input ("")
        if Log == "L" or Log =="l":
            mainV()
        else:
            logback()
    logg()
            
            
    
        
def mainV():#initial function of the app // app starting point function //Flow1
    print ("you are Now on the LibravastApp Portal")
    print ("enter Y to continue and N to abort")
    keyn = input("")
    if keyn =="Y" or keyn == "y":
        entrance()
    elif keyn == "N" or keyn =="n":
        outlog()
    else:
        print("you enterd a wrong key")
        mainV()
mainV()# app starting point
    