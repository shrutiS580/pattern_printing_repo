def is_anagram(n1, n2):
    freq = [0] * 10

    while n1 > 0:
        digit = n1 % 10
        freq[digit] += 1
        n1 //= 10

    while n2 > 0:
        digit = n2 % 10
        freq[digit] -= 1
        n2 //= 10

    for i in range(len(freq)):
        if freq[i] != 0:
            return False

    return True


print(is_anagram(1123, 3211))   

# if all(num == 0 for num in freq):
#     print("Anagram")
# else:
#     print("Not Anagram")