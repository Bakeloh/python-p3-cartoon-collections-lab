def roll_call_dwarves(dwarves):
    for i, dwarf in enumerate(dwarves, 1):
        print(f"{i}. {dwarf}")

def summon_captain_planet(elements):
    return [element.capitalize() + '!' for element in elements]

def long_planeteer_calls(calls):
    return any(len(call) > 4 for call in calls)

def find_the_cheese(items):
    cheeses = ["cheddar", "gouda", "camembert"]
    for item in items:
        if item in cheeses:
            return item
    return None
