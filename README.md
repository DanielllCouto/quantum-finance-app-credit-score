# 📊 Quantum Finance – App de Predição de Score de Crédito  

## Sobre o projeto  
Este repositório contém o **frontend do projeto Quantum Finance – Score de Crédito**, desenvolvido em **Streamlit**.  
O app funciona como a camada de interface gráfica para usuários internos (analistas de crédito) e externos (parceiros), permitindo o **consumo direto da API de inferência** criada no projeto end-to-end de MLOps.  

O fluxo principal do app:  
1. Coleta de informações cadastrais, financeiras e comportamentais do cliente.  
2. Normalização das variáveis categóricas para o formato esperado pelo modelo.  
3. Montagem do payload JSON no padrão da API.  
4. Envio do payload via POST para o endpoint seguro.  
5. Exibição da predição em **cards coloridos** que destacam o risco do cliente:  
   - 🔴 **Poor** → Alto risco  
   - 🟡 **Standard** → Risco moderado  
   - 🟢 **Good** → Bom histórico  

---
## Tecnologias e Linguagens Utilizadas  

- **Python 3.10** – Linguagem principal para desenvolvimento do app.  
- **Streamlit** – Criação da interface web interativa de forma ágil e escalável.  
- **Requests + JSON** – Comunicação com a API de inferência, montagem e envio do payload.  
- **Secrets (Streamlit Cloud)** – Armazenamento seguro de credenciais (API Key e endpoint).  
- **Git + GitHub** – Versionamento, controle de branches e integração com pipeline de deploy.  
- **CI/CD (Streamlit Cloud)** – Deploy contínuo da branch `main`, com build automático.  
- **Pylint** – Garantia de qualidade e padronização do código.  

### Competências Técnicas Demonstradas
- Capacidade de integrar **frontend em Python** com uma **API em produção** em nuvem (AWS).  
- Experiência prática em **boas práticas de MLOps**: separação de responsabilidades, versionamento e uso de secrets.  
- Vivência em **automação de deploys (CI/CD)** aplicada a aplicações de dados.  
- Conhecimento em **boas práticas de desenvolvimento**: modularização, normalização de dados e feedback visual para o usuário final.  

---
## Estrutura do Repositório  

quantum-finance-app-credit-score/
│
├── app.py # Código principal do app
├── requirements.txt # Dependências mínimas
├── .streamlit/
│ └── secrets.toml # Segredos (endpoint e API key) - não versionado
└── documentacao/
└── Documentacao_App_Quantum_Finance.docx # Documentação detalhada em Word


---

## Funcionalidades  
- **Apresentação institucional inicial** da Quantum Finance.  
- **Entradas numéricas**: idade, renda, salário, empréstimos, dívidas, etc.  
- **Campos financeiros** em dólar ($) e percentuais (%).  
- **Calculadora auxiliar**: cálculo opcional de meses de histórico de crédito a partir de datas.  
- **Entradas categóricas**: ocupação, comportamento de pagamento, tipos de empréstimos.  
- **Normalização automática** das categorias para valores canônicos usados no modelo.  
- **Montagem do payload** no formato esperado pela API.  
- **Chamada à API** com autenticação via API Key.  
- **Exibição do resultado** em cards coloridos, incluindo versão do modelo utilizado.  

---

## CI/CD  

- Deploy automatizado via **Streamlit Cloud**.  
- Monitoramento da branch `main`.  
- Cada push/merge dispara build e entrega contínua.  
- Configuração de `Secrets` diretamente no painel do Streamlit Cloud.  
- URL de produção definida:  
  [https://quantum-finance-app-credit-score.streamlit.app/](https://quantum-finance-app-credit-score.streamlit.app/)  

---

## Próximos Passos  

- Melhorias na experiência do usuário (ajuda contextual, validações).  
- Registro e exibição de histórico de predições.  
- Internacionalização (versão em inglês).  
- Integração com dashboards corporativos.  

---

## Conecte-se  

👨‍💻 **Daniel Estrella Couto**  
[LinkedIn](https://www.linkedin.com/in/daniel-estrella-couto) | [GitHub](https://github.com/estrellacouto05)  
