
from .imports import * 
import simplekml
from . import proc_data as prd


def write_kml_files():
    """Write KML files showing all paths based on the provided data.

    Entire project data archive is loaded, and for the latest data point
    in every place, a kml (Google Earth import file) is written. This is
    useful for understanding where the tomtom API is getting traffic
    data. 

    Parameters
    ----------
    None

    Returns
    -------
    None

    """
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
    """Write a KML file given a list of coordinates.

    This function generates a KML file from a list of latitude and
    longitude coordinates and saves it to the specified file path.

    Coordinates are expected to be in this form:

        coordinates = [
            {'latitude': '39.808886', 'longitude': '-104.983314'},
            {'latitude': '39.808758', 'longitude': '-104.983310'},
            {'latitude': '39.808027', 'longitude': '-104.983316'},
            {'latitude': '39.807891', 'longitude': '-104.983319'}
        ]

    Parameters
    ----------
    coordinates : list of dict
        A list of dictionaries where each dictionary contains 'latitude'
        and 'longitude' as strings.
    fp_output : str, optional
        The file path where the KML file will be saved (default is
        '/l/tmp/import.kml').

    Returns
    -------
    None

    """
    kml = simplekml.Kml()
    for d in coordinates:
        kml.newpoint(coords=[(d['longitude'], d['latitude'])])
    kml.save(fp_output)
    assert exists(fp_output)
    print(f"wrote '{fp_output}'")

