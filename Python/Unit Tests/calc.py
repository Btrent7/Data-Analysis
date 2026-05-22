#calc.py
def main():
    while True:
        try:
            n = int(input("Please choose a number: "))
            print(square(n))
        except ValueError:
            print("Not a number.")
        else: 
            break
    return n
    

def square(n):
    x = (n * n) # OR return n * n
    return x


if __name__ == "__main__":
    main()