import nose.tools as nt
import numpy.testing as nptest
import pandas
from six import StringIO

from pytemplate.utils import misc

class test_addSecondColumnLevel(object):
    def setup(self):
        self.testcsv = StringIO("""\
Date,A,B,C,D
X,1,2,3,4
Y,5,6,7,8
Z,9,0,1,2
        """)
        self.data = pandas.read_csv(self.testcsv, index_col=['Date'])
        self.known = pandas.MultiIndex.from_tuples([(u'test', u'A'), (u'test', u'B'),
                                                    (u'test', u'C'), (u'test', u'D')])

    def test_normal(self):
        newdata = misc.addSecondColumnLevel('test', 'testlevel', self.data)
        nt.assert_list_equal(self.known.tolist(), newdata.columns.tolist())

    @nptest.raises(ValueError)
    def test_error(self):
        newdata1 = misc.addSecondColumnLevel('test1', 'testlevel1', self.data)
        newdata2 = misc.addSecondColumnLevel('test2', 'testlevel2', newdata1)


def test_sigFigs_baseline_gt1():
    x1 = 1234.56
    nt.assert_equal(misc.sigFigs(x1, 3), '1,230')
    nt.assert_equal(misc.sigFigs(x1, 4), '1,235')

def test_sigFigs_baseline_lt1():
    x2 = 0.12345
    nt.assert_equal(misc.sigFigs(x2, 3), '0.123')
    nt.assert_equal(misc.sigFigs(x2, 4), '0.1235')

@nptest.raises(ValueError)
def test_sigFigs_bad_n():
    misc.sigFigs(1.234, 0)

def test_sigFigs_trailing_zeros_gt1():
    x1 = 1234.56
    nt.assert_equal(misc.sigFigs(x1, 8), '1,234.5600')

def test_sigFigs_trailing_zeros_lt1():
    x2 = 0.12345
    nt.assert_equal(misc.sigFigs(x2, 8), '0.12345000')

def test_sigFigs_exponents_notex_gt1():
    x1 = 123456789.123456789
    nt.assert_equal(misc.sigFigs(x1, 3, tex=False), '1.23e+08')

def test_sigFigs_exponents_notex_lt1():
    x2 = 0.000000123
    nt.assert_equal(misc.sigFigs(x2, 3, tex=False), '1.23e-07')

def test_sigFigs_exponents_tex_gt1():
    x1 = 123456789.123456789
    nt.assert_equal(misc.sigFigs(x1, 3, tex=True), r'$1.23 \times 10 ^ {8}$')

def test_sigFigs_exponents_tex_lt1():
    x2 = 0.000000123
    nt.assert_equal(misc.sigFigs(x2, 3, tex=True), r'$1.23 \times 10 ^ {-7}$')

def test_sigFigs_pvals_noop():
    p = 0.001
    nt.assert_equal(misc.sigFigs(p, 1, pval=True), '0.001')

def test_sigFigs_pvals_op():
    p = 0.0005
    nt.assert_equal(misc.sigFigs(p, 3, pval=True), '<0.001')

def test_sigFigs_pvals_op_tex():
    p = 0.0005
    nt.assert_equal(misc.sigFigs(p, 3, tex=True, pval=True), '$<0.001$')

@nptest.raises
def test_sigFigs_exception():
    misc.sigFigs(199, -1)


class test_uniqueIndex(object):
    def setup():
        dates = range(5)
        params = list('ABCDE')
        locations = ['Inflow', 'Outflow']
        for d in dates:
            for p in params:
                for loc in locations:
                    dual.append([d,p,loc])

        index = pandas.MultiIndex.from_arrays([dual_array[:,0],
                                                    dual_array[:,1],
                                                    dual_array[:,2]])
        index.names = ['date', 'param', 'loc']

        self.data = pandas.DataFrame(np.range.normal(size=len(index)), index=index)

        def test_getUniqueDataframeIndexVal():
            test = misc.getUniqueDataframeIndexVal(self.data.select(lambda x: x[0]=='0'), 'date')
            known = '0'
            nt.assert_equal(test, known)

        @nptest.raises(misc.DataError)
        def test_getUniqueDataframeIndexVal_error():
            misc.getUniqueDataframeIndexVal(self.data, 'date')
