import numpy as np
import matplotlib.pyplot as plt
import pandas

def addSecondColumnLevel(levelval, levelname, olddf):
    '''
    Takes a simple index on a dataframe's columns and adds a new level
    with a single value.
    E.g., df.columns = ['res', 'qual'] -> [('Infl' ,'res'), ('Infl', 'qual')]
    '''
    if isinstance(olddf.columns, pandas.MultiIndex):
        raise ValueError('Dataframe already has MultiIndex on columns')
    colarray = [[levelval]*len(olddf.columns), olddf.columns]
    colindex = pandas.MultiIndex.from_arrays(colarray)
    newdf = olddf.copy()
    newdf.columns = colindex
    newdf.columns.names = [levelname, 'quantity']
    return newdf


def getUniqueDataframeIndexVal(df, indexlevel):
    '''
    Confirms that a given level of a dataframe's index only has
    one unique value. Useful for confirming consistent units.

    Raises error if level is not a single value. Returns value
    Otherwise
    '''
    index = np.unique(df.index.get_level_values(indexlevel).tolist())
    if index.shape != (1,):
        raise DataError('index level "%s" is not unique!' % indexlevel)

    return index[0]


def sigFigs(x, n, expthresh=5, tex=False, pval=False):
    '''
    Formats a number into a string with the correct number of sig figs.

    Input:
        x (numeric) : the number you want to round
        n (int) : the number of sig figs it should have
        tex (bool) : toggles the scientific formatting of the number
        pval (bool) : if True and x < 0.001, will return "<0.001"

    Typical Usage:
        >>> print(sigFigs(1247.15, 3))
               1250
        >>> print(sigFigs(1247.15, 7))
               1247.150
    '''
    # check on the number provided
    if x is not None and not np.isinf(x) and not np.isnan(x):

        # check on the sigFigs
        if n < 1:
            raise ValueError("number of sig figs must be greater than zero!")

        # return a string value unaltered
        #if type(x) == types.StringType:
        if isinstance(x, str):
            out = x

        elif pval and x < 0.001:
            out = "<0.001"
            if tex:
                out = '${}$'.format(out)

        # logic to do all of the rounding
        elif x != 0.0:
            order = np.floor(np.log10(np.abs(x)))

            if -1.0 * expthresh <= order <= expthresh:
                decimal_places = int(n - 1 - order)

                if decimal_places <= 0:
                    out = '{0:,.0f}'.format(round(x, decimal_places))

                else:
                    fmt = '{0:,.%df}' % decimal_places
                    out = fmt.format(x)

            else:
                decimal_places = n - 1
                if tex:
                    #raise NotImplementedError('no exponential tex formatting yet')
                    fmt = r'$%%0.%df \times 10 ^ {%d}$' % (decimal_places, order)
                    out = fmt % round(x / 10 ** order, decimal_places)
                else:
                    fmt = '{0:.%de}' % decimal_places
                    out = fmt.format(x)

        else:
            out = str(round(x, n))

    # with NAs and INFs, just return 'NA'
    else:
        out = 'NA'

    return out
