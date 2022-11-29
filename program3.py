#progrqam to count the number of characters in a string

#define frequency func
def char_freq(str1):
    dict = {}
    for i in str1:
        keys = dict.keys()
        if i in keys:
            dict[i] += 1
        else:
            dict[i] = 1
    return dict
print(char_freq("rishinaitik1234"))