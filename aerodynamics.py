v = 0
a_motor = 2
t = 0

while t < 10:
    rezistenta = 0.05 * v * v
    a = a_motor - rezistenta
    v = v + a
    
    print("Timp:", t, "Viteza:", round(v,2))
    
    t = t + 1