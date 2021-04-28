import re


def regStrip(x, y):

    if y == None:
        strip = re.compile(r'^(\s+)|(\s+)$')
    else:
        strip = re.compile(re.escape(str(y)))

    mo = strip.sub('', x);
    print(mo)

if __name__ == '__main__':
    regStrip('555aaa555   ', '5')