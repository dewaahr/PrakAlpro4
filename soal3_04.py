celcius_fahrenheit=lambda celci: (9/5)*celci+32
celcius_reamur=lambda celci: 0.8 * celci
print(f'{celcius_fahrenheit(100):.0f}')
print(f'{celcius_reamur(80):.0f}')
print(f'{celcius_fahrenheit(0):.0f}')