class ArrayPairs:

    # No arguments here as arguments are passed to the individual methods and not to class itself.
    def __init__(self):
        pass

    def pair_sum(arr, k):
        # Empty list which is used to create tuples
        temp_list = []

        # Two For loops to add the elements in the list as pairs.
        for i in range((len(arr)) - 1):
            for j in range((i + 1), (len(arr))):
                # The numbers are summed as pairs.
                answer = arr[i] + arr[j]

                # If answer equals Target, we have a match.
                if answer == k:
                    # The array elements are appened to the list created initially.
                    temp_list.append(arr[i])
                    temp_list.append(arr[j])

                    # List is converted to a tuple.
                    print(tuple(temp_list))

                    # List is cleared for the next iteration.
                    temp_list.clear()


objArrayPairs = ArrayPairs

print("**********TC01**********")
objArrayPairs.pair_sum([1,9,2,8,3,7,4,6,5,5,13,14,11,13,-1], 10)  # 6 Pairs

print("**********TC02**********")
objArrayPairs.pair_sum([1,2,3,1], 3)  # 1 Pair- How on earth well' get only 1 pair ?

print("**********TC03**********")
objArrayPairs.pair_sum([1,3,2,2], 4)  # 2 Pairs
