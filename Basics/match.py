# pizza=input("toppings: ")
# base=100

# match pizza:
#     case "onion":
#         base+=100
#         print("You have choosen onion as toppings")
#         print(f"total price - {base}")
    
#     case "paneer":
#         base+=100
#         print("You have choosen paneer as toppings")
#         print(f"total price - {base}")
    
#     case "cheese":
#         base+=100
#         print("You have choosen cheese as toppings")
#         print(f"total price - {base}")


#     case _:
#         print("You haven't choosen any toppings")
#         print(f"total price - {base}")


pizza = input("Enter toppings: ")
top1 = "onion"
top2 = "paneer"
top3 = "cheese"
base = 100
total = 100

match pizza:
    case top1,top2,top3:
        base+=300
        print("You have choosen all three toppings [onion, paneer, cheese]")
        print(f"total price - {base}")
    
    case top1,top2:
        base+=200
        print("You have choosen two toppings [onion, paneer]")
        print(f"total price - {base}")

    case top1,top3:
        base+=200
        print("You have choosen two toppings [onion, cheese]")
        print(f"total price - {base}")
    
    case top2,top3:
        base+=200
        print("You have choosen two toppings [onion, cheese]")
        print(f"total price - {base}")

    case "onion":
        base+=100
        print("You have choosen onion as toppings")
        print(f"total price - {base}")
        
    case "paneer":
        base+=100
        print("You have choosen paneer as toppings")
        print(f"total price - {base}")

    case "cheese":
        base+=100
        print("You have choosen onion as toppings")
        print(f"total price - {base}")

    # case _:
    #     print("You haven't choosen any toppings")
    #     print(f"total price - {base}")

    
    