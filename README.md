# Black Litterman Investment Portfolio Optimisation using Fear-Greed Index and Markov-Switching

Black Litterman model for investment portfolio optimisation, consisting of three variants and a benchmark model. The aim of this work is to extend the traditional Black Litterman model and move away from arbitrary and uneducated perceptions about asset performances and corresponding certainties about these views.

### Key terms:
<ul>
    <li> Fear-Greed - Score used to gauge market behaviour, where a lower value indicates fear, and a higher value indicates greed. Typically consisting of seven indicators (although this implementation uses five): Relative Strength Index (RSI), Stock price strength, price breadth, market volatility, and Put-Call Ratio.
    <li> Markov-Switching - A method of regime switching where market conditions can be categorised based on whether they're in a bullish or bearish state.
</ul>

## Models:
<ol>
  <li>Benchmark Black Litterman model
  <li>Variant 1 (FG-BL): Integrates Fear-Greed sentiment indicators as a proxy for investor views
  <li>Variant 2 (MS-BL): Integrates Markov-Switching to generate view confidences
  <li>Variant 3 (FGMS-BL): Combines Fear-Greed indicators and Markov-Switching to generate both investor views and view confidences
</ol>

## Running a Model:

Each model variant has its own Jupyter Notebook. Use the steps below to run any of the models.

First, clone the repository.

Next, run the following command. This will replicate the original package setup:
```
$ pip install -r requirements.txt
```

As a user of the models, all you need to do from here is set the time period for which the asset data will be based on (from yFinance). From here, define the assets you wish to use in the portfolio allocation. These will need to be defined by their tickers i.e. Apple would be AAPL (required for data retrieval from Yahoo Finance API). This can be any number of assets, and just needs to be defined within the 'tickers' array.

## Model Components:

Each model produces several metrics that can be used to gauge the portfolio's performance and sensitivity. Performance can be assessed against either Minimum Volatility or Max Sharpe portfolios. The following metrics are produced by optimisations:
<ul>
    <li>Annual returns
    <li>Annual volatility
    <li>Sharpe Ratio (excess return per unit of risk)
    <li>Discrete Allocation (how much of each asset needs purchasing to achieve the optimal portfolio)
    <li>Sensitivity analysis of: Views, confidences, Prior, Tau
</ul>
