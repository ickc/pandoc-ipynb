# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.3
#   kernelspec:
#     display_name: all39-defaults
#     language: python
#     name: all39-defaults
# ---

# %%
import numpy as np
from bokeh.plotting import figure, show
from bokeh.io import output_notebook

# %%
output_notebook()

# %%
x = np.linspace(0, np.pi)
y = np.sin(x)

# %%
p = figure()
p.line(x, y)
show(p)
