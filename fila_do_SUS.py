#-*-coding:utf8-*-
'''
Eduardo Freire Mangabeira


#usar com jupyter notebooks para visualização

1(closed)- ainda estou pensando em como fazer isso sem precisar abrir um notebook,acho que é 
o desafio maior dado as minhas configurações atuais (chromebook 70.0.3538.16(Versão oficial)dev 64 bits)

2(update)- Não tem como rodar esse código por script vanilla, apenas pelo IPython dá pra usar.
'''
import pandas as pd
import seaborn as sd
#from IPython import get_ipython

low_memory = False
#%matplotlib inline  #1)tive que comentar essa linha por só funcionar com os notebooks abertos(.ipynb)
get_ipython().magic('matplotlib inline')#2)descobri que essa linha não retorna nada, mesmo chamando o ipython
pd.options.display.max_columns = 80
pd.options.display.max_rows = 90

filename = 'fila-pública-2017-11-30.csv'
df = pd.read_csv(filename)

df.shape

df.describe()
