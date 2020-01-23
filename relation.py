CloseDf=pd.DataFrame()

# For all coin keep Close feature
for coin in crypto:
  CloseDf[coin] = crypto[coin]['Close']

# Get the correlation
CloseDfCorr = CloseDf.corr()

print(CloseDfCorr["bitcoin"])


bitcoin 1.000000

bitconnect 0.965897

dash 0.962461

ethereum_classic 0.872567

ethereum 0.933576

litecoin 0.941633

monero 0.919344

nem 0.951953

neo 0.839645

omisego 0.908620

qtum 0.490948

ripple 0.798784

stratis 0.881124

waves 0.924165
