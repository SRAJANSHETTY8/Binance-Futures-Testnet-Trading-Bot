from binance.exceptions import BinanceAPIException, BinanceOrderException
from binance.client import Client
from bot.logging_config import setup_logging
import os
from dotenv import load_dotenv
load_dotenv()
logger=setup_logging()
class BinanceFuturesClient:
    def __init__(self):
       self.api=os.getenv("BINANCE_API_KEY")
       self.secretkey=os.getenv("BINANCE_SECRET_KEY")
       if not self.api or  not self.secretkey:
           raise Exception("Missing Binance API credentials in environment variables")
       self.client=Client(self.api,self.secretkey)
       self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
       logger.info("Binance Futures Testnet client initialized successfully")
    def testconnection(self):
        try:
            response=self.client.futures_time()
            logger.info("Binance Futures Testnet client connected successfully")
            return True
        except BinanceAPIException as e:
           logger.error(f"Binance API error:{e}")
           return False
        except Exception as e:
            logger.error(f"Generic Exception{e}")
            return False
        
    def place_order(self,symbol,side,quantity):
        try:
            logger.info(f"Placing MARKET order: {symbol} {side} {quantity}")
            response=self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity)
            logger.info(f"Order placed successfully: {response}")
            return response
        except BinanceAPIException as e:
            logger.error(f"Binance API error:{e}")
            return None
    def limit_order(self,symbol,side,quantity,price):
        try:
            logger.info(f"Placing LIMIT order: {symbol} {side} {quantity} @ {price}")
            response=self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
                )
            logger.info(f"Order placed successfully: {response}")
            return response
        except BinanceOrderException as e:
             logger.error(f"Binance Order error: {e}")
             return None
        except BinanceAPIException as e:
            logger.error(f"Binance API error:{e}")
            return None
        except Exception as e:
            logger.exception("Unexpected error occurred")
            return None

