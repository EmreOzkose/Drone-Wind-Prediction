# 
#
# Yunusemre Ozkose
# 20.11.21
#
library(readr)
library("rstudioapi") 

current_dir = dirname(rstudioapi::getSourceEditorContext()$path)
setwd(current_dir)

data_path = "../data/processed/combined_data_normalized.csv"

dataframe <- read_csv(data_path)
