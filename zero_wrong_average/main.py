
from .imports import * 
import xmltodict

CURL = "curl 'https:/api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=8JrTFy5cUhH7Lnklp5ZX6G7uuJLOjaq8&point=39.806944,-104.983333'"

IDENTIFIER = 'denver-I25@I76'
PATH_OUTPUT = f'/l/gds/wrong-average-data/{IDENTIFIER}/'
if not exists(PATH_OUTPUT):
    ex(f"mkdir -p '{PATH_OUTPUT}'")
assert exists(PATH_OUTPUT)


def get():
    d = pd.Timestamp.utcnow()
    fn = f"{d.timestamp()}-{IDENTIFIER}.json"
    fp = join(PATH_OUTPUT, fn)
    ex(f"{CURL} > '{fp}'")
    assert exists(fp), fp
    print(f"wrote '{fp}'")


def latest():
    files = sorted(glob(join(PATH_OUTPUT, '*json')))
    print(files[-1])
    d = pd.Timestamp(basename(files[-1]), unit='s', tz='UTC')
    print(d.tz_convert('America/Denver'))


def parse_archive(fp_archive):
    """Load all json files in fp_archive"""
    files = glob(join(fp_archive, '*json'))
    data = dict()

    for fp in files:
        k = basename(fp)
        with open(fp, 'r') as f:
            d = xmltodict.parse(f.read())
            d['timestamp'] = (pd.Timestamp(float(k.split('-')[0]), 
                                           unit='s', tz='UTC')
                                .isoformat())
            data[k] = d
    return data


