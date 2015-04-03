library(e1071)
dataset <- read.csv('kdd_cup_test_1.csv',head=FALSE)
index <- 1:nrow(dataset)
testindex <- sample(index, trunc(length(index)*30/100))
testset <- dataset[testindex,]
trainset <- dataset[-testindex,]
sink("summary_svm.txt")
model <- svm(V42~., data = trainset)
summary(model)
prediction <- predict(model, testset[,-42])
tab <- table(actual = testset[,42],predictions=prediction)
tn<-tab[1,1]
cat("tn")
tn
cat("fp")
fp<-tab[1,2]
fp
cat("fn")
fn<-tab[2,1]
fn
cat("tp")
tp<-tab[2,2]
tp