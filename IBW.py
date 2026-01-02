###College exercise - Class 3 part 2###
###Write a program that shows the ideal body weight based on height and gender###

def ibw_calculator():
    print("Please enter your gender (M/F) and height in meters:")
    
    while True:
        gender = input("Gender: ").upper().strip()                      ###Convert to uppercase and remove spaces
        if gender in ['M', 'F']:
            break                                                       ###If the input is valid, exit loop, if not, calls back to input
        print("Please enter 'M' and 'F' only.")       
        
    while True:
        try:
            height = float(input("Height (from 0.5 to 2.5): "))         ###Check if height is within valid range
            if 0.5 <= height <= 2.5:                                    ###If the input is valid, exit loop, if not, calls back to input
                break
            else:
                print("Please enter a height between 0.5 and 2.5 meters.")
        except ValueError:
            print("Error: Please enter a valid number for height using dot(.) separation.")
         
    if gender == 'M':         
            ibw = 72.7 * height - 58
    else:
            ibw = 62.1 * height - 44.7
    
    print(f"\nThe Ideal Body Weight (IBW) for you is {ibw:.2f} kg.")      ###Print result with 2 decimal places


ibw_calculator()