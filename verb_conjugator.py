import requests
from bs4 import BeautifulSoup

class VerbConjugator:
    def __init__(self) -> None:
        pass

    def conjugate(self, verb):
        r = requests.get(f'http://www.japaneseverbconjugator.com/VerbDetails.asp?txtVerb={verb}')
        html = r.content
        parsed_html = BeautifulSoup(html, features="html.parser")    

        output = {"verb":verb}

        tablehtml = parsed_html.body.find('table', attrs={'class':'table table-bordered'})

        
        thlist = tablehtml.find_all('td')
        if "Godan" in thlist[0].text:
            output["verb_class"] = "godan"
        else:
            output["verb_class"] = "ichigan"


        output["stem"] = thlist[1].find('span').text
        output["te_form"] = thlist[2].find('span').text
        output["infinitive"] = thlist[3].find('span').text

        

