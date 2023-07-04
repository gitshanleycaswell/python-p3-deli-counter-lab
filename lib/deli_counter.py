katz_deli = []

def line(katz_deli):
    if len(katz_deli) == 0:
        print("The line is currently empty.")
    else:
        positions = [f"{index +1}. {customer}" for index, customer in enumerate(katz_deli)]
        print("The line is currently: " + " ".join(positions))

def take_a_number(katz_deli, new_name):
    katz_deli.append(new_name)
    position = len(katz_deli)
    print(f"Welcome, {new_name}. You are number {position} in line.")

def now_serving(katz_deli):
    if len(katz_deli) > 0: 
        print(f"Currently serving {katz_deli[0]}.")
        katz_deli.pop(0)
    else:
        print("There is nobody waiting to be served!")