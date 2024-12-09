# 设计一个类
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def say_hi(self):
        print(f'你好，我是{self.name}，今年{self.age}岁')

    def say_hi2(self, msg):
        print(f'你好，我是{self.name}，今年{self.age}岁，{msg}')

# 创建一个对象
stu1 = Student()

# 给对象添加属性
stu1.name = "张三"
stu1.gender = "男"
stu1.nationality = "中国"
stu1.native_place = "广东"
stu1.age = 18
stu1.say_hi()

# 输出对象
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)

stu2 = Student()
stu2.name = "李四"
stu2.gender = "女"
stu2.nationality = "中国"
stu2.native_place = "上海"
stu2.age = 20
stu2.say_hi2("欢迎来到中国")


# 类和对象
class Clock:
    id = None
    price = None

    def ring(self):
        import winsound
        winsound.Beep(2000, 3000)
        print('时间到了')

# 构造2个闹钟
clock1 = Clock()
clock1.id = 1
clock1.price = 100
print(f"闹钟1{clock1.id}的价格是{clock1.price}，正在响")
# clock1.ring()

clock2 = Clock()
clock2.id = 2
clock2.price = 200
print(f"闹钟2{clock1.id}的价格是{clock1.price}，正在响")
# clock2.ring()

# 构造方法
# __init__()
class Person:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

    def __init__(self, name, gender, nationality, native_place, age):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place
        self.age = age
        print("Person对象创建了")

pers = Person("王五", "男", "中国", "上海", 18)

# 魔术方法（内置方法）
# __str__()
class Person:
    def __init__(self, name, gender, nationality, native_place, age):
        self.name = name
        self.gender = gender
        self.nationality = nationality
        self.native_place = native_place
        self.age = age

    # 重写字符串结果
    def __str__(self):
        return f"Person类对象：姓名：{self.name}，性别：{self.gender}，国籍：{self.nationality}，籍贯：{self.native_place}，年龄：{self.age}"

    # 小于号的比较
    def __lt__(self, other):
        return self.age < other.age

    # 小于等于号比较
    def __le__(self, other):
        return self.age <= other.age

    # 等号比较
    def __eq__(self, other):
        return self.age == other.age

p1 = Person("王五1", "男", "中国", "上海", 18)
p2 = Person("王五2", "男", "中国", "北京", 20)
p3 = Person("王五3", "男", "中国", "北京", 20)
# print(p1)
# print(str(p1))
print(p1 < p2)
print(p2 <= p3)
print(p2 == p3)

# 定义一个类，内含私有成员变量和私有成员方法
class Phone:
    __current_voltage = 0.5

    def __keep_single_core(self):
        print("保持单核运行")

    def call_by_5g(self):
        if self.__current_voltage > 1:
            print("通话中")
        else:
            self.__keep_single_core()
            print("电压不足，无法通话")

phone = Phone()
# phone.__keep_single_core() # 报错：AttributeError: 'Phone' object has no attribute '__keep_single_core'
# print(phone.__current_voltage) # 报错：AttributeError: 'Phone' object has no attribute '__current_voltage'
phone.call_by_5g()
