R Markdown
----------

This is an R Markdown document. Markdown is a simple formatting syntax for authoring HTML, PDF, and MS Word documents. For more details on using R Markdown see <http://rmarkdown.rstudio.com>.

When you click the **Knit** button a document will be generated that includes both content as well as the output of any embedded R code chunks within the document. You can embed an R code chunk like this:

``` r
library(readxl)

#####
folderName='Data'
fileName='cities.xlsx'
fileExcel=file.path(folderName,fileName)
dataFromExcel=read_excel(fileExcel,1) # table '1'
str(dataFromExcel)
```

    ## Classes 'tbl_df', 'tbl' and 'data.frame':    11 obs. of  4 variables:
    ##  $ city      : chr  "Bangkok" "Dubai" "Hong Kong" "Istanbul" ...
    ##  $ region    : chr  "Asia" "Asia" "Asia" "Europe" ...
    ##  $ visits2013: num  15.98 9.89 8.72 10.37 9.2 ...
    ##  $ visits2015: num  18.24 14.26 8.66 12.56 11.12 ...

``` r
dataFromExcel
```

    ##            city  region visits2013 visits2015
    ## 1       Bangkok    Asia      15.98      18.24
    ## 2         Dubai    Asia       9.89      14.26
    ## 3     Hong Kong    Asia       8.72       8.66
    ## 4      Istanbul  Europe      10.37      12.56
    ## 5  Kuala Lumpur    Asia       9.20      11.12
    ## 6        London  Europe      15.96      18.82
    ## 7      New York America      11.52      12.27
    ## 8         Paris  Europe      13.92      16.06
    ## 9         Seoul    Asia         NA      10.35
    ## 10    Singapore    Asia      11.75      11.88
    ## 11    Barcelona  Europe       8.41         NA

``` r
head(dataFromExcel,4) # shows first four rows
```

    ##        city region visits2013 visits2015
    ## 1   Bangkok   Asia      15.98      18.24
    ## 2     Dubai   Asia       9.89      14.26
    ## 3 Hong Kong   Asia       8.72       8.66
    ## 4  Istanbul Europe      10.37      12.56

``` r
dataFromExcel$city
```

    ##  [1] "Bangkok"      "Dubai"        "Hong Kong"    "Istanbul"    
    ##  [5] "Kuala Lumpur" "London"       "New York"     "Paris"       
    ##  [9] "Seoul"        "Singapore"    "Barcelona"

``` r
## Practice 1
dataFromExcel[which.max(dataFromExcel$visits2015),] #most visited 2015
```

    ##     city region visits2013 visits2015
    ## 6 London Europe      15.96      18.82

``` r
##
asiaOnly=dataFromExcel[(dataFromExcel$region=='Asia'),] #least visited in Asia 2013
asiaOnly
```

    ##            city region visits2013 visits2015
    ## 1       Bangkok   Asia      15.98      18.24
    ## 2         Dubai   Asia       9.89      14.26
    ## 3     Hong Kong   Asia       8.72       8.66
    ## 5  Kuala Lumpur   Asia       9.20      11.12
    ## 9         Seoul   Asia         NA      10.35
    ## 10    Singapore   Asia      11.75      11.88

``` r
asiaOnly[which.min(asiaOnly$visits2013),] 
```

    ##        city region visits2013 visits2015
    ## 3 Hong Kong   Asia       8.72       8.66

``` r
##  3 least visited cities in Asia 2013
asiaOnly=dataFromExcel[(dataFromExcel$region=='Asia'),] 
asiaOnly
```

    ##            city region visits2013 visits2015
    ## 1       Bangkok   Asia      15.98      18.24
    ## 2         Dubai   Asia       9.89      14.26
    ## 3     Hong Kong   Asia       8.72       8.66
    ## 5  Kuala Lumpur   Asia       9.20      11.12
    ## 9         Seoul   Asia         NA      10.35
    ## 10    Singapore   Asia      11.75      11.88

``` r
visits2013=asiaOnly[order(asiaOnly$visits2013),]
visits2013
```

    ##            city region visits2013 visits2015
    ## 3     Hong Kong   Asia       8.72       8.66
    ## 5  Kuala Lumpur   Asia       9.20      11.12
    ## 2         Dubai   Asia       9.89      14.26
    ## 10    Singapore   Asia      11.75      11.88
    ## 1       Bangkok   Asia      15.98      18.24
    ## 9         Seoul   Asia         NA      10.35

``` r
head(visits2013,3) # shows first three rows
```

    ##           city region visits2013 visits2015
    ## 3    Hong Kong   Asia       8.72       8.66
    ## 5 Kuala Lumpur   Asia       9.20      11.12
    ## 2        Dubai   Asia       9.89      14.26

``` r
## most and least visited city in Asia in 2015
asiaOnly
```

    ##            city region visits2013 visits2015
    ## 1       Bangkok   Asia      15.98      18.24
    ## 2         Dubai   Asia       9.89      14.26
    ## 3     Hong Kong   Asia       8.72       8.66
    ## 5  Kuala Lumpur   Asia       9.20      11.12
    ## 9         Seoul   Asia         NA      10.35
    ## 10    Singapore   Asia      11.75      11.88

``` r
asiaOnly[which.min(asiaOnly$visits2015),]
```

    ##        city region visits2013 visits2015
    ## 3 Hong Kong   Asia       8.72       8.66

``` r
asiaOnly[which.max(asiaOnly$visits2015),]
```

    ##      city region visits2013 visits2015
    ## 1 Bangkok   Asia      15.98      18.24

``` r
## Practice 2 lOOPS
#dataFromExcel
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
```

``` r
# part 1
numRows=nrow(dataFromExcel)
numCols=ncol(dataFromExcel)

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
```

``` r
# part 2
for (position in 1:numRows){
  city = dataFromExcel[position,'ages']
  if (oldestAge==age){
    countOldest=countOldest+1
    positionsOfOldest=c(positionsOfOldest,position)
  }
}
```

``` r
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
```
