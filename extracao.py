import os
import time
import json
from random import random
from datetime import datetime

import requests

URL = 'https://www2.cetip.com.br/ConsultarTaxaDi/ConsultarTaxaDICetip.aspx'

for _ in range(0,10):

  # Criando a variável data e hora
  
  data_hora = datetime.now()
  data = datetime.strftime(data_hora, '%Y/%m/%d')
  hora = datetime.strftime(data_hora, '%H:%M:%S')

  # Captando a taxa CDI do site da B3

  try:
    response = requests.get(URL)
    response.raise_for_status()
  except requests.HTTPError as error:
    print('Dado não encontrado, continuando.')
    cdi = None
  except Exception as ex:
    print('Erro, parando a execução.')
    raise ex
  else:
    dado = json.loads(response.text)
    cdi = float(dado['taxa'].replace(',', '.')) + (random() - 0.5)

  # Verificando se o arquivo 'taxa-cdi.csv' existe

  if os.path.exists('./taxa-cdi.csv') == False:
    with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
      fp.write('dado,hora,taxa\n')
        
  # Salvando dados no arquivo 'taxa-cdi.csv'
  with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
    fp.write(f'{data},{hora},{cdi}\n')
  
print('Sucesso!!!')