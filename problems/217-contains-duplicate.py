Conceptual solution:
    -use a hashSET to store each value in the array {arr[i]: 1}
    - For each value, add to hashset and increment value to 1
    - if that value already exists in the hashset, then return T/F as needed


Edgecases:
1. What about empty array/
2. Non-numercial values?
3. Large #s?
4. Negative values

Questions to get answered:
1. Hashset vs. Hashmap
    a. HashSET does not allow for duplicate values BUT hashMAP does
    b. HashSET stores values as an Object BUT HashMAP stores value as Key-value pair
    c. O(n) vs. O(1) complexity
    i.e HashSet is a set, e.g. {1, 2, 3, 4, 5, 6, 7},
HashMap is a key -> value pair(key to value) map, e.g. {a -> 1, b -> 2, c -> 2, d -> 1}

2. Read dictionary documentation


------
Solution:
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        res = {}
        for i in range(len(nums)): 
            if (res.get(nums[i]) == None):
                res[nums[i]] = 1 #ERROR: Made a mistake here of res[i] iinstead of res[nums[i]]
            else:
                return True

        return False