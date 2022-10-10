hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Basic cal price
total_price = 0
for t in prices:
  #print(i)
  total_price += t
print("Total Hair price :",total_price)
print("Average Hair Price :", total_price/len(prices))

new_prices = [new - 5 for new in prices]
print("new_prices :", new_prices)

# Revenue of the shop
total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]
print("Total Revenue:", total_revenue)
print("Average Daily Revenue:", total_revenue/len(last_week))

# Advertising all of the haircuts that under 30
cut_under_30 = []
u = 0
for cut in prices:
  if cut <= 30:
    print(hairstyles[u], prices[u])
    u += 1
