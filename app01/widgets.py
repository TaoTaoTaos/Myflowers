# app01/widgets.py

from django.forms.widgets import ClearableFileInput


class MultiFileInput(ClearableFileInput):
    allow_multiple_selected = True
