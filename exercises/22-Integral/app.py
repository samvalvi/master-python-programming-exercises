integral = {}


def integrales(x):
    for i in range(x):
        i=i+1
        integral[i]=i*i
    return integral


num = int(input("Value: ")) 
print(integrales(num))   