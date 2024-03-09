# For Loop will lop a specific number of times
# The range() function called with one, two, or three arguments
# break and continue can be used in for loops

print('My name is')
for i in range(5):
    print('Olivia five times ' + str(i))


# Fridrich Gauss - Matimatichian (1+99; 2+98; 3+97; 49+51; 50*100; 5000 + 50)
total = 0
for num in range(101):
    total = total + num
print(total)

# while loop
print('My name is')
i = 0
while i < 5:
    print('Jimmy Five Times ' + str(i))
    i = i + 1

# FOr Loop - increase from 0 to 10 bt 2 (0, 2, 4, 6, 8, 10). Or instead 2 we can insert -2 and decrease count (10, 8, 6, 4, 2, 0)
print('My name is')
for i in range(12, 16, 2):
    print('Jimmy Five Times ' + str(i))
