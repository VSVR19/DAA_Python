class SentenceReversal:

    def __init__(self):
        pass


    # @staticmethod
    # def reverse_a_sentence(sentence):
    #     result_list = []
    #     sentence_length = len(sentence)
    #     print("Sentence length is: {0}.".format(sentence_length))
    #     indexer = 0
    #     space_list = [" "]
    #     word = ""
    #
    #     while indexer < sentence_length:
    #         if sentence[indexer] != space_list[0]:
    #             word += sentence[indexer]
    #
    #         if sentence[indexer + 1] == space_list[0]:
    #             result_list.append(word)
    #             word = ""
    #
    #         indexer += 1
    #
    #         print("Indexer is: {0}.".format(indexer))
    #         print("Word is: {0}.".format(word))
    #         print("Result list is: {0}.".format(result_list))


#     @staticmethod
#     def reverse_sentence(sentence):
#         words = []
#         sentence_length = len(sentence)
#         spaces = [" "]
#
#         indexer = 0
#
#         while indexer < sentence_length:
#             if sentence_length[indexer] not in spaces[0]:
#                 word_start = indexer
#
#                 while indexer < sentence_length and sentence[indexer] not in spaces[0]:
#                     indexer += 1
#
#                 words.append()
#
#
#
#             indexer += 1
#
#
#
#
# ObjectSentenceReversal = SentenceReversal
# # ObjectSentenceReversal.reverse_a_sentence('  space here'  and 'space here      ')
# # ObjectSentenceReversal.reverse_a_sentence("                                    space here")
# ObjectSentenceReversal.reverse_a_sentence("space here             ")



#
# class Solution(object):
#     @staticmethod
#     def reverseWords(s):
#         """
#         :type s: str
#         :rtype: str
#         """
#
#         # approach: split string and swap until mid word
#
#         snippets = s.split()
#
#         print(snippets)
#
#         snippets_count = len(snippets)
#         mid_snippet = snippets_count // 2
#         for i in range(mid_snippet):
#             snippets[i], snippets[snippets_count - 1 - i] = snippets[snippets_count - 1 - i], snippets[i]
#
#
#
#
#
#         return ' '.join(snippets)
#
#
# ObjectSolution = Solution
# print(ObjectSolution.reverseWords("                          space here             "))

class ArraySwap:

    def __init__(self):
        pass

    def swap_array(array):
        array_length = len(array)
        array_midpoint = len(array) // 2

        for number in range(array_midpoint):
            temp_variable = array[number]

            array[number] = array[array_length - number - 1]

            array[array_length - number - 1] = temp_variable

        print(array)



ObjectArraySwap = ArraySwap
# ObjectArraySwap.swap_array(['A', 'B', 'C', 'D'])
# ObjectArraySwap.swap_array(['A', 'B', 'C', 'D', 'E'])
# ObjectArraySwap.swap_array(['1', '2', '3', '4', '5'])

# https://medium.com/@lenchen/leetcode-151-reverse-words-in-a-string-9d83d7840c4d


class ArrayReverse:

    def __init__(self):
        pass

    @staticmethod
    def reverse_array(sentence):
        flag = True

        if len(sentence) < 0:
            # print(len(sentence))
            flag = False

        else:
            sentence = sentence.split(" ")
            spaces = ['']

            while spaces[0] in sentence:
                sentence.remove(spaces[0])

            # print("Sentence here is: {0}.".format(sentence))

            sentence_length = len(sentence)
            sentence_mid = sentence_length // 2

            for number in range(sentence_mid):

                temp_variable = sentence[number]
                sentence[number] = sentence[sentence_length - number - 1]
                sentence[sentence_length - number - 1] = temp_variable

            sentence = " ".join(sentence)

        if len(sentence) == 0:
            sentence = sentence

        if flag:
            return sentence
            # print(sentence)
            # print(" ".join(sentence))


ObjectArrayReverse = ArrayReverse
# print(ObjectArrayReverse.reverse_array("                                  space         here            "))
# print(ObjectArrayReverse.reverse_array("the sky is blue"))
# print(ObjectArrayReverse.reverse_array("  hello world!  "))
# print(ObjectArrayReverse.reverse_array(""))
print(ObjectArrayReverse.reverse_array("lets go to 'new york'"))
