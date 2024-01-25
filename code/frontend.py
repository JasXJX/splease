from util import Receipt


class Prompter(object):
    def __init__(self):
        # self.receipt = Receipt()
        self.welcome = "Welcome to Splease, a bill splitting app!"

    # method that greets the user and asks what they wanna do next
    def begin(self):
        print(self.welcome)

    def build_receipt(self):
        receipt = Receipt()
        response = "Enter \"Done!\" when you\'re finished entering items " + \
            "or \"del\" to delete the last entry."
        print(response)
        while response.casefold() != "done!":
            print(receipt.print())
            item = input("Please enter item name:")
            if item.casefold() != "done!":
                price = input("Please enter item price:")
                person = input("Please enter who this item is for:")
                receipt.add_item(item, price, person)
        response = "no"
        while response == "no":
            tips = input("How much was the tips?")
            taxes = input("And the taxes?")
            response = input("Does this look good?\n" +
                             "Tips: {tips}\nTaxes: {taxes}")
        receipt.add_tip_n_tax(tips, taxes)
