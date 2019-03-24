# Time Complexity: O(n) --> 2n for two while loops
# Space Complexity: n (length of second array) + other variables
def merge(nums1, m, nums2, n) :
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n == 1:
            nums1 = nums2
        else:
            i = m + n - 1
            p = m - 1
            q = n - 1
            while q >= 0 and p >= 0:
                # print ("p is ", p, " q is ", q)
                if nums2[q] >= nums1[p]:
                    nums1[i] = nums2[q]
                    q = q - 1
                else:
                    nums1[i] = nums1[p]
                    p = p - 1
                i = i - 1
            while q >= 0:
                nums1[i] = nums2[q]
                q = q - 1
                i = i - 1
        return nums1

nums1 = [0, 0]
nums2 = [1]
print (merge(nums1, 0, nums2, 1))