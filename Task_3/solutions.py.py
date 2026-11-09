# Q1. Find the Frequency of Each Word in a Sentence
def q1(sentence):
    words = sentence.split()
    result = {}
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result


# Q2. Find the Frequency of Each Character in a Word
def q2(word):
    result = {}

    for char in word:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result

# Q3. Find the First Non-Repeating Character in a Word
def q3(word):
    frequency = {}

    for char in word:
        frequency[char] = frequency.get(char, 0) + 1

    for char in word:
        if frequency[char] == 1:
            return char
    return None

# Q4. Check Whether Two Strings Are Anagrams
def q4(s1, s2):
    return sorted(s1) == sorted(s2)

# Q5. Find the First Repeating Character in a String
def q5(word):
    seen = set()

    for char in word:
        if char in seen:
            return char
        else:
            seen.add(char)
    return None

# Q6. Move All Zeros to the End of a List
def q6(nums):
    non_zeros = []
    zeros = []

    for num in nums:
        if num == 0:
            zeros.append(num)
        else:
            non_zeros.append(num)
    return non_zeros + zeros

# Q7. Find the Second Highest Distinct Number
def q7(nums):
    unique_numbers = sorted(set(nums), reverse=True)

    if len(unique_numbers) < 2:
        return None
    return unique_numbers[1]

# Q8. Remove Duplicates Without Changing Original Order
def q8(nums):
    result = []

    for num in nums:
        if num not in result:
            result.append(num)
    return result

# Q9. Find the Missing Number from 1 to N
def q9(nums, N):
    total = N * (N + 1) // 2
    actual_sum = sum(nums)
    return total - actual_sum

# Q10. Find Two Numbers Whose Sum Equals a Target
def q10(nums, target):
    for j in range(len(nums)):
        for i in range(j):
            if nums[i] + nums[j] == target:
                return [nums[i], nums[j]]
    return []

# Q11. Find the Number Closest to Zero
def q11(nums):
    return min(nums, key=lambda x: (abs(x), -x))

# Q12. Find Common Elements Between Two Lists
def q12(list1, list2):
    result = []

    for num in list1:
        if num in list2 and num not in result:
            result.append(num)
    return result

# Q13. Rotate a List to the Right by K Positions
def q13(nums, k):
    if not nums:
        return []

    k = k % len(nums)

    if k == 0:
        return nums[:]
    return nums[-k:] + nums[:-k]

# Q14. Find the Maximum Sum of Two Consecutive Elements
def q14(nums):
    max_sum = nums[0] + nums[1]

    for i in range(1, len(nums) - 1):
        current_sum = nums[i] + nums[i + 1]

        if current_sum > max_sum:
            max_sum = current_sum
    return max_sum

# Q15. Find All Pairs Whose Sum Equals a Target
def q15(nums, target):
    result = set()

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                pair = tuple(sorted((nums[i], nums[j])))
                result.add(pair)
    return [list(pair) for pair in sorted(result)]



