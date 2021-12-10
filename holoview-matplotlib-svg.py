# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.1
#   kernelspec:
#     display_name: all39-defaults
#     language: python
#     name: all39-defaults
# ---

# %%
import holoviews as hv
import numpy as np

hv.extension("matplotlib")
hv.output(fig='svg')

# %%
x = np.linspace(0, np.pi)

# %%
y = np.sin(x)

# %%
hv.Curve(np.column_stack((x, y)))
