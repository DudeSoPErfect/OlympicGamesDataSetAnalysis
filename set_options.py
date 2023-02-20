import pandas as pd

def setPandasDisplayOptions():
    display              = pd.options.display
    display.max_columns  = 100
    display.max_rows     = 100
    display.max_colwidth = 199
    display.width        = 1000
    
    return 0



