import pandas as pd
import warnings
warnings.filterwarnings('ignore')
from function import *

def main():
    print("\n")
    print("\n")
    print("                ********Welcome to AN Private Bank Limited********")
    print("\n")
    card_df = pd.read_csv('card_list.csv')
    card_num = authorize_card(card_df)        
    authorize_pin(card_df,card_num)
    account_option = select_service()
    perform_service(account_option,card_num,card_df)          
    exit_atm(exit_flag=False)


if __name__ == "__main__":
    main()
else:
    print ("Please execute from main")