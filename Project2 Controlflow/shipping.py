weight = 25

# Ground shipping
if weight >= 10:
  ground_cost = weight*4.75+20
elif weight >= 6 and weight <= 10:
  ground_cost = weight*4+20
elif weight >= 2 and weight <=6:
  ground_cost = weight*3+20
else :
  ground_cost = weight*1.5+20
print("Ground shipping cost is", ground_cost)

premium_cost = 125
print("Ground shipping Premium cost is", premium_cost)

# Drone shipping
if weight >= 10:
  drone_cost = weight*14.25
elif weight >= 6 and weight <= 10:
  drone_cost = weight*12
elif weight >= 2 and weight <=6:
  drone_cost = weight*9
else :
  drone_cost = weight*4.5
print("Drone Shipping cost is", drone_cost)

