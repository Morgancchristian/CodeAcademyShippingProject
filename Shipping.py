# This program will take the weight of a package and determine the cheapest way to ship that package using Sals Shippers
print("This program will take the weight of a package and determine the cheapest way to ship that package using Sals Shippers")
# Declaration of Variables 
weight = float(input("Please enter the wieght of the item: "))

# Ground Shipping 
if weight < 2:
  y = 1.50 
elif weight > 2 and weight <= 6:
  y = 3.00
elif weight > 6 and weight <= 10:
  y = 4.00 
elif weight > 10:
  y = 4.75
  

ground_shipping = (y * weight + 20.0)

ground_shipping_premium = 125 

drone_shipping = (y * weight + 20.0) * 3
  
  
print("Ground Shipping Cost: $" + str(ground_shipping))


# Ground Shipping Premium 
print("Gorund Shipping Premium Cost: $" + str(ground_shipping_premium))

# Drone Shipping
if weight < 2:
  y = 4.50 
elif weight > 2 and weight <= 6:
  y = 9.00 
elif weight > 6 and weight <= 10:
  y = 12.00 
elif weight > 10:
  y = 14.25 

print ("Drone Shipping Price: $" + str(drone_shipping))