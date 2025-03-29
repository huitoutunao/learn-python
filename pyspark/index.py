# pyspark 需要安装 Java 环境，不然运行会报错。

# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")

# 创建SparkContext对象
sc = SparkContext(conf=conf)

# 打印PySpark的版本
print(sc.version)

# 使用SparkContext对象
# rdd = sc.parallelize([1, 2, 3, 4, 5])

# 使用map操作符
# rdd1 = rdd.map(lambda x:x * 2)

# 停止SparkContext对象运行
sc.stop()

