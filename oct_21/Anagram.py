n1 = 1123
n2 = 3211

freq = [0] * 10

while n1 > 0:
    digit = n1 % 10
    freq[digit] += 1
    n1 //= 10

while n2 > 0:
    digit = n2 % 10
    freq[digit] -= 1
    n2 //= 10

if all(num == 0 for num in freq):
    print("Anagram")
else:
    print("Not Anagram")