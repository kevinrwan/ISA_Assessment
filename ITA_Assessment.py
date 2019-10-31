import pandas as pd
import json



def population_counter(file, zip):

	df = pd.read_csv(file)

	#checks if valid zip is entered
	if any(df['JURISDICTION NAME'] == zip):
		
		#returns row of table where zip code equals zip paramater value
		df2 = df.loc[df['JURISDICTION NAME'] == zip]

		#stores female count in variable cf
		cf = int(df2['COUNT FEMALE'])
		#stores male count in variable mf
		mf = int(df2['COUNT MALE'])

		#creates python dictionary variable 
		vals = {
		    "count_female": cf,
		    "count_male": mf
		}

		#convert to json string
		js = json.dumps(vals)

		print(js)

	else:
		print("Invalid zip")


population_counter("Demographic_Statistics_By_Zip_Code.csv",10001)
population_counter("Demographic_Statistics_By_Zip_Code.csv",10002)
population_counter("Demographic_Statistics_By_Zip_Code.csv",10003)
population_counter("Demographic_Statistics_By_Zip_Code.csv",1)

