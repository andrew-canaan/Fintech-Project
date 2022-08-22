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

def process_options(option, screen_config, config_list):
    if option == 1:
        screen_config, config_list = option1(screen_config, config_list)
    elif option == 2:
        option2(screen_config, config_list)
    elif option == 3:
        option3(screen_config, config_list)  
    elif option == 4:
        option4(screen_config, config_list)
    elif option == 4:
        option4(screen_config, config_list)
    elif option == 5:
        option5(screen_config, config_list)
    elif option == 6:
        option6(screen_config, config_list)
    elif option == 7:
        option7(screen_config, config_list)
    elif option == 8:
        option8(screen_config, config_list)
    elif option == 9:
        exit_menu(screen_config, config_list) 

# Appends menu option selection to screens list
def option1(screen_config, config_list):
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Current Price? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            # set current price in screen config to true
            screen_config['Current Price']['active'] = True
        else
            print("Exiting option 1...")
            return

        while(True)
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = int(input("Please enter a price with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, price value is a negative value...")
            screen_config['Current Price']['value'] = option

            try: 
                option = int(input("Please enter whether you would like to filter price (1) greater than, (2) less than, (3) or equal to the target price (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 or option != 2 or option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['Current Price']['greater'] = True
                config_list.append(screen_config['Current Price'])
                return screen_config, config_list
            elif option == 2:
                screen_config['Current Price']['less'] = True
                config_list.append(screen_config['Current Price'])
                return screen_config, config_list
            elif option == 3:
                screen_config['Current Price']['equalto'] = True
                config_list.append(screen_config['Current Price'])
                return screen_config, config_list




def option2(screen_config, config_list):
    return 1
def option3(screen_config, config_list):
    return 1
def option4(screen_config, config_list):
    return 1
def option5(screen_config, config_list):
    return 1
def option6(screen_config, config_list):
    return 1
def option7(screen_config, config_list):
    return 1
def option8(screen_config, config_list):
    return 1
def exit_menu():
    sys.exit(0)