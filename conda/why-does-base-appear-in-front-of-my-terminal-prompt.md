https://askubuntu.com/questions/1026383/why-does-base-appear-in-front-of-my-terminal-prompt

why I have `(base)` on the left of my terminal prompt.

**To get rid of it**

https://askubuntu.com/a/1113179/308359

This can also be because `auto_activate_base` is set to True. You can check this using the following command

    conda config --show | grep auto_activate_base

To set it false

    conda config --set auto_activate_base False
    source ~/.bashrc

To reactivate set it to True

    conda config --set auto_activate_base True
    source ~/.bashrc
