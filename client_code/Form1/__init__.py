from ._anvil_designer import Form1Template
from anvil import *
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    cr = ['EUR','RON','USD']
    self.ddCurrency.items = cr

    # Any code you write here will run before the form opens.

  def ddCurrency_change(self, **event_args):
    """This method is called when an item is selected"""
    return self.ddCurrency.selected_value

  def btnCalculate_click(self, **event_args):
    """This method is called when the button is clicked"""
    pass

  def costGas_pressed_enter(self, **event_args):
    """This method is called when the user presses Enter in this text box"""
    self.label_8.text = self.costGas.text;
    return {'gas':'{}'.format(self.costGas.text)}
