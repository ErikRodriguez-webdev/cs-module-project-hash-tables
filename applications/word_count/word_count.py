def word_count(s):
    # Your code here

    # set cache to empty dictionary
    cache = {}

    # set new_list to empty list
    new_list = []

    # check if s is equal to empty strings or only symbols
    if s == "" or s == '":;,.-+=/\\|[]{}()*^&':
        # then return cache
        return cache

    # set s to lowercase using lower function
    s = s.lower()

    # set s to split at empty spaces
    s = s.split(" ")

    # for loop through s list
    for word in list(s):
        if word == "":
            continue

        # check if beginning has symbols in it '":;,.-+=/\\|[]{}()*^&'
        if word[0] in '":;,./|[{](})':
            # then replace symbols with nothing
            word = word[1:]

        # check if end has symbols in it '":;,.-+=/\\|[]{}()*^&'
        if word[-1] in '":;,./|[{](})':
            # then replace symbols with nothing
            word = word[:-1]

        new_list.append(word)

    # # for loop through new_list
    # for i in range(len(new_list)):
    #     print(new_list[i])
    #     # check if word has symbols
    #     if new_list[i].isalpha() is False:
    #         # remove word from new_list
    #         word = new_list.pop(i)
    #         # for loop through the word
    #         for j in range(len(word) - 1):
    #             new_string = ""
    #             # check if letter in word is in ['\r', '\t', '\n']
    #             if word[j] + word[j + 1] in ['\r', '\t', '\n']:
    #                 new_string += word[j]
    #                 new_list.append(new_string)

    # for loop through new_list
    for word in new_list:
        # check if word is in cache
        if word in cache:
            # add one to cache using word as key
            cache[word] += 1
        # else
        else:
            # then create cache key with word set to one
            cache[word] = 1

        # return cache
    print("new test here", cache)
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
