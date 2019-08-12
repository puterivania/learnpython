s = "singing in the rain and playing in the rain are two entirely different situations but both can be fun"
vowels = ['a','e','i','o','u']
x = 0
for i in s:
    if i in vowels:
        x += 1
print(x)




y = 0
for char in items:
    nums = 0
    for x in char:
        if x in ['w']:
            nums = nums + 1
    if nums>0: y += 1
print(y)
