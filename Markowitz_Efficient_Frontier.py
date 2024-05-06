import yfinance as yf
from pypfopt import EfficientFrontier
from pypfopt import risk_models
from pypfopt import expected_returns
from pypfopt import plotting as plot
import matplotlib.pyplot as plt
import copy
import numpy as np
import pandas as pd
import seaborn as sns


inicio = input('Qual o início da sua análise? Usar formato yyyy-mm-dd:\n')
print(inicio)
fim = input('Qual o fim da sua análise?Usar formato yyyy-mm-dd:\n')
montante = float(input('Insira o valor do seu investimento inicial:\n'))

tickers = ['ITUB4.SA','GGBR4.SA','WEGE3.SA','BBAS3.SA','MDIA3.SA','MGLU3.SA']
cotacao = yf.download(tickers, start=inicio, end=fim)['Adj Close']
benchmark = yf.download('^BVSP', start=inicio, end=fim)['Adj Close']
benchmark.rename(index={'Name': 'Primeira'}, inplace=True)

retornos = cotacao.pct_change().dropna()
rt_benchmark= benchmark.pct_change().dropna()
mtx_corr = cotacao.corr().__round__(2)
mtx_cov = risk_models.sample_cov(cotacao)
exp_ret = expected_returns.mean_historical_return(cotacao)

def markowitz(exp_ret, mtx_cov):

    ef = EfficientFrontier(exp_ret, mtx_cov)

    fig, ax = plt.subplots(figsize=(8,6))

    ef_mkz = copy.deepcopy(ef)
    plot.plot_efficient_frontier(ef,show_assets=False,show_tickers=True)

    ef_mkz.efficient_return(target_return=0.06,market_neutral=False)
    ret_tangent, std_tangent, _ = ef_mkz.portfolio_performance(verbose=True)
    ax.scatter(std_tangent, ret_tangent, marker="*", s=300, c="violet", label="Portfólio de Markowitz")

    n_samples = 1000
    w = np.random.dirichlet(np.ones(ef.n_assets), n_samples)
    rets = w.dot(ef.expected_returns)
    stds = np.sqrt(np.diag(w @ ef.cov_matrix @ w.T))

    ef = EfficientFrontier(exp_ret, mtx_cov)
    pesos_otimos = ef.efficient_return(target_return=0.1)
    pesos = pd.DataFrame.from_dict(pesos_otimos, orient='index')
    pesos.columns = ['Pesos Ótimos']
    print(pesos)

    cotacao['Portfolio Otimo'] = 0

    for ticker, pesos_otimos in pesos_otimos.items():
        cotacao['Portfolio Otimo'] += cotacao[ticker] * pesos_otimos

    pd.DataFrame.to_excel(cotacao,excel_writer='MatrizPortfolio.xlsx')

    pd.DataFrame.to_excel(mtx_cov,excel_writer='mtxcov.xlsx')

    ax.scatter(stds, rets, marker="o", c=stds, cmap="inferno")
    ax.set_title("Fronteira Eficiente do Portfólio")
    plt.tight_layout()
    plt.ylabel('Retorno',color='k')
    plt.xlabel('Risco',color='k')
    ax.legend()

    fig, ax2 = plt.subplots(figsize=(8,6))
    ax2.plot(cotacao)
    ax2.legend(tickers,loc='upper left')
    plt.xlabel('Data',color='k')
    plt.ylabel('Cotações',color='k')
    plt.title('Histórico de Cotações',color='k')

    fig, ax3 = plt.subplots(figsize=(8,6))
    sns.displot(retornos,color='k',kde=True)
    plt.xlabel('Classes',color='k')
    plt.ylabel('Frequência',color='k')
    plt.title('Distribuição dos Retornos do Portfólio',color='k')

    fig, ax4 = plt.subplots(figsize=(8,6))
    ret_port = 1 + cotacao['Portfolio Otimo'].dropna().pct_change()
    ret_port = ret_port.cumprod() * montante
    ret_index = (1 + benchmark.dropna().pct_change()).cumprod() * montante
    klaus = pd.concat([ret_port,ret_index],axis=1)
    klaus.rename(columns={'Adj Close':'Retorno do Benchmark'},inplace=True)
    print(klaus)
    sns.lineplot(klaus)
    plt.title('Retornos Cumulativos')
    plt.xlabel('Período de Tempo',color='k')
    plt.ylabel('Retornos sobre Investimento Inicial Compostos',color='k')
    plt.legend()

    plt.show()



markowitz(exp_ret,mtx_cov)







