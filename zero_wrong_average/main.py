
from .imports import * 
from .config import load_config
import xmltodict

# https://developer.tomtom.com/traffic-api/documentation/traffic-flow/flow-segment-data

CONFIG = load_config()
# TODO - this needs to go to config, api key and idlatlon
API_KEY = CONFIG['api_key']
ID_LATLON = CONFIG['id_latlon']
PATH_DATA_ARCHIVE = CONFIG['path_data_archive']


def get_all():
    for identifier, lat, lon in ID_LATLON:
        get(identifier, lat, lon)


def get(identifier, lat, lon):

    path_output = join(PATH_DATA_ARCHIVE, identifier)
    if not exists(path_output):
        ex(f"mkdir -p '{path_output}'")
    assert exists(path_output)

    d = pd.Timestamp.utcnow()
    fn = f"{d.timestamp()}-{identifier}.xml"
    fp = join(path_output, fn)

    curl = (f"curl 'https:/api.tomtom.com/traffic/services/4/flowSegmentData"
            f"/absolute/10/xml?key={API_KEY}&point={lat},{lon}'")
    ex(f"{curl} > '{fp}'")
    assert exists(fp), fp
    print(f"wrote '{fp}'")


def parse_archive(fp_archive):
    """Load all json files in fp_archive"""
    files = glob(join(fp_archive, '*xml'))
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


def latest(identifier=ID_LATLON[0][0]):
    path_output = join(PATH_DATA_ARCHIVE, identifier)
    files = sorted(glob(join(path_output, '*xml')))
    print(files[-1])
    d = pd.Timestamp(float(basename(files[-1]).split('-')[0]), unit='s', tz='UTC')
    print(d.tz_convert('America/Denver'))

    x = basename(files[-1]).split('-')[0]
    x = float(x)
    print(x)

    if 0 <= x <= pd.Timestamp.max.timestamp():
        d = pd.Timestamp(x, unit='s', tz='UTC')
        print(d.tz_convert('America/Denver'))
    else:
        print("Invalid timestamp:", x)


