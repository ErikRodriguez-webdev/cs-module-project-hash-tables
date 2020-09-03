# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
# frequency of letters in order of highest to smallest
frequency_letters = ['E', 'T', 'A', 'O', 'H', 'N', 'R', 'I', 'S', 'D', 'L',
                     'W', 'U', 'G', 'F', 'B', 'M', 'Y', 'C', 'P', 'K', 'V', 'Q', 'J', 'X', 'Z']

# set decrypt_table to empty dictionary
decrypt_table = {}

# set cache to empty dictionary
cache = {}

# open file at file location and read it
with open("./applications/crack_caesar/ciphertext.txt", "r") as document:
    # loop through words and letters
    for word in document:
        for letter in word:
            # check if the length of letter equals 1 and letter is in the alphabet using ord
            if len(letter) == 1 and ord(letter) > 65 and ord(letter) < 90:
                # check if letter is in cache
                if letter in cache:
                    # then add one to count
                    cache[letter] += 1
                # else
                else:
                    # store in cache with letter as key and value as 1
                    cache[letter] = 1

# set idx to 0
idx = 0

# for loop through cache dictionary
for key, value in sorted(cache.items(), key=lambda pair: pair[1], reverse=True):
    # store key as key to decrypt_table and value as frequency_letters with i
    decrypt_table[key] = frequency_letters[idx]

    idx += 1

# set result to empty strings
result = ""

with open("./applications/crack_caesar/ciphertext.txt", "r") as document:
    # for loop through word and letters
    for word in document:
        for letter in word:
            # check if letter in decrypt_table
            if letter in decrypt_table:
                # call using letter to decrypt_table and push letter value into result string
                result += decrypt_table[letter]
            # else
            else:
                # add letter to result string
                result += letter

print(result)
