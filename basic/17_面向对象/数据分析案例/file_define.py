"""
文件相关的类定义
"""
import json
from data_define import Record

# 先定义一个抽象类用来顶层设计，确定有哪些功能需要实现
class FileReader:
    def read_data(self, path) -> list[Record]:
        """读取文件数据，读到的每一条数据都转换为 Record 对象，将它们都封装到 list 内返回即可"""
        pass

class TextFileReader(FileReader):
    def __init__(self, path):
        self.path = path # 定义成员变量记录文件的路径

    # 复写父类的方法
    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        record_list: list[Record] = []
        for line in f.readlines():
            line = line.strip() # 去掉每行首尾的空格
            data_list = line.split(',')
            record = Record(data_list[0], data_list[1], int(data_list[2]), data_list[3])
            record_list.append(record)

        f.close()
        return record_list

class JsonFileReader(FileReader):
    def __init__(self, path):
        self.path = path

    def read_data(self) -> list[Record]:
        f = open(self.path, 'r', encoding='utf-8')
        record_list: list[Record] = []
        for line in f.readlines():
            data_dict = json.loads(line)
            record = Record(data_dict['date'], data_dict['order_id'], int(data_dict['money']), data_dict['province'])
            record_list.append(record)

        f.close()
        return record_list

# 测试代码
if __name__ == '__main__':
    reader = TextFileReader('E:/python-projects/2024data.txt')
    json_reader = JsonFileReader('E:/python-projects/2024json.txt')
    txtData = reader.read_data()
    jsonData = json_reader.read_data()

    for item in txtData:
        print(f"txtData: {item}")

    for item in jsonData:
        print(f"jsonData: {item}")
