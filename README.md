# API-Data-Visualization
- Using data from APIs to generate visualizations via Python for data analysis.
- Visualizations are created with Plotly, and Matplotlib packages.

## Using Data
- First install [plotly](https://plotly.com/python/), [matplotlib](https://matplotlib.org/), and [chart-studio](https://plotly.com/python/chart-studio/) packages via pip package manager.


`python3 -m pip install --user plotly`

`python3 -m pip install --user matplotlib`

`python3 -m pip install --user chart-studio`

- Once you have those installed, simply copy/paste code into your editor of choice and run from there.

- If you wanted to search for data on another language other than Python simply change your query

IE: 
We want to search for most starred C repos.

`https://api.github.com/search/repositories?q=language:python&sort=stars` changes to `https://api.github.com/search/repositories?q=language:c&sort=stars`

