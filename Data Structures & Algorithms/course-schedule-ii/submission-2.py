class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:


        graph = dict()
        for course,prerequisite in prerequisites:
            if prerequisite not in graph:
                graph[prerequisite] = list()
            graph[prerequisite].append(course)
        

        visited = set()
        visiting = set()
        order = []

        def dfs(course):
            if course in visiting:
                return False

            if course in visited:
                return True
            if course not in graph:
                visited.add(course)
                order.append(course)
                return True

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False
            visiting.remove(course)
            visited.add(course)
            order.append(course)
            return True
        
        for c in graph:
            if not dfs(c):
                return []
        order = order [::-1]
        for i in range(numCourses):
            if i not in visited:
                order.append(i)
        
        return order
        


               