import cohere
import pandas as pd
import numpy as np
import altair as alt
import textwrap as tr

# set the Cohere client code
api_key = '...' # Paste your API key here. Remember to not share it publicly 
co = cohere.Client(api_key)
