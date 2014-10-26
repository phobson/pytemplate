import numpy
import pandas

from ..utils import figutils


__all__ = [
    'Storm',
]

class Storm(object):
    '''
    An object representing a precipitation event.

    Parameters
    ----------
    data : pandas DataFrame
        Data structure contains the precipitation depths and runoff
        flowrates at timestamps.
    precipcol : optional string (default = 'precip')
        The name of the column in the DataFrame containing precipitation
        values.
    flowcol : optional string (default = 'flow')
        The name of the column in the DataFrame containing runoff
        values.

    Notes
    -----
    The index of the DataFrame must be of the type pandas.DatetimeIndex
    in order to use the resample method of this class.

    '''
    def __init__(self, data, precipcol='precip', flowcol='flow'):
        if not isinstance(data, pandas.DataFrame):
            raise ValueError("`data` must be a pandas DataFrame")

        self.data = data
        self.precipcol = precipcol
        self.flowcol = flowcol

        self._max_rain = None
        self._max_flow = None

    @property
    def max_rain(self):
        if self._max_rain is None:
            self._max_rain = self.data[self.precipcol].max()
        return self._max_rain

    @property
    def max_flow(self):
        if self._max_flow is None:
            self._max_flow = self.data[self.flowcol].max()
        return self._max_flow

    def resample(self, offset):
        '''
        Resamples the Storm object into a less frequent time step.

        Parameters
        ----------
        offset : string or pandas.offset
            Valid pandas time offset for resampling

        Returns
        -------
        A new Storm object with resampled data

        Notes
        -----
        Upon resampling, precipitation will be aggrated by the sum
        (total) values and flow will be aggregated by the mean value.

        '''
        if not isinstance(self.data.index, pandas.DatetimeIndex):
            msg = "resample only works with DatetimeIndexes"
            raise NotImplementedError(msg)

        rules = {
            self.precipcol: numpy.sum,
            self.flowcol: numpy.mean
        }
        rs_data = self.data.resample(offset, how=rules)
        rs_data = rs_data[[self.precipcol, self.flowcol]]
        return Storm(rs_data, precipcol=self.precipcol, flowcol=self.flowcol)

    def plot_hydro(self):
        fig = figutils.hydrograph(self.data, precipcol=self.precipcol)
        return fig


