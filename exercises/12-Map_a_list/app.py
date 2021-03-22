Celsius_values = [-2,34,56,-10]



def fahrenheit_values(x):
# the magic go here: (0 °C × 9/5) + 32 = 32 °F
    return x * (9/5) + 32
   
result = list(map(fahrenheit_values, Celsius_values))
print(result)
