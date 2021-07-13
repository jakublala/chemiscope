# -*- coding: utf-8 -*-
from .input import create_input, write_input
from chemiscopeWidget import widget
from traitlets import Unicode
import json
from IPython.display import display as show

def display(frames, properties):
    meta = {'name':' '}
    jsonData = create_input(frames, properties=properties, meta=meta)
    widgetInstance = widget()
    widgetInstance.value = json.dumps(jsonData)
    show(widgetInstance)
    return