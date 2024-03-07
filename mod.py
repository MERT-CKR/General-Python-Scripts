def mod(x,y):
    if type(x)!=int and type(x)!=float:
        raise TypeError("Function received wrong type")
    x=abs(x)
    while x>1:
        x-=y
    if x<0:
        x=x+y
    print(x)


mod(5, 2)
mod(-4, 2)
mod(8.5, 3)