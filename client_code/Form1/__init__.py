from ._anvil_designer import Form1Template
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def outlined_button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    name = self.text_area_1.text
    weight = int(self.text_area_2.text)
    address = self.text_area_3.text
    personal = self.check_box_1.checked
    anvil.server.call('submit',name=name,weight=weight,personal=personal,address=address)
    Notification("Your Response has been recorded").show()