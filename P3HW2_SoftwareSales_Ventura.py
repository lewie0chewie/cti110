# CTI-110
# P3HW2 - Software Sales
# Luis Ventura
# 3/11/2018

def main():

    amountOfPackages = int (input ("Enter the amount of packages bought: "))

    packagePrice = 99

    if amountOfPackages < 10:
        discount = 0;
    elif amountOfPackages < 20:
        discount = 0.1;
    elif amountOfPackages < 50:
        discount = 0.2;
    elif amountOfPackages < 100:
        discount = 0.3;
    else:
        discount = 0.4;

    subTotal = amountOfPackages * packagePrice
    discountAmount = discount * subTotal
    total = subTotal - discountAmount

    print ("Amount of discount: $" + format (discountAmount, ",.2f") + "\n Total Amount: $" + format (total, ",.2f"))

main()
