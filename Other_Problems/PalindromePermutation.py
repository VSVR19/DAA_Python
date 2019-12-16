class PalindromePermutation:

    def __init__(self):
        pass

    @staticmethod
    def check_palindrome_permutation(word):
        word = word.lower()

        result_dict = {}
        count = 0
        flag = True

        for letter in word:
            if ord(letter) >= 97 and ord(letter) <= 122:
                if letter not in result_dict:
                    result_dict[letter] = 1
                else:
                    result_dict[letter] -= 1

        # print(result_dict)

        for value in result_dict:
            if result_dict[value] % 2 != 0:
                count += 1
            if count == 2:
                flag = False
                break

        if flag:
            print("This string is a permutation of a palindrome.")
        else:
            print("This string is NOT a permutation of a palindrome.")

        # print(result_dict)

    @staticmethod
    def check_palindrome_permutation_sets(word):
        word = word.lower()
        result_set = set()

        for letter in word:
            if ord(letter) >= 97 and ord(letter) <= 122:
                if letter not in result_set:
                    result_set.add(letter)
                elif letter in result_set:
                    result_set.remove(letter)

        print(len(result_set) <= 1)

ObjectPalindromePermutation = PalindromePermutation
# ObjectPalindromPermutation.check_palindrome_permutation("Tact Coa")
# ObjectPalindromPermutation.check_palindrome_permutation("code")
# ObjectPalindromPermutation.check_palindrome_permutation("aab")
# ObjectPalindromPermutation.check_palindrome_permutation("carerac")
# ObjectPalindromPermutation.check_palindrome_permutation("Malayalam")

ObjectPalindromePermutation.check_palindrome_permutation_sets("Tact Coa")
ObjectPalindromePermutation.check_palindrome_permutation_sets("code")
ObjectPalindromePermutation.check_palindrome_permutation_sets("aab")
ObjectPalindromePermutation.check_palindrome_permutation_sets("carerac")
ObjectPalindromePermutation.check_palindrome_permutation_sets("Malayalam")