import json

class Student:
    def __init__(self,name,age,sex,s_num,chinese,math,english):
        self.name = name
        self.age = age
        self.sex = sex
        self.s_num = s_num
        self.chinese = chinese
        self.math = math
        self.english = english

    def mean_score(self):
        return (int(self.chinese) + int(self.math) + int(self.english))/3

class StudentManager:
    def __init__(self):
        self.students = []

    #添加学生
    def add_student(self,student):
        self.students.append(student)

    #根据学号查询学生
    def search_student(self,s_num):
        for student in self.students:
            if student.s_num == s_num:
                return student
        return None

    #根据学号删除学生
    def delete_student(self,s_num):
        for student in self.students:
            if student.s_num == s_num:
                self.students.remove(student)
                return True
        return False

    def save_json(self):
        dic_s = []
        for student in self.students:
            dic_s.append(student.__dict__)
        #将字典转化为JSON格式的字符串
        # json_str = json.dumps(dic_s,ensure_ascii=False)
        with open('student.json',mode = 'w',encoding = 'utf-8') as file:
            json.dump(dic_s,file,ensure_ascii=False)
if __name__ == '__main__':
    student1 = Student('张三','20','男','202640100882','129','130','140')
    student2 = Student('李四','23','女','202640100883','121','150','138')
    student3 = Student('王五','22','男','202640100884','118','119','120')

    manager = StudentManager()

    manager.add_student(student1)
    manager.add_student(student2)
    manager.add_student(student3)

    manager.save_json()