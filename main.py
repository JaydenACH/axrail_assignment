'''
Task:
You are tasked to code the vending machine logic out using Python Programming Language. 
In your code, you can have a few drinks as your items with any price (no coin). 
The customer should be able to insert any notes to buy his preferred drinks. 
The outcome is to release the least amount of notes back to the customer. 
'''

# drink and price
selection = {
    'A': 6,
    'B': 3,
    'C': 2,
    'D': 11,
    'E': 7,
}

# existing type of notes
notes = [1, 5, 10, 20, 50, 100]

class VendingMachine():
    def __init__(self, selection, notes) -> None:
        self.selection = selection
        self.notes = notes
    
    def __str__(self) -> str:
        available_selection = "| "
        for drink, price in self.selection.items():
            available_selection += f"{drink} | "
        return available_selection
    
    def list_out_selection(self):
        available_selection = []
        for drink, price in self.selection.items():
            available_selection.append(drink)
        return available_selection

    def show_price(self, selected_drink):
        for drink, price in self.selection.items():
            if drink == selected_drink:
                return price

    def compute_balance_notes(self, balance_amount):
        balance_notes = {}
        for note in reversed(self.notes):
            while balance_amount >= note:
                if note in balance_notes:
                    balance_notes[note] += 1
                else:
                    balance_notes[note] = 1
                balance_amount -= note
        return balance_notes


def main(selection, notes):
    # initial a vending machine with starting selection
    vending_machine = VendingMachine(selection, notes)
    
    # ask customer which drink do you want to buy
    print("Here are the available drinks:")
    print(vending_machine)

    # get the customer's choice
    selected_drink = ""
    while selected_drink not in vending_machine.list_out_selection():
        selected_drink = input("Which one do you want?\n").capitalize()

    # get the customer's payment
    price = vending_machine.show_price(selected_drink)
    print(f"This drink costs ${price}")
    payment_note = 0
    while not payment_note or price > payment_note:
        try:
            customer_note = int(input("Please input your payment amount: \n$"))
            if customer_note not in notes:
                raise NameError()
            payment_note += customer_note
            print(f"You have paid ${payment_note}")
        except ValueError:
            print("Error: Try again with integer inputs")
        except NameError:
            print("Error: Provided notes are not allowable")

    # give the drink and compute balance notes to customer
    balance = payment_note - price
    if balance:
        print(f"Here is your balance: ${payment_note-price}")
        balance_notes = vending_machine.compute_balance_notes(balance)
        for note, qty in balance_notes.items():
            if qty == 1:
                print(f"{qty} piece of ${note}")
            else:
                print(f"{qty} pieces of ${note}")        
    print("Thank you. Here is your drink.")
    print("Press up key and enter, to buy another drink")


if __name__ == "__main__":
    main(selection, notes)
