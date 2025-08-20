import streamlit as st
import requests
import json


def get_prediction(payload):
    """
    Envia o payload para a API de predição de score de crédito e exibe o resultado no Streamlit.

    Parâmetros
    ----------
    payload : dict
        Dicionário no formato esperado pela API, contendo dados numéricos e categóricos
        do cliente para classificação de risco de crédito.

    Funcionamento
    -------------
    - Realiza uma requisição POST para o endpoint definido em st.secrets["API-ENDPOINT"].
    - Inclui o cabeçalho com a API key (st.secrets["API-KEY"]).
    - Caso a resposta seja bem-sucedida (status 200), exibe um card colorido com a classe prevista:
        * Poor (Alto risco) → vermelho
        * Standard (Risco moderado) → amarelo
        * Good (Bom histórico) → verde
    - Mostra também a versão do modelo utilizada.
    - Em caso de erro, exibe mensagem de falha no Streamlit.
    """
    endpoint = st.secrets["API-ENDPOINT"]
    headers = {
        "Content-Type": "application/json",
        "x-api-key": st.secrets["API-KEY"]
    }

    response = requests.post(endpoint, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        result = response.json()

        """
        ### Predição de Score de Crédito

        De acordo com os dados fornecidos, o cliente foi classificado na seguinte categoria de risco:
        """

        # Classe prevista: 0 = Poor, 1 = Standard, 2 = Good
        classes = {
            0: ("Poor (Alto risco)", "#f8d7da", "#721c24"),      # vermelho
            1: ("Standard (Risco moderado)", "#fff3cd", "#856404"), # amarelo
            2: ("Good (Bom histórico)", "#d4edda", "#155724")      # verde
        }

        predicted_class = result.get("prediction")
        predicted_info = classes.get(predicted_class, ("Classe desconhecida", "#d1ecf1", "#0c5460"))

        predicted_label, bg_color, text_color = predicted_info

        # Card estilizado
        st.markdown(
            f"""
            <div style='
                background-color: {bg_color};
                color: {text_color};
                padding: 15px;
                border-radius: 10px;
                font-size: 18px;
                font-weight: bold;
                text-align: center;
                margin-top: 10px;
            '>
                {predicted_label}
            </div>
            """,
            unsafe_allow_html=True
        )

        st.caption(f"Versão do modelo: {result.get('version')}")

    else:
        st.error("Erro ao obter a previsão. Por favor, tente novamente mais tarde ou revise seus dados.")


"""

# Predição de Score de Crédito

Esta aplicação faz parte da **plataforma de soluções analíticas da Quantum Finance** e foi desenvolvida para apoiar instituições financeiras na **avaliação e gestão de risco de crédito**.  

O sistema utiliza modelos avançados de Machine Learning para classificar clientes em diferentes categorias de risco, com base em informações cadastrais, financeiras e comportamentais.  

### Principais Benefícios
- **Agilidade**: resultado imediato da avaliação de crédito.  
- **Consistência**: padronização do processo de análise em diferentes canais.  
- **Escalabilidade**: integração simples com sistemas internos ou plataformas digitais de atendimento.  

### Categorias de Risco
- **Poor** → Alto risco de inadimplência  
- **Standard** → Risco moderado  
- **Good** → Histórico positivo e baixo risco  

### Como utilizar
Preencha as informações solicitadas e clique em **"Gerar Predição"**.  
O sistema retornará a classificação de risco e a versão do modelo utilizada, garantindo **transparência e rastreabilidade** na análise.  

"""

st.subheader("Informações Numéricas do Cliente")

# ---------------------- Entradas Numéricas ----------------------
idade = st.number_input("Idade (anos)", min_value=18, value=35)
renda_anual = st.number_input("Renda anual ($)", min_value=0.0, value=85000.0)
salario_liquido_mensal = st.number_input("Salário líquido mensal ($)", min_value=0.0, value=5500.0)
qtd_contas_bancarias = st.number_input("Quantidade de contas bancárias", min_value=0, value=3)
qtd_cartoes_credito = st.number_input("Quantidade de cartões de crédito", min_value=0, value=2)
taxa_juros = st.number_input("Taxa de juros (%)", min_value=0.0, max_value=100.0, value=2.5)
qtd_emprestimos = st.number_input("Quantidade de empréstimos ativos", min_value=0, value=1)
dias_atraso_pagamento = st.number_input("Dias de atraso (maior atraso)", min_value=0, value=0)
qtd_pagamentos_atrasados = st.number_input("Quantidade de pagamentos atrasados", min_value=0, value=0)
variacao_limite_credito = st.number_input("Variação do limite de crédito ($)", value=500.0)
qtd_consultas_credito = st.number_input("Quantidade de consultas de crédito", min_value=0, value=2)
divida_pendente = st.number_input("Dívida pendente ($)", min_value=0.0, value=1500.0)
percentual_utilizacao_credito = st.number_input("Percentual de utilização do crédito (%)", min_value=0.0, max_value=100.0, value=35.5)
total_emprestimos_mensal = st.number_input("Total de empréstimos ($/mês)", min_value=0.0, value=800.0)
valor_investido_mensal = st.number_input("Valor investido mensal ($)", min_value=0.0, value=1200.0)
saldo_mensal = st.number_input("Saldo mensal (R$)", value=3000.0)

tempo_historico_credito_meses = st.number_input(
    "Tempo de histórico de crédito (meses)",
    min_value=0,
    value=72
)

# ---------------------- Calculadora auxiliar ----------------------
st.markdown("#### Calculadora auxiliar de tempo de histórico (opcional)")
st.caption("Informe as datas no formato **aaaa/mm/dd** (ex.: 2018/06/15). A calculadora não preenche o campo de meses automaticamente.")

data_inicio_str = st.text_input("Data de início do histórico (aaaa/mm/dd)", value="2019/01/01")
data_final_str = st.text_input("Data final / de referência (aaaa/mm/dd)", value="2025/08/20")

if st.button("Calcular meses"):
    try:
        # Quebrando as datas em ano, mês, dia
        y1, m1, d1 = map(int, data_inicio_str.split("/"))
        y2, m2, d2 = map(int, data_final_str.split("/"))

        # Converte para meses totais
        total_meses_1 = y1 * 12 + m1
        total_meses_2 = y2 * 12 + m2

        meses = total_meses_2 - total_meses_1
        # Ajuste do dia (se o dia final for menor que o inicial, não completou o mês)
        if d2 < d1:
            meses -= 1

        if meses < 0:
            st.error("Data inserida de forma errada. Use o formato **aaaa/mm/dd** e verifique se a data final é posterior à inicial.")
        else:
            st.info(f"Resultado da calculadora: **{meses} meses**. Copie este valor para o campo de histórico de crédito.")
    except Exception:
        st.error("Data inserida de forma errada. Use o formato **aaaa/mm/dd** (ex.: 2018/06/15).")
    
    # ================== OCUPAÇÃO ==================
ocupacao = st.selectbox(
    "Qual é a ocupação?",
    (
        "Accountant (Contador[a])",
        "Architect (Arquiteto[a])",
        "Developer (Desenvolvedor[a])",
        "Doctor (Médico[a])",
        "Engineer (Engenheiro[a])",
        "Entrepreneur (Empreendedor[a])",
        "Journalist (Jornalista)",
        "Lawyer (Advogado[a])",
        "Manager (Gestor[a])",
        "Mechanic (Mecânico[a])",
        "Media Manager (Gestor[a] de Mídia)",
        "Musician (Músico[a])",
        "Not Informed (Não informado)",
        "Scientist (Cientista)",
        "Teacher (Professor[a])",
        "Writer (Escritor[a])",
    )
)

# ================== PAGAMENTO VALOR MÍNIMO ==================
pagamento_valor_minimo = st.radio(
    "O cliente costuma pagar apenas o valor mínimo da fatura?",
    (
        "No (Não)",
        "Yes (Sim)",
        "Not Informed (Não informado)",
    )
)

# ================== COMPORTAMENTO DE PAGAMENTO ==================
comportamento_pagamento = st.selectbox(
    "Qual é o comportamento de pagamento?",
    (
        "High spent Large value payments (Gastos altos, pagamentos de grande valor)",
        "High spent Medium value payments (Gastos altos, pagamentos de valor médio)",
        "High spent Small value payments (Gastos altos, pagamentos de pequeno valor)",
        "Low spent Large value payments (Gastos baixos, pagamentos de grande valor)",
        "Low spent Medium value payments (Gastos baixos, pagamentos de valor médio)",
        "Low spent Small value payments (Gastos baixos, pagamentos de pequeno valor)",
    )
)

# ================== TIPOS DE EMPRÉSTIMOS ==================
tipos_emprestimos = st.selectbox(
    "Qual é o tipo de empréstimo?",
    (
        "Auto Loan (Empréstimo para Automóvel)",
        "Credit-Builder Loan (Empréstimo para Construção de Crédito)",
        "Debt Consolidation Loan (Empréstimo para Consolidação de Dívidas)",
        "Home Equity Loan (Empréstimo com Garantia de Imóvel)",
        "Mortgage Loan (Hipoteca)",
        "Not Specified (Não especificado)",
        "Payday Loan (Empréstimo Consignado/Salário)",
        "Personal Loan (Empréstimo Pessoal)",
        "Student Loan (Empréstimo Estudantil)",
        "Two or More Types of Loan (Dois ou mais tipos de empréstimo)",
    )
)

# ================== Normalização das Categóricas ==================

map_ocupacao = {
    "Accountant (Contador[a])": "Accountant",
    "Architect (Arquiteto[a])": "Architect",
    "Developer (Desenvolvedor[a])": "Developer",
    "Doctor (Médico[a])": "Doctor",
    "Engineer (Engenheiro[a])": "Engineer",
    "Entrepreneur (Empreendedor[a])": "Entrepreneur",
    "Journalist (Jornalista)": "Journalist",
    "Lawyer (Advogado[a])": "Lawyer",
    "Manager (Gestor[a])": "Manager",
    "Mechanic (Mecânico[a])": "Mechanic",
    "Media Manager (Gestor[a] de Mídia)": "Media_Manager",
    "Musician (Músico[a])": "Musician",
    "Not Informed (Não informado)": "Not Informed",
    "Scientist (Cientista)": "Scientist",
    "Teacher (Professor[a])": "Teacher",
    "Writer (Escritor[a])": "Writer",
}

map_pagamento = {
    "No (Não)": "No",
    "Yes (Sim)": "Yes",
    "Not Informed (Não informado)": "Not Informed",
}

map_comportamento = {
    "High spent Large value payments (Gastos altos, pagamentos de grande valor)": "High_spent_Large_value_payments",
    "High spent Medium value payments (Gastos altos, pagamentos de valor médio)": "High_spent_Medium_value_payments",
    "High spent Small value payments (Gastos altos, pagamentos de pequeno valor)": "High_spent_Small_value_payments",
    "Low spent Large value payments (Gastos baixos, pagamentos de grande valor)": "Low_spent_Large_value_payments",
    "Low spent Medium value payments (Gastos baixos, pagamentos de valor médio)": "Low_spent_Medium_value_payments",
    "Low spent Small value payments (Gastos baixos, pagamentos de pequeno valor)": "Low_spent_Small_value_payments",
}

map_tipos_emprestimos = {
    "Auto Loan (Empréstimo para Automóvel)": "Auto Loan",
    "Credit-Builder Loan (Empréstimo para Construção de Crédito)": "Credit-Builder Loan",
    "Debt Consolidation Loan (Empréstimo para Consolidação de Dívidas)": "Debt Consolidation Loan",
    "Home Equity Loan (Empréstimo com Garantia de Imóvel)": "Home Equity Loan",
    "Mortgage Loan (Hipoteca)": "Mortgage Loan",
    "Not Specified (Não especificado)": "Not Specified",
    "Payday Loan (Empréstimo Consignado/Salário)": "Payday Loan",
    "Personal Loan (Empréstimo Pessoal)": "Personal Loan",
    "Student Loan (Empréstimo Estudantil)": "Student Loan",
    "Two or More Types of Loan (Dois ou mais tipos de empréstimo)": "Two or More Types of Loan",
}

# Normalizando as escolhas do usuário
ocupacao_norm = map_ocupacao[ocupacao]
pagamento_valor_minimo_norm = map_pagamento[pagamento_valor_minimo]
comportamento_pagamento_norm = map_comportamento[comportamento_pagamento]
tipos_emprestimos_norm = map_tipos_emprestimos[tipos_emprestimos]

# ---------------------- Preparando o payload para a API ----------------------
payload = {
    "data": {
        "idade": idade,
        "renda_anual": renda_anual,
        "salario_liquido_mensal": salario_liquido_mensal,
        "qtd_contas_bancarias": qtd_contas_bancarias,
        "qtd_cartoes_credito": qtd_cartoes_credito,
        "taxa_juros": taxa_juros,
        "qtd_emprestimos": qtd_emprestimos,
        "dias_atraso_pagamento": dias_atraso_pagamento,
        "qtd_pagamentos_atrasados": qtd_pagamentos_atrasados,
        "variacao_limite_credito": variacao_limite_credito,
        "qtd_consultas_credito": qtd_consultas_credito,
        "divida_pendente": divida_pendente,
        "percentual_utilizacao_credito": percentual_utilizacao_credito,
        "total_emprestimos_mensal": total_emprestimos_mensal,
        "valor_investido_mensal": valor_investido_mensal,
        "saldo_mensal": saldo_mensal,
        "tempo_historico_credito_meses": tempo_historico_credito_meses,
        "ocupacao": ocupacao_norm,
        "pagamento_valor_minimo": pagamento_valor_minimo_norm,
        "comportamento_pagamento": comportamento_pagamento_norm,
        "tipos_emprestimos": tipos_emprestimos_norm
    }
}

# ================== Botão para enviar e gerar predição ==================
if st.button("Gerar Predição"):
    with st.spinner("Calculando..."):
        get_prediction(payload)
