from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts, TitleOpts

map = Map()

data = [
    ("北京市", 99),
    ("上海市", 80),
    ("广东省", 60),
    ("广西省", 50),
    ("四川省", 40),
]

map.add("测试地图", data, "china")

map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {"min": 1, "max": 30, "label": "1-30", "color": "#313695"},
            {"min": 31, "max": 60, "label": "31-60", "color": "#4575b4"},
            {"min": 61, "max": 99, "label": "61-99", "color": "#74add1"},
        ]
    ),
)

map.render("map.html")
