import requests
from rich import print
import pyfiglet
from pyfiglet import print_figlet


print_figlet('url mask')

print('[bold green]made by Taha Afous - github tahaXafous')
ourl = input('Enter your url :  ')
domain = input('Enter domain example : facebook.com or  anyting  :  ')
k = input('Enter keyword example : login or anything :  ')

response = requests.get(
        url='https://da.gd/shorten',
        params={'url':ourl}
    )
status = response.status_code
if status == 200 :

   re =  response.text.strip()
   u = re.replace('https://','')
   print('[bold green]Done ! ')
   print(f'[bold green]masked url :   https://{domain}-{k}@{u} ')
else:
   print(f'[bold red]error {status}')
