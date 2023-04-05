<h2>FAN2021.1</h2>

Este é um projeto da disciplina de <b>Programação para Web 2</b>, realizado no decorrer do semestre de <b>2021.1</b> na <b>Faculdade de Negócios - FAN</b>.

Para inicializar o projeto, deve-se executar os seguintes comandos:

```
pip install -r requirements-dev.txt

*** EM CASO DE ERRO APÓS EXECUTAR O COMANDO ACIMA, ENTÃO DEVERÁ INSTALAR O WHEEL PARA INSTALLAR CERTAS LEGACY LIBS() - NO PROMPT USAR : pip install wheel
EM CASO DE O WHEEL NÃO FUNCIONAR, DEVERÁ SER FEITO A INSTALAÇÃO DE TODAS AS LIBS 1 POR 1 ***

python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

OBS: Caso opte por fazer a <b>instalação</b> no <b>servidor de produção</b>, deve-se utilizar o arquivo de <b>requirements.txt</b> ao invés do <b>requirements-dev.txt</b>
