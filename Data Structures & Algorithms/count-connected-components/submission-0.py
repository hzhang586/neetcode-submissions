class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        count = 0
        visited = set()
        queue = deque([])
        for i in range(n):
            if i not in visited:
                visited.add(i)
                queue.append(i)
                count += 1
                while queue:
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor not in visited:
                            visited.add(neighbor)
                            queue.append(neighbor)
        
        return count


        