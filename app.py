import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import altair as alt
import pandas as pd
import json




app = dash.Dash(__name__, assets_folder='assets')
server = app.server

app.title = 'Dash app with pure Altair HTML'

## add magic
def make_plot(y_axis = 'Running_or_Chasing'):
   
    # Create a plot of the Displacement and the Horsepower of the cars dataset
    def mds_special():
        font = "Arial"
        axisColor = "#000000"
        gridColor = "#DEDDDD"
        return {
            "config": {
                "title": {
                    "fontSize": 24,
                    "font": font,
                    "anchor": "start", # equivalent of left-aligned.
                    "fontColor": "#000000"
                },
                'view': {
                    "height": 300, 
                    "width": 400
                },
                "axisX": {
                    "domain": True,
                    #"domainColor": axisColor,
                    "gridColor": gridColor,
                    "domainWidth": 1,
                    "grid": False,
                    "labelFont": font,
                    "labelFontSize": 12,
                    "labelAngle": 0, 
                    "tickColor": axisColor,
                    "tickSize": 5, # default, including it just to show you can change it
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "X Axis Title (units)", 
                },
                "axisY": {
                    "domain": False,
                    "grid": True,
                    "gridColor": gridColor,
                    "gridWidth": 1,
                    "labelFont": font,
                    "labelFontSize": 14,
                    "labelAngle": 0, 
                    #"ticks": False, # even if you don't have a "domain" you need to turn these off.
                    "titleFont": font,
                    "titleFontSize": 16,
                    "titlePadding": 10, # guessing, not specified in styleguide
                    "title": "Y Axis Title (units)", 
                    # titles are by default vertical left of axis so we need to hack this 
                    #"titleAngle": 0, # horizontal
                    #"titleY": -10, # move it up
                    #"titleX": 18, # move it to the right so it aligns with the labels 
                },
            }
                }

    # register the custom theme under a chosen name
    alt.themes.register('mds_special', mds_special)

    # enable the newly registered theme
    alt.themes.enable('mds_special')
    #alt.themes.enable('none') # to return to default    
    
    # load the data
    with open('data/b_json_count.json') as data_file:
        b_json_count = json.load(data_file)
    squirrel_b_json = alt.Data(values = b_json_count['features'])

    with open('data/alt_json_count.json') as data_file:
        alt_json_count = json.load(data_file)
    alt_base_layer_data_count = alt.Data(values = alt_json_count['features'])

    # make the plot
    
    ##################################
    # PLOT MAP of SQUIRREL COUNT
    ##################################

    def plot_map_total_count(selection):
        # Plot of squirrel count
        base_map = alt.Chart(alt_base_layer_data_count).mark_geoshape(
            stroke='black',
            strokeWidth=1
        ).encode(
        ).properties(
            width=400,
            height=600
        )

        # Add Choropleth Layer
        choropleth = (alt.Chart(alt_base_layer_data_count, 
                                title = "Central Park Squirrel Distribution: 2018 Census")
        .mark_geoshape()
        .add_selection(selection)
        .encode(
        # SELECTION SINGLE CONDITIONS -- Color is grey if not selected
            color = alt.condition(selection, 
                                'properties.Unique_Squirrel_ID:Q', 
                                alt.value('grey'),
                title = 'Squirrel Count',
                scale=alt.Scale(scheme='greens'),
                legend = alt.Legend(labelFontSize = 16, 
                                    titleFontSize = 20, 
                                    tickCount = 5,
                                orient = "top-left", direction = "vertical")),
            opacity=alt.condition(selection, 
                                alt.value(0.8), 
                                alt.value(0.1)),
            tooltip = [alt.Tooltip('properties.sitename:N', 
                                title="Park Region"), 
                alt.Tooltip('properties.Unique_Squirrel_ID:Q', 
                            title="Squirrel Count")]
        ))
        
        return(base_map + choropleth)

    # Sort data by squirrel count to display sites in ascending order
    sort_order = ["Mariner's Gate Plgd", 'Bernard Plgd', 'T.C.T Plgd', 'Bendheim Plgd', 'J.M.L. Plgd', 
        'Res. Running Track', 'P.H.F. Plgd', '110th St. Plgd', 'Heckscher Plgd', 'Cons. Garden', 
        'Northwest Corner', 'Reservoir SE', 'Strawberry Fields', "Frawleys' Run", 'The Great Hill', 
        "Nutter's Battery", 'The Met', 'Wollman Rink', 'Summit Rock', 'Pilgrim Hill', 'Wien Walk', 
        'Reservior NE', 'Turtle Pond Area', 'Central Park W (Z-1)', 'Carousel Area', 'E Meadow', 
        'Central Park W (Z-4)', 'N of the Arsenal', 'Cedar Hill', 'Cons. Gardens W.', 'Hallett Nat. Sanc.', 
        'Central Park W (Z-3)', 'Central Park W (Z-2)', 'Loch Ravine', 'Wallach Walk', 'Reservoir NW', 
        'N Meadow Rec. Ctr.', 'Ross Pinetum', 'Great Lawn', 'Central Park S.', 'Blockhouse One', 'Sheep Meadow', 
        'The Mall', 'N Meadow', 'The Pool', 'Bethesda Terrace', 'Hecksher Ballfields', 'The Ramble']

    ##########################################
    # PLOT TOTAL SQUIRREL COUNT
    ##########################################
    def plot_bar_total_count(selection):
        count_bar = (alt.Chart(alt_base_layer_data_count, 
                            title = 'Squirrel Count by Park Region')
        .mark_bar()
        .add_selection(selection)
        .encode(
            x = alt.X('properties.Unique_Squirrel_ID:Q', 
                    title = "Squirrel Count", 
                    axis = alt.Axis(labelFontSize = 16, 
                                    titleFontSize = 20)),
            y = alt.Y('properties.sitename_short:N', 
                    title = "Park Region", 
                    axis = alt.Axis(labelFontSize = 12,
                                    titleFontSize = 20), 
                    sort = sort_order),
            color = alt.Color('properties.Unique_Squirrel_ID:Q',
                            scale=alt.Scale(scheme='greens')),

        # SELECTION SINGLE CONDITIONS -- opacity is 0.2 if not selected
            opacity = alt.condition(selection, 
                                    alt.value(1.0), 
                                    alt.value(0.2)),
            tooltip = [alt.Tooltip('properties.sitename:N', 
                                title="Park Region"), 
                alt.Tooltip('properties.Unique_Squirrel_ID:Q', 
                            title="Squirrel Count")])
        .properties(width = 400, height = 600))   
        return(count_bar)

    ################################################
    # PLOT DIFFERENCE in COUNT by TIME OF DAY
    ################################################
    def plot_bar_count_diff(selection):
        area_count_shift = (alt.Chart(alt_base_layer_data_count)
        .mark_bar()
        .add_selection(selection)
        .encode(
            alt.X('properties.Count_difference:Q', 
                title = "Count Difference (PM - AM)", 
                axis = alt.Axis(labelFontSize = 16, 
                                titleFontSize = 20)),
            alt.Y('properties.sitename_short:N',
                axis = alt.Axis(labelFontSize = 12,
                                titleFontSize = 20), 
                title = "Park Region",
                sort = sort_order),
            opacity = alt.condition(selection, 
                                    alt.value(1.0), 
                                    alt.value(0.2)),
            color=alt.condition(
                # If count is negative, color bar blue. If positive, red.
                alt.datum['properties.Count_difference'] > 0,
                alt.value("darkred"),  # The positive color
                alt.value("steelblue")  # The negative color
            ),
            tooltip = [alt.Tooltip('properties.sitename:N', title="Park Region"), 
                    alt.Tooltip('properties.Count_difference:Q', title="Count difference")]
        ).properties(title = "Squirrel Count by Park Region: AM vs. PM",
                    width = 400,
                    height = 600))
        return(area_count_shift)


    ###################################
    # PLOT BEHAVIOR by PARK AREA
    ###################################
    def plot_bar_behavior(selection, y_axis = y_axis):
        #b = ['Running or Chasing', 'Climbing', 'Eating or Foraging', 'Vocalizing', 'Approaches Humans']
        #b_dropdown = alt.binding_select(options=b)
        #b_select = alt.selection_single(fields=['properties.behavior'], 
        #                                bind = b_dropdown, name="Squirrel", 
        #                                init = {'properties.behavior' : 'Running or Chasing'})

        b_chart = (alt.Chart(squirrel_b_json)
            .mark_bar(color = 'gray')
            #.add_selection(b_select)
            .add_selection(selection)
            .encode(alt.X('properties.'+y_axis+':Q', 
                          title = "Squirrel Count", axis = alt.Axis(labelFontSize = 18, titleFontSize = 20)),
                
                alt.Y('properties.sitename_short:N', 
                          title = "Park Region", axis = alt.Axis(labelFontSize = 12, titleFontSize = 20),
                          sort = sort_order), 
                    opacity = alt.condition(brush, 
                                        alt.value(1.0), 
                                        alt.value(0.2)),
                    tooltip = [alt.Tooltip('properties.sitename:N', title = "Park Region"), 
                            alt.Tooltip('properties.b_count:Q', title = y_axis)]
                )
            #.transform_filter(b_select)
            .properties(title = "Squirrel Behavior by Park Region: "+y_axis,
                        width = 400,
                        height = 600))
        return b_chart


    # Create selection conditions and link plots by setting resolve = 'global'
    brush = alt.selection_multi(fields = ['properties.sitename_short'],
        resolve='global'
    )


    # Render stacked plots
    chart = ((plot_map_total_count(brush) | plot_bar_total_count(brush)) & (plot_bar_count_diff(brush) | plot_bar_behavior(brush, y_axis))).configure_title(fontSize = 24)

    # source (code): https://www.districtdatalabs.com/altair-choropleth-viz

    return chart
## add magic

app.layout = html.Div([

    ### ADD CONTENT HERE like: html.H1('text'),
    html.H1("Welcome to Squirrle Park App!!"),
    html.H2("Add some description or user guidance?"),
    html.H2("We'll need to resize the plots for it to fit well in the page."),

    html.Iframe(
        sandbox='allow-scripts',
        id='plot',
        height='2000',
        width='2000',
        style={'border-width': '0px'},

        ################ The magic happens here
        srcDoc = make_plot().to_html()
        ################ The magic happens here
    ),

    dcc.Dropdown(
    id='dd-chart',
    # ['Running or Chasing', 'Climbing', 'Eating or Foraging', 'Vocalizing', 'Approaches Humans']
    options=[
        {'label': 'Running or Chasing', 'value': 'Running_or_Chasing'},
        {'label': 'Climbing', 'value': 'Climbing'},
        {'label': 'Eating or Foraging', 'value': 'Eating_or_Foraging'},
        {'label': 'Vocalizing', 'value': 'Vocalizing'},
        {'label': 'Approaches Humans', 'value': 'Approaches Humans'},
        # Missing option here
    ],
    value='Running_or_Chasing',
    style=dict(width='45%',
            verticalAlign="middle")
    ),
    # html.Img(src='https://i.ibb.co/GcC3tpM/MG-0084-2.jpg')
    html.H2("Maybe we want to create some space here so that the drop_down menu is more noticeable.")

])

@app.callback(
    dash.dependencies.Output('plot', 'srcDoc'),
    [dash.dependencies.Input('dd-chart', 'value')])

def update_plot(yaxis_column_name):
    '''
    Takes in an xaxis_column_name and calls make_plot to update our Altair figure
    '''
    updated_plot = make_plot(yaxis_column_name).to_html()
    return updated_plot


if __name__ == '__main__':
    app.run_server(debug=True)
