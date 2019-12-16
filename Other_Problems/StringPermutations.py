def permutations(string, step=0):
    print("**************************************************")
    print("String is: {0}.".format(string))
    print("Here Step is: {0}.".format(step))
    # if we've gotten to the end, print the permutation
    if step == len(string):
        print("Base case result is: {}.".format("".join(string)))
        print("".join(string))
        print("Here StepO is: {0}.".format(step))
    # everything to the right of step has not been swapped yet
    print("Before For.")
    for i in range(step, len(string)):
        print("Step is: {0}.".format(step))
        print("I is: {0}.".format(i))

        # copy the string (store as array)
        string_copy = [character for character in string]
        print("String copy is: {0}.".format(string_copy))

        # swap the current index with the step
        string_copy[step] = string_copy[i]
        print("String copy after Swap 1: {0}.".format(string_copy))
        string_copy[i] = string_copy[step]
        print("String copy after Swap 2: {0}.".format(string_copy))

        print("**************************************************")
        # recurse on the portion of the string that has not been swapped yet (now it's index will begin with step + 1)
        permutations(string_copy, step + 1)
print("Calling again!")
permutations('ab')