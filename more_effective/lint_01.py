def maxNode(root):
    # Write your code here
    r = []
    for i in root:
        r.append(i)
    return max(r)
print(maxNode({1, -5, 3, 1, 2, -4, -5}))
