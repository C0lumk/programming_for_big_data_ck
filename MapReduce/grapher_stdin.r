library(ggplot2)
dat <- read.csv(file="stdin", header=TRUE, sep=",")
dat
ggplot(data=dat, aes(x=Words, y=Count)) +
    geom_bar(stat="identity")