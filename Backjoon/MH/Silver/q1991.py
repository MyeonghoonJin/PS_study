"""
트리 순회 - s1

"""
def solve():
    N = int(input())
    nodes = []
    child_nodes = dict()
    for _ in range(N):
        n,l,r = map(str,input().split())
        nodes.append(n)
        child_nodes[n] = [l if l != '.'else None,r if r != '.' else None]
    def preorder(node):
        print(node,end = '')
        for i in child_nodes[node]:
            if i:
                preorder(i)
    def inorder(node):
        # 자식 노드가 없을 때
        if not child_nodes[node][0] and not child_nodes[node][1]:
            print(node,end = '')
            return
        if child_nodes[node][0]:
            inorder(child_nodes[node][0])
        print(node,end = '')
        if child_nodes[node][1]:
            inorder(child_nodes[node][1])
    def postorder(node):
        # 자식 노드가 없을 때
        if not child_nodes[node][0] and not child_nodes[node][1]:
            print(node, end='')
            return
        if child_nodes[node][0]:
            postorder(child_nodes[node][0])
        if child_nodes[node][1]:
            postorder(child_nodes[node][1])
        print(node, end='')

    preorder(nodes[0])
    print()
    inorder(nodes[0])
    print()
    postorder(nodes[0])
if __name__ == '__main__':
    solve()