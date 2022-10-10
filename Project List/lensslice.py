# Your code below:

toppings = ["pepperoni","pineapple","cheese","sausage","olives","anchovies","mushrooms"]
prices = [2,6,1,3,2,7,2]
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)

num_pizzas = len(toppings)
#print(num_pizzas)

print("We sell", num_pizzas, "different kinds of pizza!")

## print(list(zip(a,b))
pizza_and_prices = list(zip(prices,toppings))
#print(pizza_and_prices)

pizza_and_prices.sort()
#print(pizza_and_prices)

cheapest_pizza = pizza_and_prices[0]
#print(cheapest_pizza)

pizza_and_prices.pop()
#print(pizza_and_prices)

pizza_and_prices.insert(-2,[2.5, "peppers"])
#print(pizza_and_prices)

three_cheapest = pizza_and_prices[0:3]
print(three_cheapest)
