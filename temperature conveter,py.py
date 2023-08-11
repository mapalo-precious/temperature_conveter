welcome='Hello, welcome to my temperature conveRter'
print(welcome)
num_degree=int(input('What is the number of your degree'))
converting=input('what unit do you choose\n1. Degrees Celsius -> Farenheit(Type"1")\n2.Degrees Celsius -> Kelvin  (Type"2")\n3.Farenheit -> Celsius (Type"3")\n4.Farenheit -> Kelvin (Type"4")\n5.Kelvin -> Celsius(Type"5")\n6.Kelvin -> Farenheit(Type"6")\n')


# /////////////////////////////////////////TEMPERATURE CONVERTER//////////////////////////////////////////////////////////

#Celsius->Farenheit
def c_f(x):
  ans_cf=x*9/5+32
  return ans_cf

  #Celsius->Kelvin
def c_k(x):
  ans_ck=x+ 273.15
  return ans_ck

def f_c(x):
  ans_fc=(x-32)*5/9
  return ans_fc

def f_k(x):
  ans_fk=(x-32)*5/9+273.15 
  return ans_fk

def k_c(x):
  ans_kc=x-273.15 
  return ans_kc

# Kelvin->Farenheit
def k_f(x):
  ans_kf=(x-273.15)*9/5 + 32  
  return ans_kf

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ IF STATEMENT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

if converting=='1':
  print(c_f(num_degree))
elif converting=='2':
  print(c_k(num_degree))
elif converting=='3':
  print(f_c(num_degree))
elif converting=='4':
  print(f_k(num_degree))
elif converting=='5':
  print(k_c(num_degree))
elif converting=='6':
  print(k_f(num_degree))
else:
  print('Error : Invalid convert')