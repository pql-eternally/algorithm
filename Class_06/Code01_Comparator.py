class Student(object):
    name: str
    id: int
    age: int

    def __init__(self, name: str, _id: int, age: int):
        self.name = name
        self.id = _id
        self.age = age

    def __lt__(self, other):
        """
        如果返回负数，认为第一个参数应该拍在前面
        如果返回正数，认为第二个参数应该拍在前面
        如果返回0，认为谁放前面都行
        根据age从小到大排序
        """
        return self.age < other.age

    def __str__(self):
        return f'{self.id}:{self.name}:{self.age}'


def print_students(students):
    for s in students:
        print(s)


def sort_by_age(student):
    return student.age


def sort_by_id(student):
    return student.id


def main():
    s1 = Student('张三', 1, 18)
    s2 = Student('李四', 2, 17)
    s3 = Student('王五', 3, 19)
    s4 = Student('赵六', 4, 18)
    students = [s1, s2, s3, s4]
    # 要使得student可以排序，重写__lt__内置函数，或者给sort函数传入key为
    # students.sort()
    # students.sort(key=lambda s: s.age)
    students.sort(key=sort_by_age)
    students.sort(key=sort_by_id)
    print_students(students)


if __name__ == '__main__':
    main()
