import json
import urllib.request

def find(search_name):
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        html = response.read()
   
    postal_codes=json.loads(html)

    if (search_name.upper() in postal_codes.values()) == True:
        list = ""
        for postal_place in postal_codes:
            if (postal_codes[postal_place] == search_name.upper().replace(" ", "")):
                list += " " + postal_place
        
        return 'Postinumerot:' + list
    
    else:
        return 'Postitoimipaikkaa ei löydy'

def manual():
    name = input("Kirjoita postitoimipaikka: ")

    print(find(name))

if __name__ == '__main__':
    manual()
