

from .imports import * 

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




