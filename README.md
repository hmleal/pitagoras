Pitágoras
=========

Esse repositório é destinado ao meu projeto de TFG, mas você bem vindo a fazer sugestões. Aproveite :)

### Descrição

Com o aumento do número de pesquisas na área da biologia e consequentemente com o aumento dos dados coletados nessa área, surge à necessidade de realizar a análise de informações contidas nos bancos de dados que mapeiam essas informações, para que seja possível acessá-las de forma simplificada.

### Manual de instalação

Sequência de passos necessários para instalação do projeto.

1. Dependências

  ```sh
  $ pip install -r requirementst.txt
  ```

2. Criando o banco de dados e sincroniza as migrations

  ```sh
  $ ./manage.py syncdb
  ```

3. Carrega a base de dados para dentro do sistema

  ```sh
  $ ./manage.py loaddata core/fixtures/initial.json
  ```

4. Rodar o projeto

  ```sh
  $ ./manage.py runserver
  ```

5. Acessar via página web através do seguinte endereço:

  htttp://localhost:8000/

### Licença

```
Copyright (C) 2013 - Henrique Leal

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
```
