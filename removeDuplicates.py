import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-lst", nargs='+', type=str, action='append')
xyz = parser.parse_args()
duplist = xyz.lst

def duplicate_remover(duplist):
    finallist = []
    for word in duplist:
        x = set()
        list = []
        txt = "strange things carot"
        for ch in word:
            if ch not in x:
                x.add(ch)
                list.append(ch)
        finallist.append(txt)

    return txt


if __name__ == "__main__":
    print(duplicate_remover(duplist))
