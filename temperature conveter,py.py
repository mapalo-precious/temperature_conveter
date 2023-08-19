welcome = 'Hello, welcome to my temperature converter'
print(welcome)
num_degree = int(input('What is the number of your degree?\nANSWER:  '))
converting = input('what unit do you choose\n1. Degrees Celsius -> Fahrenheit(Type"1")\n2.Degrees Celsius -> Kelvin  (Type"2")\n3.Fahrenheit -> Celsius (Type"3")\n4.Fahrenheit -> Kelvin (Type"4")\n5.Kelvin -> Celsius(Type"5")\n6.Kelvin -> Fahrenheit(Type"6")\nANSWER:  ')


# /////////////////////////////////////////TEMPERATURE CONVERTER///////////////////////////////////////////////////////


# Celsius->Fahrenheit
def celsius_fahrenheit(x):
  ans_celsius_fahrenheit = x*9/5+32
  return ans_celsius_fahrenheit

# Celsius->Kelvin


def celsius_kelvin(x):
  ans_celsius_kelvin = x + 273.15
  return ans_celsius_kelvin

# Fahrenheit->Celsius


def fahrenheit_celsius(x):
  ans_fahrenheit_celsius = (x-32)*5/9
  return ans_fahrenheit_celsius

# Fahrenheit->Kelvin


def fahrenheit_kelvin(x):
  ans_fahrenheit_kelvin = (x-32)*5/9+273.15
  return ans_fahrenheit_kelvin

# Kelvin->Celsius


def kelvin_celsius(x):
  ans_kelvin_celsius = x-273.15
  return ans_kelvin_celsius

# Kelvin->Fahrenheit


def kelvin_fahrenheit(x):
  ans_kelvin_fahrenheit = (x-273.15)*9/5 + 32
  return ans_kelvin_fahrenheit


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ IF STATEMENT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if converting == '1':
  print(celsius_fahrenheit(num_degree))
elif converting == '2':
  print(celsius_kelvin(num_degree))
elif converting == '3':
  print(fahrenheit_celsius(num_degree))
elif converting == '4':
  print(fahrenheit_kelvin(num_degree))
elif converting == '5':
  print(kelvin_celsius(num_degree))
elif converting == '6':
  print(kelvin_fahrenheit(num_degree))
else:
  print('Error : Invalid convert')
