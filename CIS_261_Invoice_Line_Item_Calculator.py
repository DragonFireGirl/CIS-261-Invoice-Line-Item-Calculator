#Invoice Line Item Calculator

#!/usr/bin/env python3

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    print("The Invoice Line Item Calculator\n")

    answer = "y"
    while answer.lower() == "y":
        # get the price and quantity
        price = get_price()
        quantity = get_quantity()
    
        # calculate the total
        total = price * quantity

        # display the results
        print()
        print("PRICE:    ", f"{price: .2f}")
        print("QUANTITY: ", quantity)
        print("TOTAL:    ", f"{total: .2f}")
        answer = input("Enter another line item? (y/n): ")
        print()
        
    print("Bye!")


if __name__ == "__main__":
    main()
