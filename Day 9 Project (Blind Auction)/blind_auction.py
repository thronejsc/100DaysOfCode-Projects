# from replit import clear

from art import logo
print(logo)



bid_list = []

def add_new_bid():
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bid_dict = {}
    bid_dict["name"] = name
    bid_dict["bid"] = bid  
    bid_list.append(bid_dict)



def highest_bid():
  winner_name = " "
  winner_bid = 0
  if len(bid_list) < 1:
      winner = bid_list[0]
  else:
      for i in bid_list:
          if i["bid"] > winner_bid:
              winner_name = i['name']
              winner_bid = i['bid']
        
      print(f"Congratulations!\nThe winner is {winner_name}, with a bid of ${winner_bid}\n")

    
def ask_another_bid():
    a = input("Do you want a another bid? y/n ").lower()
    if a == 'y':
        print("\n"*100)        
        add_new_bid()
        ask_another_bid() 
    elif a == 'n':
        highest_bid()


def blind_auction():
    add_new_bid()
    ask_another_bid()
    

blind_auction()