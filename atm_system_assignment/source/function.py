
def authorize_card(card_df):
    print("\n")
    c_card = 0
    while (c_card < 3):
        card_num = int(input("Please enter your Card number :"))
        print("\n")
        c_card += 1
        card_num_list = card_df['card_number'].values
        if card_num in card_num_list:
            card_owner_name = card_df[card_df['card_number']==card_num]['card_owner'].iloc[0]
            print(f"Welcome to the AN Private Bank Ltd. ATM : {card_owner_name}")
            return card_num
        else:
            print("     You have entered incorrect card number, Please try again!")

    print("\n")
    exit_atm(exit_flag=True)


def authorize_pin(card_df,card_num):
    print("\n")
    c_pin = 0
    while (c_pin < 3):
        card_pin = int(input("Please enter your 3 digit pin :"))
        print("\n")
        c_pin += 1
        original_pin = card_df[card_df['card_number']==card_num]['card_pin'].iloc[0]
        if (card_pin == original_pin):
            return None
        else:
            print("     You have entered incorrect pin, Please try again!")

    print("\n")
    exit_atm(exit_flag=True,msg="   Your Card is blocked, Please visit Bank")


def select_service():
    c_service = 0
    while(c_service < 3):
        print("\n")
        print("Please find the menu list")
        print(" 1. Account Info")
        print(" 2. Balance Inquiry")
        print(" 3. Pin change")
        print(" 4. Cash Withdrawal")
        print(" 5. Cash Deposit")
        account_option = int(input("Enter the option from the menu :"))
        c_service += 1
        if account_option in (1,2,3,4,5):
            return account_option
        else:
            print("     Invalid Service requested, Please enter again from given options")
    
    print("\n")
    exit_atm(exit_flag=True)


def perform_service(account_option,card_num,card_df):
    if account_option == 1:
        account_info(card_num,card_df)
    elif account_option == 2:
        balance_inquiry(card_num,card_df)
    elif account_option == 3:
        pin_change(card_num,card_df)
        update_account(card_df)
    elif account_option == 4:
        cash_withdrawal(card_num,card_df)
        update_account(card_df)
    elif account_option == 5:
        cash_deposit(card_num,card_df)
        update_account(card_df)
    

def account_info(card_num,card_df):
    print("\n")
    print("------Account Information------:")
    print("Account Number   :",card_df[card_df['card_number']==card_num]['card_number'].iloc[0])
    print("Account Holder Name  :",card_df[card_df['card_number']==card_num]['card_owner'].iloc[0])
    print("Account Balance  :",card_df[card_df['card_number']==card_num]['card_balance'].iloc[0])
    print("-------------End---------------:")
    print("\n")

def balance_inquiry(card_num,card_df):
    print("\n")
    print("------Account Information------:")
    print("Account Number   :",card_df[card_df['card_number']==card_num]['card_number'].iloc[0])
    print("Account Balance  :",card_df[card_df['card_number']==card_num]['card_balance'].iloc[0])
    print("-------------End---------------:")
    print("\n")

def pin_change(card_num,card_df):
    print("\n")
    new_pin = int(input("Enter the 3 digit new pin :"))
    card_df.loc[card_df[card_df['card_number']==card_num].index,'card_pin'] = new_pin
    print("------Pin Change Request------:")
    print(f"Pin chnaged successfully for account number {card_num}")
    print("-------------End---------------:")
    print("\n")

def cash_withdrawal(card_num,card_df):
    print("\n")
    withdrawal_amt = int(input("Enter the amount for withdrawal :"))
    total_amount = card_df[card_df['card_number']==card_num]['card_balance'].iloc[0]
    if withdrawal_amt > total_amount:
        exit_atm(exit_flag=True,msg="Insufficient Balance in the account, Please visit Bank")
    print("Amount Withdrawn :",withdrawal_amt)
    print("Net Balance :",total_amount - withdrawal_amt)
    card_df.loc[card_df[card_df['card_number']==card_num].index,'card_balance'] = total_amount - withdrawal_amt
    print("\n")

def cash_deposit(card_num,card_df):
    print("\n")
    deposit_amt = int(input("Enter the amount for deposit :"))
    total_amount = card_df[card_df['card_number']==card_num]['card_balance'].iloc[0]
    print("Amount deposited :",deposit_amt)
    print("Net Balance :",total_amount + deposit_amt)
    card_df.loc[card_df[card_df['card_number']==card_num].index,'card_balance'] = total_amount + deposit_amt
    print("\n")

def update_account(card_df):
    card_df.to_csv("card_list.csv",index=False)
    #card_df = pd.read_csv('card_list.csv')
    #print(card_df.head())

def exit_atm(exit_flag,msg="    You have exhausted your ATM usage limit, Good bye!"):
    if exit_flag:
        print(msg)
        print("\n")
    else:
        print("     Thank you for using our services. Please visit us again!")
        print("\n")
    exit()
