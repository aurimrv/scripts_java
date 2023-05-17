from bs4 import BeautifulSoup as bs
import re

html = open("index.html")

soup = bs(html, 'html.parser')
divs = soup.findAll(attrs={'class':'coveragePercentage'})
covs = soup.findAll(attrs={'class':'coverage_ledgend'})

prj="01Max"
clazz="ds.Max"


print "PRJ;CLASSE;Cobertos;Gerados;Cobertura;Mortos;Total;Escore"

print prj,";",
print clazz,";",
print covs[2].text.split("/")[0],";",
print covs[2].text.split("/")[1],";",
print divs[0].text,";", 

print covs[3].text.split("/")[0],";",
print covs[3].text.split("/")[1],";",
print divs[1].text

