# Week 8 homework assignment
# Create a function that accepts a list of sandwich ingredients
# Function has 1 parameter that collects as many arguments as provided
# print a summary of the sandwich order
def build_sandwich(bread_type, size, *toppings):
    """Collect bread type, size, and all ingredients for a sandwich"""
    print(f"Now building a {size}-inch sandwich on {bread_type} ")
    for topping in toppings:
        print(f" - {topping}")
    print("Your sandwich is completed.")

build_sandwich('white', 12, 'ham', 'lettuce', 'tomato')
build_sandwich('rye', 6, 'turkey')