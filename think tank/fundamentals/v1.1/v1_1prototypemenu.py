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
    9: 'Option 9: Exit Program',
}

# Displays menu options
def display_menu():
    for key in menu_options.keys():
        print(menu_options[key])

def process_options(option, screen_config):
    if option == 1:
        screen_config = option1(screen_config)
        return screen_config
    elif option == 2:
        screen_config = option2(screen_config)
        return screen_config
    elif option == 3:
        screen_config = option3(screen_config)  
        return screen_config
    elif option == 4:
        screen_config = option4(screen_config)
        return screen_config
    elif option == 4:
        screen_config = option4(screen_config)
        return screen_config
    elif option == 5:
        screen_config = option5(screen_config)
        return screen_config
    elif option == 6:
        screen_config = option6(screen_config)
        return screen_config
    elif option == 7:
        screen_config = option7(screen_config)
        return screen_config
    elif option == 8:
        screen_config = option8(screen_config)
        return screen_config
    elif option == 9:
        print("Program terminated. Happy trading")
        sys.exit(0)

# Appends menu option selection to screens list
def option1(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Current Price (only one may be active)? Y/N: '))
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
                option = float(input("Please enter a price with which you would like to filter: "))
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
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Market Cap (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['Market Cap']['active'] = True
            print("Successfully activated Market Cap screen, standby...")
        else:
            print("Exiting option 2...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter a market cap value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, market cap value is a negative value...")
            screen_config['Market Cap']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter market caps (1) greater than, (2) less than, (3) or equal to the target market cap (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['Market Cap']['greater'] = True
                print(f"Successfully applied screen for market caps greater than ${user_val}!")
                return screen_config
            elif option == 2:
                screen_config['Market Cap']['less'] = True
                print(f"Successfully applied screen for market caps less than ${user_val}!")
                return screen_config
            elif option == 3:
                screen_config['Market Cap']['equalto'] = True
                print(f"Successfully applied screen for market caps equal to ${user_val}!")
                return screen_config

def option3(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Volume (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['Volume']['active'] = True
            print("Successfully activated Volume screen, standby...")
        else:
            print("Exiting option 3...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter a volume value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, volume value is a negative value...")
            screen_config['Volume']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter volumes (1) greater than, (2) less than, (3) or equal to the target volume (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['Volume']['greater'] = True
                print(f"Successfully applied screen for volumes greater than {user_val}!")
                return screen_config
            elif option == 2:
                screen_config['Volume']['less'] = True
                print(f"Successfully applied screen for volumes less than {user_val}!")
                return screen_config
            elif option == 3:
                screen_config['Volume']['equalto'] = True
                print(f"Successfully applied screen for volumes equal to {user_val}!")
                return screen_config

def option4(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for dividen-sharing companies (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            # set current price in screen config to true
            screen_config['Dividends Y/N']['active'] = True
            print("Successfully activated Dividends screen, standby...")
        else:
            print("Exiting option 4...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = str(input("Please enter whether you would like to view companies that share dividends (Y/N): "))
            except:
                print("Invalid value, please try again.")

            if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
                screen_config['Dividends Y/N']['value'] = True
                print("Successfully activated screen for dividend sharing companies!")
            else:
                print("Successfuly activated screen for non-dividend sharing companies!")
            
            return screen_config    

def option5(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for EPS (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['EPS']['active'] = True
            print("Successfully activated EPS screen, standby...")
        else:
            print("Exiting option 5...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter an EPS value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, EPS value is a negative value...")
            screen_config['EPS']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter EPS values (1) greater than, (2) less than, (3) or equal to the target EPS (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['EPS']['greater'] = True
                print(f"Successfully applied screen for EPS values greater than {user_val}!")
                return screen_config
            elif option == 2:
                screen_config['EPS']['less'] = True
                print(f"Successfully applied screen for EPS values less than {user_val}!")
                return screen_config
            elif option == 3:
                screen_config['EPS']['equalto'] = True
                print(f"Successfully applied screen for EPS values equal to {user_val}!")
                return screen_config

def option6(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for P/E (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['P/E']['active'] = True
            print("Successfully activated P/E screen, standby...")
        else:
            print("Exiting option 6...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter a P/E value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, P/E value is a negative value...")
            screen_config['P/E']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter P/E values (1) greater than, (2) less than, (3) or equal to the target P/E (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['P/E']['greater'] = True
                print(f"Successfully applied screen for P/E values greater than {user_val}!")
                return screen_config
            elif option == 2:
                screen_config['P/E']['less'] = True
                print(f"Successfully applied screen for P/E values less than {user_val}!")
                return screen_config
            elif option == 3:
                screen_config['P/E']['equalto'] = True
                print(f"Successfully applied screen for P/E values equal to {user_val}!")
                return screen_config

def option7(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for P/E/G (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['P/E/G']['active'] = True
            print("Successfully activated P/E/G screen, standby...")
        else:
            print("Exiting option 7...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter a P/E/G value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, P/E/G value is a negative value...")
            screen_config['P/E/G']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter P/E/G values (1) greater than, (2) less than, (3) or equal to the target P/E/G (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['P/E/G']['greater'] = True
                print(f"Successfully applied screen for P/E/G values greater than {user_val}!")
                return screen_config
            elif option == 2:
                screen_config['P/E/G']['less'] = True
                print(f"Successfully applied screen for P/E/G values less than {user_val}!")
                return screen_config
            elif option == 3:
                screen_config['P/E/G']['equalto'] = True
                print(f"Successfully applied screen for P/E/G values equal to {user_val}!")
                return screen_config

def option8(screen_config):
    user_val = 0
    while (True):
        option = ''
        try:
            option = str(input('Are you sure you would like to apply a screen for Beta (only one may be active)? Y/N: '))
        except:
            print("Invalid input, please try again.")
    
        if option == 'y' or option == 'Y' or option == 'yes' or option == 'Yes':
            screen_config['Beta']['active'] = True
            print("Successfully activated Beta screen, standby...")
        else:
            print("Exiting option 8...")
            return screen_config

        while(True):
            # Grab user input for price and whether the filter should be for greater, less, or equal to that value
            try:
                option = float(input("Please enter a Beta value with which you would like to filter: "))
            except:
                print("Invalid value, please try again.")

            if option < 0:
                print("Warning, Beta value is a negative value...")
            screen_config['Beta']['value'] = option
            user_val = option

            try: 
                option = int(input("Please enter whether you would like to filter Beta values (1) greater than, (2) less than, (3) or equal to the target Beta (enter 1-3): "))
            except:
                print("Invalid selection. Please try again.")

            if option != 1 and option != 2 and option != 3:
                print("Please select an option 1, 2, or 3... Retrying.")
            elif option == 1:
                screen_config['Beta']['greater'] = True
                print(f"Successfully applied screen for Beta values greater than {user_val}!")
                return screen_config
            elif option == 2:
                screen_config['Beta']['less'] = True
                print(f"Successfully applied screen for Beta values less than {user_val}!")
                return screen_config
            elif option == 3:
                screen_config['Beta']['equalto'] = True
                print(f"Successfully applied screen for Beta values equal to {user_val}!")
                return screen_config