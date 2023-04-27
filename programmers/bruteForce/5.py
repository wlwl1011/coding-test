def search(nodes, node, check_node):
    for j in nodes:
        arr = []
        if isinstance(node[0],list):
            arr = node
            arr.append(j)
        else:    
            arr.append(node)
            arr.append(j)
        temp = nodes.copy()
        temp.pop(nodes.index(j))
        if arr not in check_node:
            check_node.append(arr)                 
        if temp:
            search(temp,arr,check_node)

def solution(k, dungeons):
    answer = 0 
    check_node = []
    index = 0
    for i in dungeons:
        i.append(index)
        index += 1
    for i in dungeons:
        temp = dungeons.copy()
        temp.pop(dungeons.index(i))   
        search(temp,i,check_node)
    for i in check_node:
        check = 0
        k_value = k
        for temp in i:
            if k_value>= temp[0] :
                k_value = k_value - temp[1]
                check +=1

        if check >= answer:
            answer = check   
    return answer

print(solution(40,[[40, 20], [10, 10], [10, 10], [10, 10], [10, 10]]))
