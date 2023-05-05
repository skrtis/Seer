# output = F(a-1) + k[F(a-2)] for n iterations
#for n number of generations, k number of new pairs of offspring
n = input("Enter input n:")
k = input("Enter input k:")
#initialize n-1 and n-2
nm1 = 1
nm2 = 1
fin = 0

#iterate through generations
n = int(n) - 2
for i in range(n):
    fin = nm1 + (int(k)*nm2)
    nm2 = nm1
    nm1 = fin 

print(fin)