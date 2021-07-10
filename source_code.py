#Created by Jesus Vasquez-Cipriano
#Last Edit on: January 17, 2020
#Copyright © 2020 Jesus Vasquez-Cipriano. All rights reserved.

#This program can convert temperature in Fahrenheit to Celsius
#and Miles/Hour to Meters/Second. A main function is defined, which calls
#one of two possible functions, based on user input.

#Part 1 - Defining a function that converts temperature in Fahrenheit to Celsius.

def convert_to_celcius(fahrenheight):
    #Convert temperature in Fahrenheit to Celsius.
    celcius = (fahrenheight-32)*(5/9)
    print("Your temperature is", celcius, "in Celcius.")

#Part 2 - Defining a function that converts miles per hour to meters per second.
    
def convert_to_meters_second(miles_hour):
    #Convert miles to meters and hours to seconds.
    meters_second = miles_hour*1609/3600
    print("You currently run", meters_second, "meters per second.")

# Part 3 - Main function that calls two functions based on user input.

def main():
    #User decides what conversion to execute.
    main_input = input("Enter 1 to convert Fahrenheit temperature to Celsius.\
\nEnter 2 to convert speed from miles per hour to meters per second.\
\nEnter 1 or 2: ")
    if main_input == '1':
        #Choosing '1' has user input a temperature integer, which is assigned
        #to the variable fahrenheight and passed to the convert_to_celcius function.
        fahrenheight = int(input("Give me a temperature in Fahrenheit to convert to degrees in Celcius: "))
        convert_to_celcius(fahrenheight) #call convert_to_celcius function.
    elif main_input == '2':
        #Choosing '2' has user input a meter per hour integer, which is assigned
        #to the variable miles_hour and passed to the convert_to_meters_second function.
        miles_hour = int(input("Tell me how many miles per hour you currently run to conver to meters per second: "))
        convert_to_meters_second(miles_hour) #call convert_to_meters_second function.
    else:
        #Prints error message if necessary input isn't provided.
        print("Error. You can only input the digit '1' or '2'") 

#Call main function.
main()
