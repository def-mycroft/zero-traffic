
from .imports import * 
import simplekml


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

