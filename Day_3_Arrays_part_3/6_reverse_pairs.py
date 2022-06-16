'''
##################### Reverse Pairs #####################

Given an integer array nums, return the number of reverse pairs in the array.

A reverse pair is a pair (i, j) where 0 <= i < j < nums.length and nums[i] > 2 * nums[j].


'''

# class Solution:
#     def merge(self, arr, temp, left, mid, right):
#         i, j = left, mid
#         t_idx = left
#         count = 0

#         while i <= mid - 1 and j <= right:
#             if arr[i] <= arr[j]:
#                 temp[t_idx] = arr[i]
#                 t_idx += 1
#                 i += 1
#             else:
#                 temp[t_idx] = arr[j]
#                 if arr[i] > 2*arr[j]:

#                     print("vdfvdf", arr[left:mid], arr[mid:right+1])
#                     count += (mid-i)
#                 else:
#                     for x in range(i, mid):
#                         if arr[x] > 2*arr[j]:
#                             count += 1
#                 j += 1
#                 t_idx += 1

#         while i <= mid-1:
#             temp[t_idx] = arr[i]
#             t_idx += 1
#             i += 1

#         while j <= right:
#             temp[t_idx] = arr[j]
#             t_idx += 1
#             j += 1

#         i = left
#         while i <= right:
#             arr[i] = temp[i]
#             i += 1

#         return count



#     def merge_sort(self, arr, temp, left, right):
#         count = 0
#         if right > left:
#             mid = (left + right) // 2

#             count += self.merge_sort(arr, temp, left, mid)
#             count += self.merge_sort(arr, temp, mid+1, right)

#             count += self.merge(arr, temp, left, mid+1, right)

#         return count


#     def reversePairs(self, nums):
#         temp = [0]*len(nums)

#         ans = self.merge_sort(nums, temp, 0, len(nums)-1)
#         print(nums, temp)
#         return ans


# s = Solution()
# print(s.reversePairs([1,3,2,3,1]))