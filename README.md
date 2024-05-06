# Fronteira Eficiente de Markowitz
Utilizando a biblioteca PyPortfolio para realizar uma otimização de portfolio pelos critérios da Teoria Moderna dos Portfólios.

Um dos desafios de um gestor de portfólios ou um gestor de riscos é encontrar a melhor combinação de ativos que leve ao máximo retorno esperado com o menor risco. A dificuldade de realizar esse tipo de tarefa é que é necessário levar em conta não apenas o risco dos ativos individuais, mas como o risco é modificados pela _combinação_ de ativos. Isso é medido por uma matriz de covariância entre os ativos. Markowitz (1952) solucionou esse problema ao considerar a criação de uma "fronteira de eficiência" daqueles portfólios teóricos que estariam no limite das preferências de risco de um agente econômicos. Dentro dessa fronteira existiria, no entanto, ao menos um portfólio que maximizaria o retorno esperado com o menor risco possível; considerando que o retorno de um portfólio é o somatório dos retornos esperados dos ativos individuais multiplicado pelos _pesos_ de cada ativo dentro da carteira de investimentos. 

A grande dificuldade computacional da fronteira de eficiência está em determinar quais seriam os pesos que criariam o portfólio ótimo segundo os critérios de eficiência de Markowitz. Para nossa sorte, o Python possui uma biblioteca voltada somente para isso que facilita enormemente esse trabalho outrora hercúleo. A *PyPortfolioOpt* possui uma série de funções que permite que seja realizado uma otimização de portfólio; tanto pelo critério de eficiência de Markowitz como pela maximização do Índice de Sharpe. 

O presente código mostra como realizar esse tipo de otimização. O resultado gráfico é a criação de uma fronteira de eficiência:

![image](https://github.com/Sav-Coelho/Fronteira-Eficiente-de-Markowitz/assets/116724820/f6950676-788f-4f4c-a43d-a89f8e581ee2)

Além disso, o algoritmo elaborado ainda nos trás os pesos ótimos do portfólio:

![image](https://github.com/Sav-Coelho/Fronteira-Eficiente-de-Markowitz/assets/116724820/23dfdd8b-1289-44fa-b603-a8213f3f4a3c)

E o retorno esperado ao longo do período selecionado, o risco e o índice de sharpe do mesmo:

![image](https://github.com/Sav-Coelho/Fronteira-Eficiente-de-Markowitz/assets/116724820/1a62af66-2c98-47a6-9c08-cd227156b288)

Mas esse portfólio gerado é realmente bom para um investimento real? Sim, ele é. O portfólio gerado e calibrado pelo algoritmo ao longo do tempo bate o benchmark do Ibovespa em retorno compostos:

![image](https://github.com/Sav-Coelho/Fronteira-Eficiente-de-Markowitz/assets/116724820/dd63dda5-91ed-4f2f-af93-c1e268ae2f69)



 
