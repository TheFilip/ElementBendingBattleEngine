from characterDB import *
import pandas as pd
import plotly.express as px


def outputStats(a):  
    for i in a:
        mainTitle = f"{i.name} - {i.element} {i.role}"
        df = pd.DataFrame(dict(
            #r=[i.attackStat, i.blockStat, i.bendingStat, i.maneuverStat, i.observeStat],
            r=[i.bendingStat, i.attackStat, i.observeStat, i.maneuverStat, i.blockStat],
            #theta=['Offense', 'Defense', 'Bending', 'Maneuver', 'Vision'],
            theta=['Bending', 'Offense', 'Vision', 'Maneuver', 'Defense'],
        ))
        fig = px.line_polar(df, r='r', theta='theta', line_close=True)
        fig.update_polars(
            radialaxis_tickvals=[0, 20, 40, 60, 80, 100],
            radialaxis_tickmode="array",
            radialaxis_range=[0, 100],
        )
        fig.update_layout(
            font=dict(size=20),
            title=mainTitle,
            title_x=0.5,
        )
        # Add fill to the polar area
        fig.update_traces(fill='toself')  # Added fill='toself'
        fig.show()

    for i in a:
        print(i.name,"-","Offense:",i.attackStat,"Defense:",i.blockStat,"Bending:",i.bendingStat,"Maneuver:",i.maneuverStat,"Vision:",i.observeStat)