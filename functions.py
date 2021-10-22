import config as cfg

class WordCount:
    def __init__(self):
        self.hiscoreindex = 0
        self.wordcountlist = []
        self.curr_word = ""
        self.wordlist = []

    def searchandadd(self, word):
        try:
            if word == self.wordcountlist[self.hiscoreindex]["word"]:
                self.wordcountlist[self.hiscoreindex]["count"] += 1
                return
            i = 0
            j = len(self.wordcountlist) - 1
            while i < j:
                mid = i + (j - i) // 2
                if self.wordcountlist[mid]["word"] < word:
                    i = mid + 1
                elif self.wordcountlist[mid]["word"] > word:
                    j = mid - 1
                else:
                    i = mid
                    break
            if self.wordcountlist[i]["word"] == word:
                self.wordcountlist[i]["count"] += 1
                if self.wordcountlist[i]["count"] > self.wordcountlist[self.hiscoreindex]["count"]:
                    self.hiscoreindex = i
            elif self.wordcountlist[i]["word"] < word:
                self.wordcountlist.insert(i+1, {"word": word, "count": 1})
            else:
                self.wordcountlist.insert(i, {"word": word, "count": 1})
            return
        except IndexError:
            self.wordcountlist = [{"word": word, "count": 1}]

    def sort(self, desc=True):
        return sorted(
            sorted(self.wordcountlist, key=lambda i: (i["word"])),
            key=lambda i: (i["count"]), reverse=desc)

    def neatstr(self):
        neatstr = ""
        if self.wordcountlist:
            lst = self.sort()
            maxlen = max([len(word["word"]) for word in lst])
            for word in lst:
                spaces = maxlen - len(word["word"])
                neatstr = neatstr + f'{word["word"]} {spaces*" "}{word["count"]}\n'
        return neatstr

    def processbuffer(self, buffer):
        if buffer:
            for char in buffer:
                if char in cfg.SEPARATORS or char in cfg.DELIMITERS:
                    if self.curr_word != "":
                        self.searchandadd(self.curr_word.lower())
                        self.curr_word = ""
                    else:
                        pass
                else:
                    self.curr_word = self.curr_word + chr(char)
        elif self.curr_word != "":
            self.searchandadd(self.curr_word.lower())
            self.curr_word = ""
