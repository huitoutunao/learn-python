from typing import Union

# 类型注解

# 基础数据类型注解
var_1: int = 1
var_2: str = "hello"
var_3: bool = True
var_4: float = 3.14

# 类对象类型注解
class Person:
    pass

var_5: Person = Person()

# 基础容器类型注解
my_list: list = [1, 2, 3]
my_tuple: tuple = (1, 2, 3)
my_set: set = {1, 2, 3}
my_dict: dict = {"name": 111, "age": 18}

# 容器类型详细注解
my_list_1: list[int] = [1, 2, 3]
my_tuple_1: tuple[int, str, bool] = (1, "hello", True)
my_set_1: set[int] = {1, 2, 3}
my_dict_1: dict[str, int] = {"name": 111, "age": 18}

# 在注释中进行类型注解
var_6 = "hello" # type: str

# 类型注解的限制

# 函数类型注解
def add(a: int, b: int) -> int:
    return a + b

add(1, 2)

# 联合类型注解

my_list: list[Union[int, str]] = [1, "hello"]

def add_num(a: Union[int, str], b: Union[int, str]) -> Union[int, str]:
    return a + b


# 多态
class Animal:
    def eat(self):
        print("吃")

class Dog(Animal):
    def eat(self):
        print("吃骨头")

class Cat(Animal):
    def eat(self):
        print("吃鱼")

def feed(animal: Animal):
    animal.eat()

dog: Dog = Dog()
cat: Cat = Cat()
feed(dog)
feed(cat)
