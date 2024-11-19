import sys
import requests
from lxml import html


def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    
    response = requests.get(url)

    if response.status_code != 200:
        print("chyba")
        return []
    
    webpage = html.fromstring(response.content)
    elements = webpage.xpath(f'//a/@href')
    
    #for el in elements:
    #    odkaz = el.text_content()
    #    hrefs.append(odkaz)
    hrefs.append(elements)
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        all_hrefs = download_url_and_get_all_hrefs(url)
        print(all_hrefs)
    # osetrete potencialni chyby pomoci vetve except
    except Exception as e:
        print(f"Program skoncil chybou: {e}")