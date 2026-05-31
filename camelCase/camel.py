def main():

    # user's input : assuming it's in camelcase
    camelcase = snake_conversion(input("camelCase: "))



    # convert camel case to snake case

def snake_conversion(name):
    print("snake_case: ", sep=" ", end="")
    for char in name:
       if char == char.lower():
           print(char, sep=" ", end="")

       elif char == char.upper():
           char = "_" + char.lower()
           print(char, sep=" ", end="")






main()
