class MergeSortTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.tree = [None] * (4 * self.n)
        self.build(nums, 0, 0, self.n - 1)

    def build(self, nums, index, low, high):
        if low == high:
            self.tree[index] = [nums[low]]
        else:
            mid = (low + high) // 2
            self.build(nums, 2 * index + 1, low, mid)
            self.build(nums, 2 * index + 2, mid + 1, high)
            self.tree[index] = self.merge(self.tree[2 * index + 1], self.tree[2 * index + 2])

    def merge(self, arr1, arr2):
        result = []
        i, j = 0, 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                result.append(arr1[i])
                i += 1
            else:
                result.append(arr2[j])
                j += 1
        result.extend(arr1[i:])
        result.extend(arr2[j:])
        return result

    def query(self, left, right, index=0, low=0, high=None):
        if high is None:
            high = self.n - 1
        if left > high or right < low:
            return []
        if left <= low and right >= high:
            return self.tree[index]
        mid = (low + high) // 2
        left_result = self.query(left, right, 2 * index + 1, low, mid)
        right_result = self.query(left, right, 2 * index + 2, mid + 1, high)
        return self.merge(left_result, right_result)

# Example usage:
arr = [4, 1, 7, 3, 9, 5]
merge_sort_tree = MergeSortTree(arr)

print("Sorted elements in range [1, 4]:", merge_sort_tree.query(1, 4))
