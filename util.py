from decimal import Decimal


# Method for calculating results (i.e. each person's subtotal, tips, etc.)
def calculator(items: dict[str, dict[str, list]],
               tip: Decimal, tax: Decimal) -> (list[str], list[list[float]]):

    # Calculates the subtotal of each person;
    # because this method returns data in lists,
    # an additional list of names is used to keep track of which person each
    # index is for
    subtotals = []
    names = []
    for person in items:
        if person != "everyone":
            names.append(person)
            subtotals.append(sum(items[person]["price"]))

    # Adding shared items to each person's subtotal
    shared_total = sum(items["everyone"]["price"])
    shared_per_person = shared_total/len(subtotals)
    subtotals = [i + shared_per_person for i in subtotals]
    total = sum(subtotals)
    ratio_to_total = [i/total for i in subtotals]

    # Calculating the each person's share of tips and taxes
    tips = []
    taxes = []
    for person in ratio_to_total:
        tips.append(person*tip)
        taxes.append(person*tax)

    # Combining all the results together into a list;
    # first dim is index for person, second dim is for subtotal, tips, taxes,
    # in that order
    results = []
    for i in range(len(subtotals)):
        results.append([subtotals[i], tips[i], taxes[i]])
    return names, results

# Next steps: store data in sql / make frontend display
# Decided: use MySQL for DB.
# Need to figure out how to implement: use SQLAlchemy/direct connect/Docker
# If use SQLAlchemy/direct connect: install MySQL and go ahead
# If use Docker just build as normal and do Docker Compose later
# MySQL is still good as it can show multi-container builds


# An object to keep track of the receipt and for printing receipts
class Receipt():
    def __init__(self, subreceipt: bool = False):
        if subreceipt:
            self.data = {"item": [], "price": []}
        else:
            self.data = {"item": [], "price": [], "for": []}
            tb = self.Textbox(left_align=True)
            self.printer = ["".join((tb.print("Item"), "|",
                                     tb.print("Price"), "|",
                                     tb.print("For"))),
                            "".join("-"*(tb.size*3 + 2))]

    def add_item(self, item: str, price: Decimal, person: str):
        self.data["item"].append(item)
        self.data["price"].append(price)
        self.data["for"].append(person)
        tb = self.Textbox()
        output = "".join((tb.print(item), "|",
                          tb.print(str(price)), "|",
                          tb.print(person)))
        self.printer.append(output)

    def pop_item(self):
        self.data["item"].pop()
        self.data["price"].pop()
        self.data["for"].pop()
        self.printer.pop()

    def calc_total(self):
        pass

    def print(self) -> str:
        return "\n".join(self.printer)

    def output_data(self) -> dict:
        output: dict[str, dict[str, list]] = {}
        for item, price, person in zip(self.data["item"],
                                       self.data["price"],
                                       self.data["for"]):
            if person in output:
                output[person]["item"].append(item)
                output[person]["price"].append(price)
            else:
                output[person]["item"] = [item]
                output[person]["price"] = [price]
        return output

    class Textbox():

        def __init__(self,
                     size: int = 12,
                     left_align: bool = False):
            self.size = size
            self.left_align = left_align

        def print(self, text: str) -> str:
            if len(text) <= self.size:
                if self.left_align:
                    return text.ljust(self.size)
                else:
                    return text.rjust(self.size)
            else:
                return text[0:self.size-3] + "..."


def make_table(names: list[str], results: list[list[float]]):
    pass
