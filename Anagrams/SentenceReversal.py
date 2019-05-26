class SentenceReversal:

    def __init__(self):
        pass

    @staticmethod
    def sentence_reversal(sentence):
        result_list = []

        sentence_list = list(sentence.split(" "))

        for word in sentence_list:
            if word != "":
                result_list.insert(0, word)
                result_list.insert(0, "")

        return ' '.join(result_list).strip()

    @staticmethod
    def jose_sentence_reversal(sentence):
        words = []
        length = len(sentence)
        spaces = [' ']
        i = 0

        while i < length:
            if sentence[i] not in spaces:
                word_start = i

                while sentence[i] not in spaces and i < length:
                    # print(sentence[i])
                    i += 1

                words.append(sentence[word_start : i])
                print(words)

            i += 1

        return " ".join(words)


ObjectSentenceReversal = SentenceReversal()
'''
print(ObjectSentenceReversal.sentence_reversal('    space before'))
print(ObjectSentenceReversal.sentence_reversal('space after     '))
print(ObjectSentenceReversal.sentence_reversal('   Hello John    how are you   '))
print(ObjectSentenceReversal.sentence_reversal('1'))
'''
print(ObjectSentenceReversal.jose_sentence_reversal("   Hello John    how are you   "))
