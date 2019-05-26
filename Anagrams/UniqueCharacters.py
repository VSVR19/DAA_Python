class UniqueCharacters:

    # Just 'pass' as args. are passed to the method below.
    def __init__(self):
        pass

    # A static method as no parameters are passed to the init() and hence no variables are used by '.self'
    @staticmethod
    def unique_characters(sentence):
        # A dictionary to hold the letters and their count.
        super_dict = {}
        # A cute& lovely flag variable!
        flag = 0

        # Looping through the 'sentence' string.
        for word in sentence:
            # If that letter is not already in dictionary, it means that were' seeing it for
            # the first time and is not a duplicate.
            if word not in super_dict:
                # Add that letter to dictionary and have its' initial count as 1.
                super_dict[word] = 1
            # Else if the letter is already in dictionary it means that were' facing a duplicate.
            elif word in super_dict:
                # Set the cute& lovely flag variable as 1 and 'break' exit the loop.
                flag = 1
                break

        # If the flag is 1, it means weve' faced no duplicate letters.
        if flag == 1:
            return False
        # If the flag is 0, it means' weve' faced duplicates.
        else:
            return True

    @staticmethod
    def new_unique_characters(sentence):
        # A dictionary to hold the letters and their count.
        super_dict = {}

        # Looping through sentence.
        for i in sentence:
            '''
            If the letter is not already present in dictionary,
            it means were' seeing it for the first time.
            We assign the count to be 1
            '''
            if i not in super_dict:
                super_dict[i] = 1
            # Were' seeing the letter again; a duplicate; we now increment the count.
            else:
                super_dict[i] += 1
        '''
        https://stackoverflow.com/questions/18807079/selecting-elements-of-a-python-dictionary-greater-than-a-certain-value
        Looping through the dictionary to create a new dictionary if a particular
        key is greater than 1, which means its a duplicate
        '''
        result_dict = dict((k, v) for k, v in super_dict.items() if v > 1)

        # Simple: length is greater than 0? Then weve' got duplicates!
        return len(result_dict) == 0


ObjectUniqueCharacters = UniqueCharacters
# print(ObjectUniqueCharacters.unique_characters(""))
# print(ObjectUniqueCharacters.unique_characters("goo"))
# print(ObjectUniqueCharacters.unique_characters("abcdefg"))

print(ObjectUniqueCharacters.new_unique_characters(""))
print(ObjectUniqueCharacters.new_unique_characters("goo"))
print(ObjectUniqueCharacters.new_unique_characters("abcdefg"))
