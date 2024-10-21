# Array Easy: 01 Two Sum

def two_sum(nums, target):

    # Get the lenght of the list
    n = len(nums)

    # Iterate from each element of the list
    for i in range(n):
        # Iterate trough the elements after the current element
        for j in range(i + 1, n):
            # Check if the sum of the two numbes equal the target
            if nums[i] + nums[j] == target:
                # Return the index of each number
                return [i, j]

    # If no solution is found return an empty list
    return []

def hash_two_sum(nums, target):

    # Define an empty dictionary of previous elements
    prevMap = {} # val : index

    # Itarate each value of the array by index
    for i, n in enumerate(nums):
        # Store the difference of t - n
        difference = target - n
        # Checks if it exists in the dictionary
        if difference in prevMap:
            # If it exists, return the index
           return [prevMap[difference], i] # index of number that already exist, index of actual number
        # If it doesnt exist, update the hashmap
        prevMap[n] = i  # Updates the  dictionary with the current number n as the key and its index i as the value
    return

nums = [2, 1, 5, 3]
target = 4
result1 = two_sum(nums, target)
result2 = hash_two_sum(nums, target)
print("brute force: ",result1)
print("hash: ",result2)
