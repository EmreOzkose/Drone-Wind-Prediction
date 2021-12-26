# 
#
# Yunusemre Ozkose
# 11.12.21
#

library(readr)
library(ggplot2) 
library("rstudioapi") 

set.seed(1234)

# set current directory as work-directory. R uses /home/username as work-directory.
current_dir = dirname(rstudioapi::getSourceEditorContext()$path)
setwd(current_dir)

# Read data
data_path = "../data/processed/combined_data_normalized.csv"
dataframe <- read_csv(data_path)

dataframe

summary(dataframe)

ggplot(dataframe, aes(x=windspeed)) + geom_histogram(binwidth = 0.05) + xlab("windspeed")
ggplot(dataframe, aes(x=h)) + geom_histogram() + xlab("h")
ggplot(dataframe, aes(y=windspeed)) + geom_boxplot() + xlab("") + ylab("windspeed")
ggplot(dataframe, aes(x=h, y=windspeed)) + geom_boxplot() + xlab("h") + ylab("windspeed")

dataframe$h_group <- cut(dataframe$h, breaks = c(-Inf,0.1,0.7,Inf), labels = c("<0.1","0.1-0.7",">0.7"))
ggplot(dataframe, aes(x=h, y=windspeed, color=h_group)) + geom_point()
ggplot(dataframe, aes(x=h, y=windspeed, color=h_group)) + geom_point() + facet_wrap(~ h_group)
