library(gganimate)
library(transformr)
# library(magick)
library(gifski)
library(tidyverse)
library(readxl)
library(rnaturalearth)
library(rnaturalearthdata)
library(dplyr)

setwd("/Users/blc/rspace/semester/bcb504/blog/bcb504-blog/posts/Practice-with-Spatial-Data/")
Malaria <- read.csv("National_Unit_data.csv")

Incidence<- Malaria%>%
  filter(Metric == "Infection Prevalence")%>%
  mutate(Prevalence = Value, Year = as.factor(Year))
world_map <- ne_countries(scale = "medium", returnclass = "sf")

map_data <- world_map %>%
  left_join(Incidence, by = c("iso_a3" = "ISO3"))

ggplot() +
  geom_sf(data = map_data%>%
            filter(continent=="Africa"),
          aes(fill = Prevalence)) +
  scale_fill_gradient(low = "white", high = "red", na.value = "gray", name = "Malaria Prevalence") +
  theme_minimal() +
  theme(axis.text = element_blank(), axis.ticks = element_blank(), axis.title = element_blank()) +
  labs(title = "Malaria Prevalence by Country")

p <- ggplot() +
  geom_sf(data = map_data%>%
            filter(continent=="Africa"),
          aes(fill = Prevalence)) +
  scale_fill_gradient(low = "white", high = "red", na.value = "gray", name = "Malaria Prevalence") +
  theme_minimal() +
  theme(axis.text = element_blank(), axis.ticks = element_blank(), axis.title = element_blank()) +
  labs(title = "Malaria Prevalence by Country") +
  transition_states(Year, transition_length = 2, state_length = 2)

animate(p, fps = 25, width = 800, height = 500)