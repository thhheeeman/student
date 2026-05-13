1. spark-shell
#-> if sucessfull : Spark context available as 'sc'

2. nano input.txt

3. #Add Sample Data
ERROR Disk failure
INFO System started
WARN Memory low
ERROR Disk failure
INFO Login successful
WARN CPU high


#4. Save file
CTRL + O
ENTER
CTRL + X


#5. Inside spark-shell type:
val inputFile = sc.textFile("input.txt")

#6. **🔹 4. Display File Content**
inputFile.collect.foreach(println)

#7.  5. MapReduce Program (MAIN CODE)
val counts = inputFile
.flatMap(line => line.split(" "))
.map(word => (word,1))
.reduceByKey(_ + _)

#8. Disply Output
counts.collect.foreach(println)


#Save Output
counts.saveAsTextFile("output")


#10. Exit spark Shell
:quit

#11. Now Check output
cd output
ls

#12. Display Result
cat part-00000



#13. Final Code
// Load file
val inputFile = sc.textFile("input.txt")

// Word Count using MapReduce
val counts = inputFile
.flatMap(line => line.split(" "))
.map(word => (word,1))
.reduceByKey(_ + _)

// Display result
counts.collect.foreach(println)

// Save output
counts.saveAsTextFile("output")





#14. Expected output
(ERROR,2)
(INFO,2)
(WARN,2)
(Disk,2)
(failure,2)
(System,1)
(started,1)
(Login,1)
(successful,1)
(CPU,1)
(high,1)
(Memory,1)
(low,1)