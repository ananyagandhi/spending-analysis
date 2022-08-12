# spending.py
# aim to analyze financial data from venmo and credit card 

import pandas as pd
import numpy as np
from datetime import datetime
#import plotly.express as px
#import plotly.graph_objecst as go
#from jupyter_dash import JupyterDash
#import dash_core_components as dcc
#import dash_html_components as html

venmo = pd.read_csv('data/merged-venmo.csv')
print(venmo.head())
