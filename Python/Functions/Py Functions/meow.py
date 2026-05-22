#PART 1
cat = 3
while cat > 0:
    cat -= 1
    print("meow")

while cat < 6:
    cat = cat + 1
    print("bark")

#PART 2
list = [0, 1, 2]
for i in list:
    print("list")

for _ in range(3):
    print("hi")

print(f"""meow
meow
meow""")

print("bark\n" * 3, end='')

#PART 3
while True:
    n = int(input("what's n? "))
    if n > 0:
         break

for _ in range(n):
    print("positive number! Yay!")

#PART 4
def main():
    n = get_num()
    meow(n)

def get_num():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n

def meow(n):
    for _ in range(n):
        print("meow")

main()