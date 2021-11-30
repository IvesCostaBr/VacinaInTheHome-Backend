<h1  align="center">VacinaInTheHome🚀</h1>

![Settings Window](https://i.imgur.com/U59PCdc.jpeg)


## 📝 Sobre o projeto

- Trata-se de uma plataforma de agendamento de vacinas.Visando a dificuldade de algumas pessoas de ir até o local de vacinação, seja por medo ou por problemas de saúde, o vacinaInTheHome chegou para resolver esse problema. Com a plataforma você pode agendar sua vacinação no cnforto e segurança da sua casa!

    
## 🛠️ Tecnologias Utilizadas

[Python](https://www.python.org/)

[Django](https://www.djangoproject.com/)

[Django RestFramework](https://www.django-rest-framework.org/)


## 🔍 Pré-requisitos

[Python](https://www.python.org/)

[Docker](https://www.docker.com/)

[docker-compose](https://docs.docker.com/compose/)



## ⚙️ Como executar o projeto

Para executar o projeto é necessário que instale os pŕe-requesitos acima como docker, docker-compose caso queira utilixar o docker para rodar a aplicação, caso queria rodar ela com python direto na sua maquina, basta o python instlado e bem configurado no seu ambiente.

## .ENV

- Para o rodar o projeto localmente , vai precisar do arquivo .env dentro da pasta /app/ então crie-o colocando o conteudo abaixo.

```text
SECRET_KEY=django-insecure-@irl6g)r5^-rwrn&%vr3(lp3#53+1=ghi20$8k@drjeif55g1)
DEBUG=True
```
Caso queria trocar a aplicação para modo Debug , basta trocar de False para True


### Rodar com Docker
caso queira rodar a aplicação utilizando docker, basta digitar os comando abaixo utilizando o docker-compose.

```bash
# startando o container docker do docker

#comando para buildar a imagen docker
$ docker-compose build

#comando para subir os containers
$ docker-compose up -d

```

### Rodar com Python nativo

 - Se estiver rodando em ambiente Unix basta executar o script run_api.sh que ele criará um maquina virutal python e vai instalar todas dependências nela e executar a aplicação.

 ```bash
    bash run_api.sh
 ```

- Se estiver rodando em ambiente Windows siga os passos abaixo:
  - 1 - Criar um Virtual Env Python com o comando `python -m venv "nome da venv"`
  - 2 - Em seguida temos que ativar essas venv com o comando `cd /"nome da venv"/Scripts/activate`
  - 3 - Com a venv ativada vamos instalar os pacotes com o comando `pip install -r requirements-dev.txt`
  - 4 - Agora já podemos rodar o programa com o comando `python manage.py runserver`.



#### Se você seguiu todos os dados Certinho o servidor já está ativo com a aplicação na rota http://127.0.0.1:8000/
