import numpy as np
import pandas

__all__ = [
    'MonitoringStation',
    'DrainageArea'
]


class MonitoringStation(object):
    '''
    Object representing a hydrologic monitoring station

    Parameters
    ---------
    name : string
        The officel handle of the station.
    lat, lon : floats
        Coordinates (y, x) of the station.
    drainagearea : DrainageArea object
        Object representing the drainage area of the monitoring station
    *storms : optional features.Storm object
        Arbitrary number of storms recorded at the monitoring station

    '''

    def __init__(self, name, lat, lon, drainagearea, *storms):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.da = drainagearea
        self.storms = [s for s in storms]


class DrainageArea(object):
    def __init__(self, total_area=1.0, imp_area=1.0, bmp_area=0.0):
        '''
        A simple object representing the drainage area of a BMP. Units are not
        enforced, so keep them consistent yourself. The calculations available
        assume that the are of the BMP and the "total" area are mutually
        exclusive. In other words, the watershed outlet is at the BMP inlet.

        Parameters
        ----------
        total_area : optional float (default=1.0)
            The total geometric area of the BMP's catchment
        imp_area : optional float (default=1.0)
            The impervious area of the BMP's catchment
        bmp_area : optional float (default=0.0)
            The geometric area of the BMP itself.

        Methods
        -------
        simple_method - estimates the influent volume to the BMP based on
            storm depth.
        '''
        self.total_area = float(total_area)
        self.imp_area = float(imp_area)
        self.bmp_area = float(bmp_area)

    def simple_method(self, storm_depth, volume_conversion=1, annualFactor=1):
        '''
        Estimate runoff volume via Bob Pitt's Simple Method.

        Input
        -----
        storm_depth : float
            Depth of the storm.
        volume_conversion : float (default = 1)
            Conversion factor to go from [area units] * [depth units] to
            the desired [volume units]. If [area] = m^2, [depth] = mm, and
            [volume] = L, then `volume_conversion` = 1.

        Returns
        -------
        runoff : float
            estimate of the total volume of runoff from the given storm depth

        '''
        # volumetric run off coneffiecient
        Rv = 0.05 + (0.9 * (self.imp_area/self.total_area))

        # run per unit storm depth
        drainage_conversion = Rv * self.total_area * volume_conversion
        bmp_conversion = self.bmp_area * volume_conversion

        # total runoff based on actual storm depth
        runoff = (drainage_conversion * annualFactor + bmp_conversion) * storm_depth
        return runoff
