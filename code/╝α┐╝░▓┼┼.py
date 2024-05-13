from random import shuffle

def func(teacherNames, examNumbers, maxPerTeacher):
    '''teacherNames:教师名单，列表类型
       examNumbers:监考总场次，整数
       maxPerTeacher:每个老师最大监考次数，整数
       假设每场考试需要安排两位老师监考'''
    # 构建字典，键为教师名称，值为已安排监考次数
    teachers = {teacher:0 for teacher in teacherNames}
    # 存放监考安排的列表
    result = []
    for _ in range(examNumbers):
        # 选择已安排场次最少的老师
        teacher1 = min(teachers.items(), key=lambda item:item[1])[0]
        # 在其他老师中选择已安排监考场次最少的老师
        restTeachers = [item for item in teachers.items() if item[0]!=teacher1]
        # 乱序，避免总是两个人在一起
        shuffle(restTeachers)
        teacher2 = min(restTeachers, key=lambda item:item[1])[0]
        if max(teachers[teacher1],teachers[teacher2])>=maxPerTeacher:
            return '数据不合适'
        # 安排一场监考
        teachers[teacher1] += 1
        teachers[teacher2] += 1        
        result.append((teacher1, teacher2))
    return result

teacherNames = ['教师'+str(i) for i in range(10)]
# 获取并查看监考安排情况
result = func(teacherNames, 30, 10)
print(result)
# 查看每位老师安排的监考场次
if result != '数据不合适':
    for teacher in teacherNames:
        num = sum((1 for item in result if teacher in item))
        print(teacher, num)
