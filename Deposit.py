
Max_line = 3
Min_bet = 1
Max_bet = 500

def deposit():
    while True:     
         
        amount = input("Enter an amount to be deposited: $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                print("You are good to go with $", amount)
                break
            else:
                 print("Amount should be greater than 0. ")
        else:
            print("Please enter a valid number.")
    
    return amount


def get_number_lines():
    while True:
        lines = input("Enter the number of lines to bet on (1-" + str(Max_line) + ")? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= Max_line:
                break
            else:
                print("Enter the valid number of lines.")
        else:
            print("Enter a number.") 
            
    return lines


def get_bet():
    while True:
        amount = input("How much would you like to bet? $")
        if amount.isdigit():
            amount = int(amount)
            if Min_bet <= amount <= Max_bet:
                break
            else:
                print(f"Amount must be in between ${Min_bet} - ${Max_bet}.")
        else:
            print("Please enter a number.")
            
    return amount



def main():
    balance = deposit()
    line = get_number_lines()
    while True:
        bet = get_bet()
        total_bet = bet * line
        left_amount = balance - total_bet 
        remaining = total_bet - balance
        if total_bet > balance:
            print(f"You do not have enough amount to bet. Your balance is ${balance}, and the bet amount you chose is ${total_bet}. Please try again later.")
            print(f"You need ${remaining} more to bet at your price.")
        else:
            break
    
    print(f"You are betting ${bet} on {line} lines. Your total bet is: ${total_bet}.")
    print(f"If u bet ${total_bet}. You are left with ${left_amount}.")
    
    x = input("If u wish to continue Press 'Y' else if u wish to do it later press 'N': ")
    if x=='Y' and balance > total_bet:
        print("You are good to go.")
        print(f"Your bet is placed. \nYour total balance is now ${left_amount}.")
        
    elif x=='Y' and total_bet > balance:
        print("You cannot continue as u dont have sufficient amount to continue.")
        
    elif x=="N":
        print("Done.")
        
    print(balance, line)
 
    
main()