#Python V. 2.7.9

cost = float(raw_input("Enter the total cost of the meal: "))
tip = raw_input("Enter the percent tip: ")
tip_as_decimal = float(tip) / 100

total = cost + (cost * tip_as_decimal)
tip_total = total - cost
       
print ("\nCost: %.2f" % cost)
print ("Tip: %.2f" % tip_total)
print ("Your total: %.2f" % total)