from xml.dom import minidom
import sys
import os
from bs4 import BeautifulSoup as bs
import re

if len(sys.argv) < 2:
	print("error: metrics-xml.py <Project-List-File>")
	print("Example: metrics-xml.py files-completo.txt")
	sys.exit(1)

dados = open(sys.argv[1], 'r')

output = open('prj-metrics.csv', 'w')

output.write("ID;#Classes;#Methods;NCSS;Max CC;Avg CC\n")

count=1
for x in dados:
	x = x.strip()
	info = x.split(':')
	prj = info[0]
	clazz = info[1]
	
	print(prj)
	
	java = clazz.replace('.','/') + '.java'
	xml = prj+'.xml'
	
	cmd = "/local/tools/javancss-32.53/bin/javancss -package -function -xml "
	cmd = cmd + prj+"/src/main/java/" + java + " > " + xml

	os.system(cmd)


	output.write(str(count)+':')
	
	#coletando dados da classe
	xmldoc = minidom.parse(xml)

	pkg=xmldoc.getElementsByTagName('package')

	for node in pkg:
		for val in ['classes','functions','ncss']:
			alist=node.getElementsByTagName(val)
			for a in alist:
				output.write(a.firstChild.data+':')
	
	#coletando CC maxima
	maior=0
        
	pkg=xmldoc.getElementsByTagName('function')

	for node in pkg:
		alist=node.getElementsByTagName('ccn')
		for a in alist:
			atual = int(a.firstChild.data)
			if atual > maior:
				maior = atual

	output.write(str(maior)+':')

	#obtendo dados do CC medio
	
	pkg=xmldoc.getElementsByTagName('function_averages')

	for node in pkg:
		alist=node.getElementsByTagName('ccn')
		for a in alist:
			output.write(a.firstChild.data)

	#iniciando nova linha
	count = count + 1
	output.write("\n")