import numpy.testing as nptest
import nose.tools as nt

import matplotlib
matplotlib.use('agg')
from matplotlib.testing.decorators import image_comparison, cleanup
import matplotlib.pyplot as plt
import pandas

from pytemplate.utils import figutils

from six import StringIO


@nt.nottest
def assert_fig_and_ax(fig, ax):
    nt.assert_true(isinstance(fig, plt.Figure))
    nt.assert_true(isinstance(ax, plt.Axes))


class test__check_ax(object):
    def setup(self):
        fig, ax = plt.subplots()
        self.fig = fig
        self.ax = ax

    def teardown(self):
        plt.close('all')

    def test_no_ax(self):
        fig, ax = figutils._check_ax(None)
        assert_fig_and_ax(fig, ax)

    def test_ax(self):
        fig, ax = figutils._check_ax(self.ax)
        assert_fig_and_ax(fig, ax)

        nt.assert_equal(fig, self.fig)
        nt.assert_equal(ax, self.ax)

    @nt.raises(ValueError)
    def test_ax_bad_value(self):
        fig, ax = figutils._check_ax('junk')

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
    fig = figutils.hydrograph(data, precipcol='precip')
    nt.assert_true(isinstance(fig, plt.Figure))
