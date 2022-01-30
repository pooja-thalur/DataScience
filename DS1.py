%load_ext rpy2.ipython #to run R code on python codelab

%%R
install.packages("dslabs")
library(dslabs)
data(movielens)
data(movielens)
str(movielens)
class(movielens$title)
nlevels(movielens$genres)