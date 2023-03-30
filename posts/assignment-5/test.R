library(tidyverse)
library(dplyr)
library(ggplot2)
library(readxl)
library(plotly)
library(viridis)
setwd("/Users/blc/rspace/semester/bcb504/blog/bcb504-blog/posts/assignment-5")

NHLDraft<-read.csv("NHLDraft.csv")
NHLDictionary<-read_excel("NHLDictionary.xlsx")
draft2018<-NHLDraft%>%
  filter(draftyear==2018 & postdraft<6)

drafttot2018 <- draft2018%>%
  group_by(playerId, round, overall, position, name)%>%
  summarise(totgames=sum(NHLgames))

drafttot2018_sorted  <- drafttot2018[order(drafttot2018$round), ]

color_palette <- viridis(length(unique(drafttot2018_sorted$round)))

plot <- plot_ly(drafttot2018_sorted, x = ~name, y = ~totgames, type = "bar", color = ~as.factor(round),
                colors = color_palette)
plot <- plot %>%
  layout(xaxis = list(type = "category", automargin = TRUE),
         margin = list(l = 100),
         title = list(text = paste0('Fig 4.1 Total games for the players',
                                    '<br>',
                                    '<sup>',
                                    'Channel: Position, Mark: Point, Line',
                                    '</sup>')),
         annotations = 
           list(x = 1, y = -0.1, text = "The draft year of 2018", 
                showarrow = F, xref='paper', yref='paper', 
                xanchor='right', yanchor='auto', xshift=0, yshift=-100,
                font=list(size=15, color="black")))%>%
  config(scrollZoom = TRUE)%>%
  layout(xaxis = list(categoryorder = "array", categoryarray = drafttot2018_sorted$name))

ggplotly(plot)