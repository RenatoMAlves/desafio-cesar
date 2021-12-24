# desafio-cesar

Este repositório foi criado com objetivo de realizar o desafio do CESAR para a vaga de Engenheiro de dados. Os objetivos do desafio foram Analisar descritiva dos dados e criar um modelo para predizer a variável target Next_Tmax. A base de dados disponibilizada pode ser encontrada neste [link](https://archive.ics.uci.edu/ml/datasets/Bias+correction+of+numerical+prediction+model+temperature+forecast#). Esta base consiste de dados meteorológicos coletados durante a estação de verão (meses de Junho, Julho e Agosto) na Coréia do Sul para os anos de 2013 a 2017.

Conforme proposto este projeto foi elaborando utilizando ambos Jupyter Notebook e Python para análise dos dados/criação de modelo e deploy do modelo criado, respectivamente. A configuração de setup para ambos os ambientes é apresentada logo abaixo.

## Ferramentas utilizadas

Para a análise dos dados e construção de modelos foram utilizadas as seguintes bibliotecas:
1. Pandas
2. Matplotlib
3. Seaborn
4. Missingno
5. Numpy
6. Pycaret

Para a construção do modelo e deploy as bibliotecas utilizadas foram:
1. Pycaret
2. FastAPI
3. Uvicorn
4. Pandas
## Setup para Jupyter-notebooks

Os Notebooks estão localizados dentro da pasta **code/notebooks**. Caso queira executar os notebooks novamente, é aconselhado criar um ambiente para instalação dos pacotes python a serem executados neste projeto. Para isso basta entrar na pasta code e digitar o seguinte comando no terminal (caso queira criar o ambiente em outra pasta não há problema).
```
$ python3 -m venv /cesar-env
$ source cesar/bin/activate
```

este comando deve ser seguido da instalação dos pacotes:
```
pip install -r requirements.txt
```

Ao fim da instalação dos pacotes os notebooks podem ser executados.

## Setup para API com modelo

Para o deploy da API foi criado um container docker que hospeda tanto o PyCaret quanto o FastAPI. De inicio é necessário fazer o build da imagem criada no Dockerfile. Para isso execute as seguintes linhas de código no terminal:
```
$ cd code/
$ docker build -t desafio-cesar .
```

Após isso será iniciado o processo de building do container e instalação dos pacotes. Após a ter a instalação finalizada é necessário executar o container que executará o Uvicorn para a requisição. Para isso rode o comando:
```
docker run -p 8000:8000 cesar-desafio
```

Acesse a documentação para fazer a requisição de teste para o modelo acesse o endereço local do navegador através do seguinte link:
[http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)

Para fazer uma requisição teste basta apenas clicar na opção POST /predict e em seguida **Try it out**. Nisso aparecerá uma caixa de texto para inserir o body, basta substituir a informação lá dentro pelos dados em forma de json e clicar em **execute**. Para fim de teste segue abaixo um exemplo de json preenchido para ser colocado, os valores foram retirados do conjunto de validação utilizado no notebook **exploratory_prediction**. Este teste retornará o valor de 29.6º, por se tratar de uma temperatura o valor sempre é arredondado para 1 casa decimal. 
```
{
  "input": {
        "station": 1.0,
        "Present_Tmax": 29.2,
        "Present_Tmin": 21.5,
        "LDAPS_RHmin": 59.24028015,
        "LDAPS_RHmax": 85.28312683,
        "LDAPS_Tmax_lapse": 29.91538275,
        "LDAPS_Tmin_lapse": 22.13205443,
        "LDAPS_WS": 7.295952598,
        "LDAPS_LH": 111.038305,
        "LDAPS_CC1": 0.306907301,
        "LDAPS_CC2": 0.08745181,
        "LDAPS_CC3": 0.480662905,
        "LDAPS_CC4": 0.271983078,
        "lat": 37.6046,
        "lon": 126.991,
        "DEM": 212.335,
        "Slope": 2.785,
        "Solar radiation": 5275.070313
    }
}
```

## Dúvidas

Qualquer dúvida pode me contatar pelos seguintes meios: 
e-mail: renato.mar.alves@gmail.com
Telefone: (19) 98261-0537
