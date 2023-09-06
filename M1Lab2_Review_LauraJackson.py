# -*- coding: utf-8 -*-
# Description: 
# 9/7/23
# CSC 121 M1Lab2 - Review
# Laura K. Jackson

# initialize variables
item_count = 0
unit_cost = 0
more_items = "y"
pre_tax_cost = 0        # subtotal of 
# sales_tax = 0         # in dollars, not percent
total_cost_tax = 0      # total cost of all items that are taxable
non_tax_item_tot = 0    # total for all non-taxable items
tot_cost_per_item = 0   # total cost for one item
tax = 0              # keep initializing to 0 when asking user input
tot_amt_tax_and_nontax_items = 0   # total amt for all items, taxable + non-taxable

count = 1

# while loop
while more_items == 'y': # changed from true to 'y'
    print("Item", count)
    item_count = int(input("Enter count of item " + str(count) + ": "))  
    unit_cost = float(input("Enter unit cost for item " + str(count) + ": "))  
    
    tot_cost_per_item = unit_cost * item_count      #calculation for each item total
    
    
    item_taxable = input("Is this item taxable (y/n)? ")
    
    if item_taxable == 'y':
        
        total_cost_tax += tot_cost_per_item     # accumulator var
    else:
        
        non_tax_item_tot += tot_cost_per_item   # accumulator var
    
    more_items = input("More items (y/n)? ") # ask user for more items, to avoid infinite loop
    print()             # blank line
    count += 1          # need count to show each item number
    
    
# ask user for tax percent

tax = float(input("Enter sales tax rate (%): "))    # need to convert to decimal number
tax_in_decimal = tax / 100          # user input tax converted to decimal form, now can use in calculation

tax_on_taxable_items = total_cost_tax * tax_in_decimal   # tax amt in dollars



print("Total cost (pre_tax): ", non_tax_item_tot)      # display subtotal (pre-tax) for all items that are non-taxable

print("Sales tax: ", )



# add all non-tax items + all taxable items


tot_amt_tax_and_nontax_items = tax_on_taxable_items + non_tax_item_tot
print("Total cost (with tax): ", tot_amt_tax_and_nontax_items)




