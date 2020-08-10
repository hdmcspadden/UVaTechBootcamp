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


