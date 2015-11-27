# servidorDadosJson
Servidor de dados que atende as requisições através de respostas no formato Json



NOTA DE LIBERAÇÃO: SERVIDOR DE DADOS RESTFUL COM JSON	
INTRODUÇÃO

O servidor diponibilizado através deste trabalho, visa fornecer mecanismos para que qualquer aplicação que implemente o protocolo HTTP, consiga acessar os metódos disponiveis no servidor para que seja realizada operações do tipo CRUD.
O servidor foi implementado na linguagem javascript atráves do framework NodeJS junto com o Express para as requisições HTTP, onde cada requisição feita pelo cliente é tratada e encaminhada ao controller que irá acessar o banco de dados MongoDB que é um banco de dados NoSQL, armazendo dados diferente da forma tradicional SQL, para o acesso ao banco MongoDB foi utilizado o framework Mongoose.
Para o Cliente foi realizado os teste com o plugin Postman do navegador Google Chrome, onde é possível realizar diversos tipos de requisições para um determinado servidor. Foi implementado também uma versão standalone do cliente na linguagem Python onde é possível realizar as operações CRUD da mesma forma em que pode ser feita em um Browser tradicional.
Desta forma foi interessante o desenvolvimento deste servidor porque através de tecnologias diferentes, foi possível o acesso do serviço e consequentemente dos dados disponíveis no servidor, deixando disponível um serviço dinâmico que pode ser acessado através de um aplicativo desktop, mobile ou através do Browser da mesma forma.
1.	NOTA DE RELEASE A SER PUBLICADO
•	Implementar através de muitas tecnologias disponíveis o acesso ao servidor.

2.	PROBLEMAS CONHECIDOS E LIMITAÇÕES
Limitação
•	O sistema de segurança do servidor ainda é fraco, sendo necessário um estudo mais aprofundado sobre segurança para garantir uma maior segurança  dos dados.

3.	DATAS IMPORTANTES
Segue abaixo as datas importante do desenvolvimento:
Data	Evento
01/10/2015	Início do planejamento
01/11/2015	Início do desenvolvimento
15/11/2015	Entrega para teste
23/11/2015	Fim do teste
26/11/2015	Liberação para produção
4.	COMPATIBILIDADE
Segue abaixo os requisitos:
Requisitos	Ferramentas
Navegadores	Browser:
**	Internet Explorer
**	Firefox
**	Google Chrome
**	Opera
Sistema operacional
**	Window Seven
**	Linux

	Tecnologias
Linguagem de   Programação	JavaScrip, Python
Framework WEB	NodeJs, Express,Mongoose
IDE 	Atom, PyCharm 
Design pattern	                            ---
Servidor Web	NodeJs

5.	PROCEDIMENTO E ALTERAÇAO DE CONFIGURAÇÃO DO AMBIENTE
É necessário a instalação do servidor em um sistema de hospedagem que suporte NodeJs, atualmente há vários serviços disponíveis de forma fácil. Após a instalação somente é necessário realizar a instalação das dependências contidas no arquivo "package.json", que pode ser feito de forma rápida e fácil através do comando do npm disponível no NodeJS, "npm install" na mesma pasta onde se encontra o "package.json", após a instalação de todas as dependências, basta iniciar o servidor com o comando "node app.js", que o servidor está apto para atender as requisições dos clientes.

6.	ATIVIDADES REALIZADAS NO PERÍODO
Nessa liberação foram contemplados os seguintes itens:
Cód	Título	Tarefa	Situação	Observação
1	Título da funcionalidade	Servidor de dados RestFul com Json. 	Concluído	
2	Implementação dos métodos e adequação das requisições	Foi implementado as requisições Rest com respostas no formato Json.	Concluído	
3	Instalar e configurar o banco de dados	Foi realizado uma pesquisado sobre o banco MongoDB e implementado os métodos necessários para o acesso aos serviços do banco.
	Concluído	
4	Implementação clientes em mais de duas tecnologias	Foi realizado os testes em somente duas tecnologias, sendo necessário a implementação em outras tecnologias.	Não Concluiido	A demanda de tempo não foi o suficiente para a pesquisa e implementação.


