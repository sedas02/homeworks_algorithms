# Задача 1: ПРОВЕРКА КОРРЕКТНОСТИ КУЧИ (МАССИВ)
def is_max_heap(arr):
    n = len(arr)

    for i in range((n - 2) // 2 + 1):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n and arr[i] < arr[left_idx]:
            return False

        if right_idx < n and arr[i] < arr[right_idx]:
            return False

    return True

def is_min_heap(arr):
    n = len(arr)

    for i in range((n - 2) // 2 + 1):
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n and arr[i] > arr[left_idx]:
            return False
        if right_idx < n and arr[i] > arr[right_idx]:
            return False

    return True

# Задача 2: ПРОВЕРКА КУЧИ ЧЕРЕЗ BFS НА МАССИВЕ (ОБХОД В ШИРИНУ)
def is_max_heap_bfs(arr):
    if len(arr) <= 1:
        return True

    queue = [0]  # Начинаем с корня
    n = len(arr)

    while queue:
        i = queue.pop(0)
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2
        # Проверяем левого потомка
        if left_idx < n:
            if arr[i] < arr[left_idx]:
                return False
            queue.append(left_idx)
        # Проверяем правого потомка
        if right_idx < n:
            if arr[i] < arr[right_idx]:
                return False
            queue.append(right_idx)

    return True

# Задача 3: ПОЛНОЕ БИНАРНОЕ ДЕРЕВО
def is_complete_tree(root):
    if not root:
        return True

    queue = [root]
    should_be_leaf = False

    while queue:
        node = queue.pop(0)

        if node is None:
            # Встретили None - значит дальше должны быть только None
            should_be_leaf = True
        else:
            # Если должны быть листья, но встретили узел - не полное
            if should_be_leaf:
                return False
            # Добавляем потомков
            queue.append(node.left)
            queue.append(node.right)

    return True

 # Задача 4: ОБЪЕДИНЕНИЕ K ОТСОРТИРОВАННЫХ МАССИВОВ
import heapq
def merge_k_sorted_arrays_naive(arrays):
    min_heap = []
    # Добавляем все элементы в кучу
    for array in arrays:
        for num in array:
            heapq.heappush(min_heap, num)
    # Извлекаем в отсортированном порядке
    result = []
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result

# Задача 5: K-ый НАИМЕНЬШИЙ/НАИБОЛЬШИЙ ЭЛЕМЕНТ В BST
# K-ый наименьший - Iterative (стек)
def kth_smallest_iterative(root, k):
    stack = []
    current = node
    counter = 0
    while stack or current:
        while current:
            stack.append(current)
            current = current.left
        current = stack.pop()
        counter += 1

        if counter == k:
            return current.val
        current = current.right

    return None
#  K-ый наибольший
def kth_largest_iterative(root, k):
    stack = []
    current = root
    counter = 0

    while stack or current:
        while current:
            stack.append(current)
            current = current.right

        current = stack.pop()
        counter += 1
        if counter == k:
            return current.val
        current = current.left
    return None

# Задача 6:  BALANCE FACTOR (ФАКТОР БАЛАНСА)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.balance_factor = 0
def calculate_heights_and_balance(node):
    if not node:
        return 0
    left_height = calculate_heights_and_balance(node.left)
    right_height = calculate_heights_and_balance(node.right)
    node.balance_factor = left_height - right_height
    return 1 + max(left_height, right_height)
def print_balance_factors(node):
    if not node:
        return
    print(f"Узел {node.val}: BF = {node.balance_factor}")
    print_balance_factors(node.left)
    print_balance_factors(node.right)

# Задача 7:ПРЕОБРАЗОВАНИЕ В ЗЕРКАЛЬНОЕ ДЕРЕВО (рекурсивное)
def mirror_tree_recursive(node):
    if not node:
        return None

    # Меняем левое и правое
    node.left, node.right = node.right, node.left

    # Рекурсивно для левого (новое правое)
    mirror_tree_recursive(node.left)

    # Рекурсивно для правого (новое левое)
    mirror_tree_recursive(node.right)

    return node
