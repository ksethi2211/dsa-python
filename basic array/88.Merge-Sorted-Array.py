class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1Ptr = m - 1
        nums2Ptr = n - 1
        resPtr = m + n - 1
        while True:
            if (nums1Ptr < 0 and nums2Ptr < 0) or nums2Ptr < 0:
                break
            if nums1Ptr < 0 or nums2[nums2Ptr] > nums1[nums1Ptr]:
                nums1[resPtr] = nums2[nums2Ptr]
                nums2Ptr -= 1
                resPtr -= 1
            else:
                nums1[resPtr] = nums1[nums1Ptr]
                nums1Ptr -= 1
                resPtr -= 1
        