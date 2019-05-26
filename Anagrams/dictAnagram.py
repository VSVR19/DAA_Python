class DictAnagram:

    def __init__(self):
        pass

    @staticmethod
    def dict_anagram_checker(word1, word2):

        word1 = word1.replace(" ", "")
        word2 = word2.replace(" ", "")

        if len(word1) != len(word2):
            return False

        dict = {}
        dict1 = {}

        listword1 = list(word1)
        listword2 = list(word2)

        for i in listword1:
            if i not in dict.keys():
                dict[i] = 0
            else:
                # dict[i] = 1
                dict[i] += 1 # dict[i] = dict[i] + 1

        for i in listword2:
            if i not in dict1.keys():
                dict1[i] = 0
            else:
                dict1[i] += 1

        return dict == dict1


objectDictAnagram = DictAnagram()
print(objectDictAnagram.dict_anagram_checker("go go go","gggooo"))
print(objectDictAnagram.dict_anagram_checker("abc","cba"))
print(objectDictAnagram.dict_anagram_checker("hi man","hi     man"))
print(objectDictAnagram.dict_anagram_checker("aabbcc","aabbc"))
print(objectDictAnagram.dict_anagram_checker("123","1 2"))
