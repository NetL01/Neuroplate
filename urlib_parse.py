# f = urllib.request.urlopen("https://streambet.cc/slots/sr_aviator?mode=demo").read()
# print(f)

import urllib.request

user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'

url = "https://streambet.cc/slots/sr_aviator?mode=demo"
headers={'User-Agent':user_agent,}

request=urllib.request.Request(url,None,headers) #The assembled request
response = urllib.request.urlopen(request)
data = response.read() # The data u need
print(data)