# Aplicação web para demonstração da rede neural

Aplicação usando web framework Django para implementação
do projeto de Redes Neurais com uma interface web.

## Passos para execução
Lembre-se de executar tudo em um virtualenv!

### 1º - Instalar dependências
Para instalar as dependências de execução do projeto, execute:
```bash
pip install -r requirements.txt
```
Também coloquei uns pacotes para ajudar no desenvolvimento. Caso queira, execute também:
```bash
pip install -r dev-requirements.txt
```

### 2º - Execute o script auxiliar
Execute o script auxiliar para criar as variáveis de ambiente necessárias, tendo como principal a SECRET_KEY que, como o nome diz, é secreta, e não pode aparecer em um repositório.
```bash
python contrib/env_gen.py
```

### 3º - Treinar a rede neural
Execute o arquivo de gerenciamento do projeto Django, com o nome da tarefa "train_questions":
```bash
python manage.py train_questions
```

### 3 e 1/2º(opcional) - Faça a pergunta pelo terminal
Tem como continuar no terminal e testar a pergunta por aí mesmo.
~~Na verdade era só um teste que virou uma feature~~

Execute o arquivo de gerenciamento do projeto Django, com o nome da tarefa "classify_question" e como parâmetro coloque a pergunta. Use aspas.
```bash
python manage.py classify_question "Pergunta aqui entre aspas porque normalmente tem espaço"
```

### 4º - Inicie o servidor web
O framework vem com um "mini servidor http" embutido.
Isso é útil para ambientes de desenvolvimento.
```bash
python manage.py runserver
```
E sim... vai aparecer coisinha chamando atenção. Como não vamos usar nada disso (por enquanto), pode ignorar.

### 5º - Acesse pelo navegador
Como deve aparecer no shell, você pode acessar a aplicação através do endereço http://127.0.0.1:8000.
A página inicial já deverá ter um formulário para que você possa preencher o formulário testar a rede treinada.
