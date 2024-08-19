
import xmltodict
from warnings import warn
from .imports import * 

# TODO - this should be in a config 
PATH_DATA = '/l/gds/wrong-average-data/'

# TODO - create a config that allows for tracking data, someon else 
# should be able to use this. 


def load_xml():
    """Retrieve xml files from project directory"""
    files = glob(join(PATH_DATA, '*', '*xml'))
    xml = dict()
    for fp in files:
        with open(fp, 'r') as f:
            try:
                xml[fp] = xmltodict.parse(f.read())
            except Exception as e:
                if not len(f.read()):
                    warn(f"file '{fp}' is empty, skipping. ")
                else:
                    raise e
    return xml


def collect():
    """Parse project xml files, return dataframe 

    Parse XML files from a specified directory structure and return a 
    DataFrame with the parsed data and a dictionary of the XML content.

    Returns
    -------
    df : pandas.DataFrame
        A DataFrame containing the parsed data, including file paths,
        timestamps, place descriptions, and traffic-related metrics.
        Columns include ['path', 'timestamp_float', 'place_description',
        'datetime', 'currentSpeed', 'freeFlowSpeed', 'confidence',
        'roadClosure'], where the latter 4 are documented in the tomtom
        api docs. 

    xml : dict
        A dictionary where keys are file paths and values are the parsed
        XML content.

    Raises
    ------
    Exception
        If a non-empty file fails to parse, an exception is raised.
    """
    xml = load_xml()

    # extract selected data from dataframe 
    data = list()
    for fp in xml.keys():
        row = {
            'path':fp,
            'timestamp_float':float(basename(fp).split('-')[0]),
            'place_description':basename(os.path.split(fp)[-2]),
        }
        row['datetime'] = (pd.Timestamp(row['timestamp_float'], unit='s', 
                                        tz='UTC')
                             .tz_convert('America/Denver'))

        for col in ['currentSpeed', 'freeFlowSpeed', 'confidence']:
            row[col] = float(xml[fp]['flowSegmentData'][col]) 
        for col in ['roadClosure']:
            row[col] = xml[fp]['flowSegmentData'][col] 

        data.append(row)

    df = (pd.DataFrame(data).sort_values(by=['place_description', 'datetime'])
            .reset_index(drop=True))
    df['roadClosure'] = (df['roadClosure'].map({'true':True, 'false':False}))

    return df, xml
