import pandas as pd
from os import listdir
from os.path import isfile, join

def adding_per(lines, per):
	for i in range(lines):
		per.append("D")
	return per

def adding_time(lines, time):
	for i in range(lines):
		time.append("000000")
	return time

def convert(files, cols):
	index = 1
	for file in files:
		deleted_part = '.xlsx'
		lines = 0
		per = []
		time = []
		df = pd.read_excel('import/'+file, index_col=None, usecols=cols)
		df['date'] = df['date'].dt.strftime('%Y%m%d')
		lines = df.shape[0]
		df.insert(1, 'per', adding_per(lines, per))
		df.insert(3, 'time', adding_time(lines, time))
		df.columns = ["<TICKER>","<PER>","<DATE>","<TIME>","<OPEN>","<HIGH>","<LOW>","<CLOSE>","<VOL>"]
		df.to_csv("export/"+(file.split('.xlsx')[0])+".csv", index=False)
		print(str(index)+ "/"+ str(len(files)) + " File " + file + " done!")
		index += 1

if __name__ == '__main__':
	dirName = "import"
	files = [f for f in listdir(dirName) if isfile(join(dirName, f))]
	print("Total files: " + str(len(files)))
	cols = ['quandl_code','date','open','high','low','settle','volume']
	convert(files, cols)