# -*- coding: utf-8 -*-
from pyspark.sql import SparkSession
import os

def create_context():
    spark = SparkSession.builder.master("local").appName("directline_test").config("spark.some.config.option").getOrCreate()
    return spark

def csv_to_parquet():
    spark= create_context()
    for currFile in os.listdir():
        if os.path.splitext(currFile)[1]=='.csv':
            data = spark.read.format("csv").options(delimiter = ',',header=True,inferSchema=True).load(os.getcwd()+"/"+currFile)
            data.write.parquet(os.getcwd()+"/"+os.path.splitext(currFile)[0]+'.parquet')

def read_parquet_files():
    spark = create_context()
    df=spark.read.parquet(os.getcwd()+"/"+"*.parquet")
    df.registerTempTable("wheather")

def hottest_day():
    spark = create_context()
    read_parquet_files()
    print('the hottest day was:')
    stats = spark.sql('select ObservationDate from wheather where ScreenTemperature= (select max(ScreenTemperature) from wheather)')
    stats.show()

def hottest_temperature():
    spark = create_context()
    read_parquet_files()
    print('the hottest temperature was:')
    stats = spark.sql('select max(ScreenTemperature) from wheather')
    stats.show()

def hottest_region():
    spark = create_context()
    read_parquet_files()
    print('the hottest region was:')
    stats = spark.sql('select Region from wheather where ScreenTemperature= (select max(ScreenTemperature) from wheather)')
    stats.show()




