 # Take 2 inputs, Cost Price, Selling Price of a product from user and return following :
# * Profit from this sell.
# * What should be the selling price if we want to increase our current profit by 5%;
cp=int(input("enter cost price"))
sp=int(input("enter selling  price"))
profit=sp-cp
new_sp=cp+cp*0.05
print(f"your profit is {profit} \n profit increase by 5 percent if selling price is {new_sp}")
