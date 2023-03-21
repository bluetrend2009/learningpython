# Prompt user to input cost and selling price of an item
# Write prog to determine if user made profit or loss
# Determine how much profit or loss the user made

selling_price = input("What is the selling price? ")
cost_price = input("What is the cost price? ")

profit = int(selling_price) - int(cost_price)

#if selling_price > cost_price: selling_price - cost_price
#else cost_price - selling cost_price

print(f"Your profit is {profit}")

#another way, using if else

selling_price = input("What is the selling price? ")
cost_price = input("What is the cost price? ")

if selling_price > cost_price:
    profit = selling_price - cost_price
    print(f"You made a profit of {profit}")

elif selling_price < cost_price:
    loss = cost_price - selling_price
    print(f"You made of loss of {loss}")

else:
    print(f"You made no profit")

