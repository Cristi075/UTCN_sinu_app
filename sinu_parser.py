import re


class SinuParser(object):
    def __init__(self):
        self.state=0
        # States description:
        # State = 0  - waiting for the table with class=table2
        # State = 1  - Take the next table element and parse it
        # State = 2  - When the table element that has a height property is reached (we stop there)

    def feed(self, html_data):
        self.state = 0
        result = []

        tables = re.findall('<table (.+?)</?table>', html_data)

        for table in tables:
            match = re.search('class="table2"', table)
            if match:
                self.state = 1
            elif self.state == 1:
                match2 = re.search('height', table)
                if match2:
                    self.state = 2
                    print self.state

                else:
                    data = re.findall('<td .+?>(.+?)</td>', table)

                    extracted={}
                    extracted['An'] = str(int(data[0]))
                    extracted['Semestru'] = str(int(data[1]))
                    extracted['Disciplina'] = str(data[2].strip().replace('&nbsp;', ''))
                    extracted['Tip'] = str(data[3].strip())
                    extracted['Data'] = str(data[4].strip())
                    extracted['Nota'] = str(data[5].strip().replace('<strong>', '').replace('</strong>', ''))

                    result.append(extracted)

        return result