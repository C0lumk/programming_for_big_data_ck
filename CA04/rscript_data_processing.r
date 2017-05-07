
getwd()
setwd("C:/Users/Colum/programming_for_big_data_ck/CA04")

days <- read.csv(file="days.csv",sep="-")
colnames(days) <- c("Year","Month","Day")
days
str(days)
summary(days)
counts <- table(days$Month)
barplot(counts, main="Month Breakdown",xlab="Commits per Month")
counts2 <- table(days$Day)
barplot(counts2, main="Day Breakdown",xlab="Daily Commits",col = 4)

week_days <- read.csv(file = "week_days.csv")
colnames(week_days) <- c("WeekDay")
week_days
str(week_days)
summary(week_days)
counts3 <- table(week_days)
barplot(counts3, main="Week Day Breakdown",xlab="Commits",col = 2)
