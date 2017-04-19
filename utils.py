""" Various uncomplex functionality"""

import time
import scipy.special as spc
import scipy.stats as st
import numpy as np


def string_to_filename(string):
    """ Cleans a string up to be used as a filename"""
    keepcharacters = ('_', '-')
    filename = ''.join(c for c in string if c.isalnum()
                       or c in keepcharacters).rstrip()
    filename = filename.lower()
    return filename


def print_nnl(text):
    """Print without adding a new line """
    print(text, end='', flush=True)


def debug(is_debug_mode=False, time_start=None, text=None):
    """ Times execution and outputs log messages"""
    if not is_debug_mode:
        return

    if time_start is None:
        if text is not None:
            print_nnl(text)
        time_start = time.process_time()
        return time_start
    else:
        time_diff = time.process_time() - time_start
        print_nnl(': {:.3f} seconds\n'.format(time_diff))
        return time_diff


def square2cond(n, i, j):
    """Converts the squareform indices i and j of the condensed vector with size n to the
    condensed index k. See also: scipy.spatial.distance.squareform"""
    k = int(spc.comb(n, 2) - spc.comb(n - i, 2) + (j - i - 1))
    return k


def net_connectivity_stats(net_connectivities, confidence=0.95):
    """Calculates the means and confidence intervals for network connectivity results"""

    means = np.mean(net_connectivities, axis=0)
    conf_intervals = np.zeros([np.size(means), 2])

    for index, mean in enumerate(means):
        conf_intervals[index] = st.t.interval(confidence, len(
            net_connectivities[:, index]) - 1, loc=mean, scale=st.sem(net_connectivities[:, index]))

    return means, conf_intervals
