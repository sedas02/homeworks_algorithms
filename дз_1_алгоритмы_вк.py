# task 1. Two sum
def two_sum(nums, target):
    left, right = 0, len(nums) - 1
    while left < right:
        current_sum = nums[left] + nums[right]
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    return []


# task 2. Развернуть массив
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr


# task 3. Развернуть часть массива
def reverse_part(arr, left, right):
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    reverse_part(arr, 0, n - 1)
    reverse_part(arr, 0, k - 1)
    reverse_part(arr, k, n - 1)
    return arr


# task 4. Слияние двух отсортированных массивов
def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


# task 5. Сортировка массива из нулей и единиц
def sort_binary_array(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        if arr[left] == 0:
            left += 1
        elif arr[right] == 1:
            right -= 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return arr


# task 6. Задача флага Нидерландов
def sort_colors(nums):
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


# task 7. Передвинуть четные числа вперед
def even_first(arr):
    even_index = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            arr[i], arr[even_index] = arr[even_index], arr[i]
            even_index += 1
    return arr


# task 8. Передвинуть нули в конец
def move_zeros(arr):
    non_zero_index = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[non_zero_index], arr[i] = arr[i], arr[non_zero_index]
            non_zero_index += 1
    return arr