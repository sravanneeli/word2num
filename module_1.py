import re
from word2number import w2n


class process_input:
    pattern = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|thirteen|fourteen|fifteen'
                         r'|sixteen|seventeen|eighteen|nineteen|twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety)('
                         r'.*?)(dollars|rupees|euros)')
    currency_codes = {"dollars": '$', "dollar": '$', "rupees": '₹', 'rupee': '₹', "euros": '€', "euro": '€'}
    abr_pattern = re.compile(r'["](.*?)["]')
    repeat_keywords = {'Single': 1, 'Double': 2, 'Triple': 3, 'Quadruple': 4, 'Quintuple': 5}

    def __init__(self, para):
        self.para = para
        self.matches = process_input.pattern.findall(para)
        self.eng_list, self.currency = self.make_list()
        self.abbreviations = process_input.abr_pattern.findall(self.para)

    def make_list(self):
        eng_list = []
        currency = []
        for match in self.matches:
            eng_list.append(match[0] + match[1])
            currency.append((match[2]))
        return eng_list, currency

    def word2num(self):
        i = 0
        for word in self.eng_list:
            #print(word)
            converted = str(w2n.word_to_num(word)) + process_input.currency_codes[self.currency[i]]
            self.para = self.para.replace(word + self.currency[i], converted)
        if len(self.abbreviations) > 0:
            for string in self.abbreviations:
                dummy = string
                temp = string.split()[::-1]
                repeats = 0
                for i in range(len(temp) - 1):
                    if temp[i - repeats + 1] in process_input.repeat_keywords:
                        temp[i - repeats] *= process_input.repeat_keywords[temp[i - repeats + 1]]
                        del temp[i - repeats + 1]
                        repeats += 1
                string = " ".join(temp)[::-1]
                #print(string)
                string = string.replace(" ", "")
                self.para = self.para.replace(dummy, string)
        return self.para



