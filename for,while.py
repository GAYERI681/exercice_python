# affichage des 10 premiers nombres pairs
print("Les 10 premiers nombres pairs :")
for i in range(2, 21, 2):
    print(i)

# affichage des 10 premiers nombres impairs
print("Les 10 premiers nombres impairs :")
count = 0
number = 1
while count < 10:
    print(number)
    number += 2
    count += 1