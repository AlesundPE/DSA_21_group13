Group 13  
PageRank with PySpark and MPI  
Group member: Yiran Tan (yt270) yt270@scarletmail.rutgers.edu  
  
This project is aimed to implement a MPI approach of PageRank algorithm, in compare with the PySpark approach  
In addition, find the factors that may affect the performance  
  
To compile the project, you must read the following:  
The MPI and PySpark implementations take directed graph file to process  
Thus, various datasets are prepared. Eg. graph10000, contains 10000 page ids with random number of links  
  
To generate a new sample graph, you can run "python GenerateGraph.py" in command line in source directory  
You can customize the number of pages and number of links in the code as shown in comment  
   
To run the PySpark implementation, you need to install PySpark and findspark  
The testing platform is Windows. You may directly download the Apache PySpark package from here:https://spark.apache.org/downloads.html  
You need to modify the code to have a correct path of PySpark  
Findspark can be installed with instruction "pip install findspark"  
When both PySpark and findspark installed, you need to modify the path of reading graph file as shown in code comments  
By default, the program will repartition the joined RDD to 2 partitions, you can modify it in the code  
You can simply run the program with instruction "python PagerankPySpark.py"  
  
To run the MPI implmentation, you need to install a working MPI library, eg. Microsoft MPI:https://www.microsoft.com/en-us/download/details.aspx?id=57467  
Next, you need to install the mpi4py library with the instruction "pip install mpi4py"  
The sample command line instruction to run the program is "mpiexec -n 1 python PagerankMPI.py graph10000"  
Where -n specify the number of workers, in this case, 1 worker is spawned in the execution  
PagerankMPI.py takes the argument of a graph file  
