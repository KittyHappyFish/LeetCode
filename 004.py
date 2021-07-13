class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        # 保证nums2比nums1长
        if len(nums1) > len(nums2): return self.findMedianSortedArrays(nums2,nums1)

        maxmum = 2**40
        m, n = len(nums1), len(nums2)
        left, right = 0, m  # 因为m<=n，所以right至少是m开始，同时使用二分法
        med1, med2 = 0, 0

        while left <= right:
            # 左半部分包括 0..i-1, 0...j-1
            # 右半部分包括 i..m-1, j..n-1
            i = (left + right)//2
            # i+j = m+n+1 // 2
            j = (m+n+1)//2-i

            # 判断是否达到满足要求的位置
            # 最左侧为-无穷大，最右侧为正无穷大
            nm1_i1 = -maxmum if i == 0 else nums1[i-1]
            nm1_i = maxmum if i==m else nums1[i]
            nm2_j1 = -maxmum if j==0 else nums2[j-1]
            nm2_j = maxmum if j==n else nums2[j]

            if nm1_i1<=nm2_j :
                med1, med2 = max(nm1_i1,nm2_j1), min(nm1_i, nm2_j)
                left = i + 1
            else:
                right = i - 1

        return (med1+med2)/2 if (m+n) % 2 ==0 else med1