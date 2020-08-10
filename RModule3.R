# author: Diana
# date: 8/10/2020

# determine working directory
getwd()

# set a new working directory
setwd("C://Program Files//R")
# and confirm
getwd()


# set back to my working directory
setwd("C://Users//Diana McSpadden//Documents//UVa//Preparation//TechBootCamp/exercises")
# confirm
getwd()

# set the environment langauge to English
Sys.setenv(LANGUAGE = "en")

# using dput to produce a data set
dput(mtcars)

# standard hello world
print('hello world')

# use a built-in function
mean(20:40)
#> 30

# create a random number plot
# load a random num gen and make some random numbers and save them
?rnorm
rnums <- rnorm(10)
print(rnums)

# use a different random package
install.packages("random")
library("random")

?random
rSeq <- randomSequence(min=1, max=20, col=1, check=TRUE)
print(rSeq)

# create a "random" vector
rVector <- c(1,23,45,62,3,57,98,2,43)


# make a histogram
hist(rSeq)
hist(rVector)

