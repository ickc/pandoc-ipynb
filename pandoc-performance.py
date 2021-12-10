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
from copy import deepcopy
import timeit
import json
from pathlib import Path
from functools import partial

from panflute import convert_text
import numpy as np
import plotly.express as px
import pandas as pd
import statsmodels.api as sm
from map_parallel import map_parallel

# %%
# pandoc commit 6b962e6b0e729e925c4313427926cc6bfc5d3d1f
pandoc_path = Path("~/.local/bin/pandoc").expanduser()
# input ipynb
path = Path("holoview-load-only-manual_filtered.ipynb").expanduser()

# %%
# !$pandoc_path --version

# %%
with path.open("r") as f:
    data = json.load(f)

# %%
n_original = len(data["cells"][0]["outputs"][0]["data"]["application/vnd.holoviews_load.v0+json"])
n_original

# %%
data["cells"][0]["outputs"][0]["data"]["application/vnd.holoviews_load.v0+json"] = '"'


# %%
def cook_new_data(data, n):
    res = deepcopy(data)
    res["cells"][0]["outputs"][0]["data"]["application/vnd.holoviews_load.v0+json"] = '"' * n
    return res


# %%
def timethis(
    data,
    n,
    number=1,
    repeat=1,
):
    return np.mean(
        timeit.repeat(
            'convert_text(text, input_format="ipynb", output_format="native", pandoc_path=pandoc_path)',
            setup='import json; from panflute import convert_text; text = json.dumps(cook_new_data(data, n))',
            globals={"data": data, "n": n, "cook_new_data": cook_new_data, "pandoc_path": pandoc_path},
            number=number,
            repeat=repeat,
        )
    )


# %%
N = 18
n = 2**np.arange(1, N)

# %%
res = map_parallel(partial(timethis, data), n, mode="multithreading", processes=len(n))

# %%
df = pd.DataFrame(
    {
        "n": n,
        "time (s)": res,
    }
)

# %%
df

# %%
df.plot(backend="plotly", x="n", y="time (s)", log_x=True, log_y=True)

# %%
df_fit = df.iloc[10:]

# %% [markdown]
# $$t = A n^x$$
#
# $$\log t = C + x \log n$$

# %%
X = sm.add_constant(np.log(df_fit["n"]))
y = np.log(df_fit["time (s)"])
model = sm.OLS(y, X)
results = model.fit()
results.summary()

# %% [markdown]
# Predicted time

# %%
np.exp(results.params.const + results.params.n * np.log(n_original))
