# Atualizado - Sistema CRUD para Inventário de Ativos de TI - 1ºa Atividade Avaliativa - Sprints 1 e 2
Aluno: Pedro dos Santos Sales

1. Introdução
O presente repositório hospeda a minha solução para a 1ºa Atividade Avaliativa do curso de Cibersegurança da UFU. O problema a ser resolvido é o seguinte:

"Deve ser desenvolvido um programa de computador, em linguagem Python, que permita realizar operações de cadastro, consulta, atualização e remoção (CRUD) de ativos de TI e de vulnerabilidades associadas a esses ativos. A aplicação deverá simular, de forma simplificada, uma base de inventário de segurança utilizada por uma equipe de Computação ou Cibersegurança para acompanhar quais equipamentos, sistemas ou serviços existem em uma organização, quais vulnerabilidades foram identificadas neles e qual é a situação de tratamento dessas vulnerabilidades."

"Neste trabalho, considera-se como ativo de TI qualquer recurso computacional que precise ser acompanhado pela organização, como notebooks, servidores, estações de trabalho, roteadores, impressoras de rede, sistemas internos, softwares licenciados, aplicações web ou bancos de dados. Cada ativo deverá possuir um identificador único no sistema, além de informações básicas que permitam sua localização, classificação e consulta. Também deverá ser possível associar vulnerabilidades aos ativos cadastrados."

2. Requerimentos
2.1. Requerimento 1
"O programa deve possuir um prompt, menu textual ou interface gráfica para interagir com o usuário. No caso de prompt ou menu textual, devem ser apresentadas opções claras para as operações disponíveis. As entradas de dados devem possuir tratamento de erros para evitar falhas causadas por comandos inválidos, campos vazios ou tipos de dados incorretos."

2.2. Requerimento 2
"Criar no programa uma lista de tipos de ativos de TI com pelo menos 4 categorias, utilizando uma estrutura de dados de enumeração. Exemplos de categorias possíveis são: notebook, servidor, roteador, software licenciado, aplicação web, banco de dados, impressora de rede ou estação de trabalho. A cada tipo de ativo deve estar associado um código inteiro para referência no sistema."

2.3. Requerimento 3
"Ler do prompt um comando de cadastro de ativo de TI contendo, no mínimo, identificador único do ativo, nome ou hostname, responsável, setor ou localização, tipo de ativo e lista inicial de vulnerabilidades associadas, quando houver. Essas informações devem ser gravadas ou concatenadas em um ou mais arquivos de texto, que funcionarão como base de dados da aplicação. O identificador do ativo deve ser um número inteiro e deve ser usado como identificador único no sistema."

2.4. Requerimento 4
"Buscar na base de dados os registros de um ativo solicitado pelo usuário e exibi-los de forma organizada. A busca deve poder ser realizada, no mínimo, pelo identificador do ativo ou pelo nome/hostname."

2.5. Requerimento 5
"Atualizar os dados de um ativo de TI já cadastrado na base de dados, com base em novas informações inseridas pelo usuário no prompt. A atualização poderá envolver, por exemplo, mudança de responsável, setor, localização, tipo de ativo ou descrição do ativo."

2.6. Requerimento 6
"Deletar o registro de um ativo de TI da base de dados, removendo também as vulnerabilidades associadas a esse ativo, quando existirem."

2.7. Requerimento 7
"Permitir cadastrar, a qualquer momento após o cadastro de um ativo, vulnerabilidades associadas a ele. Para cada vulnerabilidade, o programa deverá registrar pelo menos uma descrição, uma categoria ou tipo, uma severidade e um status de tratamento. A severidade pode seguir uma escala simples, como baixa, média, alta e crítica. O status pode indicar, por exemplo, se a vulnerabilidade está aberta, em tratamento, corrigida ou aceita como risco."

2.8. Requerimento 8
"Visualizar as vulnerabilidades associadas a um ativo de TI, exibindo, quando houver vulnerabilidades cadastradas, sua descrição, severidade e status de tratamento. Quando não houver vulnerabilidades associadas ao ativo, o sistema deve informar que o ativo está sem vulnerabilidades registradas."

2.9. Requerimento 9
"Utilizar uma estrutura de dicionário (em Python, por exemplo, temos o tipo dict, uma estrutura do tipo hash map) para otimizar buscas, consultas ou organização interna dos registros. Por exemplo, o dicionário pode indexar ativos pelo identificador único, pelo hostname ou por outro campo considerado relevante."

2.10. Requerimento 10
"O código deve estar disponível no GitHub, Bitbucket ou plataforma similar. No repositório, o estudante deve demonstrar que, durante a produção do trabalho, soube trabalhar com mais de 2 branches e realizar merge entre eles."

2.11. Requerimento 11 - Optativo
"Optativo: Utilizar um banco de dados relacional no projeto (aumenta o valor da nota)."

3. Desenvolvimento
A fim de atender a todos os 11 requerimentos, dividi o desenvolvimento dessa solução em duas fases. Em um primeiro momento, busquei atender ao requisito 3 utilizando um arquivo json como banco de dados da aplicação. Em um segundo momento, para atender ao requisito 11, implementei separadamente uma versão da aplicação que utiliza o SQLite, uma biblioteca padrão da linguagem Python para a criação e gerenciamento de bancos de dados relacionais. Nesse sentido, a estrutura geral do projeto consiste em duas arquiteturas de persistência de dados que possuem 3 módulos, ou arquivos, em comum e 4 exclusivos, sendo 2 para a arquitetura baseada em json e 2 para a arquitetura baseada em SQLite.

3.1. Arquivos/Módulos Compartilhados entre Arquiteturas
main.py: Inicializa o banco de dados, exibe o menu interativo e roteia a escolha do usuário para a função CRUD adequada.
modelos_enums.py: Emprega a biblioteca nativa enum para definir opções fixas e padronizadas no sistema.
utilidades.py: Implementa a lógica de validação de entrada de dados e tratamento de erros.
3.2. Arquivos/Módulos Específicos da Arquitetura de Persistência com json
operacoes_crud.py: Implementa as operações de CRUD para os ativos e as vulnerabilidades na arquitetura baseada em json.
banco_dados.py: Implementa as funções de inicialização do banco de dados, sincronização de memória, e salvamento do banco.
3.3. Arquivos/Módulos Específicos da Arquitetura de Persistência com SQLite
operacoes_crud: Implementa as operações de CRUD para os ativos e as vulnerabilidades na arquitetura baseada em SQLite.
banco_dados.py: Implementa as funções de inicialização do banco de dados, sincronização de memória, e salvamento do banco.
5. Considerações Finais
Em suma, a atividade em questão constituiu uma oportunidade de prática dos conceitos estudados ao longo dos sprints 1 e 2.
