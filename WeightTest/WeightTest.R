
TestWeights<-function(index,weight){

complaints.csv<-read.csv("C:/UF/AQA/Church's chicken/Complians_test/R_all matrices.csv",header = TRUE)# input the fille

ComplaintNames<-c('Appearance/Size Issue','Delivery Issue',	'Foreign Material',	'Mislabeled','Missing Bags','Missing Pieces',	'other','Short Date','Spoilage','Taste Issue','Texture') # make label for each weights

weight_complaints_1<-c(-1.229,0.36,-19.85,82.89,6.19,0.33,-0.46,5.54,-75.59,-60.96,-15)# the vector of weights
weight_complaints_2<-c(0,0,-26.23,51.82,0,0,-0.47,5.6,-60.04,-84.68,-21.91)
weight_complaints_1[index]<-weight
weight_complaints_2[index]<-weight

# The following is to build new columns for changed complaints
complaint_3<-c()
complaint_4<-c()

for(row in 1:14){
    records_each_supplier<-c()
  for(col in 2:12){
    records_each_supplier<-c(records_each_supplier,complaints.csv[row,col])
  }
    complaint_3<-c(complaint_3,(92.26+sum(records_each_supplier*weight_complaints_1))/100.0)# 92.26 is the constant
    complaint_4<-c(complaint_4,(92.84+sum(records_each_supplier*weight_complaints_2))/100.0)
}

# add the new column into the table 
complaints.csv<-data.frame(complaints.csv)
complaints.csv$complaint_3<-complaint_3
complaints.csv$complaint_4<-complaint_4

# simple linear regression
# model_1
model_1<-lm(Score~Test...Pass.Rate+Test...Mean.Deviation+Complaint.Responsiveness+Document.Compliance+complaint_3,data = complaints.csv )
print("Model_1")
print(summary(model_1))
# model_2
model_2<-step(model_1,direction="backward",trace=0)
print("Model_2")
print(summary(model_2))
# model_3
model_3<-lm(Score~Test...Pass.Rate+Test...Mean.Deviation+Complaint.Responsiveness+Document.Compliance+complaint_4,data = complaints.csv )
print("Model_3")
print(summary(model_3))
# model_4
model_4<-step(model_3,direction="backward",trace=0)
print("Model_4")
print(summary(model_4))

}

TestWeights(3,-10)


