import pandas as pd


def adding_per(lines, per):
	for i in range(lines):
		per.append("D")
	return per

def adding_time(lines, time):
	for i in range(lines):
		time.append("000000")
	return time

per = []
time = []
cols = ['quandl_code','date','open','high','low','settle','volume']

df = pd.read_excel('CL.xlsx', index_col=None, usecols=cols)
lines = df.shape[0]
print(lines)
df.insert(1, 'per', adding_per(lines, per))
df.insert(3, 'time', adding_time(lines, time))
df.columns = ["<TICKER>","<PER>","<DATE>","<TIME>","<OPEN>","<HIGH>","<LOW>","<CLOSE>","<VOL>"]
# print(df)

df.to_csv("test.csv", index=False)



# columns = df[['quandl_code','date','open','high','low','settle','volume']]
# new_df = columns.copy
# df.to_csv("test.csv", )
# csv = pd.read_csv("test.csv", )
# print(csv)
# print(new_df)