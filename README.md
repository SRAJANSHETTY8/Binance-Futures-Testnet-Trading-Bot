
# Binance Futures Testnet Trading Bot

Binance Futures Testnet Trading Bot is a Python-based command-line application that allows users to place MARKET and LIMIT orders on Binance Futures Testnet (USDT-M). The system provides structured logging, input validation, and proper error handling.

## Overview

Backend Python-based trading application using Binance Futures API to execute trades on the Testnet environment.

Command Line Interface allows users to input trading parameters such as symbol, side, order type, quantity, and price directly from the terminal.

Purpose: Demonstrates API integration, structured code design, logging practices, and exception handling for trading systems.

## Tech Stack

Python 3.x  
python-binance  
python-dotenv  
argparse  
logging  

API Used: Binance Futures Testnet (USDT-M)  
Base URL: https://testnet.binancefuture.com  

## Project Structure

bot/
  client.py
  cli.py
  logging_config.py

requirements.txt  
README.md  
.gitignore  

## Core Features

- Place MARKET orders  
- Place LIMIT orders  
- Support BUY and SELL  
- CLI input validation  
- Logging to file  
- Exception handling  

## Setup Instructions

Clone the repository:

git clone https://github.com/SRAJANSHETTY8/Binance-Futures-Testnet-Trading-Bot.git

Navigate into project folder:

cd Binance-Futures-Testnet-Trading-Bot

Install dependencies:

pip install -r requirements.txt

Create a .env file in the root directory and add:

BINANCE_API_KEY=your_testnet_api_key  
BINANCE_SECRET_KEY=your_testnet_secret_key  

## Running the Application

Example MARKET order:

python bot/cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.01

Example LIMIT order:

python bot/cli.py --symbol BTCUSDT --side BUY --type LIMIT --quantity 0.01 --price 30000

## Logging

All API requests, responses, and errors are logged inside the logs directory.

## Conclusion

This project demonstrates structured API integration, clean CLI design, logging implementation, and proper error handling while interacting with Binance Futures Testnet.
