import sys
import os
from bs4 import BeautifulSoup as bs
import re

if len(sys.argv) < 2:
	print("error: run.py <TestCaseName>")
	print("Example: run.py ds.Evo")
	sys.exit(1)


test = sys.argv[1]

dados = open('files-completo.txt', 'r')
output = open('report-' + test + '.csv', 'w') 

output.write("PRJ;CLASSE;Cobertos;Gerados;Cobertura;Mortos;Total;Escore\n")

for x in dados:
	x = x.strip()
	info = x.split(':')
	prj = info[0]
	clazz = info[1]
	
	#cmd = "cd " + prj + "; mvn -DclassName=\"" + clazz + "\" -DtestName=\""+ test
	#cmd = cmd + "\" clean install org.pitest:pitest-maven:mutationCoverage"
	#os.system(cmd)
		
	html = open(prj+"/reports/"+test+"/index.html",'r')
				
	soup = bs(html, 'html.parser')
	divs = soup.findAll(attrs={'class':'coveragePercentage'})
	covs = soup.findAll(attrs={'class':'coverage_ledgend'})

	output.write(prj + ";")
	output.write(clazz + ";")
	output.write(covs[2].text.split("/")[0].strip() + "/")
	output.write(covs[2].text.split("/")[1].strip() + ";")
	output.write(divs[0].text.strip() + ";")

	output.write(covs[3].text.split("/")[0].strip() + "/")
	output.write(covs[3].text.split("/")[1].strip() + ";")
	output.write(divs[1].text.strip() + "\n")


dados.close()
output.close()
