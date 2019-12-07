### Reflection

- One benefit of our app is that users are allowed to directly click on the map and all the related information in other plots will be highlighted at the same time. This interaction helps efficiently retrieve the information that users need.
- Users are allowed to select multi-area for comparing the amount of squirrels in those areas by simply press and hold shift and click the area on the map or bars in the chart.
- The squirrel counts bars are sorted in an ascending order from top to bottom, when clicking on the bar, the area will as be highlighted on the map. This function makes it easier for users to find a place in the park where they want to see more or fewer squirrels.
- One thing that needs to be fixed is that the Park Region in y-axis of Squirrel Behaviour by Park Region plot is not in the same order as other two bar charts. It took us quite a while trying to fix it and we even asked TA and Instructor's help but we failed to do so because there is a bug in Dash that currently has no solution. The graphs plotted in Jupyter lab are correct, but when moved into Dash, the "sort" attribute in alt.Y() doesn't apply correctly.
- We can improve the layout of the four plots by adding the tab function to allow users to choose one plot (to be displayed) at a time.  
- Depending on the screen size of the users, the plots by default might look a bit too big so that the users need to zoom out for the dashboard to look nice as a whole. We are marking this issue for future improvement.

### New reflection from users

#### - Things we decided to work on with:
1. The selection dropdown changes one chart only. This should be made a bit more obvious for users to know.
2. Legend for plot 4 (AM versus PM) could be more clear that blue is AM and red is PM as well as the AM-PM formula.
3. Font sizes could be a bit bigger.
4. Remove the ability to clear selection for the drop-down menu.
5. Add instructions on how to "de-select" bars in a plot.
6. Make app description point-form(make it more noticeable).

#### - Things we decided to work on in the future:
1. Order plot 3 and plot 4 so the y-axes labels match up or the order of the regions could be arranged in ascending or descending for all graphs for better comprehension. 
- This is a bug we've noticed already and it takes very long to fix. We are not expecting to fix it right away.

2. Add scale (km or miles) to see how far different park regions are from one another.
3. Add zoom-in interactivity onto the map.
4. Add a compass to map so the user can orient themselves.
- These are something we need to learn. (Time restraints)

#### - Feedbacks we found not that constructive:
1. Add names to white nondescript regions in the map and add background color (try overlaying plots).
2. The scrolling makes the reader lose focus on what he/she is looking at, maybe have horizontal scrolling instead.
- These are considered not necessary. Horizontal scrolling makes it hard to see four plots at the same time.

#### - Conclusion of feedbacks:
Most of the feedbacks are very constructive. Users overall love the layout of our app but want more descriptions about some functions and more clear stated legend on the plot. Based on the feedbacks we received from our users, we worked on and updated with a much well-organized and orientated app.