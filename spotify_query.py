from pyspark.sql import SparkSession #SparkSession is the entry point for programming Spark applications. It let you interact with DataSet and DataFrame APIs provided by Spark.
from pyspark.sql import SQLContext
from sqlalchemy import create_engine
import pandas as pd
from sqlalchemy import exc
import sys

#POSTGRE SQL CONNECTION/ QUERY
def sps_query(engine):
	print('\n* CONNECTED TO POSTGRESQL DATABASE  *')
	query = False
	while not query:
		try:
			query = input('\nQuery >> ')
			pandas_df = pd.read_sql(query, engine)
			pandas_to_sparkdf(pandas_df)
		except exc.ProgrammingError:
			print('\nCheck your query, value not accepted.')
			query = False
		except KeyboardInterrupt:
			print('\nGoodbye!\n')
			sys.exit()

#SPARK DF TO PANDAS DF
def pandas_to_sparkdf(pandas_df):
	spark_df = sps.createDataFrame(pandas_df)
	spark_df.show(spark_df.count(), False)
	export_csv_xlsx(spark_df)

#EXPORT CSV/XLSX
def export_csv_xlsx(spark_df):
	file_export = False
	while not file_export:
		file_export = input('Export Query as csv or xlsx? ').lower()
		if file_export == 'csv':
			pandas_df_2 = spark_df.toPandas()
			file_csv_name = input('File Name (Do not include .csv) >> ')
			pandas_df_2.to_csv(file_csv_name+'.csv', index=False)
		if file_export == 'xlsx':
			file_xlsx_name = input('File Name (Do not include .xlsx) >> ')
			spark_df.toPandas().to_excel(file_xlsx_name+'.xlsx', sheet_name=file_xlsx_name, index = False)

#SPARKSESSION CREATION/SQLALCHEMY ENGINE
if __name__ == '__main__':
	sps = SparkSession.builder.appName('Spotify db query').getOrCreate()
	engine = create_engine('postgresql+psycopg2://', connect_args = {"sslmode" : "allow"})
	sps_query(engine)
