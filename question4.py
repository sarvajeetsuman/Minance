"""
Written to get data from NSEINDIA
"""

import os
import io
import requests
import zipfile
import datetime
from bs4 import BeautifulSoup


if __name__ == "__main__":
	base_date = datetime.datetime.today()

	num_of_days = 365
	date_list = [base_date - datetime.timedelta(days=x) for x in range(0, num_of_days)] # Date list
	# print(date_list)

	file_open = open("data.csv", "a")
	file_open.write("SYMBOL,SERIES,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,TOTTRDQTY,TOTTRDVAL,TIMESTAMP,TOTALTRADES,ISIN,\n") # Header Line
	file_open.close()
	base_link = "https://nseindia.com"
	for item in date_list:
		date_obj = "{:%d-%m-%Y}".format(item)
		first_url = "/ArchieveSearch?h_filetype=eqbhav&date={0}&section=EQ".format(date_obj)
		first_full_url = base_link + first_url # First API URL
		print(first_full_url)
		response = requests.get(first_full_url)
		content = response.content
		soup = BeautifulSoup(content, "html.parser")
		full_link = ""
		try:
			link = soup.find("a")
			par_link = link["href"]
			full_link = base_link + par_link
		except Exception as e:
			continue
		try:
			data = requests.get(full_link)  #ZIP FILE
			z = zipfile.ZipFile(io.BytesIO(data.content))
			z.extractall()
			lst =[]
			lst = z.namelist()
		except Exception as e:
			continue
		if lst:
			file_open = open("data.csv", "a") 
			for name in lst:
				with open(name, "r") as data_file:
					data_from_csv = data_file.read().splitlines(True)
				os.remove(name)
				file_open.writelines(data_from_csv[1:])  # Append File without header
			file_open.close()

