customer_info = {'name':'shaik ayoub','age':20,'purchase_history':['product A' , 'pruduct B']}

purchase_history = customer_info['purchase_history']
if (len(purchase_history) < 2):
    print("customer does not have a second purchase")
else:
    print(f"{purchase_history[1]} is his second purchase  ")