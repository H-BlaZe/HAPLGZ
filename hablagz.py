#WAP to find plagiarism. [HAPLAGZ]

from googlesearch import *
import requests
from bs4 import BeautifulSoup

def main():
  foundstat = False
  quest=input('Enter question: ')
  ans=input("Enter the student's answer: ")
  count=int(input('Enter the number of websites you want to search: '))
  websites=[]

  #Creates a list with first n number of websites
  for site in search(quest, tld="co.in", num=count ,stop=count, pause=2):
    websites.append(site)

  #starts the loop
  for site in websites:
    url = site
    try:
      res = requests.get(url)
    except:
      print('Looks like something is preventing the system from proceeding in',site)
    html_page = res.content
    soup = BeautifulSoup(html_page, 'html.parser')
    text = soup.find_all(text=True)

    output = ''
    blacklist = [
        '[document]',
        'noscript',
        'header',
        'html',
        'meta',
        'head', 
        'input',
        'script',
        'style'
    ]

    for t in text:
        if t.parent.name not in blacklist:
            output += '{} '.format(t)
    print("---------")
     
    if ans in output:
      print('PLAGIARISM DETECTED : ',site)
      foundstat = True
      break
    else:
      print(':NF:')
      brk_ans=list(ans)
      lenans=len(ans)
      s_ans=''
      for i in range(int(lenans/2)):
        s_ans+=brk_ans[i]
      if s_ans in output:
        print('PLAGIARISM DETECTED : ',site)
      else:
        print(':NF:')
        continue
        
        
    #print(output)
  if foundstat == False:
    print("Couldn't find any plagiarism in first ",count, " wesbites.")
  print("---------")

main()
