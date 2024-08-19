
from .imports import * 
import simplekml
from . import proc_data as prd


def write_kml_files():
    """Based on data, write out kml files showing all paths"""
    path_out = join(expanduser('~'), 'Downloads', 'traffic-kml')
    if not exists(path_out):
        ex(f"mkdir -p '{path_out}'")
    df, xml = prd.collect()
    keys = (df.sort_values(by=['timestamp_float'])
              .drop_duplicates(subset=['place_description'], 
                               keep='last')
              ['path'].tolist())
    for key,d in [(k,v) for k,v in xml.items() if k in keys]:
        coords = d['flowSegmentData']['coordinates']['coordinate']
        fn = os.path.splitext(basename(key))[0]
        write_kml(coords, fp_output=join(path_out, f"{fn}.kml"))


def write_kml(coordinates, fp_output='/l/tmp/import.kml'):
    """Given list of coordinates, write kml file

        coordinates = [
            {'latitude': '39.808886', 'longitude': '-104.983314'},
            {'latitude': '39.808758', 'longitude': '-104.983310'},
            {'latitude': '39.808027', 'longitude': '-104.983316'},
            {'latitude': '39.807891', 'longitude': '-104.983319'}
        ]

    """
    kml = simplekml.Kml()
    for d in coordinates:
        kml.newpoint(coords=[(d['longitude'], d['latitude'])])
    kml.save(fp_output)
    assert exists(fp_output)
    print(f"wrote '{fp_output}'")

