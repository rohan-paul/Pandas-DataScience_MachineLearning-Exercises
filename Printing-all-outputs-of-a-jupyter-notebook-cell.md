## Printing all the outputs of a cell

Consider a cell of Jupyter Notebook containing the following lines of code:

```
    In  [1]: 10+5
             11+6

    Out [1]: 17

```

It is a normal property of the cell that only the last output gets printed and for the others, we need to add the `print()` function. Well, it turns out that we can print all the outputs just by adding the following snippet at the top of the notebook.

```
from IPython.core.interactiveshell import InteractiveShell  InteractiveShell.ast_node_interactivity = "**all**"

```

Now all the outputs get printed one after the other.

```
    In  [1]: 10+5
             11+6
             12+7

    Out [1]: 15
    Out [1]: 17
    Out [1]: 19

```

To revert to the original setting :

InteractiveShell.ast_node_interactivity = "**last_expr**"
