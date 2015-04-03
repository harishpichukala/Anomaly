library('DMwR')
dataset=read.csv("H:\\kdd_cup1.csv")
dataset=dataset[1:100,]
outlier.scores<-lofactor(dataset,5)
plot(density(log(outlier.scores)))
outliers<-order(outliers.scores,decreasing=T)[1:5]
print(outliers)
n<-nrow(dataset)
labels<-1:n
labels[-outliers]<-"."
biplot(prcomp(dataset),cex=1.2 xlabs=labels)
pch<-rep(".",n)
pch[outliers]<-"+"
col<-rep("black",n)
col[outliers]<-"red"
pairs(dataset,pch=pch,col=col)