# Databricks notebook source
# MAGIC %md
# MAGIC #### 1.What is Data Stream?
# MAGIC
# MAGIC *  Any data source that grows over time
# MAGIC *  New files landing in cloud storage
# MAGIC *  Updates to a database captured in a CDC feed
# MAGIC *  Events queued in a pub/sub messaging feed

# COMMAND ----------

#dbutils.fs.mkdirs("dbfs:/FileStore/streaming/")

# COMMAND ----------

dbutils.fs.ls("dbfs:/FileStore/streaming/")

# COMMAND ----------

from pyspark.sql.types import StructType, StructField, StringType , IntegerType, FloatType

schema = StructType([   
                     StructField('Country',StringType()),
                     StructField('Citizens',IntegerType())
])

# COMMAND ----------

source_dir = 'dbfs:/FileStore/streaming/'

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC CREATE SCHEMA IF NOT EXISTS  stream;
# MAGIC --use stream

# COMMAND ----------

df = spark.readStream.format("csv")\
        .option('header','true')\
        .schema(schema)\
        .load(source_dir)

# COMMAND ----------

display(df)

# COMMAND ----------

 WriteStream = ( df.writeStream
        .option('checkpointLocation',f'{source_dir}/AppendCheckpoint')
        .outputMode("append")
        .queryName('Query1')
        .toTable("stream.AppendTable"))

# COMMAND ----------

dbutils.fs.rm("dbfs:/user/hive/warehouse/stream.db/appendtable",True)

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT * FROM stream.AppendTable

# COMMAND ----------

WriteStream.stop()

# COMMAND ----------


