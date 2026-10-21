n = 1234256278399
freq = [0] * 10

while n != 0:
    last_digit = n % 10
    freq[last_digit] += 1
    n //= 10

print(freq)

# Hash mapping is a way to store data in key : value pairs so we can find information quickly.
# Key: Used to search for data.
# Value: The data stored against that key.
# Hashing: A process that helps determine where the key's data should be stored and found
# Hash Mapping: Hash mapping is a technique in Data Structures and Algorithms (DSA) used 
# to store and organize data using keys and values. It uses a hash function to convert a
#  key into an index or location where the data can be stored and retrieved efficiently.
#  It is commonly used for frequency counting, finding duplicate elements, and fast
#  searching. Its average time complexity for insertion, searching, and deletion is O(1).