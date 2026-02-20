import argparse
from bot.client import BinanceFuturesClient
def main():
            parser=argparse.ArgumentParser(description="Hi,Binance Futures Testnet Trading Bot")
            
            parser.add_argument("--symbol", type=str,required=True,help="specify the symbol")
            parser.add_argument("--side",choices=["BUY", "SELL"] ,required=True,type=str, help="specify the side")
            parser.add_argument("--type", choices=["MARKET", "LIMIT"],required=True, help="specify the type(MARKET / LIMIT)")
            parser.add_argument("--quantity", type=float,required=True,help="specify the quantity")
            parser.add_argument("--price", type=float, help="specify the price")
            args=parser.parse_args()
            args.symbol = args.symbol.upper()
            client=BinanceFuturesClient()
            if args.type == "LIMIT" and not args.price:
                print("Error: Price is required for LIMIT orders")
                exit(1)
            if args.quantity <= 0:
                print("Error: Quantity must be greater than 0")
                exit(1)


            if args.type == "MARKET":
                response = client.place_order(args.symbol, args.side, args.quantity)
            else:
                response = client.limit_order(args.symbol, args.side, args.quantity, args.price)

            if response:
                print("Order executed successfully")
                print(f"Order ID: {response.get('orderId')}")
                print(f"Status: {response.get('status')}")
                print(f"Executed Quantity: {response.get('executedQty')}")

                avg_price = response.get("avgPrice")
                if avg_price:
                    print(f"Average Price: {avg_price}")
            else:
                print("Order failed")


if __name__ == "__main__":
    main()