import requests
try:
    array = [] 
    requisicao = requests.get('https://putsreq.com/Y518kDHIyH2nw3fheBhk')
    print(requisicao.text)

except Exception as e:
    print("Requisição deu erro:", e) 
