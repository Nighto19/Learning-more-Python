price = 0
discount = 0

def apply_discount(price, discount):
    if isinstance(price, int) == False and isinstance(price, float) == False:
        return("The price should be a number")
    elif isinstance(discount, int) == False and isinstance(discount, float) == False:
        return("The discount should be a number")
    elif discount < 0 or discount > 100:
        return("The discount should be between 0 and 100")
    elif price < 0:
        return("The price should be greater than 0")
    else:
        fprice = price - ((price*discount)/100)
        print fprice
        return fprice

apply_discount(100, 20)
apply_discount(200, 50)
apply_discount(50, 0)
apply_discount(74.5, 20.0)
