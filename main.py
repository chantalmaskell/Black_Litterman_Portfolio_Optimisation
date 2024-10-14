import numpy as np
import pandas as pd
import scipy as sp
import yfinance as yf
import pypfopt
import matplotlib.pyplot as plt

from pypfopt import black_litterman, plotting
from pypfopt import BlackLittermanModel
from pypfopt.efficient_frontier import EfficientFrontier

class BlackLittermanAllocation:
    tickers = ["TSLA", "NVDA", "AMZN", "META", "MSFT", "AAPL", "AMD"] # Initial asset universe
    start_date = '2013-01-01'
    end_date = '2024-01-01'

    def Download_YFinance_Data(self, tickers, start_date, end_date):
        data = yf.download(tickers, start=start_date, end=end_date)
        # print(data.head())
        closing_prices = data["Adj Close"]
        closing_prices.head(10)

        returns = np.log(closing_prices / closing_prices.shift(1).dropna())
        return returns
    
    def Construct_Prior(self, start_date, end_date):
        # Construct priors (market equillibrium)
        market_prices = yf.download("VOO", start=start_date, end=end_date)["Adj Close"]
        return market_prices

    def Get_Market_Caps(self, tickers):
        market_caps = {}

        for ticker in tickers:
            stock = yf.Ticker(ticker)
            market_caps[ticker] = stock.info["marketCap"]
        return market_caps

    def Create_Covariance_Matrix(self, returns):
        # create covariance matrix of stocks (correlations/movements in prices)
        covariance_matrix = returns.cov()
        return covariance_matrix

    def Plot_Covariance_Matrix(self, covariance_matrix):
        plotting.plot_covariance(covariance_matrix, plot_correlation=True)
        plt.show()

    def Create_Prior_Delta(self, market_prices, market_caps, delta, covariance_matrix):
        delta = black_litterman.market_implied_risk_aversion(market_prices)
        prior = black_litterman.market_implied_prior_returns(market_caps, delta, covariance_matrix)
        return delta, prior

    def Calculate_Weights(self, cov_matrix):
        view_dict = {"NVDA": 0.05, "AMD": 0.03}
        bl = BlackLittermanModel(cov_matrix, absolute_views=view_dict)
        returns_series = bl.bl_returns()
        return returns_series

    def Plot_Efficient_Frontier(self, returns_series, cov_matrix):
        efficient_frontier = EfficientFrontier(returns_series, cov_matrix)
        
        weights = efficient_frontier.max_sharpe()  # Maximise Sharpe
        cleaned_weights = efficient_frontier.clean_weights()
        
        plotting.plot_efficient_frontier(efficient_frontier)
        plt.show()

        print(cleaned_weights)

        # InstantiationError: Adding constraints to an already solved problem might have unintended consequences. 
        # A new instance should be created for the new set of constraints.
        return efficient_frontier

allocation = BlackLittermanAllocation()
returns = allocation.Download_YFinance_Data(allocation.tickers, allocation.start_date, allocation.end_date)
cov_matrix = allocation.Create_Covariance_Matrix(returns)
bl_returns = allocation.Calculate_Weights(cov_matrix)
plot_efficient_frontier = allocation.Plot_Efficient_Frontier(bl_returns, cov_matrix)