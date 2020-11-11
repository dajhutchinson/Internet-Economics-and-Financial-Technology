import secrets
import eikon as ek

ek.set_app_key(secrets.APP_KEY)

""" REAL TIME DATA """
# df,err=ek.get_data(
#     instruments=["LLOY.L"],
#     fields=["BID","ASK"]
# )
# print(df)

""" REAL TIME DATA STREAM """
# streaming_prices = ek.StreamingPrices(
#     instruments = ['EUR=',"GBP="],
#     fields = ['DSPLY_NAME', 'BID', 'ASK'],
#     on_update = lambda streaming_price, instrument_name, fields :
#         print("Update received for {}: {}".format(instrument_name, fields))
# )
# streaming_prices.open()

""" FUNDAMENTALS ABOUT A BUSINESS """
# df, err = ek.get_data(
#     instruments = ['GOOG.O','MSFT.O', 'FB.O'],
#     fields = ['TR.LegalAddressCity','TR.LegalAddressLine1','TR.Employees']
# )
# print(df)

""" TIME SERIES FOR LAST DAY """
# df=ek.get_timeseries('AAPL.O', interval='minute')
# print(df.head(),df.tail())

""" HEADLINE NEWS """
df=ek.get_news_headlines('LLOY.L', count=10)
print(df.head()["text"])
