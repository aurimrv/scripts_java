import sys
from bs4 import BeautifulSoup as bs
import re

if len(sys.argv) < 3:
	print("error: randoop-reports.py <CSV DIR> <CSV-Base-Name> <SerieName>")
	print("Example: randoop-reports.py Tabelas/randoop-maior report-RegressionTest Maior")
	sys.exit(1)

csvdir = sys.argv[1]
csvbase = sys.argv[2]
csvserie = sys.argv[3]

#Reinicializa arquivo de saida
outCov = open('consolidated-coverage-'+csvserie+'.csv', 'w')
outMut = open('consolidated-score-'+csvserie+'.csv', 'w')


for id in range(1,33):
	outCov.write(str(id)+';')
	outMut.write(str(id)+';')
	
	for csv in range(0,30):
		csvname = csvdir + '/' + csvbase + str(csv) + csvserie + '-' + str(csv) + '.csv'
		
		dados = open(csvname, 'r')
		
		count=1
		
		for x in dados:
			if (count == id):
				x = x.strip()
				info = x.split(';')
				cov = info[2]
				score = info[5]
				outCov.write(str(cov)+';')
				outMut.write(str(score)+';')
				break
			else:
				count = count + 1
			
		dados.close()
		
	outCov.write('\n')
	outMut.write('\n')

outCov.close()
outMut.close()