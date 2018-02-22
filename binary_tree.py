from binarytree import Node, build

#inorder traversal
def inorder(root):
    if (root != None):
        inorder(root.left)
        print (str(root.value) + ' ', end = " ")
        inorder(root.right)

#height of the tree
def get_height(node):
    if node == None or (node.left == None and node.left == None):
        return 0

    else:
        left_height = get_height(node.left)
        right_height = get_height(node.right)

        return max(left_height, right_height)+1

#isbalanced O(n)
def isbalanced(node):
    if node == None:
        return [True, -1]

    left_height = isbalanced(node.left)
    right_height = isbalanced(node.right)

    if left_height[0] == True and right_height[0] == True:
        if abs(left_height[1] - right_height[1]) > 1:
            return [False, 0]
        else:
            return [True, max(left_height[1], right_height[1])+1]
    else:
        return [False, 0]

#symmetric
def issymmetric(l, r):
    if l == None and r == None:
        return True

    elif l != None and r != None:
        return l.value == r.value and issymmetric(l.left, r.right) and issymmetric(l.right, r.left)

    return False

#find Lowest common ancesstor
def lca(node, a,b):
    if node == None:
        return None

    if node.value == a or node.value == b:
        return node.value

    left = lca(node.left, a, b)
    right = lca(node.right, a, b)

    if left != None and right != None:
        return node.value
    if left == None and right == None:
        return None

    if left != None and right == None:
        return left
    elif left == None and right != None:
        return right

#diameter of a tree
def _diameter(node):
    if node is None:
        return 0,0
    l_dia, l_height = _diameter(node.left)
    r_dia, r_height = _diameter(node.right)
    return max(l_height + r_height + 1, l_dia, r_dia), 1 + max(l_height, r_height)

def diameter(node):
    dia, h = _diameter(node)
    return dia

def second_minimum(node):
    if node == None:
        return -1

    # if node.left == None and node.right == None:
    #     return node.value

    if node.left.value != node.right.value:
        if node.left.value == node.value:
            return node.right.value
        else:
            return node.left.value
    else:
        l_sec = second_minimum(node.left)
        r_sec = second_minimum(node.right)

#level order traversal using temp queue and then reversig the odd level nodes
def level_order_reverse_odd(node):
    stack = [node]
    print (stack[0].value)
    count = 0
    while len(stack) > 0:
        temp = []
        while len(stack) > 0:
            current = stack[0]
            stack = stack[1:]
            if current.left != None:
                temp.append(current.left)
            if current.right != None:
                temp.append(current.right)
        stack = temp
        count = count + 1
        if count % 2 != 0:
            i = len(temp) - 1
            while i >= 0:
                print (temp[i].value)
                i = i - 1
        else:
            for i in range(len(temp)):
                print (temp[i].value)

#check if a tree is BST (O(n), space complexity = O(h)
def isBST(node, range = [float('-inf'), float('inf')]):
    if node == None:
        return True

    if node.value < range[0] or node.value > range[1]:
        return False

    ret = isBST(node.left, [range[0], node.value])
    if ret == True:
        r = isBST(node.right, [node.value, range[1]])
        if r == True:
            return True
        else:
            return False
    else:
        return False

#lca if both of the numbers are present in the tree
def lca_bst(node, a, b, status = 0, count=0):
    if node == None:
        return None

    if a < node.value and b < node.value:
        return lca(node.left, a, b)
    elif a > node.value and b > node.value:
        return lca(node.right, a, b)
    else:
        return node.value

#lca bst iterative solution
def lca_bst_iter(node, a, b):
    low = None
    high = None
    if a < b:
        low = a
        high = b
    else:
        low = b
        high = a
    while node != None:
        if high < node.value:
            node = node.left
        elif low > node.value:
            node = node.right
        else:
            return node.value

#insert node bst
def insert_bst(node, k):
    if node == None:
        return Node(k)

    if node.value > k:
        node.left = insert_bst(node.left, k)
    else:
        node.right = insert_bst(node.right, k)

    return node

#find value greater than the given key
def find_greater(node, k):
    f = None
    while node != None:
        if k > node.value:
            node = node.right
        else:
            f = node.value
            node = node.left
            
    return f

#given an array, return a BST
def array_to_bst(arr, start, end):
    if start > end:
        return None

    mid = int((start + end)/2)
    root = Node(arr[mid])
    root.left = array_to_bst(arr, start, mid - 1)
    root.right = array_to_bst(arr, mid+1, end)

    return root

def find_nodes_in_range(node, low, high, result):
    while node != None:
        if high < node.value:
            node = node.left
        elif low > node.value:
            node = node.right
        # else:
        #     result.append(node.value)
        #     print (result)
    return result

def main():
    root1 = build([1, 2, 3, 5, None, 8, 9, 10, 1, None, None, 9, 11])
    root2 = build([1, 2, 3, 5, 6, None, 8, 9, 10])
    root3 = build([5,3,3, 7, 2, 2, 7, None, None, 9, None, None, 9])
    root4 = build([9,9,9,None, None, 9, 11])
    bst = build([13,9,14,7,11, None, 16, 6, None, 10,12])

    print (bst)

    # print (find_nodes_in_range(bst, 8, 15, []))

    # print (lca_bst_iter(bst,16,14))

    # arr = [1,2,3,4,5]
    # print (array_to_bst(arr, 0, len(arr)-1))
    # print (find_greater(bst,12))
    # insert_bst(bst, 8)
    # print (bst)

    # print (root1)
    # print (level_order_reverse_odd(root1))
    # print (diameter(root2))
    # print (lca(root2, 3, 11))
    # print (root3)
    # print (issymmetric(root3.left, root3.right))
    # print (get_height(root))
    # print (isbalanced(root2))


if __name__ == "__main__":
    main()