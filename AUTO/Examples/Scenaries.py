from itertools import permutations, combinations

# seq = set()
# for i in permutations(['GaP', 'GE', 'SRA', 'ACC', '-']):
#     mentions = {car: None for car in i}.keys()
#     if list(mentions) == sorted(mentions):
#         seq.add(i)
#     print(i)

# a = permutations(['GaP', 'GE', 'SRA', 'ACC'])
# seq = []
# for i in list(a):
#     if i[0]=='GaP':
#         seq.append(i)
# seq = list(set(seq))
# print(seq)

# combi = combinations(['GaP', 'GE', 'SRA', 'ACC'], 2)
# for e in list(combi):
#     print(e)

# seq = []
# cars = ['GaP', 'GE', 'SRA', 'ACC']
# for r in range(1, len(cars) + 1):
#     for combination in combinations(cars, r):
#         mentions = {car: None for car in combination}.keys()
#         if list(mentions) == sorted(mentions):
#             seq.append(combination)
#             print(combination)

# seq = []
# cars = ['GaP', 'GE', 'SRA', 'ACC']
# for r in range(2, len(cars) + 1):
#     for combination in combinations(cars, r):
#         for perm in permutations(combination):
#             mentions = {car: None for car in perm}.keys()
#             if list(mentions) == sorted(mentions):
#                 seq.append(perm)
#                 print(perm)

# seq = []
# cars = ['GaP', 'GE', 'SRA', 'ACC']
# for r in range(1, len(cars)):
#     for combination in combinations(cars[1:], r):
#         full_combination = ('GaP',) + combination
#         for perm in permutations(full_combination):
#             mentions = {car: None for car in perm}.keys()
#             if list(mentions) == sorted(mentions):
#                 seq.append(perm)
#                 print(perm)
# A1 = 'Nuevo'
# A2 = 'Seminuevo'
# A3 = 'Moto'
# B1 = 'Particular'
# B2 = 'Chofer privado'
# B3 = 'Comercial'
# C1 = 'Física'
# C2 = 'Física AE'
# D1 = 'Con Accesorios'
# D2 = 'Sin Accesorios'
# E1 = 'Con Garantia extendida'
# E2 = 'Sin Garantia extendida'
# F1 = 'Con Seguro de robo autopartes'
# F2 = 'Sin Seguro de robo autopartes'
# G1 = 'Con Seguro GAP'
# G2 = 'Sin Seguro GAP'
# H1 = 'Marsh: Contado - Al frente'
# H2 = 'Marsh: Financiado - Al frente'
# H3 = 'Marsh: Contado - Fraccionado'
# H4 = 'Marsh: Financiado - Fraccionado'
# H0 = 'Sin Seguro de daños'
# I1 = 'Prima manual: Contado - Al frente'
# I2 = 'Prima manual: Financiado - Al frente'
# I3 = 'Prima manual: Contado - Fraccionado'
# I4 = 'Prima manual: Financiado - Fraccionado'
# J1 = 'Con Tasa fija mayor que 0'
# J2 = 'Con Tasa fija en 0'
# K1 = 'Con Seguro de vida'
# K2 = 'Sin Seguro de vida'

A1 = 'NVO'
A2 = 'SNVO'
A3 = 'M'
B1 = 'P'
B2 = 'CP'
B3 = 'C'
C1 = 'FI'
C2 = 'FAE'
D1 = 'ACC'
D2 = 'SIN ACC'
E1 = 'GE'
E2 = 'SIN GE'
F1 = 'SRA'
F2 = 'SIN SRA'
G1 = 'GAP'
G2 = 'SIN GAP'
H1 = 'Marsh: Contado - Al frente'
H2 = 'Marsh: Financiado - Al frente'
H3 = 'Marsh: Contado - Fraccionado'
H4 = 'Marsh: Financiado - Fraccionado'
H0 = 'Sin Seguro de daños'
I1 = 'Prima manual: Contado - Al frente'
I2 = 'Prima manual: Financiado - Al frente'
I3 = 'Prima manual: Contado - Fraccionado'
I4 = 'Prima manual: Financiado - Fraccionado'
J1 = 'TASA<0'
J2 = 'TASA=0'
K1 = 'SDV'
K2 = 'SIN SDV'

# Combinaciones con A1, A2, A3:

# Combinaciones con A1, A2, A3:

print(sorted(A1), ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con B1, B2, B3:
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B2, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A1, ',', B3, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B2, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B3, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B2, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B3, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con C1, C2:
print(A1, ',', B1, ',', C1, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D2, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con D1, D2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E2, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con E1, E2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F2, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con F1, F2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G2, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con G1, G2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J2, ',', K1, sep='')
# Combinaciones con H0:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K2, sep='')
# Combinaciones con I1, I2, I3, I4:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
# Combinaciones con J1,',', J2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
# Combinaciones con K1, K2:
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H0, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')

print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H1, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H2, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H3, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', H4, ',', J1, ',', K1, sep='')

print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I1, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I2, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I3, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
print(A1, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
print(A2, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C1, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
print(A3, ',', B1, ',', C2, ',', D1, ',', E1, ',', F1, ',', G1, ',', I4, ',', J1, ',', K1, sep='')
