import os
import sys

import pandas

def _load_raw_data(dataset):
    file_map = {
        'wq': 'WaterQualityData.csv'
        'met': 'WeatherData.csv'
    }

    try:
        filepath = os.path.join(sys.prefix, 'pytemplate', 'example_data',
                                file_map[dataset])
    except KeyError:
        msg = "Only 'wq' and 'met' datasets are available"
        raise NotImplementedError(msg)

    data = pandas.read_csv(filepath)
    return data



def loadLocationData(dataset, location):
    location_column_map = {
        'wq': 'sampleloc'
        'met': 'airport'
    }

    loccol = location_column_map[dataset]
    raw = _load_raw_data(dataset)
    data = raw.query("{0} == '{1}'".format(loccol, location))
    return data

