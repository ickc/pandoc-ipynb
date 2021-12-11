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
import matplotlib.pyplot as plt

# %%
# %config InlineBackend.figure_formats = ['pdf']

# %%
x = np.linspace(0, np.pi)
y = np.sin(x)

# %%
plt.plot(x, y)
