fahrenheit=lambda celcius: (9/5)*celcius+32
reamur=lambda celcius: 0.8 * celcius

#Tes Case
print(f'C = 100 ke Fahrenheit = {fahrenheit(100):.0f}')
print(f'C = 80 ke Reamur = {reamur(80):.0f}')
print(f'C = 0 ke Fahrenheit = {fahrenheit(0):.0f}')