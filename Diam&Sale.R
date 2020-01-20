df<-data.frame(read.csv("C:/Users/nalini.agarwala/Downloads/diamonds.csv"))
library(dplyr)
#Que11
dupl_rows<- function(df){
  return(count(distinct(df))-count(df))
}
#Que12
drop_row<- function(df){
  df_new<-na.omit(df,cols="carat")
  df_new<-na.omit(df_new,cols="cut")
  return (df_new)
}
#Que13
sub_numeric <- function(df){
  df_new<-df %>% select_if(is.numeric)
  return (df_new)
}
#Que14
volume<-function(df,x,y,z){
  if(df$depth>80){
    return(x*y*z)
  }
  else{
    return (8)
  }
}

#Que15
impute<-function(df){
  df$price[which(is.na(df$price))]<- mean(df$price,na.rm=T)
  return(df)
}