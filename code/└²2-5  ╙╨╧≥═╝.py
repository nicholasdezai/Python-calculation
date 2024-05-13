from collections import Counter

def __generatePath(graph, path, end, results):
    current = path[-1]
    if current == end:
        results.append(path)
    else:
        for n in graph[current]:
            if n not in path:
                __generatePath(graph, path + [n], end, results)

def searchPath(graph, start, end):
    results = []
    __generatePath(graph, [start], end, results)
    #results.sort(key=len)    #按路径长度排序
    return results

def showPath(results):
    print('The path from ',results[0][0], ' to ', results[0][-1], ' is:')
    for path in results:
        print(path)

if __name__ == '__main__':
    graph = {'A': ['B', 'C', 'D'],
             'B': ['E'],
             'C': ['D', 'F'],
             'D': ['B', 'E', 'G'],
             'E': ['D'],
             'F': ['D', 'G'],
             'G': ['E']}
    nodes = sum(graph.values(), [])
    print(Counter(nodes).most_common(1))
    #print(max(graph.keys(), key=lambda k: len(graph[k])))
    #r1 = searchPath(graph, 'A', 'E')
    #showPath(r1)
    #r2 = searchPath(graph, 'A', 'E')
    #showPath(r2)
