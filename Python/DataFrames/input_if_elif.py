#Enter Category Code and TPP Value
cat_code = input("Category: " )
tpp = float(input("TPP Value: " ))


#List Price Categories
markup = 0
if cat_code in ["501A", "501B", "501C"]:
    markup = ((1.9 * tpp) / 0.999)
elif cat_code in ["501D", "503G", "503H", "503I"]:
    markup = ((1.9 * tpp) / 0.999)
elif cat_code in ["501F", "501G", "501H", "501I"]:
    markup = ((1.9 * tpp) / 0.999)
elif cat_code == "F":
    markup = ((1 * tpp) / 1.999)
else:
    print(f"Undefined Item Category: '{cat_code}'")

print("List Price: $", round(markup, 4))
