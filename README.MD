# Teste Engenheiro de dados 

O código fonte referente a esse repositório tem como objetivo, a implementação de um 
Job spark realizando os tratamentos solicitados nos requisitos do desafio.


- Tecnologias
  - pyspark 3.3.0
  - python 3.10


- O Job foi desenvolvido seguindo os seguintes padrões:
  - Estrutura de projeto python, contendo requeriments e src do projeto
  - Estrutura por contexto domain e helper
  - POO

- Input
  - data/input/lake

- Output
  - data/output/lake

- Formato de Saída
  - Parquet

- Modo de Execução
  - O processo foi pensando inicialmente para execução local, mas a adaptação para execução em nuvem não se torna complexa, para a execução em nuvem, os ajustes necessário são a forma de busca do arquivo de entrada e escrita que seria necessário utilizar tecnologias que fossem compatíveis com a cloud me refiro a AWS especificamente utilizando o EMR, o código spark em que realiza os tratamentos não seria necessário ajustes. 

- Sequência de execução
  - O processo é executado seguindo a seguinte sequência de tratamento:
    - Leitura dos arquivos parquet no diretório de input
    - Identificação do dominio e tipo de evento
    - Tratamento individual pelo tipo de evento em cada dominio
    - Formatação das colunas
    - Remoção dos Duplicados (Seguindo a regra demandada)
    - Persiste o resultado

- Monitoramento
  - O processo conta com um logger custom, o mesmo gera logs locais e também um arquivo de log por execução a saída do arquivo está em data/output/logs

- Observações
  - O processo tem como saída o path data/output/lake

