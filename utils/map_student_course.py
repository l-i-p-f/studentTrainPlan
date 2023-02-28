from utils.query import exec_sql


def get_map_student():
    map_student = {}
    stu_no2_mat_no = {}
    sql = "SELECT NAME, STU_NO FROM STUDENT WHERE STU_NO<>'admin'"
    result = exec_sql(sql)
    map_student_id = 0
    for cur in result:
        values = list(cur)
        map_student[map_student_id] = values
        map_student_id = map_student_id + 1

    map_course = {}
    sql = "SELECT CO_NAME FROM EDUCATION_PLAN"
    result = exec_sql(sql)
    map_course_id = 0
    for cur in result:
        map_course[map_course_id] = cur[0]
        map_course_id = map_course_id + 1

    for idx in range(len(map_student)):
        stu_no2_mat_no[map_student[idx][1]] = idx
    return map_student, map_course, stu_no2_mat_no


def get_matrix(map_student):
    matrix = []
    for i in range(30):
        matrix.append([])
    for i in range(30):
        stu_no = map_student[i][1]
        # print(stu_no)
        sql = "SELECT COMMENT FROM CHOOSE WHERE STU_NO='%s'" % (stu_no)
        score = exec_sql(sql)
        # print(score)
        for j in range(118):
            matrix[i].append(int(score[j][0]))

    return matrix
