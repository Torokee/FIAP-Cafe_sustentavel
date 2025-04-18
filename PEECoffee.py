def mostrar_menu():
    print("\n=== CAFÉ SUSTENTÁVEL – Simulador de Economia e Impacto Ambiental ===")
    print("1 - Informar dados do equipamento a combustão")
    print("2 - Informar dados do equipamento elétrico")
    print("3 - Calcular economia, impacto ambiental e payback")
    print("0 - Sair")

# Variáveis globais
qtd_equipamentos = 0
abastecimentos_dia = 2
dias_mes = 30
capacidade_tanque = 0.6
valor_combustivel = 0
consumo_mensal_eletrico = 0
economia_mensal = 0

def dados_combustao():
    global qtd_equipamentos, abastecimentos_dia, valor_combustivel
    print("\n-- DADOS DO EQUIPAMENTO A COMBUSTÃO --")
    qtd_equipamentos = int(input("Quantidade de equipamentos: "))
    abastecimentos_dia = int(input("Abastecimentos por dia (padrão 2): "))
    valor_combustivel = float(input("Valor do combustível (R$/L): "))

def dados_eletrico():
    global consumo_mensal_eletrico
    print("\n-- DADOS DO EQUIPAMENTO ELÉTRICO --")
    tensao = float(input("Tensão da bateria (V): "))
    capacidade = float(input("Capacidade da bateria (Ah): "))
    baterias_por_dia = int(input("Quantas baterias são utilizadas por dia por equipamento? "))
    tarifa = float(input("Tarifa de energia elétrica (R$/kWh): "))

    eficiencia = 0.75  # valor fixo baseado em média de mercado
    energia_por_bateria = (tensao * capacidade) / 1000  # em kWh
    energia_consumida = energia_por_bateria / eficiencia
    consumo_diario = energia_consumida * baterias_por_dia

    consumo_mensal_eletrico = consumo_diario * qtd_equipamentos * dias_mes
    custo_mensal_eletrico = consumo_mensal_eletrico * tarifa

    return custo_mensal_eletrico

def calcular_impacto():
    global economia_mensal

    consumo_total_combustao = qtd_equipamentos * abastecimentos_dia * dias_mes * capacidade_tanque
    custo_combustao = consumo_total_combustao * valor_combustivel

    custo_eletrico = dados_eletrico()
    economia_mensal = custo_combustao - custo_eletrico

    print(f"\n🔥 Custo mensal com combustível: R$ {custo_combustao:.2f}")
    print(f"⚡ Custo mensal com energia elétrica: R$ {custo_eletrico:.2f}")
    print(f"✅ Economia mensal estimada: R$ {economia_mensal:.2f}")

    co2_evitar = (economia_mensal / 0.85) * 0.084  # Conversão estimada baseada no custo evitado
    print(f"🌿 Emissão evitada: {co2_evitar:.2f} kg de CO₂")

    calcular_payback()

def calcular_payback():
    opcao = input("\nDeseja calcular o payback da substituição? (s/n): ").lower()
    if opcao == 's':
        custo_unitario = float(input("Informe o custo de cada equipamento elétrico (R$): "))
        qtd = input(f"Quantidade a adquirir (padrão {qtd_equipamentos}): ")
        qtd = int(qtd) if qtd else qtd_equipamentos
        investimento_total = custo_unitario * qtd
        if economia_mensal > 0:
            payback = investimento_total / economia_mensal
            print(f"\n📊 Payback estimado: {payback:.1f} meses")
        else:
            print("⚠️ Economia mensal não definida. Verifique os dados.")

# Execução principal
while True:
    mostrar_menu()
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        dados_combustao()
    elif escolha == "2":
        dados_eletrico()
    elif escolha == "3":
        calcular_impacto()
    elif escolha == "0":
        print("Encerrando o sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
