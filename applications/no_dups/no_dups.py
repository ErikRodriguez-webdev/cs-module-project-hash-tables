def no_dups(s):
    # Your code here
    # set cache to empty dictionary
    cache = {}

    # set result to emtpy list
    result = []

    # set s to split string at emtpy spaces
    s = s.split(" ")

    # for loop through s list
    for word in s:
        # check if word is not in cache
        if word not in cache:
            # then store in cache using word as key and value to 1
            cache[word] = 1
            # add word to results list
            result.append(word)

    # return list as string
    return " ".join(result)


if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))
