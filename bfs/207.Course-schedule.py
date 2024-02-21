class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_meta = {}
        for i in range(numCourses):
            course_meta[i] = {
                "inbound": 0,
                "outbound": []
            }
        
        for prerequisite in prerequisites:
            course_meta[prerequisite[0]]["inbound"] += 1
            course_meta[prerequisite[1]]["outbound"].append(prerequisite[0])
        
        courses_finished = 0
        course_que = deque()
        
        for course, meta in course_meta.items():
            if meta["inbound"] == 0:
                course_que.append(course)
        
        while len(course_que):
            current_course = course_que.popleft()
            courses_finished += 1
            outbound_courses = course_meta[current_course]["outbound"]
            for o in outbound_courses:
                course_meta[o]["inbound"] -= 1
                if course_meta[o]["inbound"] == 0:
                    course_que.append(o)

        return courses_finished == numCourses