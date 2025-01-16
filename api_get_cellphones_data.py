import requests
import json

url = ""

headers = {""}

def fetch info():

'''
ESta funcion se dedca unicamente a hacer la consulta da la api seleccionada y almacenarla en un archivo json.
'''
	response = request.get(url, headers=headers)
	if response.status_code == 200:
	
		data = response.json()
		with open("datos.json", "w", encoding="utf-8") as file:
		    json.dump(data, file, indent=4, ensure_ascii=false)

		return data
	else:
	    print(f"Error al obtener datos %s"%response.status_code)
	    return -1	
		
def main
   phone_data = fetch_info()
   
if__name__ = "__main__"
	main()   
