import numpy.testing as nptest
import nose.tools as nt

from pytemplate import features


class test_MonitoringStation_NoStorms(object):
    def setup(self):
        self.da = features.DrainageArea(5., 2., 1.)
        self.ms = features.MonitoringStation('test', 45.2, -115.3, self.da)
        self.known_name = 'test'
        self.known_lat = 45.2
        self.known_lon = -115.3

    def teardown(self):
        pass

    def test_name(self):
        nt.assert_true(hasattr(self.ms, 'name'))
        nptest.assert_equal(self.ms.name, self.known_name)

    def test_lat(self):
        nt.assert_true(hasattr(self.ms, 'lat'))
        nptest.assert_equal(self.ms.lat, self.known_lat)

    def test_lon(self):
        nt.assert_true(hasattr(self.ms, 'lon'))
        nptest.assert_equal(self.ms.lon, self.known_lon)

    def test_drainagearea(self):
        nt.assert_true(hasattr(self.ms, 'da'))
        nt.assert_true(isinstance(self.ms.da, features.DrainageArea))

class test_DrainageArea(object):
    def setup(self):
        self.da = features.DrainageArea(5., 2., 1.)
        self.known_total_area = 5.
        self.known_imp_area = 2.
        self.known_bmp_area = 1.

    def test_total_area(self):
        nt.assert_true(hasattr(self.da, 'total_area'))
        nptest.assert_equal(self.da.total_area, self.known_total_area)

    def test_imp_area(self):
        nt.assert_true(hasattr(self.da, 'imp_area'))
        nptest.assert_equal(self.da.imp_area, self.known_imp_area)

    def test_bmp_area(self):
        nt.assert_true(hasattr(self.da, 'bmp_area'))
        nptest.assert_equal(self.da.bmp_area, self.known_bmp_area)

    def test_simple_method(self):
        known_runoff = 6.1
        nptest.assert_almost_equal(
            self.da.simple_method(2),
            known_runoff,
            decimal=5
        )


