library(readxl)

#####
folderName='Data'
fileName='cities.xlsx'
fileExcel=file.path(folderName,fileName)
dataFromExcel=read_excel(fileExcel,1) # table '1'
str(dataFromExcel)
dataFromExcel
head(dataFromExcel,4) # shows first four rows
dataFromExcel$city

## Practice 1
dataFromExcel[which.max(dataFromExcel$visits2015),] #most visited 2015

##
asiaOnly=dataFromExcel[(dataFromExcel$region=='Asia'),] #least visited in Asia 2013
asiaOnly
asiaOnly[which.min(asiaOnly$visits2013),] 

##  3 least visited cities in Asia 2013
asiaOnly=dataFromExcel[(dataFromExcel$region=='Asia'),] 
asiaOnly
visits2013=asiaOnly[order(asiaOnly$visits2013),]
visits2013
head(visits2013,3) # shows first three rows

## most and least visited city in Asia in 2015
asiaOnly
asiaOnly[which.min(asiaOnly$visits2015),]
asiaOnly[which.max(asiaOnly$visits2015),]

## Practice 2 lOOPS
dataFromExcel
numRows=nrow(dataFromExcel)
numCols=ncol(dataFromExcel)

MostVisited2015=0
for (visits2015 in dataFromExcel$visits2015){
  if (MostVisited2015<visits2015){
    MostVisited2015=visits2015
  }
}
# Then:
MostVisited2015

dataFromExcel[(MostVisited2015$city)]

# part 1

MostVisited2015=0
positionsOfMostVisits15=c()
countMost=0
for (position in 5:numRows){
  visits2015 = dataFromExcel[position,'visits2015']
  if (MostVisited2015<visits2015){
    MostVisited2015=visits2015
  }
}
MostVisited2015
dataFromExcel[positionsOfMostVisits15]

# part 2
for (position in 1:numRows){
  city = dataFromExcel[position,'ages']
  if (oldestAge==age){
    countOldest=countOldest+1
    positionsOfOldest=c(positionsOfOldest,position)
  }
}

