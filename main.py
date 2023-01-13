def main():
    nombre = float(input("nombre "))
    devinne(nombre)
    # a = float(input("a"))
    # b = float(input("b"))
    # addition(a, b)
    # hi()


def devinne(nb):
    rdm = 55
    if nb < rdm :
        print("inférieur")
    elif nb > rdm :
        print("supérieur")
    else:
        print("win")


#
# def addition(a, b):
#     print(a + b)


# def hi():
#     name = input('nom : ')
#     print(f'salut, {name}')


main()
