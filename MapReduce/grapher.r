install.packages('ggplot2')
library(ggplot2)
dat <- read.csv(file="1999_words.txt", header=F, sep="\t")
dat
#attach(dat)
words <- dat[1]
words
count <- dat[2]
count
ggplot(data=dat, aes(x=words, y=count)) +
    geom_bar(stat="identity")