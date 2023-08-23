def tofareinheit(celcius):
    fareinheit = ((celcius * 9) / 5) + 32
    return fareinheit


celciustemp = 0
print(f"{celciustemp} celcius = {tofareinheit(0)} fareinheit")
