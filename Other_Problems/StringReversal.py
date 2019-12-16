# This program reverses a string using Recursion!
# TC ? I must learn to calculate TCs of programs' using Recursion.
class StringReversal():

    # The default constructor.
    def __init__(self, index, result_queue):
        # An integer variable, this is used to index the string to be reversed, original_text.
        self.index = index
        # This queue will store the reversed input sting.
        self.result_queue = result_queue

    def print_reversed_string(self, original_text):
        # Base Case- When the length of the result queue is equal to the length of the input text,
        # it implies that we have traversed all the characters in the input string and its reversed.
        if len(self.result_queue) == len(original_text):
            # Convert the queue to a string and return it.
            return "".join(self.result_queue)
        else:
            # Take one letter of the input string at a time.
            string_letter = original_text[self.index]
            # 'Enqueue' that letter into the result queue.
            self.result_queue.insert(0, string_letter)
            # Increment the index by one;
            # so that, in the next iteration, index will refer to the next character in the input string.
            self.index += 1

            # Return the input string as is; this is because we use index to traverse through the string.
            return ObjectStringReversal.print_reversed_string(original_text)


ObjectStringReversal = StringReversal(0, [])
print(ObjectStringReversal.print_reversed_string('MILO'))
