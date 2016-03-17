# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
from QdHandler import QdDataProvider
from QdHandler import ImfRequestGenerator
from QdHandler import FrExchangeRateRequestGenerator
from matplotlib import pyplot as plt

provObj = QdDataProvider("oPAL8s4KyTyVUjzz1SrR")

reqImf = ImfRequestGenerator()
reqImf.setCriterias(['KOR', 'USA'], 'PCPIPCH')
ptcCpi = provObj.get(reqImf, "1990-12-31", "2015-12-31")
ptcCpi.columns = ['KORCPI','USACPI']

diffCpi = pd.DataFrame({'diffCpi': ptcCpi['KORCPI']-ptcCpi['USACPI']})

reqFrExchangeRate = FrExchangeRateRequestGenerator()
reqFrExchangeRate.setCriterias('N', 'A', ['KO'])
excRate = provObj.get(reqFrExchangeRate, "1989-12-31", "2015-12-31")
ptcExcRate = pd.DataFrame.pct_change(excRate)
ptcExcRate.columns = ['KRWUSD']
ptcExcRate = ptcExcRate['KRWUSD'].dropna()
ptcExcRate = ptcExcRate

ax1 = plt.subplot()

ax1.plot(diffCpi, 'k', label = 'difference of CPI')
ax1.set_ylabel('%')
ax1.legend(loc=0)
ax2 = ax1.twinx()
ax2.plot(ptcExcRate, 'k--', label = 'ptc of Exchange')
ax2.legend(loc='best')
plt.show()
