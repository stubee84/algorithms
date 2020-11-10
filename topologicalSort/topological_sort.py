'''
    Using Kahn's algorithm
'''

def topo_sort(n: int, m: int, graph: list) -> list:
    sorted_list = list()
    queue = list()

    in_degree = dict()
    adjacency = dict()
    for arr in graph:
        for j in range(len(arr)):
            try:
                if j > 0:
                    in_degree[arr[j]] += 1
                    adjacency[arr[j]].append(arr[j-1])
                else:
                    if in_degree[arr[j]] == 0:
                        in_degree[arr[j]] = 0
            except KeyError:
                if j > 0:
                    in_degree[arr[j]] = 1
                    adjacency[arr[j]] = [arr[j-1]]
                else:
                    in_degree[arr[j]] = 0
    
    for k, v in in_degree.items():
        if v == 0:
            queue.append(k)

    index = 0
    while queue:
        item = queue.pop(0)
        sorted_list.append(item)
        index += 1

        for key, values in adjacency.items():
            for value in values:
                if value == item:
                    in_degree[key] -= 1

                    if in_degree[key] == 0:
                        queue.append(key)

    
    if index != n:
        print("found cycle in graph")
    return sorted_list


# Write your code here
if __name__ == "__main__":
    adj1 = [[5,0],[5,2],[2,3],[4,0],[4,1],[1,3]]
    num, edges = 6,6
    print(topo_sort(n=num, m=edges, graph=adj1))

    num, edges = 4, 3
    adj2 = [[3,0], [1,0], [2,0]]
    print(topo_sort(n=num, m=edges, graph=adj2))

    n, m = 5, 6
    graph = [[1,2],[1,3],[2,3],[2,4],[3,4],[3,5]]
    print(topo_sort(n=n, m=m, graph=graph))