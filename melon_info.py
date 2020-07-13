"""Print out all the melons in our inventory."""


import melons


def print_melon(melons):
    """Print each melon with corresponding attribute information."""


    for melon, key in melons.items():
        print(melon).upper()
        for attribute, description in key.items():
            print(attribute, description)
        
print_melon(melons)