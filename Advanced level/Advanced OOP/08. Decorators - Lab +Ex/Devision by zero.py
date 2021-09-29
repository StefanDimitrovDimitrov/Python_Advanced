def Div_by_zero(func):
    def wrapper(x, y):
        if y == 0:
            return "Quantity is zero"
        return func(x, y)

    return wrapper


@Div_by_zero
def unit_price(Amount, Quantity):
    return Amount / Quantity


print(unit_price(500, 0))
