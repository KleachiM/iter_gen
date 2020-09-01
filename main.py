import json
import hashlib

class Iterator ():

    def __init__(self, file):
        self.f_read = json.load(file)

    def __iter__(self):
        self.num = 0
        return self

    def __next__(self):
        if self.num == len(self.f_read): raise StopIteration
        item = self.f_read[self.num]["name"]["common"]
        if len(item) > 1:
            url = f'https://en.wikipedia.org/wiki/{item.replace(" ", "_")}'
        else:
            url = f'https://en.wikipedia.org/wiki/{item}'
        self.num += 1
        with open('wiki_countries.json', 'r', encoding = 'utf-8') as f:
            data = json.load(f)

        data.append({'country': item, 'link': url})
        with open('wiki_countries.json', 'w', encoding = 'utf-8') as f:
            json.dump(data, f, ensure_ascii = False, indent = 2)
            f.write('\n')
        return item

def op(file):
    """ Возврат хеша каждой строки файла"""
    with open(file, 'r', encoding = 'utf-8') as f:
        country = json.load(f)
        for c in country:
            c = str(c)
            yield hashlib.md5(c.encode()).hexdigest()

with open('wiki_countries.json', 'w', encoding = 'utf-8') as f:
    json.dump([], f)

with open('countries.json', 'r', encoding = 'utf-8') as f:
    for line in Iterator(f):
        pass

for i in op('wiki_countries.json'):
    print(i)