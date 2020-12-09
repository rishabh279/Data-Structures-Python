def majority_element_in_sorted_array(arr):
    """Find a majority element in a sorted array of size 'n'"""
    n = len(arr)
    for i in range(int(n/2)+1):
        if arr[i] == arr[i + int(n/2)]:
            return arr[i]
    print("No Majority Element....")


def majority_element(arr):
    """Find a majority element in an array of size 'n' using Moore_voting_algorithm."""
    n = len(arr)
    vote = 0
    count = 0
    for i in range(n):
        if i == 0:
            var = arr[i]
            vote += 1
        elif arr[i] != var and vote > 0:
            vote -= 1
        elif arr[i] == var:
            vote += 1
        elif arr[i] != var and vote == 0:
            var = arr[i]
            vote += 1

    for i in range(int(n)):
        if arr[i] == var:
            count += 1
        if count == int(n/2) + 1:
            print(f"{var} is the majority element.")
            return


if __name__ == '__main__':
    arr = [1, 1, 1, 1, 4, 8, 9]
    #arr = [1, 2, 1, 3, 1, 8, 1]
    #arr = [1, 2, 1, 3, 1, 4, 5]
    #print(majority_element_in_sorted_array(arr))
    majority_element(arr)