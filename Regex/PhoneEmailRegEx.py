import re


def fonct(text):

    x = re.compile(r'[A-Za-z0-9]{8,}')
    mo = x.search(text)

    if mo is not None:
        x = re.compile(r'\d+')
        y = re.compile(r'[a-z]+')
        z = re.compile(r'[A-Z]+')
        mo1 = x.search(text)
        mo2 = y.search(text)
        mo3 = z.search(text)
        if mo1 is None or mo2 is None or mo3 is None:
            print("FALSE 2")
        else:
            print("CORRECT")

    else:
        print("FALSE 1")


if __name__ == '__main__':
    fonct("Che145dyfefe")
