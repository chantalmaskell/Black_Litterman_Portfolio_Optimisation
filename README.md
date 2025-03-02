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

## Running the Models:

Each model variant has its own Jupyter Notebook. Use the steps below to run the models:

<ol>
    <li>Clone the repository.</li>
    <li></li>
</ol>
