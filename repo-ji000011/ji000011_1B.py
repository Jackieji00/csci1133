# CSCI1133 Homework1
# Peiqi Ji
# Problem 1B
def CurrencyConverter(value):
    euro = 0.83 * value
    euro = format(euro,".2f")
    print("$ " + str(value) + " = " + str(euro) + " Euro")
    yen = 111.14 * value
    yen = format(yen,".2f")
    print("$ " + str(value) + " = " + str(yen) + " Yen")
    bitcoin = 0.000076 * value
    bitcoin = format(bitcoin,".2f")
    print("$ " + str(value) + " = " + str(bitcoin) + " Bitcoin")
def main():
    print("Welcome to the Currency Converter!")
    value = float(input("Enter an amount in US Dollars: $ "))
    CurrencyConverter(value)
if __name__ == "__main__":
    main()
