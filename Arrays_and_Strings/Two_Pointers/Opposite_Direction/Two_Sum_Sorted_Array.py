# Given a List in Sorted Form and a Target. find two numbers that sum to the target. Return their indices (1-based).
def two_sum_sorted_array(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return [left , right ]   
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return "No Target Value sum in Given Array"


k = list(map(int, input().split()))
target = int(input())
print(two_sum_sorted_array(k, target))