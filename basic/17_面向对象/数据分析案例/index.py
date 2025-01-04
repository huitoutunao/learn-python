"""
1、设计一个类，可以完成数据的封装。
2、设计一个抽象类，定义文件读取的相关功能，并使用子类实现具体功能。
3、读取文件，生成数据对象。
4、进行数据需求的逻辑计算（计算每一天的销售类型）。
5、通过PyEchart进行图形绘制。
"""

from file_define import FileReader, TextFileReader, JsonFileReader
from data_define import Record
from pyecharts.charts import Bar
from pyecharts.options import *
from pyecharts.globals import ThemeType

txt_reader = TextFileReader('E:/python-projects/2024data.txt')
json_reader = JsonFileReader('E:/python-projects/2024json.txt')

jan_data: list[Record] = txt_reader.read_data()
feb_data: list[Record] = json_reader.read_data()
all_data: list[Record] = jan_data + feb_data

# 计算每一天的销售额
# {"2024-01-01": 100, "2024-01-02": 200, ...}
data_dict = {}
for record in all_data:
    date = record.date
    if date in data_dict:
        data_dict[date] += record.money
    else:
        data_dict[date] = record.money

# 可视化图表
bar = Bar(init_opts=InitOpts(theme=ThemeType.LIGHT))
bar.add_xaxis(list(data_dict.keys()))
bar.add_yaxis("销售额", list(data_dict.values()), label_opts = LabelOpts(is_show=False))
bar.set_global_opts(
    title_opts = TitleOpts(title="每日销售额"),
    xaxis_opts = AxisOpts(axislabel_opts = LabelOpts(rotate=30)),
    yaxis_opts = AxisOpts(axislabel_opts = LabelOpts(formatter="{value} 元")),
)

bar.render("每日销售额柱状图.html")
