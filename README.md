# Projeto Tech News


## Contexto :selfie:

Projeto de Web Scraping onde serão feito raspagem de dados no _Blog da Trybe_: https://blog.betrybe.com/.

Essas notícias serão salvas em banco de dados MongoDB.

As notícias serão armazenadas em uma coleção chamada `news`.


## Tecnologias utilizadas :technologist:

- Projeto desenvolvido em Python utilizando banco de dados MongoDB.


## Habilidades desenvolvidas

  - Utilizar o terminal interativo do Python;

  - Escrever seus próprios módulos e importá-los em outros códigos;

  - Aplicar técnicas de raspagem de dados;

  - Extrair dados de conteúdo HTML;

  - Armazenar os dados obtidos em um banco de dados;


## Executando aplicação

1. Clone o repositório:
  * `git clone git@github.com:LucasAccurcio/tech-news.git`.
  * Entre na pasta do repositório que você acabou de clonar:
    - cd `tech-news`
    
2. Crie o ambiente virtual para o projeto

  - `python3 -m venv .venv && source .venv/bin/activate`
  
3. Instale as dependências

  - `python3 -m pip install -r dev-requirements.txt`
  
### Executando a aplicação com banco de dados local:

  Com o mongoDB rodando em sua máquina local, execute o seguinte comando na pasta raiz:

  `tech-news-analyzer`

  O comando inicializará a função de Web Scraping já povoando o banco de dados com 5 notícias, pode demorar um pouco.

  Em seguida será exibido um menu no terminal solicitando ao usuário qual operação deseja ser realizada.


### Executando a aplicação com banco de dados via Docker:

  Com o Docker e Docker Compose já instalados, execute o seguinte comando no terminal:

  `docker-compose up -d mongodb`

  Em seguida execute o seguinte comando na pasta raiz:
  
  `tech-news-analyzer`

  O comando inicializará a função de Web Scraping já povoando o banco de dados com 5 notícias, pode demorar um pouco.

  Em seguida será exibido um menu no terminal solicitando ao usuário qual operação deseja ser realizada.


### Menu da aplicação :computer:

  ```sh
  Selecione uma das opções a seguir:
  0 - Popular o banco com notícias;
  1 - Buscar notícias por título;
  2 - Buscar notícias por data;
  3 - Buscar notícias por tag;
  4 - Buscar notícias por categoria;
  5 - Listar top 5 notícias;
  6 - Listar top 5 categorias;
  7 - Sair.
  ```
