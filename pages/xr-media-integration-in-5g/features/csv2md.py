import pandas as pd
from collections import defaultdict
import markdown
import sys 
from pathlib import Path

# columns = [
#     "Extension",
#     "Property",
#     "Status",
#     "Requirement",
#     "Test content" ]
#     #, "notes" ]

class StringConverter(dict):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return str

    def get(self, default=None):
        return str

def main(fp, csv2md, md2html):

    mdfp = fp.with_suffix('.md')
    htmlfp = fp.with_suffix('.html')

    # df = pd.read_csv(fp, usecols=columns, converters=StringConverter())

    if csv2md:
        df = pd.read_csv(fp, converters=StringConverter())
        with open(mdfp, 'w') as md:
            df.to_markdown(buf=md, index=False)

    if md2html:
        with open(htmlfp, 'w') as fo:
            with open(mdfp, 'r') as md:
                data = md.read()
                data = data.replace("[ ]", "&#x2610;")
                data = data.replace("[x]", "&#x2611;")
                html = markdown.markdown(data, extensions=['markdown.extensions.tables'])
                fo.write(html)

if __name__ == "__main__":

    assert len(sys.argv) > 1
    fp = Path(sys.argv[1])
    assert fp.exists()

    if len(sys.argv) == 2:
        csv2md = True
        md2html = True
    else:
        csv2md = 'csv2md' in sys.argv
        md2html = 'md2html' in sys.argv
    

    main(fp, csv2md, md2html)