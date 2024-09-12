import json

my_list = [{"name": "John", "age": 30}, {"name": "Jane", "age": 28}]
json_str = json.dumps(my_list, ensure_ascii=False)
print(type(json_str))
print(json_str)

json_obj = json.loads(json_str)
print(type(json_obj))
print(json_obj)

# pyecharts 官网地址 https://pyecharts.org/#/
# pyecharts-gallery 画廊 https://gallery.pyecharts.org/#/

import pyecharts

print(pyecharts.__version__)

bar = pyecharts.charts.Bar()
bar.add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
bar.add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
bar.render("bar.html")
