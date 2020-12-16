
# Dash packages
import dash_bootstrap_components as dbc
import dash_html_components as html

from app import app


###############################################################################
########### LANDING PAGE LAYOUT ###########
###############################################################################
app.layout = dbc.Container([

        html.H2('Page 1 Layout'),
        html.Hr(),


], className="mt-4")
