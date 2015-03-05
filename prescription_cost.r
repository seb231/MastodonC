setwd('~/Google Drive/Dropbox/Job Applications/2015/MastodonC');
data1<-read.csv("data/drugs.month2",header=F);
data_subset <- subset(data1, V2 == "0404000M0");
colnames(data1) <- c("date", "drug", "amount", "practise", "net_cost", "act_cost");
attach(data1);
dates <- as.Date(as.character(date), format("%Y%m%d"));
par(mfrow=c(1,2));
plot(dates, net_cost, xlab="Date", ylab="Net cost", main="Net cost of ADHD prescriptions over time")
plot(dates, act_cost, xlab="Date", ylab="Actual cost", main="Actual cost of ADHD prescriptions over time");