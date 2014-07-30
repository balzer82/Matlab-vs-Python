# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# <markdowncell>

# Read in the [Stockoverflow Query](http://data.stackexchange.com/stackoverflow/query/211291/matlab-simulink-and-python-questions-per-month)

# <codecell>

data = pd.read_csv('QueryResults.csv')

# <codecell>

gd = data.pivot(index='month', columns='tag', values='count').fillna(0)

# <codecell>

gd.index = pd.to_datetime(gd.index)
gd.columns.name = 'Frage zu'
gd.rename(columns={'python': 'Python', 'matlab': 'Matlab', 'simulink': 'Simulink'}, inplace=True)
gd.plot()
plt.savefig('stockoverflow-gesamt.png')

# <codecell>

gd['Matlab+Simulink'] = gd.Matlab+gd.Simulink

# <codecell>

for yearbegin in range(2010, 2013):
    st = '01-01-%i' % yearbegin
    df = gd[['Python','Matlab+Simulink']][st:'01-01-2014']

# <headingcell level=4>

# Normalize it

# <codecell>

    def normalize(df):
        return 100.0*df.values/df.values[0]

# <codecell>

    df = df.apply(normalize)

# <headingcell level=4>

# Plot it

# <codecell>

    df.plot(title='Fragen auf stockoverflow.com nach Stichwort')
    plt.ylabel='Prozent'
    plt.ylim(0, 1000)
    plt.savefig('stockoverflow-%i-2014.png' % yearbegin, dpi=72)

# <codecell>


