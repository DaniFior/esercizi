'''
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively. Write a function to merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
'''
    


def merge(nums1, m, nums2, n):
    nums1_tmp = nums1.copy()
    i = 0 
    j = 0
    k = 0
    while i < m and j < n:
        if nums1_tmp[i] <= nums2[j]:
            nums1[k] = nums1_tmp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

    while i < m:
        nums1[k] = nums1_tmp[i]
        i += 1
        k += 1




import unittest

def merge(nums1, m, nums2, n):
    nums1_tmp = nums1.copy()
    i = 0 
    j = 0
    k = 0
    while i < m and j < n:
        if nums1_tmp[i] <= nums2[j]:
            nums1[k] = nums1_tmp[i]
            i += 1
        else:
            nums1[k] = nums2[j]
            j += 1
        k += 1

    while j < n:
        nums1[k] = nums2[j]
        j += 1
        k += 1

    while i < m:
        nums1[k] = nums1_tmp[i]
        i += 1
        k += 1

class TestMergeFunction(unittest.TestCase):

    def test_merge_vuotoentrambi(self):
        nums1 = []
        nums2 = []
        merge(nums1, 0, nums2, 0)
        self.assertEqual(nums1, [])

    def test_merge_nums2vuoto(self):
        nums1 = [1, 2, 3]
        nums2 = []
        merge(nums1, 3, nums2, 0)
        self.assertEqual(nums1, [1, 2, 3])

    def test_merge_nums1vuoto(self):
        nums1 = [0, 0, 0]
        nums2 = [1, 2, 3]
        merge(nums1, 0, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3])

    def test_merge_nonmischiato(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_merge_mischiato(self):
        nums1 = [1, 3, 5, 0, 0, 0]
        nums2 = [2, 4, 6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

    def test_merge_uguali(self):
        nums1 = [2, 2, 2, 0, 0, 0]
        nums2 = [2, 2, 2]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [2, 2, 2, 2, 2, 2])

    def test_merge_alternato(self):
        nums1 = [1, 4, 7, 0, 0, 0]
        nums2 = [2, 5, 8]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 4, 5, 7, 8])

    def test_merge_tuttiprimo(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [0, 0, 0]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [0, 0, 0, 1, 2, 3])

    def test_merge_tuttisecondo(self):
        nums1 = [0, 0, 0, 0, 0, 0]
        nums2 = [1, 2, 3]
        merge(nums1, 0, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 0, 0, 0])

    def test_merge_valorimischiati(self):
        nums1 = [1, 3, 5, 0, 0, 0]
        nums2 = [2, 4, 6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

if __name__ == '__main__':
    unittest.main()