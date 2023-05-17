import sys
import os
from bs4 import BeautifulSoup as bs
import re

if len(sys.argv) < 2:
	print("error: generate-randoop.py <CLASSES FILE NAMES>")
	print("Example: generate-randoop files-randoop.txt")
	sys.exit(1)


arquivo = sys.argv[1]

dados = open(arquivo, 'r')

for x in dados:
    x = x.strip()
    info = x.split(':')
    prj = info[0]
    clazz = info[1]
    limit = info[2]

    for y in range(0,30):
        test="RegressionTest" + str(y) + "Maior"
        
        output = open('report-' + test + "-" + str(y) + '.csv', 'a')
        
        cmd="cd " + prj + ";java -cp target/classes:/local/tools/randoop/randoop-all-3.0.1.jar randoop.main.Main gentests --testclass=" + clazz + " --outputlimit="+limit+" --junit-package-name=ds --junit-output-dir=src/test/java/ --regression-test-basename=" + test + " --randomseed="+str(y)
        
        # Para o programa 22 tem que omitir o metodo flaky
        if (prj == "22TabelaHash"):
            cmd = cmd + " --omitmethods=[.*]retira"

        print cmd
              
        os.system(cmd)
        
        
        cmd = "cd " + prj + "; mvn -DclassName=\"" + clazz + "\" -DtestName=\"ds."+ test
	cmd = cmd + "\" clean install org.pitest:pitest-maven:mutationCoverage"
	os.system(cmd)
		
	html = open(prj+"/reports/ds."+test+"/index.html",'r')#
				
	soup = bs(html, 'html.parser')
	divs = soup.findAll(attrs={'class':'coveragePercentage'})
	covs = soup.findAll(attrs={'class':'coverage_ledgend'})

	output.write(prj + ";")
	output.write(clazz + ";")
	output.write(covs[2].text.split("/")[0].strip() + ";")
	output.write(covs[2].text.split("/")[1].strip() + ";")
	output.write(divs[0].text.strip() + ";")

	output.write(covs[3].text.split("/")[0].strip() + ";")
	output.write(covs[3].text.split("/")[1].strip() + ";")
	output.write(divs[1].text.strip() + "\n")

        output.close()
        
dados.close()
