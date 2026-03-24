# Databricks notebook source
# MAGIC %sql
# MAGIC SELECT * FROM `supplychain`.`sc`.`riskdata2026`;

# COMMAND ----------

from pyspark.sql.functions import col, when, current_timestamp

df_raw = spark.table("supplychain.sc.riskdata2026")

# cleaning data 


df_silver = df_raw.filter(col("Shipment_ID").isNotNull()).withColumn("ingestion_time", current_timestamp())

# save it as silver table 

df_silver.write.format("Delta").mode("overwrite").saveAsTable("supplychain.sc.riskdata2026_silver")
display(df_silver)



# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC DESCRIBE TABLE supplychain.sc.riskdata2026_silver;
# MAGIC
# MAGIC
# MAGIC select *from supplychain.sc.riskdata2026_silver where Lead_Time_Days > 100 

# COMMAND ----------

df_group = df_silver.groupby("Transport_MOde").agg({"Lead_time_days" :"avg" }).orderBy("avg(Lead_time_days)", ascending= False)
display(df_group)

# COMMAND ----------

# DBTITLE 1,Count rows per Weather_Condition
df_wether_count = df_silver.groupBy("Weather_Condition").agg({"Weather_Condition" :  "count"})
display(df_wether_count)

# COMMAND ----------

df_silver.selectExpr("count(distinct Weather_Condition) as unique_weather_count").show()

# COMMAND ----------

display(df_silver)

# COMMAND ----------

# DBTITLE 1,Create Largest_Destination view with top destination
# MAGIC %sql
# MAGIC CREATE OR REPLACE VIEW Largest_Destination AS
# MAGIC SELECT Destination_Port, format_number(sum(Weight_MT), "0,00,000.00") as total_weight
# MAGIC FROM supplychain.sc.riskdata2026_silver
# MAGIC GROUP BY Destination_Port
# MAGIC ORDER BY total_weight DESC
# MAGIC LIMIT 10;
# MAGIC
# MAGIC SELECT * FROM Largest_Destination;

# COMMAND ----------

# MAGIC %sql 
# MAGIC
# MAGIC CREATE OR REPLACE VIEW Category_winner AS
# MAGIC SELECT Product_Category, format_number(sum(Weight_MT), "0,00,000.00") as total_weight
# MAGIC FROM supplychain.sc.riskdata2026_silver
# MAGIC GROUP BY Product_Category
# MAGIC ORDER BY total_weight DESC
# MAGIC ;
# MAGIC
# MAGIC SELECT * FROM Category_winner;
# MAGIC      
# MAGIC

# COMMAND ----------

df_category = spark.read.table("Category_winner")
display(df_category)
df_category.write.format("Delta").mode("overwrite").saveAsTable("supplychain.sc.Category_winner")
