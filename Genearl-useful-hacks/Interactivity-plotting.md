## 2. Bringing Interactivity to pandas plots

**Pandas** has a built-in `.plot()` function as part of the DataFrame class. However, the visualisations rendered with this function aren't interactive and that makes it less appealing.

Ofcourse the ease to plot charts with `pandas.DataFrame.plot()` function is something to be considered. So what if we could plot interactive plotly like charts with pandas without having to make major modifications to the code? You can actually do that with the help of [**Cufflinks**](https://github.com/santosjorge/cufflinks) library.

Cufflinks library binds the power of [**plotly**](http://www.plot.ly/) with the flexibility of [pandas](http://pandas.pydata.org/) for easy plotting. Let’s now see how we can install the library and get it working in pandas.

#### Installation

```
pip install plotly # Plotly is a pre-requisite before installing cufflinks
pip install cufflinks
```

#### Usage

```
import pandas as pd  #importing Pandas
import cufflinks as cf #importing plotly and cufflinks in offline mode
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
```

Time to see the magic unfold with the Titanic dataset.

```
df.iplot()
```

![](https://cdn-images-1.medium.com/max/600/1*Qqsl_6xGeccaTU1AjAibrA.gif)

![](https://cdn-images-1.medium.com/max/600/1*YUY7ITHRA3KyfaOjhCjmBg.png)

**df.iplot() vs df.plot()**

The visualisation on the right shows the static chart while the left chart is interactive and more detailed and all this without any major change in the syntax.

[**Click here**](https://github.com/santosjorge/cufflinks/blob/master/Cufflinks%20Tutorial%20-%20Pandas%20Like.ipynb) for more examples.
