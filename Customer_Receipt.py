Items = {
    "lovely_loveseat": [254.0, "\n Lovely Loveseat. Tufted polyester blend on wood. "
                               "32 inches high x 40 inches wide x 30 inches deep. Red or white."],
    "stylish_settee": [180.5, "\n Stylish Settee. Faux leather on birch. "
                              "29.50 inches high x 54.75 inches wide x 28 inches deep. Black."],
    "luxurious_lamp": [52.15, "\n Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."]
}

purchaselist: list = []  # List of purchases to be appended during program flow
total: int = 0  # Tallying up
desc: str = ""  # Tallying up


def purchase(plist, key):
    """

    :param plist: The current receipt (short for purchaselist, as defined above)
    :param key: The item to be added, to be searched in the dictionary
    """
    plist.append(Items[key])


def tax(currtot):
    """

    :currtot: Current total.
    :return: Returns the total including tax.
    """
    return currtot * 1.088


def inputanalysis(inp):
    """

    :param inp: The string the user input
    :return: Returns which item is meant accounting for capitalization
    """
    inp = inp[0:2]
    inp = inp.lower()
    if inp == "lo":
        return "lovely_loveseat"
    if inp == "lu":
        return "luxurious_lamp"
    if inp == "st":
        return "stylish_settee"
    return "unknown"

cont = True
# A sentinel boolean to control the following loop.
while cont:
    buy = input("Enter the item to be purchased. \n")
    buy = inputanalysis(buy)
    if buy == "unknown":
        print("Invalid item. Please try again.")
        continue
    purchase(purchaselist, buy)
    # Convert input to key accounting for capitalization of input and then add the purchase to the list

    more = input("Are there more items? Y/N \n")
    if more == "N":
        cont = False
    # Check if there are more items to be purchased.


for index, element in enumerate(purchaselist):
    total += element[0]
    desc += element[1] + " "

total = tax(total)
print("Items:", desc)
print("Total including tax:", total)
