

from .imports import * 

CURL = "curl 'https:/api.tomtom.com/traffic/services/4/flowSegmentData/absolute/10/xml?key=8JrTFy5cUhH7Lnklp5ZX6G7uuJLOjaq8&point=39.806944,-104.983333'"

IDENTIFIER = 'denver-I25@I76'
PATH_OUTPUT = f'/l/gds/wrong-average-data/{IDENTIFIER}/'
if not exists(PATH_OUTPUT):
    ex(f"mkdir -p '{PATH_OUTPUT}'")
assert exists(PATH_OUTPUT)


def get():
    d = pd.Timestamp.utcnow()
    fn = f"{d.timestamp()}-{IDENTIFIER}.xml"
    fp = join(PATH_OUTPUT, fn)
    ex(f"{CURL} > '{fp}'")
    assert exists(fp), fp
    print(f"wrote '{fp}'")


def latest():
    files = sorted(glob(join(PATH_OUTPUT, '*xml')))
    print(files[-1])
    x = basename(files[-1]).split('-')[0]
    x = float(x)
    print(x)

    # Convert the timestamp from seconds to nanoseconds (if necessary) and ensure it's within range
    if 0 <= x <= pd.Timestamp.max.timestamp():
        d = pd.Timestamp(x, unit='s', tz='UTC')
        print(d.tz_convert('America/Denver'))
    else:
        print("Invalid timestamp:", x)


