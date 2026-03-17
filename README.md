![Processamento](https://i.giphy.com)


# Requisitos Funcionais (RF) 


Os requisitos funcionais descrevem o que o sistema deve ser capaz de fazer.

- RF01: O sistema deve receber ou armazenar listas com as notas dos alunos.

- RF02: O sistema deve verificar se os dados recebidos estão completos e válidos.

- RF03: Caso existam dados inválidos, incompletos ou corrompidos,
      o sistema deve tratá-los ou ignorá-los para evitar erros no processamento.

- RF04: O sistema deve calcular automaticamente a média das notas de cada aluno.

- RF05: O sistema deve identificar quais alunos estão em situação de recuperação.

- RF06: O sistema também deve identificar os alunos com melhor desempenho acadêmico.

- RF07: O sistema deve realizar o processamento dessas informações de forma 
      automática, reduzindo o trabalho manual da coordenação.

- RF08: Após o processamento, o sistema deve gerar um relatório com os resultados
     obtidos.

- RF09: Esse relatório deve ser salvo em um arquivo no formato .txt,
      permitindo fácil consulta e armazenamento.



#  Requisitos Não-Funcionais (RNF) 


Os requisitos não-funcionais descrevem como o sistema deve funcionar, 
considerando qualidade e organização do código.

- RNF01: O sistema deve ser desenvolvido de forma modular,
       separando as responsabilidades em diferentes funções.

- RNF02: Deve existir tratamento de erros, principalmente para lidar com dados
       incompletos ou inválidos.

- RNF03: O processamento das informações deve ser rápido e eficiente,
       permitindo analisar os dados de vários alunos sem demora.

- RNF04: O código deve ser organizado e de fácil manutenção,
       facilitando futuras melhorias.

- RNF05: O relatório gerado deve ser claro, organizado e bem formatado,
        facilitando a leitura das informações.

- RNF06: A estrutura do sistema deve permitir facilidade de entendimento
     e evolução do código ao longo do tempo.


# Regras de Negócio (RN) 



As regras de negócio definem como algumas decisões do sistema devem ser tomadas,
com base nas informações analisadas.

- RN01: A média de cada aluno deve ser calculada com base nas notas
      válidas disponíveis.

- RN02: Alunos cuja média esteja abaixo do valor mínimo definido
      devem ser classificados em recuperação.

- RN03: Alunos com maior média devem ser destacados como alunos de melhor desempenho.

- RN04: Dados incompletos ou inválidos não devem comprometer o processamento
      geral das informações.

- RN05: Todos os resultados devem ser organizados em um relatório final,
      permitindo que a coordenação consulte os dados de forma rápida e clara.



# Mapa de Empatia 

# O que vê:
  - Dados desorganizados
  - Informações inconsistentes
  - Dificuldados em análizar os dados

# O que ouve:

 - Reclamações sobre erros 
 - Pressão por rapidez
 - O que pensa e sente:
 - Insegurança nos dados
 - Dificuldade em confiar nos resultados

# O que fala e faz:

 - Analisa manualmente
 - Perde tempo com retrabalho

# Dores:

 - Dados incompletos
 - Falta de automação
 - Alto risco de erro

# Ganhos:

 - Automação
 - Relatórios rápidos
 - Decisões mais seguras




