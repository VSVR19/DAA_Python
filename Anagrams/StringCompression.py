class StringCompression:

    # Just 'pass' as args. are passed to the method below.
    def __init__(self):
        pass

    # A static method as no parameters are passed to the init() and hence no variables are used by '.self'
    @staticmethod
    def string_compression(sentence):
        # A dictionary to hold the letters and count of it.
        super_dict = {}

        # Looping through sentence.
        for i in sentence:
            # If i is not already in dictionary, it means weve' found a new letter.
            if i not in super_dict:
                super_dict[i] = 1
            # Else, weve' meet the letter already; just incrementing its' count by 1.
            else:
                super_dict[i] += 1

        # Extracting all keys from the dictionary as a list.
        kys = list(super_dict.keys())
        # Extracting all values from the dictionary as a list.
        vls = list(super_dict.values())

        # The resultant list which will be converted to a list and returned.
        result_list = []

        # Doesnt matter whether were' looping through kys or vls; both have the same length.
        for i in range(len(kys)):
            # Appending keys to the resultant list.
            result_list.append(kys[i])
            # Appending values converted as a string to the resultant list.
            result_list.append(str(vls[i]))

        # Returning the resultant list by removing all the intermittent spaces.
        return "".join(result_list)


ObjectStringCompression = StringCompression
print(ObjectStringCompression.string_compression(""))
print(ObjectStringCompression.string_compression("AABBCC"))
print(ObjectStringCompression.string_compression("AAABCCDDDDD"))
print(ObjectStringCompression.string_compression("AAb"))
print(ObjectStringCompression.string_compression("AAAaaa"))
print(ObjectStringCompression.string_compression("A"))
