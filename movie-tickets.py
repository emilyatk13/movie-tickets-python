print('Welcome to the movies!')

adult_tix_price = 11.50
kid_tix_price = 7.25
tax_rate = 0.075

choice = 'y'

#saying while the choice is equal to y, keep the loop going. everything needs to be tabbed in
while choice == 'y':
# while loop starts here
    print('Movie List:')
    print('1 - Nope')
    print('2 - Minions Movie')
    print('3 - Bodies Bodies Bodies')

    movie_choice = int(input('Which movie do you want to see? '))
    adult_tix = int(input('How many adult tickets do you want to purchase? '))
    kid_tix = int(input("How many children's tickets do you want to purchase? "))

    total_price = ((adult_tix * adult_tix_price) + (kid_tix * kid_tix_price)) * (1 + tax_rate)
    total_price_str = str(total_price)

    print('Thank you for your purchase! Your total is: $'+"{:.2f}".format(total_price))
    choice = input('Do you want to make another purchase? Enter y for yes and n for no. ')
# end of loop

print('Have a nice day!')