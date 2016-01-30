## PUT YOUR library(..) calls here e.g.
packages <- c("lubridate", "tidyr", "dplyr", "ggplot2")
lapply(packages, function(package) {
  quiet_library <- function(p) suppressWarnings(suppressMessages(library(package=p, character.only = T, quietly=TRUE, logical.return=TRUE)))

  if(!quiet_library(package)){
    cat("Package",package,"was not found, installing it...", "\n")
    install.packages(package)
    quiet_library(p)
  }
})