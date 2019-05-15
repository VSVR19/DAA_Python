class AnagramCheck:

    def __init__(self, text_one, text_two):
        self.text_one = text_one
        self.text_two = text_two

    def anagram_checker_method(self): 

        # The variable to be returned to the function call
        result = False

        # Removing white-spaces within the strings
        self.text_one = self.text_one.replace(" ", "")
        self.text_two = self.text_two.replace(" ", "")

        # Removing any trailing white spaces
        self.text_one = self.text_one.strip()
        self.text_two = self.text_two.strip()

        # print("Removing Spaces: {0} and {1}".format(self.text_one, self.text_two))

        # Directly convert a list to a string without For loops!
        text_one_list = list(self.text_one)
        text_two_list = list(self.text_two)

        # print("New lists {0} and {1}".format(text_one_list, text_two_list))

        # Checks if the lists are identical
        return sorted(text_one_list) == sorted(text_two_list)


ac = AnagramCheck("go go go", "gggooo")
print(ac.anagram_checker_method())

ac = AnagramCheck("abc", "cba")
print(ac.anagram_checker_method())

ac = AnagramCheck("hi man", "hi     man")
print(ac.anagram_checker_method())

ac = AnagramCheck("aabbcc", "aabbc")
print(ac.anagram_checker_method())

ac = AnagramCheck("123", "1 2")
print(ac.anagram_checker_method())
