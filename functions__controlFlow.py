def calculate_discount(orginal_price, discount_percentage = 10):
    discount_price = orginal_price - (orginal_price*discount_percentage/100)
    return discount_price

orginal_price = int(input("input original amount"))
discount_price = calculate_discount(orginal_price)
if (discount_price<500):
    print(f"{discount_price} Low Cost Item")
elif(discount_price >500 and discount_price<1000):
    print(f"{discount_price}Moderate-cost item")
else:
    print(f"{discount_price} High Cost Item")