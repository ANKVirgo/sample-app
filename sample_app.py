#import moduels
import urllib.parse 
import requests
import os
import colorsys
import colorama
from colorama import Fore, Style, Back #text colors and format

def clear(): #clears the console
    os.system('clear')

main_api = "https://www.mapquestapi.com/directions/v2/route?" #API for MapQuest
key = "6qshbqYuEzLdvnVfN69qmcQMYwAf3V5X" #Personal Consumer Key

def ESUnit(json_data,orig,dest): #display output using English System of Units
    json_data = json_data
    orig =orig
    dest = dest
    if json_status == 0:   #if the route is found     
        print(Fore.LIGHTGREEN_EX+"API Status: " + str(json_status) + " = A successful route call.\n"+Style.RESET_ALL) 
        print(Fore.BLUE+"============================================="+Style.RESET_ALL)
        print(Fore.GREEN+"Directions from " + (orig) + " to " + (dest))         
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))
        print("Miles:           " + str("{:.2f}".format(json_data["route"]["distance"])))  #english system use inches, feet, yards, and miles to measure distance                
        print("Fuel Used (Gal): " + str("{:.2f}".format(json_data["route"]["fuelUsed"])))   #english system use  ounce, cups, pints, quarts, and gallons to measure capacity or volume      
        print(Style.RESET_ALL)
        print(Fore.BLUE+"=============================================\n"+Style.RESET_ALL) 
        for each in json_data["route"]["legs"][0]["maneuvers"]:   #step by step directions  
            print(Fore.CYAN+(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])) + " mi)"+Style.RESET_ALL)) 
            print(Fore.BLUE+"=============================================\n"+Style.RESET_ALL) 

def SIUnit(json_data,orig,dest): #display output using international system of Units(SI)
    json_data = json_data
    orig =orig
    dest = dest
    if json_status == 0:   #if the input field is filled and route is found    
        print(Fore.LIGHTGREEN_EX+"API Status: " + str(json_status) + " = A successful route call.\n"+Style.RESET_ALL) 
        print(Style.RESET_ALL)
        print(Fore.BLUE+"============================================="+Style.RESET_ALL)
        print(Fore.GREEN+"Directions from " + (orig) + " to " + (dest))         
        print("Trip Duration:   " + (json_data["route"]["formattedTime"]))           
        print("Kilometers:           " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))        
        print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))) 
        print(Style.RESET_ALL)        
        print(Fore.BLUE+"=============================================\n"+Style.RESET_ALL) 
        for each in json_data["route"]["legs"][0]["maneuvers"]:   #step by step or narative directions  
            print(Fore.CYAN+(each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"+Style.RESET_ALL)) 
            print(Fore.BLUE+"=============================================\n"+Style.RESET_ALL) 
    

while True: 
    print()
    #user input: choose metric system
    print(Fore.MAGENTA+"English System of Units || SI Unit" + Style.RESET_ALL)
    metric = input(Fore.YELLOW+"Select a Metric System [ES/SI]: "+Style.RESET_ALL)
    

#if user input is in lowercase ES Units
    if metric.lower() == "es": 
        #user input starting point 
        orig = input(Fore.YELLOW+"Starting Location: "+Style.RESET_ALL)  
        if orig == "quit" or orig == "q": 
            clear() #call clear console terminal
            break #stop

        #user input end point
        dest = input(Fore.YELLOW+"Destination: "+Style.RESET_ALL)  
        #user input to stop the program
        if dest == "quit" or dest == "q":
            clear()  
            break

        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})    
        print(Fore.LIGHTGREEN_EX+"\nURL: " + (url)) 
        print(Style.RESET_ALL)  #stop colorama 
        json_data = requests.get(url).json()    #requests.get will make the API call to the MapQuest API
        json_status = json_data["info"]["statuscode"]    #check route is valid
        
        if json_status == 0:  #route exists
            ESUnit(json_data,orig,dest)   
        elif json_status == 402: #invalid route
            print("**********************************************")         
            print(Fore.RED+"Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations."+Style.RESET_ALL)         
            print("**********************************************\n")     
        elif json_status == 611: #missing input
            print("**********************************************")         
            print(Fore.RED+"Status Code: " + str(json_status) + "; Missing an entry for one or both locations."+Style.RESET_ALL)         
            print("**********************************************\n")     
        else: #uncited errors
            print("************************************************************************")         
            print(Fore.RED+"For Staus Code: " + str(json_status) + "; Refer to:")         
            print("https://developer.mapquest.com/documentation/directions-api/status-codes"+Style.RESET_ALL) 
            print("************************************************************************\n") 
            
    #if user input is in lowercase SI Units
    elif metric.lower() == "si": 
        #user input starting point 
        orig = input(Fore.YELLOW+"Starting Location: "+Style.RESET_ALL)  
        if orig == "quit" or orig == "q": 
            clear() #call clear console terminal
            break #stop

        #user input end point
        dest = input(Fore.YELLOW+"Destination: "+Style.RESET_ALL) 
        #user input to stop the program
        if dest == "quit" or dest == "q":
            clear()  
            break

        url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})  

        print(Fore.LIGHTGREEN_EX+"\nURL: " + (url)) 
        print(Style.RESET_ALL)   
        json_data = requests.get(url).json()    
        json_status = json_data["info"]["statuscode"]    #check route is valid
        
        if json_status == 0:  #route exists
            SIUnit(json_data,orig,dest)   
        elif json_status == 402: #invalid route
            print("**********************************************")         
            print(Fore.RED+"Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations."+Style.RESET_ALL)         
            print("**********************************************\n")     
        elif json_status == 611: #missing input
            print("**********************************************")         
            print(Fore.RED+"Status Code: " + str(json_status) + "; Missing an entry for one or both locations."+Style.RESET_ALL)         
            print("**********************************************\n")     
        else: #uncited errors
            print("************************************************************************")         
            print(Fore.RED+"For Staus Code: " + str(json_status) + "; Refer to:")         
            print("https://developer.mapquest.com/documentation/directions-api/status-codes"+Style.RESET_ALL) 
            print("************************************************************************\n") 

    elif metric.lower()=="q" or metric.lower()=="quit": #if user input is lower q or quit for choosing ES or SI, stop
        clear() #call clear console terminal
        break #stop
    else: #not a valid input for type of metric system
        print(Fore.RED+"Invalid Metric System!"+Style.RESET_ALL)
        break



    
