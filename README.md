# docker_python_redis_compose
Projeto para a utilização do docker compose, banco de redis e python  
Vamos utilizar volumes, network e a construção de um projeto em python 
Estava com um problema de não atualizar o compose, que foi resolvido com o comando docker-compose up --build --remove-orphans --force-recreate  
Para esse caso rodamos o seguintes comandos:
Construir o projeto  
- docker compose build --no-cache  
Rodar  
- docker compose build --no-cache

Para build e rodar  
- docker compose up --build


# Comandos do docker compose
- docker-compose up --build --remove-orphans --force-recreate    força a recriação 
- depends on   -- cria dependencia entre os serviços
- docker compose up -d -- 
- docker compose ps -- mostrar os serviços
- docker compose down  -- remover
  
