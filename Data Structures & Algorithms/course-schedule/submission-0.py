class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph = defaultdict(list)
        for course,prerequisite in prerequisites:
            graph[prerequisite].append(course) 

        visited = set()
        visiting = set()

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

            return True
        
        for n in range(numCourses):
            if not dfs(n):
                return False
        
        return True



        