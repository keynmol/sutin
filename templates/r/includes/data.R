
if(!exists("DATA")) {
  DATA <- list(dataset_hello = read.csv("data/hello.csv", stringsAsFactors=F),
               dataset_world =read.csv("data/world.csv", stringsAsFactors=F))
}
