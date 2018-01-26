#!/usr/bin/env python3
import sys
import base64


def b64_file(fname):
    with open(fname, 'rb') as f:
        return base64.b64encode(f.read()).decode()


if __name__ == '__main__':
    FONT_NAME = 'Rickty Diminished L'
    FONT_FACES = [{'style': 'normal',
                   'weight': 'normal',
                   'fname': 'RictyDiminishedL-Regular.ttf'},
                  {'style': 'normal',
                   'weight': 'bold',
                   'fname': 'RictyDiminishedL-Bold.ttf'},
                  {'style': 'italic',
                   'weight': 'normal',
                   'fname': 'RictyDiminishedL-Oblique.ttf'},
                  {'style': 'italic',
                   'weight': 'bold',
                   'fname': 'RictyDiminishedL-BoldOblique.ttf'}]

    def out(data):
        sys.stdout.write(data)

    for fface in FONT_FACES:
        out('@font-face {\n')
        out('font-family: "%s";\n' % FONT_NAME)
        out('font-style: %s;' % fface['style'])
        out('font-weight: %s;' % fface['weight'])
        out('src: url(data:font/ttf;charset-utf-8;')
        out(b64_file(fface['fname']))
        out(');\n')
        out('}\n')
