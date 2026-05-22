def main():
    x = get_markup("Please provide the Cost (TPP): ")
    print("Markup (List) Price:", x)

def get_markup(prompt):
    while True:
        try:
            x = float(input(prompt)) # OR return int(input("Please provide a number: "))
            total = float(x * 2)
        except ValueError:
            print("Value provided is not a number.") # OR pass (no message)
        else:
            break
    return total

main()