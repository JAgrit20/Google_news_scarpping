from sqlite3 import Cursor
import psycopg2
import requests
from bs4 import BeautifulSoup
import uuid
import random
import os.path
import sys, os



from boto3 import session

from botocore.client import Config

ACCESS_ID = 'DO008G7NQJWP9X94A9DU'
SECRET_KEY = 'qv67dcZlrGQKeGLT0/jAxMXMUn5lC5qc26gvb+bmm50'


def connectSQL(title,comp,url):
		try:
			connection = psycopg2.connect(user="doadmin",
										password="AVNS_RCeNg6wvaknnSmFUmDy",
										host="ebooks-pdf-database-do-user-12810010-0.b.db.ondigitalocean.com",
										port="25060",
										database="defaultdb")
			cursor = connection.cursor()
			postgres_insert_query = """INSERT INTO the_indegenous_backend_book (title,description,year,url) VALUES  (%s,%s,%s,%s)"""
			record_to_insert = (title,comp,2022,url)
			cursor.execute(postgres_insert_query, record_to_insert)
			# cursor.execute(postgres_insert_query)

			connection.commit()
			count = cursor.rowcount
			print(count, "Record inserted successfully into mobile table")

		except (Exception, psycopg2.Error) as error:
			print("Failed to insert record into mobile table", error)

skip=1
for i in range(10   ):
    	

	url = f"https://indiankanoon.org/search/?formInput=doctypes%3A+supremecourt+fromdate%3A+1-1-1947+todate%3A+31-3-2023&pagenum={i}"


	# Requests URL and get response object
	response = requests.get(url,timeout=15) 

	# Parse text obtained
	soup = BeautifulSoup(response.text, 'html.parser')

	# Find all hyperlinks present on webpage
	links = soup.find_all(class_ = "item-ttl C C2")

	i = 0

	# From all links check for pdf link and
	# if present download file
	for link in links:
		
		# print(link)
		try:
			if(skip>1):
				ans = link.find('a')['href']
				print("ans",ans)
				filename = ans.split('/')[-1]
				print("filename",filename)

				comp_url =( "https://archive.org/"+ans)

				# data_type =link.get('data-category')
				response_2 = requests.get(comp_url,timeout=15) 
					# Parse text obtained
				soup = BeautifulSoup(response_2.text, 'html.parser')
				# Find all hyperlinks present on webpage
				links_2 = soup.find_all(class_ = "format-summary download-pill")
				title = soup.find(class_ = "breaker-breaker").text
				print("title",title)
				for hit in links_2:
						
						i=i+1
						hit_detail = hit.text.strip()	
						if(hit_detail == "PDF              download"):
								try:
									# print("yes inside",hit['href'])
									
									comp_url =( "https://archive.org"+hit['href'])
									print("comp_url",comp_url)
								

									print("File ",title , " uploaded")

								except Exception as ex:
									template = "An exception of type {0} occurred. Arguments:\n{1!r}"
									exc_type, exc_obj, exc_tb = sys.exc_info()
									message = template.format(type(ex).__name__, ex.args)
									print (message,exc_tb.tb_lineno)
			else:
				print(skip)
				skip=skip+1


		except Exception as ex:
			
			template = "An exception of type {0} occurred. Arguments:\n{1!r}"
			exc_type, exc_obj, exc_tb = sys.exc_info()
			message = template.format(type(ex).__name__, ex.args)
			print (message,exc_tb.tb_lineno)

