# 
#
# Yunusemre Ozkose
# 20.11.21
#
library(readr)
library("rstudioapi") 

# set current directory as work-directory. R uses /home/username as work-directory.
current_dir = dirname(rstudioapi::getSourceEditorContext()$path)
setwd(current_dir)

# Read data
data_path = "../data/processed/combined_data_normalized.csv"
dataframe <- read_csv(data_path)

