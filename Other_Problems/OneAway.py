class OneAway:

    def __init__(self):
        pass

    @staticmethod
    def check_one_away(word1, word2):
        # result_set = set()
        result_dict = {}
        count = 0
        flag = True

        word1 = word1.lower()
        word2 = word2.lower()

        for letter in word1:
            if 97 <= ord(letter) <= 122:
                if letter not in result_dict:
                    result_dict[letter] = 1
                elif letter in result_dict:
                    result_dict[letter] += 1

        # print(result_dict)

        for letter in word2:
            if 97 <= ord(letter) <= 122:
                if letter in result_dict:
                    result_dict[letter] -= 1
                elif letter not in result_dict:
                    result_dict[letter] = 1

        # print(result_dict)

        for value in result_dict:
            if result_dict[value] >= 1:
                count += 1
            if count == 3:
                flag = False
                break

        # print(count)

        if count == 0:
            print("These are similar words")
        elif flag:
            print("These words are One pass away.")
        else:
            print("These words are NOT one pass away.")

    @staticmethod
    def check_one_away_improved(word1, word2):
        # A cute and lovely flag variable. As ever!
        flag = True

        # For the words to be One Away, their lengths can never be more than 1 apart.
        # They can either be same, or just have a difference of a single character.
        # If the length difference is greater than 1,
        # it means that well'
        length_difference = len(word1) - len(word2)

        if length_difference > 1:
            return "Strings are not of appropriate length."

        counter = 0

        for letter in word1:
            
            if letter not in word2:
                counter += 1

            if counter == 2:
                flag = False
                break

        print(flag)


ObjectOneAway = OneAway
# ObjectOneAway.check_one_away("Pale", "Ple")
# ObjectOneAway.check_one_away("Pales", "Pale")
# ObjectOneAway.check_one_away("Pale", "Bale")
# ObjectOneAway.check_one_away("Pale", "Bake")

# ObjectOneAway.check_one_away("geeks", "geek")
# ObjectOneAway.check_one_away("geeks", "geeks")
# ObjectOneAway.check_one_away("geaks", "geeks")
# ObjectOneAway.check_one_away("peaks", "geeks")

ObjectOneAway.check_one_away_improved("Pale", "Ple")
ObjectOneAway.check_one_away_improved("Pales", "Pale")
ObjectOneAway.check_one_away_improved("Pale", "Bale")
ObjectOneAway.check_one_away_improved("Pale", "Bake")

ObjectOneAway.check_one_away_improved("geeks", "geek")
ObjectOneAway.check_one_away_improved("geeks", "geeks")
ObjectOneAway.check_one_away_improved("geaks", "geeks")
ObjectOneAway.check_one_away_improved("peaks", "geeks")
