def intersection(nums1, nums2) -> List[int]:
        k = []
        for i in nums1: 
            if i in nums2:
                k.append(i)
        k = list(set(k))
        return k
