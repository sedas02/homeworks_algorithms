# задача 1: Поиск квадратного корня
def findSqrt(target):
    if target == 0: return 0
    left, right = 1, target
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == target: return mid
        elif mid * mid < target: left = mid + 1
        else: right = mid - 1
    return right

# задача 2: Очень лёгкая задача
def copyTime(n, x, y):
    def can_copy_in_time(time):
        fast, slow = min(x, y), max(x, y)
        parts = time // fast
        parts += (time - (time // slow) * slow) // slow
        return parts >= n

    left, right = 1, n * max(x, y)
    while left < right:
        mid = (left + right) // 2
        if can_copy_in_time(mid):
            right = mid
        else:
            left = mid + 1
    return left

# задача 3:Накормить животных
# Наивная реализация (двойной цикл)
def feed_animals_naive(animals, food):
    if not animals or not food:
        return 0
    used_food = [False] * len(food)
    count = 0
    for age in animals:
        for i, f in enumerate(food):
            if not used_food[i] and f >= age:
                used_food[i] = True
                count += 1
                break
    return count

#Реализация с сортировкой (жадный, оптимальный)
def feed_animals_sorted(animals, food):
    if not animals or not food:
        return 0
    animals.sort()
    food.sort()
    count = 0
    for f in food:
        if count < len(animals) and f >= animals[count]:
            count += 1
    return count


# задача 4: Найти разницу между двух строк
from collections import Counter

def extra_letter(a: str, b: str) -> str:
    count_a = Counter(a)
    count_b = Counter(b)
    for ch in count_a:
        if count_a[ch] != count_b.get(ch, 0):
            return ch
    return ""

# задача 5:Сумма двух элементов массива (Two Sum). Решение с хеш-таблицей
def two_sum(nums, target):
    index_by_value = {}
    for i, x in enumerate(nums):
        need = target - x
        if need in index_by_value and index_by_value[need] != i:
            return index_by_value[need], i
        index_by_value[x] = i
    return None

# задача 6: Сортировка Шелла
def shell_sort(arr):
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return arr

# задача 7: Массив анаграмм
def group_anagrams(strs):
    groups = {}
    for s in strs:
        key = ''.join(sorted(s))
        if key not in groups:
            groups[key] = []
        groups[key].append(s)
    return list(groups.values())
