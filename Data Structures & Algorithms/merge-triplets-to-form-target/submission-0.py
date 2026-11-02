class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        found = [False,False,False]

        for triplet in triplets:
            if triplet[0] <= target[0] and triplet[1] <= target[1] and triplet[2] <= target[2]:

                if triplet[0] == target[0]:
                    found[0] = True
                if triplet[1] == target[1]:
                    found[1] = True
                if triplet[2] == target[2]:
                    found[2] = True
        
        return found[0] and found[1] and found[2]
        