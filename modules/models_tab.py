import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from common.server import app

class ModelsTab:

	def __init__(self):
		pass

	def getTab():
		return html.Div(children=[
			html.H2('LineChartTab',
				style={
					'margin': '5px'
				})
			])