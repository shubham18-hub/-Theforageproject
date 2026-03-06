#Your task is to create a test suite to verify your Dash app is working as expected. Using the standard Dash testing framework (documentation linked in the resources below) write three tests which ensure the following:
#The header is present.
from app import *
def test_header(dash_duo):
  #start app
  dash_duo.start_server(app)
  #Wait for element Header
  header = dash_duo.wait_for_element("#header")
  #check if header is present
  assert header is not None



  
