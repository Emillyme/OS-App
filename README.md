# Sistema de Ordem de Serviço - OS-App

## Descrição

Este projeto foi desenvolvido para o **Senai Roberto Manje**, com o objetivo de criar um **Sistema de Ordem de Serviço**. A aplicação foi construída utilizando o **Django** para o back-end e o **Next.js** para o front-end, proporcionando uma solução robusta e escalável para a gestão de ordens de serviço.

### Tecnologias Utilizadas:
- **Back-end**: Django (Python)
- **Front-end**: Next.js (React) com Tailwind
- **Banco de Dados**: MySQL
- **Gerenciamento de estados**: Zustand
  
## Funcionalidades

1. **Gerenciamento de Ordens de Serviço (OS):**
   - **Criação, Leitura, Atualização e Exclusão (CRUD)** de ordens de serviço.
   - **Localização de Dados**: Implementação de filtros e buscas para facilitar a localização das ordens.
   - **Atualização de Status da OS**: Os status das ordens de serviço podem ser atualizados para **pendente**, **em andamento** ou **concluído**.
   - **Relacionamento entre Tabelas**: Tabelas relacionadas serão listadas nos campos correspondentes, conforme o diagrama de relacionamento entre tabelas.
   
2. **Cadastro de Dados Inicial**:
   - Serão disponibilizadas planilhas para popular o banco de dados.
   - Existe a opção de usar **endpoints** ou **código Python** para popular o banco de dados com os dados dessas planilhas.

3. **Gerenciamento de Acesso**:
   - O sistema possui diferentes níveis de acesso, garantindo que somente usuários com permissões específicas possam acessar certas funcionalidades:
     - **Gestor de Manutenção**: Acesso total a todas as funcionalidades administrativas.
     - **Funcionários**: Podem criar ordens de serviço.
     - **Técnicos de Manutenção**: Podem visualizar e atualizar o status das ordens de serviço, mas não podem criar ou excluir OS.
     - **Administrador**: Acesso total a todas as funcionalidades do sistema.
   - O gerenciamento de permissões será baseado nos papéis de usuário definidos no sistema.
     
4. **Relacionamentos de Dados**:
   - Os relacionamentos entre as tabelas do banco de dados serão implementados conforme o diagrama de relacionamento.
   - Dados de tabelas relacionadas serão exibidos corretamente nos campos correspondentes nas telas do front-end.
