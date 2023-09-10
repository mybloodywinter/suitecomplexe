termes = int(input("x premiers termes : "))
um1 = 1

# un+1 = (1+i)*un

for i in range(termes):
        un = (complex(1,1)*um1)
        um1 = un
        print(f"Un({i+1})={un}")
