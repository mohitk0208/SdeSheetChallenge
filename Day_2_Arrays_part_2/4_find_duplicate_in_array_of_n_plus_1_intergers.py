'''

######################### Find duplicate in array of n+1 integers #########################

Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

leetcode : https://leetcode.com/problems/find-the-duplicate-number/
codestudio :

'''

# approach 1
  # 1. sort the array
  # 2. check if the next element is the same as the current element
  # 3. if yes, return the current element


# approach 2
  # 1. create a set
  # 2. iterate through the array
  # 3. if the element is in the set, return the element
  # 4. else, add the element to the set

# approach 3 using slow and fast pointer
  # move the slow pointer by 1 element
  # move the fast pointer by 2 elements
  # after first collision
  # set fast pointer to initial
  # now move both pointers by 1 element (at same speed)
  # if they collide, return the element

#leetcode solution
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast = nums[0]
        slow = nums[0]

        while True:                       # find the first collision
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

              # slow is now the collision point
              # distance from initial to duplicate is equal to the distance from the collision point to the duplicate
              # so set the fast pointer to the initial
              # move both pointers at same speed
              # if they collide, return the element

        fast = nums[0]
        while fast != slow:
            slow = nums[slow]
            fast = nums[fast]

        return fast