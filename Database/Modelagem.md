# Modelagem de Banco de Dados
O Banco de dados de um sistema sempre tem um arquivo para demonstrar qual é a estrutura do sistema.

Este é o devido arquivo!

Neste projeto terão três tabelas de início, 

## TABELA DE USUÁRIOS:
A tabela de usuários armazenará os dados dos colaboradores responsáveis por cadastrar equipamentos e realizar inspeções.

Contendo os seguintes conteúdos:
            ID_USUARIO (primary key),
            NOME (VarChar(100)),
            SETOR (VarChar(100)),
            CONTATO (VarChar(100)),
            EMAIL (VarChar(100)),
            SENHA (VarChar(100)),



## TABELA DE INSPEÇÕES
A tabela de Inspeções as quais serão catalogadas as informações de cada inspeção realizada pelo técnico responsável.

Contendo os seguintes conteúdos:
            ID_INSPECAO (primary key),
            USUARIO_ID(Aqui ficará o id do usuário que realizou a inspecao) (id referenciado da tabela usuários)
            EQUIPAMENTO_ID(Aqui ficará o equipamento que foi inspecionado) (id referenciado da tabela equipamento),
            DATA_INSPECAO (Date),
            STATUS (VarChar(20)),
            OBSERVAÇÃO(TEXT)


## TABELA DE EQUIPAMENTOS 
A tabela de Equipamentos será onde serão colocadas todos os equipamentos utilizados pela empresa.

Contendo os seguintes conteúdos:
            ID_EQUIPAMENTO(primary key),
            NOME (VarChar(100)),
            SETOR(VarChar(100)),
            DESCRIÇÃO(TEXT)
