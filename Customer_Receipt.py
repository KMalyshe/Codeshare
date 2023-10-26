
Pricedict = {"lovely_loveseat": 254.0, "stylish_settee": 180.5, "luxurious_lamp": 52.15}
Descdict = {
    "lovely_loveseat": "Lovely Loveseat. Tufted polyester blend on wood. "
                       "32 inches high x 40 inches wide x 30 inches deep. Red or white.",
    "stylish_settee": "Stylish Settee. Faux leather on birch. "
                      "29.50 inches high x 54.75 inches wide x 28 inches deep. Black.",
    "luxurious_lamp": "Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."
}

c1total: int = 0
c1items: str = ""

def c1purchase(currtot, curritem, key):
    """

    :param currtot: The current monetary total
    :param curritem: The current itemized total
    :param key: The item to be added, to be searched in the dictionary
    :return: Returns the current monetary total and itemized total as a float and a string.
    """
    currtot += Pricedict[key]
    curritem += Descdict[key] + " \n"
    return currtot, curritem


def c1tax(currtot):
    """

    :param currtot:  Multiplies the current total by sales tax, used at the end.
    :return: Returns the total including tax.
    """
    currtot *= 1.088
    return currtot


c1total, c1items = c1purchase(c1total, c1items, "lovely_loveseat")
c1total, c1items = c1purchase(c1total, c1items, "luxurious_lamp")
c1total = c1tax(c1total)
print("Customer One Items: \n", c1items)
print("Customer One Total:", c1total)
