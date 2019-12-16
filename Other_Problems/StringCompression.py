class StringCompression:

    def __init__(self):
        pass

    @staticmethod
    def print_compressed_string(word):

        word = word.lower()

        if len(word) == 1:
            return word + str(1)

        index_counter = 0
        result_list = []
        result_string = ""
        counter = 1

        for number in range(len(word) - 1):

            slow_marker = word[index_counter]
            fast_marker = word[index_counter + 1]

            if slow_marker == fast_marker:
                counter += 1
                result_string = slow_marker + str(counter)

            elif slow_marker != fast_marker:
                counter = 1

                if result_string == "":
                    result_string = slow_marker + str(counter) + fast_marker + str(counter)
                else:
                    result_list.append(result_string)
                    result_string = fast_marker + str(counter)

            index_counter += 1

        result_list.append(result_string)
        print("The compressed string is: {0}.".format("".join(result_list)))


ObjectStringCompression = StringCompression
print(ObjectStringCompression.print_compressed_string("aabcccccaaa"))
print(ObjectStringCompression.print_compressed_string("venkata"))
print(ObjectStringCompression.print_compressed_string("ramana"))
print(ObjectStringCompression.print_compressed_string("vvvvvv"))
print(ObjectStringCompression.print_compressed_string("minneapolis"))
