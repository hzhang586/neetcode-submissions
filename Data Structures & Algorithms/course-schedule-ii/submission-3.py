class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = defaultdict(list)
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course)
        

        visited = set()
        visiting = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return []
        order = order [::-1]
        
        return order
        


               