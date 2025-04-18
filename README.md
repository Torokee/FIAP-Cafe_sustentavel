
# ☕ Café Sustentável – Simulador de Economia e Impacto Ambiental

## 🎯 Objetivo
Este projeto tem como objetivo calcular a economia gerada na substituição de equipamentos agrícolas a combustão por modelos elétricos, promovendo sustentabilidade, redução de custos operacionais e diminuição das emissões de CO₂ na colheita de café.

## 🌱 Contexto
Nossa fazenda de café possui 270 hectares. Durante o período de colheita, que dura aproximadamente 30 dias, 50 funcionários utilizam equipamentos movidos a combustão com motor 4 tempos (modelo MM4 – 0,77 kW de potência e tanque de 0,6 L). Esses equipamentos são abastecidos duas vezes ao dia, em dois turnos.

Diante da crescente preocupação ambiental e dos avanços tecnológicos no agronegócio, o projeto visa simular a substituição desses motores por equipamentos elétricos Makita 40Vmax, que utilizam baterias recarregáveis.

## 💡 Como o sistema funciona

### 🔥 Dados do equipamento a combustão:
- Quantidade de equipamentos em uso
- Abastecimentos por dia
- Valor do combustível (R$/L)

### ⚡ Dados do equipamento elétrico:
- Tensão da bateria (V)
- Capacidade da bateria (Ah)
- Quantidade de baterias usadas por dia
- Tarifa de energia elétrica (R$/kWh)

> ⚠️ A eficiência do carregador é fixada internamente em 75%, com base em médias de mercado.

### 📊 O sistema então calcula:
- Custo mensal com combustível
- Custo mensal com energia elétrica
- Economia gerada pela substituição
- Estimativa de CO₂ evitado (0,084 kg por kWh economizado)
- (Opcional) Payback com base no custo de aquisição dos novos equipamentos

## 📈 Exemplo de resultado
🔥 Custo mensal com combustível: R$ 10.800,00  
⚡ Custo mensal com energia elétrica: R$ 2.754,00  
✅ Economia mensal estimada: R$ 8.046,00  
🌿 Emissão evitada: 755,76 kg de CO₂  
📊 Payback estimado: 7,1 meses

## 🧠 Conteúdos aplicados
- Subalgoritmos (funções)
- Estruturas de dados
- Cálculos matemáticos
- Entrada de dados com input()
- Estrutura condicional e repetição
- Princípios de sustentabilidade e eficiência energética

## ⚙️ Como executar
1. Execute o arquivo `main.py` em um ambiente Python (VSCode, IDLE ou terminal).
2. Siga o menu exibido na tela.
3. Informe os dados solicitados e veja os resultados.

## 🌍 Justificativa de Sustentabilidade
O uso de equipamentos elétricos reduz a dependência de combustíveis fósseis, elimina emissões diretas de gases poluentes no campo, diminui o ruído e os custos operacionais. O projeto estimula práticas agrícolas mais limpas e conscientes, utilizando tecnologia acessível e dados reais.

## 📎 Fonte de conversão CO₂
> Instituto de Energia e Meio Ambiente (IEMA): média nacional de 0,084 kg CO₂ evitado por kWh economizado.
