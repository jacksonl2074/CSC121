# -*- coding: utf-8 -*-
# Description: Calculates hotel charges for customers
# 9/7/23
# CSC 121 M1Lab1 - Review
# Laura K. Jackson



# ask user for number of nights they're staying in hotel
num_nights = int(input("# of nights: "))

# ask user if they are a platinum member
platinum_member = input("Platinum member (y/n)? ")

if platinum_member == 'y':
    plat_hotel_charges = 90
    if num_nights >= 5:
        plat_disc_price = (plat_hotel_charges * num_nights) - 90
        print("Charge = $", plat_disc_price)
        print("Note: charges discounted for one free night")
    else:
        plat_price = plat_hotel_charges * num_nights
        print("Charges = $ ", plat_price)
else:
    hotel_charges = 100
    if num_nights >= 3:
        reg_hotel_charge = num_nights * hotel_charges
        print("Charge = $", reg_hotel_charge)
        print("Note: Please consider becoming a platinum member.")
    else:
        reg_hotel_price = hotel_charges * num_nights
        print("Charge = $", reg_hotel_price)
