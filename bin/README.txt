Andrew Canaan
29 July 2022

    - This program is the second iteration of Andrew Canaan and Alex Brennan's stock screening prototype. 
    - It will prompt the user for which criteria it would like to screen with, as well as whether the user
    wants to generate excel sheets.
    - The following are loose requirements for a V1 prototype:
            1. Market Cap CHECK - Company Overview.xlsx

            2. Current Price CHECK - Daily Price xlsx

            3. Volume CHECK - Daily Price xlsx

            4. Dividends Y/N CHECK (DIVIDEND DATE AND EX DIVIDEND DATE) - Company Overview xlsx

            5. Earnings Per Share CHECK (CURRENT AND PER FISCAL YEAR) - quarterly/annual earnings xlsx 
            
            6. Price to Earnings Ratio CHECK - Company Overview xlsx (PERatio)

            7. Price to Earnings to Growth Ratio CHECK - Company Overview xlsx (PERatio)

            8. Beta CHECK - Company Overview xlsx (PERatio)


            Recommend against these for now.
            
            9. Sector CHECK

            10. Industry CHECK

Andrew Canaan
27 September 2022

    - Demo works for Agilent Technologies, and serves as a proof of concept.
    - Screens the user can apply inclue:
        - Market Cap
        - Most recent closing price 
        - Volume
        - Dividends Y/N 
        - EPS (quarterly, annual is very easy to add back in)
        - P/E
        - P/E/G 
        - Beta
    - The UI is very brittle, but hey it works on my machine >:-)
    - Next hurdle is how to deal with the API limit... Would take 2h+ to process all 10k listings... Yikes.
