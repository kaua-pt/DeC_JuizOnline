class Solution:
    def kth(self,nums1,nums2,k):
        
        if not nums1:
            return nums2[k]
        if not nums2:
            return nums1[k]

        mid1=len(nums1)//2
        mid2=len(nums2)//2

        if mid1+mid2< k:
            if nums1[mid1]<nums2[mid2] :
                return self.kth(nums1[mid1+1:],nums2,k-1-mid1)

            else:
                return self.kth(nums1,nums2[mid2+1:],k-1-mid2)
        else:
            if nums1[mid1] > nums2[mid2]:
                return self.kth(nums1[:mid1], nums2, k)
            else:
                return self.kth(nums1, nums2[:mid2], k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n=len(nums1)
        m=len(nums2)

        total=n+m
        if total%2==0:
            return (self.kth(nums1,nums2,total//2) + self.kth(nums1,nums2,total//2-1))/2
        else:
            return self.kth(nums1,nums2,total//2)