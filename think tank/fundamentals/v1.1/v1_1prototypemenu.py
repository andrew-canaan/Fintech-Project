import sys

menu_options = {
    1: 'Option 1: Current Price',
    2: 'Option 2: Market Cap',
    3: 'Option 3: Volume',
    4: 'Option 4: Has Dividends', 
    5: 'Option 5: Earnings Per Share:', 
    6: 'Option 6: Price to Earnings Ratio', 
    7: 'Option 7: Price to Earnings to Growth Ratio', 
    8: 'Option 8: Beta', 
    9: 'Exit Program',
}

# Displays menu options
def display_menu():
    for key in menu_options.keys():
        print(menu_options[key])

def process_options(option, screen_config):
    if option == 1:
        screen_config= option1(screen_config)
    elif option == 2:
        option2(screen_config)
    elif option == 3:
        option3(screen_config)  
    elif option == 4:
        option4(screen_config)
    elif option == 4:
        option4(screen_config)
    elif option == 5:
        option5(screen_config)
    elif option == 6:
        option6(screen_config)
    elif option == 7:
        option7(screen_config)
    elif option == 8:
        option8(screen_config)
    elif option == 9:
        exit_menu(screen_config) 

# Appends menu option selection to screens list
def option1(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Current Price? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            # set current price in screen config to true
            screen_config['Current Price']['active'] = True
            print("Successfully activated Current Price screen, standby...")
        else:
            print("Exiting option 1...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = int(input("Please enter a price with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, price value is a negative value...")
            screen_config['Current Price']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter price (1) greater than, (2) less than, (3) or equal to the target price (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['Current Price']['greater'] = True
                print(f"Successfully applied screen for assets greater than ${user_val}!")
                return screen_config
            elif option == 2:
                screen_config['Current Price']['less'] = True
                print(f"Successfully applied screen for assets less than ${user_val}!")
                return screen_config
            elif option == 3:
                screen_config['Current Price']['equalto'] = True
                print(f"Successfully applied screen for assets equal to ${user_val}!")
                return screen_config




def option2(screen_config):
    return 1
def option3(screen_config):
    return 1
def option4(screen_config):
    return 1
def option5(screen_config):
    return 1
def option6(screen_config):
    return 1
def option7(screen_config):
    return 1
def option8(screen_config):
    return 1
def exit_menu():
    sys.exit(0)