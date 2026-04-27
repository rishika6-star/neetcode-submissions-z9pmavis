class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums) - 1

        while lo <= hi:
            mid = (lo + hi) // 2

        # Found it!
            if nums[mid] == target:
                return mid

        # ── Left half is sorted ──
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]:
                    hi = mid - 1      # target is in left half
                else:
                    lo = mid + 1      # target is in right half

        # ── Right half is sorted ──
            else:
                if nums[mid] < target <= nums[hi]:
                    lo = mid + 1      # target is in right half
                else:
                    hi = mid - 1      # target is in left half

        return -1                     # target not found



        