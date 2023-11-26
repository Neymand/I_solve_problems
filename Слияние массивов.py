nums1 = list(map(int, input().split()))
m = int(input())
nums2 = list(map(int, input().split()))
n = int(input())




nums1[m:] = nums2[:n]

nums1.sort()

print(nums1)

