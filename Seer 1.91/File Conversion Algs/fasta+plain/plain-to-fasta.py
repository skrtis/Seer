import math
x = input("Enter String(s), split multiple strings with semicolon:")
y = int(input("Enter preferred line length: "))
strings = x.split(";")
names = []
for i in range(len(strings)):
    n = input("Enter SeqID: " + str(i+1)+": ")
    names.append(n)
    n = ''

for x,i in zip(names,strings):
    print(">"+x) #prints FASTA id
    nums = math.floor(len(i)/y)
    for z in range(nums):
      print(i[:y])
      i = i.replace(i[:y],'')
    if i != '':
        print(i)
