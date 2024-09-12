from pyecharts.charts import Bar, Timeline
from pyecharts.options import LabelOpts
from pyecharts.globals import ThemeType

bar1 = Bar()
bar1.add_xaxis(["中国", "美国", "日本"])
bar1.add_yaxis("GDP", [30, 20, 10], label_opts=LabelOpts(position="right"))
bar1.reversal_axis()

bar2 = Bar()
bar2.add_xaxis(["中国", "美国", "日本"])
bar2.add_yaxis("GDP", [40, 30, 20], label_opts=LabelOpts(position="right"))
bar2.reversal_axis()

bar3 = Bar()
bar3.add_xaxis(["中国", "美国", "日本"])
bar3.add_yaxis("GDP", [50, 40, 30], label_opts=LabelOpts(position="right"))
bar3.reversal_axis()

timeline = Timeline(
    { "theme": ThemeType.LIGHT }
)
timeline.add(bar1, "2020年")
timeline.add(bar2, "2021年")
timeline.add(bar3, "2022年")

timeline.add_schema(
    is_timeline_show=True,
    is_loop_play=True,
    is_auto_play=True,
    play_interval=1000,
)

timeline.render("timelinebar.html")
