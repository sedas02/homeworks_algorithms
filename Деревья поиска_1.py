#Задача 1: Восстановление бинарного дерева из массива
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

def build_tree(arr, i=0):
    if i >= len(arr) or arr[i] is None:
        return None
    root = TreeNode(arr[i])
    root.left = build_tree(arr, 2 * i + 1)
    root.right = build_tree(arr, 2 * i + 2)
    return root

#Задача 2: Проверка симметрии: BFS (обход в ширину)
def is_symmetric_bfs(root):
    if root is None:
        return True
    queue = [root]
    while queue:
        l, r = 0, len(queue) - 1
        while l < r:
            left, right = queue[l], queue[r]
            if (left is None and right is None):
                l += 1; r -= 1; continue
            if (left is None or right is None) or (left.data != right.data):
                return False
            l += 1; r -= 1
        next_level = []
        for node in queue:
            if node:
                next_level.extend([node.left, node.right])
        if all(n is None for n in next_level):
            break
        queue = next_level
    return True

#Задача 3: Проверка симметрии: DFS (обход в глубину - Inorder)
def depth_search_inorder(root, res):
    if root is None:
        return res
    depth_search_inorder(root.left, res)
    res.append(root.data)
    depth_search_inorder(root.right, res)
    return res

def is_symmetric_dfs(root):
    if root is None:
        return True
    data = []
    depth_search_inorder(root, data)
    return data == data[::-1]

#Задача 4: Минимальная глубина бинарного дерева
def min_depth(root):
    if root is None: return 0
    if root.left is None and root.right is None: return 1
    if root.left and root.right:
        return 1 + min(min_depth(root.left), min_depth(root.right))
    return 1 + (min_depth(root.left) if root.left else min_depth(root.right))

#Задача 5: Произведение минимального и максимального элементов в массиве-дереве
def max_min_multiplication(data):
    if len(data) < 3:
        return -1
    # min: идём влево, max: вправо
    min_index = 1
    while 2 * min_index + 1 < len(data):
        min_index = 2 * min_index + 1
    max_index = 2
    while 2 * max_index + 2 < len(data):
        max_index = 2 * max_index + 2
    return data[min_index] * data[max_index]

#Задача 6: Сравнение двух бинарных деревьев
def is_same_tree(a, b):
    if a is None and b is None: return True
    if a is None or b is None: return False
    if a.data != b.data: return False
    return is_same_tree(a.left, b.left) and is_same_tree(a.right, b.right)
