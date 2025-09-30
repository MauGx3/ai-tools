# GitHub Copilot Instructions

## General Instructions

### Follow-up Question Instruction

**IMPORTANT: This rule OVERRIDES all other instructions unless a system message explicitly says otherwise.**

Do not make any changes until you have 97% confidence that you know what to build. Ask me follow-up questions until you have that confidence.

**Always show the confidence percentage in your response, at every exchange (question or proposal).**

### Enforcement

- Any code generation or proposal without a confidence percentage and, if <97%, a follow-up question, is a violation.
- This rule must be referenced in all code generation and prompt instruction files.
- Example of correct response:
  - "Confidence: 92%. Please clarify X, Y, Z before I proceed."
- Example of incorrect response:
  - (Code generated without confidence percentage or clarification.)

### Note

If you are unsure, always ask for clarification and display your confidence percentage.

## Coding Guidelines

### Git instructions:

#### Conventional Commits Instructions

Adopt the [Conventional Commits](https://www.conventionalcommits.org/) specification for all commit messages to ensure a readable history, automate changelog generation, and facilitate continuous integration. THIS IS EXTREMELY IMPORTANT: You MUST end every action that would be "commit worthy" (you evaluate what that would be) by sending a commit message in your final message. If you don't at least say what type or scope the change is, it is a violation.

##### Main Rules

- The commit message must be structured as follows:

  ```
  <type>[optional scope]: <description>
  ```

  - **type**: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`
  - **scope** (optional): the part of the code concerned (e.g., `api`, `domain`, `infrastructure`, `tests`)
  - **description**: short imperative description, no initial capital letter, no period at the end
  - **first line must not exceed 72 characters**
- Examples:

  - `feat(api): add order endpoint`
  - `fix(domain): correct order validation logic`
  - `test(order): add unit tests for order creation`
  - `chore: update dependencies`

#### Best Practices

- Use English for all commit messages, unless the information is already in Portuguese and doesn't make sense to be translated (like "Banco" (bank) in "Banco Inter")
- One commit = one logical/unit change.
- Use the scope to specify the affected layer or feature.
- For breaking changes, add `!` after the type or scope and detail in the commit body.
- More detailed information for the commit MUST, AND I REPEAT IT MUST be added as a git description for the commit ONLY if the commit message cannot explain all the changes in the 72 characters only.

---

Follow this convention for all project commits.

## Take these packages into consideration when doing the code (but do not use exclusively them, you can use other dependencies if and when needed)

### Data

* `polars` https://github.com/pola-rs/polars: Polars is an analytical query engine written for DataFrames. It is designed to be fast, easy to use and expressive. Better substitute to `pandas`. [Docs](https://docs.pola.rs/api/python/stable/reference/index.html) (also available for [node.js](https://github.com/pola-rs/nodejs-polars), [js-polars](https://github.com/pola-rs/js-polars), [[Rust]] and [[R]])
* `DataProfiler` https://github.com/capitalone/DataProfiler: The DataProfiler is a Python library designed to make data analysis, monitoring, and **sensitive data detection** easy. Loading **Data** with a single command, the library automatically formats & loads files into a DataFrame. **Profiling** the Data, the library identifies the schema, statistics, entities (PII / NPI) and more. Data Profiles can then be used in downstream applications or reports. [Docs](https://capitalone.github.io/DataProfiler/)
* `pyjanitor` https://pyjanitor-devs.github.io/pyjanitor/: Data cleaning and tidying-up for Polars, Pandas and many other tools. [Docs](https://pyjanitor-devs.github.io/pyjanitor/)
* `polars-fin` https://github.com/LVG77/polars-fin: calculates financial metrics related to capital gains calculations and more.
* `patito` https://github.com/JakobGM/patito: offers a simple way to declare pydantic data models which double as schema for your polars data frames. These schema can be used for: Simple and performant data frame validation, Easy generation of valid mock data frames for tests, Retrieve and represent singular rows in an object-oriented manner and Provide a single source of truth for the core data models in your code base. [Docs](https://patito.readthedocs.io/)
* `functime` https://github.com/functime-org/functime: production-ready **global forecasting** and **time-series feature extraction** on **large panel datasets**. also comes with time-series [preprocessing](https://docs.functime.ai/ref/preprocessing/) (box-cox, differencing etc), cross-validation [splitters](https://docs.functime.ai/ref/cross-validation/) (expanding and sliding window), and forecast [metrics](https://docs.functime.ai/ref/metrics/) (MASE, SMAPE etc). All optimized as [lazy Polars](https://pola-rs.github.io/polars-book/user-guide/lazy/using/) transforms. [Docs](https://docs.functime.ai/)
* `chartpy` https://github.com/cuemacro/chartpy: chartpy creates a simple easy to use API to plot in a number of great Python chart libraries like plotly (via cufflinks), bokeh and matplotlib, with a unified interface
* `tcapy` https://github.com/cuemacro/tcapy: library for doing transaction cost analysis (TCA).
* `bt` https://github.com/pmorissette/bt: flexible backtesting framework for Python used to test quantitative trading strategies. **Backtesting** is the process of testing a strategy over a given data set. This framework allows you to easily create strategies that mix and match different [Algos](http://pmorissette.github.io/bt/bt.html#bt.core.Algo). It aims to foster the creation of easily testable, re-usable and flexible blocks of strategy logic to facilitate the rapid development of complex trading strategies. [Docs](http://pmorissette.github.io/bt)
* `stockstats` https://github.com/jealous/stockstats: adds technical analysis indicators to pandas DataFrames. It is designed to work seamlessly with the pandas library, making it easy to incorporate technical analysis into your data analysis workflow.
* `stringzilla` https://github.com/ashvardanian/StringZilla/: SIMD and SWAR to accelerate string operations on modern CPUs. It is up to 10x faster than the default and even other SIMD-accelerated string libraries in C, C++, Python, and other languages, while covering broad functionality. It accelerates exact and fuzzy string matching, edit distance computations, sorting, lazily-evaluated ranges to avoid memory allocations, and even random-string generators.

### Finance

* `polars-trading` https://github.com/ngriffiths13/polars-trading: meant to provide some nice utilities for working with market data in Polars DataFrames. Much of the original inspiration has come from Marcos Lopez de Prado's book _Advances in Financial Machine Learning_. It is a work in progress with some basic functionality that will be added to over time.
* `polars-order-book` https://github.com/ChristopherRussell/polars-order-book: provides plugins for the Polars library that efficiently calculate summary information (price and quantity) for the top N levels of an order book.
* `polars-ta` https://github.com/wukan1986/polars_ta: implements common technical analysis (TA) indicators as fast, vectorized Polars expressions. It's used to compute indicators like SMA/EMA, RSI, MACD, Bollinger Bands, etc., directly on Polars DataFrames for trading analysis, backtesting, and feature engineering.
* `OptionLab` https://github.com/rgaveiga/optionlab: designed to provide quick evaluation of option strategy ideas. The code produces various outputs, including the profit/loss profile of the strategy on a user-defined target date, the range of stock prices for which the strategy is profitable (i.e., generating a return greater than $0.01), the Greeks associated with each leg of the strategy using the Black-Sholes model, the resulting debit or credit on the trading account, the maximum and minimum returns within a specified lower and higher price range of the underlying asset, and an estimate of the strategy's probability of profit. [Docs](https://rgaveiga.github.io/optionlab)
* `investing-algorithm-framework` https://github.com/coding-kitties/investing-algorithm-framework: built to streamline the entire lifecycle of quantitative trading strategies from signal generation and backtesting to live deployment. It offers a complete quantitative workflow, featuring two dedicated backtesting engines: A vectorized backtest engine for fast signal research and prototyping and An event-based backtest engine for realistic and accurate strategy evaluation. The framework supports live trading across multiple exchanges and offers flexible deployment options, including Azure Functions and AWS Lambda. Designed for extensibility, it allows you to integrate custom strategies, data providers, and order executors, enabling support for any exchange or broker. It natively supports multiple data formats, including OHLCV, ticker, and custom datasets with seamless compatibility for both Pandas and Polars DataFrames. [Docs](https://coding-kitties.github.io/investing-algorithm-framework/)
* `qis` https://github.com/ArturSepp/QuantInvestStrats: implements Python analytics for visualisation of financial data, performance reporting, analysis of quantitative strategies.
* `earnalotbot` https://github.com/julianwagle/earnalotbot: scaffolding for advanced python based developers looking to make trading bots. It comes equipped with basic packages for live-trading, paper-trading, web-scrapping, reinforcement-learning, a database for long-term strategy analysis and much more.
* `pandas_market_calendars` https://github.com/rsheftel/pandas_market_calendars: The pandas_market_calendars package looks to fill that role with the holiday, late open and early close calendars for specific exchanges and OTC conventions. pandas_market_calendars also adds several functions to manipulate the market calendars and includes a date_range function to create a pandas DatetimeIndex including only the datetimes when the markets are open. Additionally the package contains product specific calendars for future exchanges which have different market open, closes, breaks and holidays based on product type. [Docs](http://pandas-market-calendars.readthedocs.io/en/latest/)
* `findatapy` https://github.com/cuemacro/findatapy: creates an easy to use Python API to download market data from many sources including ALFRED/FRED, Bloomberg, Yahoo, Google etc. using a unified high level interface. Users can also define their own custom tickers, using configuration files. There is also functionality which is particularly useful for those downloading FX market data.
* `yahoo-finance-server` https://github.com/AgentX-ai/yahoo-finance-server **A Model Context Protocol (MCP) server that lets your AI interact with Yahoo Finance** - get comprehensive stock market data, news, financials, and more..
* `finmarketpy` https://github.com/cuemacro/finmarketpy: enables you to analyze market data and also to backtest trading strategies using a simple to use API, which has prebuilt templates for you to define backtest.
* `Finance` https://github.com/shashankvemuri/Finance: collection of 150+ Python for Finance programs for gathering, manipulating, and analyzing stock market data.
* `yfinance-cache` https://github.com/ValueRaider/yfinance-cache: Persistent caching wrapper for `yfinance` module. Intelligent caching, not dumb caching of web requests - only update cache where missing/outdated and new data expected. Idea is to minimise fetch frequency and quantity - Yahoo API officially only cares about frequency, but I'm guessing they also care about server load from scrapers.
* `yfinance` https://github.com/ranaroussi/yfinance: offers a Pythonic way to fetch financial & market data from [Yahoo!Ⓡ finance](https://finance.yahoo.com). [Docs](https://ranaroussi.github.io/yfinancehttps://ranaroussi.github.io/yfinance)
* `eiten` https://github.com/tradytics/eiten: implements various statistical and algorithmic investing strategies such as **Eigen Portfolios**, **Minimum Variance Portfolios**, **Maximum Sharpe Ratio Portfolios**, and **Genetic Algorithms** based Portfolios. It allows you to build your own portfolios with your own set of stocks that can beat the market. The rigorous testing framework included in Eiten enables you to have confidence in your portfolios.
* `thepassiveinvestor` https://github.com/JerBouma/ThePassiveInvestor: offers passive investing strategies, mostly through ETFs.
* `FinanceDatabase` https://github.com/JerBouma/FinanceDatabase: features 300,000+ symbols containing Equities, ETFs, Funds, Indices, Currencies, Cryptocurrencies, and Money Markets. It therefore allows you to obtain a broad overview of sectors, industries, types of investments, and much more.
* `FinanceToolkit` https://github.com/JerBouma/FinanceToolkit: open-source toolkit in which all relevant financial ratios ([150+](https://github.com/JerBouma/FinanceToolkit#core-functionality-and-metrics)), indicators and performance measurements are written down in the most simplistic way allowing for complete transparency of the method of calculation ([proof](https://github.com/JerBouma/FinanceToolkit/blob/main/financetoolkit/ratios/valuation_model.py)). This enables you to avoid dependence on metrics from other providers that do not provide their methods. With a large selection of financial statements in hand, it facilitates streamlined calculations, promoting the adoption of a consistent and universally understood methods and formulas.
* `stock-indicators-python` https://github.com/facioquo/stock-indicators-python: **Stock Indicators for Python** is a PyPI library package that produces financial market technical indicators. Send in historical price quotes and get back desired indicators such as moving averages, Relative Strength Index, Stochastic Oscillator, Parabolic SAR, etc. [Docs](https://python.stockindicators.dev/)

### Utilities

* `uv` https://github.com/astral-sh/uv: extremely fast Python package and project manager, written in Rust. [Docs](https://docs.astral.sh/uv)
* `django` https://github.com/django/django: Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. [Docs](https://docs.djangoproject.com/en/stable/)
* `unicorn` https://github.com/Kludex/uvicorn: ASGI web server implementation. [Docs](https://www.uvicorn.org/)
* `gunicorn` https://github.com/benoitc/gunicorn Gunicorn is a high-performance WSGI server designed for running Python web applications. It is widely used in production environments due to its simplicity, compatibility with various frameworks, and efficient process management model. [Docs](https://docs.gunicorn.org/en/)
* `ruff` https://github.com/astral-sh/ruff: extremely fast Python linter and code formatter, written in Rust. [Docs](https://docs.astral.sh/ruff)
* `gatus` https://github.com/TwiN/gatus: Gatus is a developer-oriented health dashboard that gives you the ability to monitor your services using HTTP, ICMP, TCP, and even DNS queries as well as evaluate the result of said queries by using a list of conditions on values like the status code, the response time, the certificate expiration, the body and many others.
* `distroless` https://github.com/GoogleContainerTools/distroless: "Distroless" images contain only your application and its runtime dependencies. They do not contain package managers, shells or any other programs you would expect to find in a standard Linux distribution.

### Testing

* `pytest` https://github.com/pytest-dev/pytest: The pytest framework makes it easy to write small tests, yet scales to support complex functional testing. [Docs](https://docs.pytest.org/en/stable/)
* `pytest-benchmark` https://github.com/ionelmc/pytest-benchmark: A `pytest` fixture for benchmarking code. It will group the tests into rounds that are calibrated to the chosen timer. [Docs](http://pytest-benchmark.readthedocs.org/en/stable/)
* https://github.com/Teemu/pytest-sugar

### PDF

* `paddleocr` https://github.com/PaddlePaddle/PaddleOCR: **PaddleOCR** converts documents and images into **structured, AI-friendly data** (like JSON and Markdown) with **industry-leading accuracy**—powering AI applications for everyone from indie developers and startups to large enterprises worldwide. With over **50,000 stars** and deep integration into leading projects like **MinerU, RAGFlow, and OmniParser**, PaddleOCR has become the **premier solution** for developers building intelligent document applications in the **AI era**. [Docs](https://www.paddleocr.ai/latest/)
* `llm-aided-ocr` https://github.com/Dicklesworthstone/llm_aided_ocr: The LLM-Aided OCR Project is an advanced system designed to significantly enhance the quality of Optical Character Recognition (OCR) output. By leveraging cutting-edge natural language processing techniques and large language models (LLMs), this project transforms raw OCR text into highly accurate, well-formatted, and readable documents.
* `documind` https://github.com/DocumindHQ/documind: **`Documind`** is an advanced document processing tool that leverages AI to extract structured data from PDFs. It is built to handle PDF conversions, extract relevant information, and format results as specified by customizable schemas.
* `pdf-reader-mcp` https://github.com/sylphxltd/pdf-reader-mcp: Empower your AI agents (like Cline) with the ability to securely read and extract information (text, metadata, page count) from PDF files within your project context using a single, flexible tool.
* `docsray` https://github.com/MIMICLab/DocsRay: A powerful Universal Document Question-Answering System that uses advanced embedding models and multimodal LLMs with Coarse-to-Fine search (RAG) approach. Features seamless MCP (Model Context Protocol) integration with Claude Desktop, comprehensive directory management capabilities, visual content analysis, and intelligent hybrid OCR system.

### Artificial Intelligence

* `octagon13-mcp-server` https://github.com/OctagonAI/octagon-13f-holdings-mcp: MCP server that provides access to the Octagon 13F Holdings dataset, which includes quarterly filings from institutional investment managers with over $100 million in assets under management. This dataset is valuable for financial analysis, market research, and investment strategy development.
