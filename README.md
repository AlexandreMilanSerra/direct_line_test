# Project files

 The project's folders contains the following files:

    1 - '*.csv' files with the input data
    2 - 'Data Engineer Python Test.pdf' with test question
    3 - 'weather_data_processing.py' script contains a few functions which using the pyspark framework does the work asked on the test pdf file:
        
        - 'csv_to_parquet' function converts the input csv files into parquet files. It automatically create the spark context and read/write the files
        - 'hottest_day' function queries the parquet files and prints the hottest day among all the data. It automatically create the spark context and run the Spark SQL queries.
        - 'hottest_temperature' function queries the parquet files and prints the hottest temperature among all the data. It automatically create the spark context and run the Spark SQL queries.
        - 'hottest_region' function queries the parquet files and prints the hottest region among all the data. It automatically create the spark context and run the Spark SQL queries.

    4 - 'README.md' file with some intructions

# Prerequisites 

0 - We are using the python3.7 version. From the following link you can donwload it and install it:

    https://www.python.org/downloads/release/python-378/
       

1 - You need to have 
installed java and spark and configure the environment variables. 

Open the terminal.


Java installation:

    >>brew install java

Spark installation:

    >>brew install spark


Launch the bash_profile:

    >>open .bash_profile

Environment variables configuration:

    PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
    export PATH=/usr/local/bin:/usr/local/sbin:$PATH
    export SPARK_LOCAL_HOSTNAME=localhost

    # Setting PATH for Python 3.7
    # The original version is saved in .bash_profile.pysave

    PATH="/Library/Frameworks/Python.framework/Versions/3.7/bin:${PATH}"
    export PATH

    PYSPARK_PYTHON="/usr/bin/python3.7"
    PYSPARK_DRIVER_PYTHON="/usr/bin/python3.7"

    JAVA_HOME "/Library/Java/JavaVirtualMachines/jdk1.8.0_241.jdk/Contents/Home"
    SPARK_HOME "/SPARK_HOME=/usr/local/Cellar/apache-spark/2.4.5/libexec"

# Usage
0 - Clone the repository:

    >>git clone https://github.com/AlexandreMilanSerra/direct_line_test.git
    
1 - change to project directory 

    >>cd /PathToYourDirectory

2 - Install the requirements of this project:

    >>pip3 install -r requirements.txt
   
3 - Copy the raw data from the source folder into the project folder. For security reasons the weather data is not stored on the repository.
    
    >>cp <source folder>/weather.20160201.csv <target folder>/weather.20160201.csv
    >>cp <source folder>/weather.20160301.csv <target folder>/weather.20160301.csv

4 - Launch python3:

    >>python3

5 - Change the working directory to your project folder where the .py script and the raw data are placed:

    >>import os
    >>os.chdir('PathToYourDirectory/direct_line_test')
 
6 - Import the functions:
    
    >>from weather_data_processing import *
 
7 - Now you can convert the csv files into parquet files

    >>csv_to_parquet()
   
8 - Once you get your parquet files you can query them launching either of the following functions

    >>hottest_day()
    >>hottest_temperature()
    >>hottest_region()