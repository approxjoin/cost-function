for i in {1..9};do

    spark-submit --master spark://stream10:7077  --conf spark.driver.maxResultSize=6g   --conf spark.network.timeout=10000000 --executor-memory 6g --executor-cores 8 --driver-memory 6g  --class "CostFunction" target/scala-2.11/approxjoin-assembly-1.0.jar stream10 /inputa.txt /inputb.txt 0.113543 72 &> costfunction.txt.200s.$i;

    spark-submit --master spark://stream10:7077  --conf spark.driver.maxResultSize=6g   --conf spark.network.timeout=10000000 --executor-memory 6g --executor-cores 8 --driver-memory 6g  --class "CostFunction" target/scala-2.11/approxjoin-assembly-1.0.jar stream10 /inputa.txt /inputb.txt 0.390476 72 &> costfunction.txt.400s.$i;

    spark-submit --master spark://stream10:7077  --conf spark.driver.maxResultSize=6g   --conf spark.network.timeout=10000000 --executor-memory 6g --executor-cores 8 --driver-memory 6g  --class "CostFunction" target/scala-2.11/approxjoin-assembly-1.0.jar stream10 /inputa.txt /inputb.txt 0.667410 72 &> costfunction.txt.600s.$i;

    spark-submit --master spark://stream10:7077  --conf spark.driver.maxResultSize=6g   --conf spark.network.timeout=10000000 --executor-memory 6g --executor-cores 8 --driver-memory 6g  --class "CostFunction" target/scala-2.11/approxjoin-assembly-1.0.jar stream10 /inputa.txt /inputb.txt 0.944344 72 &> costfunction.txt.800s.$i;

done
