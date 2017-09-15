import requests
from lxml import html

def read_file(filename):
    with open(filename) as input_file:
        text = input_file.read()
    return text


def parseEventsData():
    url = 'http://www.uldosug.com/afisha'
    r = requests.get(url)
    with open('test.html', 'w') as output_file:
        output_file.write(r.text.encode('UTF-8'))
    filename = 'test.html'
    text = read_file(filename)
    result = []
    tree = html.fromstring(text)
    list_blocs = tree.xpath('//div[@class = "aidanews2_positions"]')
    titles = list_blocs[0].xpath('//div[@class = "aidanews2_head"]')[0].xpath(
        '//h3[@class = "aidanews2_title"]/a/text()')
    text = list_blocs[0].xpath('//div[@class = "aidanews2_main"]')[0].xpath('//span[@class = "aidanews2_text"]')
    i = 0
    while i < len(text):
        result.append(titles[i] + text[i].text)
        i += 1
    return result
