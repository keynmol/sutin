import org.apache.spark.{SparkConf, SparkContext}
import org.apache.log4j.Logger
import org.apache.log4j.Level

object Main {

  def main(args: Array[String]) = {
    implicit val sc: SparkContext = new SparkContext(sparkConf("hello"))

    // quiet you peasants!
    Logger.getLogger("org").setLevel(Level.WARN) 
    Logger.getLogger("akka").setLevel(Level.WARN)


    val x = List("Hello", "from", "Spark", "ya", "filthy", "animal", "!")
    val rdd = sc.parallelize(x)

    rdd.foreach(println)

    sc.stop()
  }

  def sparkConf(task: String) = {
    new SparkConf().setAppName(task).setMaster("local[2]").set("spark.executor.memory", "512M")
  }
}