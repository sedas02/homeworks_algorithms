class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Задача 1: Проверить, является ли список циклическим
def hasCycle(head):
    if head == None or head.next == None:
        return False
    slow = head
    fast = head.next
    while slow != fast:
        if fast == None or fast.next == None:
            return False
        slow = slow.next
        fast = fast.next.next
    return True

# Задача 2: Развернуть односвязный список
def reverseLinkedList(head):
    prev = None
    current = head
    while current != None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    head = prev
    return head

# Задача 3: Найти середину списка
def middleNode(head):
    slow = fast = head
    while fast != None and fast.next != None:
        slow = slow.next
        fast = fast.next.next
    return slow

# Задача 4: Удалить элемент из односвязного списка
def removeElements(head, val):
    dummy = ListNode()
    dummy.next = head
    prev = dummy
    cur = head
    while cur != None:
        if cur.val == val:
            prev.next = cur.next
        else:
            prev = cur
        cur = cur.next
    return dummy.next

# Задача 5: Является ли одна строка исходной для другой (очередь)
def isSubsequence_queue(a, b):
    from collections import deque
    q = deque()
    for el in a:
        q.append(el)
    for el in b:
        if len(q) > 0 and q[0] == el:
            q.popleft()
    return len(q) == 0

# Задача 6: Является ли одна строка исходной для другой (два указателя)
def isSubsequence(a, b):
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            i += 1
        j += 1
    return i == len(a)

# Задача 7: Является ли слово палиндромом (стек)
def isPalindrome_stack(s):
    stack = []
    for char in s:
        stack.append(char)
    for char in s:
        if char != stack.pop():
            return False
    return True

# Задача 8: Является ли слово палиндромом (два указателя)
def isPalindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# Задача 9: Слияние двух отсортированных списков
def mergeTwoLists(list1, list2):
    dummy = ListNode()
    current = dummy
    while list1 != None and list2 != None:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    if list1 != None:
        current.next = list1
    else:
        current.next = list2
    return dummy.next
