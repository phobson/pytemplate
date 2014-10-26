import numpy.testing as nptest
import nose.tools as nt
import pandas
from matplotlib.testing.decorators import image_comparison, cleanup
import matplotlib.pyplot as plt


from pytemplate import events

from six import StringIO


class test_Storm(object):
    def setup(self):
        self.testdata = StringIO("""time,precip,flow
2012-01-01 14:05,0.,0.
2012-01-01 14:10,1.,0.
2012-01-01 14:15,1.,0.
2012-01-01 14:20,2.,0.
2012-01-01 14:25,3.,1.
2012-01-01 14:30,6.,2.
2012-01-01 14:35,2.,5.
2012-01-01 14:40,0.,2.
2012-01-01 14:45,0.,0.
""")

        self.resample_data = StringIO("""time,precip,flow
2012-01-01 14:00,0.,0.
2012-01-01 14:10,2.,0.
2012-01-01 14:20,5.,0.5
2012-01-01 14:30,8.,3.5
2012-01-01 14:40,0.,1.0
""")
        self.data = pandas.read_csv(self.testdata, index_col='time', parse_dates=True)
        self.storm = events.Storm(self.data)
        self.known_max_rain = 6
        self.known_max_flow = 5
        self.known_precipcol = 'precip'
        self.known_flowcol = 'flow'

    def test_max_rain(self):
        nt.assert_true(hasattr(self.storm, 'max_rain'))
        nptest.assert_equal(self.storm.max_rain, self.known_max_rain)

    def test_max_flow(self):
        nt.assert_true(hasattr(self.storm, 'max_flow'))
        nptest.assert_equal(self.storm.max_flow, self.known_max_flow)

    def test_precipcol(self):
        nt.assert_true(hasattr(self.storm, 'precipcol'))
        nptest.assert_equal(self.storm.precipcol, self.known_precipcol)

    def test_flowcol(self):
        nt.assert_true(hasattr(self.storm, 'flowcol'))
        nptest.assert_equal(self.storm.flowcol, self.known_flowcol)

    def test_resample(self):
        newstorm = self.storm.resample('10T')
        known_data = pandas.read_csv(self.resample_data, index_col='time', parse_dates=True)
        nt.assert_true(isinstance(newstorm, events.Storm))
        pandas.util.testing.assert_frame_equal(
            newstorm.data.reset_index(),
            known_data.reset_index(),
            check_column_type=True,
            check_exact=True
        )

@nt.raises(ValueError)
def test_storm_bad_data():
    events.Storm('junk')


@nt.raises(NotImplementedError)
def test_storm_resample_bad_index():
    testdata = StringIO("""time,precip,flow
2012-01-01 14:05,0,0
2012-01-01 14:10,1,0""")
    data = pandas.read_csv(testdata)
    storm = events.Storm(data)
    storm.resample('10T')

@cleanup
@image_comparison(['test_hydro'], extensions=['png'])
def test_hydrograph():
    data = StringIO("""time,precip,flow
2012-01-01 14:05,0.,0.
2012-01-01 14:10,1.,0.
2012-01-01 14:15,1.,0.
2012-01-01 14:20,2.,0.
2012-01-01 14:25,3.,1.
2012-01-01 14:30,6.,2.
2012-01-01 14:35,2.,5.
2012-01-01 14:40,0.,2.
2012-01-01 14:45,0.,0.
""")
    data = pandas.read_csv(data, index_col='time', parse_dates=True)
    storm = events.Storm(data)
    fig = storm.plot_hydro()
    nt.assert_true(isinstance(fig, plt.Figure))
