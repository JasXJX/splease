# import numpy as np
# import pandas

# Method for calculating results (i.e. each person's subtotal, tips, etc.)
def calculator(items: dict[str: list],
               tip: float, tax: float) -> (list[str], list[list[float]]):

    # Calculates the subtotal of each person;
    # because this method returns data in lists,
    # an additional list of names is used to keep track of which person is
    # each index for
    subtotals = []
    names = []
    for person in items:
        if person != "Shared":
            names.append(person)
            subtotals.append(sum(items[person]))

    # Adding shared items to each person's subtotal
    shared_total = sum(items["Shared"])
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
