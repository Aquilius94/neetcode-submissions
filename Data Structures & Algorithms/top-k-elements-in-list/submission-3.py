class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # create a freq table
        '''
        nums [1, 1, 2, 3, 100]
         Count: 0   |       1        |    2   |   3   |   4  |    5     |
       Symbols: []  | [2,3,100 ]     |   [1]  | []    |  []  |   []     |
        '''

        counts = {} # create a counter for specific number in nums 
        freq = [[] for i in range(len(nums) + 1)] # create n empty arrays in array

        for num in nums:  # iterate
            counts[num] = 1 + counts.get(num, 0)
        '''
            we get 
            {
            1 -> 3, 
            2 -> 1,
            3-> 1,
            100 -> 1
            }
        '''
        # now we access the index of freq at the keys value of counts, and append elements of it 

        for key, value in counts.items():
            index = value 
            element = key 

            if element not in freq[index]:
                freq[index].append(element)
        
        # once we populate everything 
        # iterate backwards for top k elements 
        result = []
        for i in range(len(freq) -1, 0, -1):
            # access the bucket and put all elements from it into the array 
            bucket:list = freq[i]
            for val in bucket: # iterate over elements in a bucket 
                # append to our result 
                result.append(val)
                # if we reach the length of k elements, return early 
                if len(result) == k:
                    return result
            

        


