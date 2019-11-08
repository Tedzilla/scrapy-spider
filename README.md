# scrapy-spider
Project created with educational purposes.

Технологичен стак:
*  [python](https://www.python.org/)
*  [Scrapy](https://scrapy.org/)

Използвайки Scrapy, извлечете/кролнете следният [лист](https://www.dea.gov/fugitives/all) с издирвани престъпници от
DEA.  

Извлечете и запишете информация за всеки един от описаните профили на престъпници.
*  name
*  alias
*  violations
*  race
*  sex
*  height
*  weight
*  hair color
*  eye color
*  year of birht
*  last known addres
*  NCIC
*  jurisdiction
*  Notes

Запишете информацията в csv.

Напишете скрипт на питон, който от запазената информация да генерира файл,  
като keyword arguments да е възможно да се подават:
*  --format=json/xml формат на оутпута
*  --outputfile='file_name.format' по дефолт оутпут на скрипта да е stdout, ако се подаде outputfile да се записва в файл дефолт format json
*  --sex=male/female output с престъпници от по пол
*  --yob=1985 output с престъпници от родени в подадената година
*  --name='Ezequiel' search by name
