#CSCI 1133 Homework 3
#Peiqi Ji
#Problem B
def check(food):
    if food[len(food)-1] not in food[:len(food)-1]:
        return False
    else:
        return True
def end(food):
    if food[len(food)-1] == '':
        return False
    else:
        return True
def count(food):
    price = 0.00
    for x in food:
        if 'burger' in x:
            price += 3.00
        elif 'soda' in x:
            price += 2.00
        elif x != '':
            price += 5.00
    return price
def main():
    print('Welcome to the Python Buffet, the hippest restaurant in town!\n')
    food = []
    food.append(input('What would you like to order? ' ))
    while end(food):
        food.append(input('Would you like to order anything else? '))
        while check(food):
            print('Oops. You must have entered',food[len(food)-1],'again by accident.')
            food.remove(food[len(food)-1])
    print("You have ordered the following:")
    for x in food:
        print(x)
    price = count(food)
    print("This will cost you a total of $",format(price,'.2f'))
    print('Thank you for your patronage!')
if __name__ == '__main__':
    main()
