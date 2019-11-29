# DSCI-532_group-203_Lab1-2
Milestones 1 and 2 for DSCI 532

## This this the first milestone project.

Authors:  
* Cari Gostic  
* Roc Zhang  
* Lori Fang  

## Description of the app & sketch  

#### App description:

> Our app contains four plots to help our users learn about the distribution of squirrels in the Central Park. It will enable users to  efficiently plan their visit to the park, either to have more interaction with the squirrels or avoid them (for example, if they were planning a picnic). Additionally, users can find information about where to go to observe a certain behavior of the squirrels.
>
>The first plot on the top-left is a map of the park, with a color gradient filling in each region. The deeper the color, the more squirrels are observed in that region. With this map, the users can directly plan to which part of the park they should go to find more or fewer squirrels. We think this will be really helpful because the users are shown both the region names as well as the location on an actual map. They won't need to look up those region names if they are unfamiliar with the park. 
>
>The bar chart on the bottom-left gives information on the exact amount of squirrels observed in each region of the park during the 2018 Squirrel Census. This bar chart displays explicitly the difference in number of squirrels across park regions. The bars are ordered so that our users can quickly identify the most- and the least-squirrel-populated regions. The bar chart on the top-right shows the difference in the number of squirrels between morning (AM) and afternoon (PM). The value is calculated by `PM` - `AM`, which means positive-value bars (red ones) indicates more squirrels in the afternoon (PM).  
>
>The last plot on the bottom-right gives information about the squirrel behavior throughout the park. Users can choose a behavior of interest in the drop-down menu, and the plot will update accordingly to show the number of observed instances of that behavior in each park area.  
>
>Users can select certain regions by clicking on any of the bar charts, or directly on the map, and all plots will interactively highlight the selected regions (as is shown in the second sketch). 
>

#### Sketch:

![image](https://i.ibb.co/sKKNZzw/Screen-Shot-2019-11-22-at-11-15-11-AM.png)  

> An example of how the plots will interact with user's selection of regions:

![image](https://i.ibb.co/7Vk3qJ0/Screen-Shot-2019-11-22-at-3-11-33-PM.png)  


#### Reflection

- One benefit of our app is that users are allowed to directly click on the map and all the related information in other plots will be highlighted at the same time. This interaction helps efficiently retrieve the information that users need.
- Users are allowed to select multi area for comparing the amount of squirrels in those area by simply press and hold shift and click the area on the map or bars in the chart.
- The squirrels counts bars are sorted in an ascending order from top to bottom, when clicking on the bar, the area will as be highlighted on the map. This function make it easier for the users to find a place in the park where they want to see more or less squirrels.
- One thing that need to be fixed is that the Park Region in y-axis of Squirrel Behaviour by Park Region plot is not in same order as other two bar charts. It took us a while trying to fix it and we even asked TA and Instructor's help but we failed to do so.
- TO BE CONTINUE (I WILL KEEP ADDING COMMENTS TO THIS PART)