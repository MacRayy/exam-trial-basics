pirates = [
    {'Name': 'Olaf', 'has_wooden_leg': False, 'gold': 12},
    {'Name': 'Uwe', 'has_wooden_leg': True, 'gold': 9},
    {'Name': 'Jack', 'has_wooden_leg': True, 'gold': 16},
    {'Name': 'Morgan', 'has_wooden_leg': False, 'gold': 17},
    {'Name': 'Hook', 'has_wooden_leg': True, 'gold': 20},
]

# Write a function that takes any list that contains pirates as in the example,
# And returns a list of names containing the pirates that
# - have wooden leg and
# - have more than 15 gold

def list_o_pirates(any_pirate_list):
    pirate_names = []
    for pirate in any_pirate_list:
        if pirate['has_wooden_leg'] is True and pirate['gold'] > 15:
            pirate_names.append(pirate['Name'])
    return pirate_names

print(list_o_pirates(pirates))
