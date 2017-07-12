"""
Tests for the basic masking and filtering operations
"""
from ccd.qa import *
#from ccd.qa import checkbit, count_clear_or_water, count_total, ratio_clear, \
#    ratio_snow, enough_clear, enough_snow, filter_median_green, mask_duplicate_values
#import numpy as np

clear = 0
water = 1
fill = 255
snow = 3
clear_thresh = 0.25
snow_thresh = 0.75


def test_checkbit():
    packint = 1
    offset = 0

    assert checkbit(packint, offset)

    #offset = 1

    #assert not checkbit(packint, offset)

#
# # def test_qabitval():
# #     packint = 3
# #
# #     assert qabitval(packint, params) == fill
#
#
# def test_count_clear_or_water():
#     arr = np.arange(5)
#     ans = 2
#
#     assert ans == count_clear_or_water(arr, clear, water)
#
#
# def test_count_total():
#     arr = np.arange(5)
#     arr[-1] = 255
#     ans = 4
#
#     assert ans == count_total(arr, fill)
#
#
# def test_ratio_clear():
#     arr = np.arange(5)
#     arr[-1] = 255
#     ans = 0.5
#
#     assert ans == ratio_clear(arr, clear, water, fill)
#
#
# def test_ratio_snow():
#     arr = np.arange(5)
#     ans = 1/3.01
#
#     assert ans == ratio_snow(arr, clear, water, snow)
#
#
# def test_enough_clear():
#     arr = np.arange(5)
#     ans = True
#
#     assert ans == enough_clear(arr, clear, water, fill, clear_thresh)
#
#     arr[1:] = snow
#     ans = False
#     assert ans == enough_clear(arr, clear, water, fill, clear_thresh)
#
#
# def test_enough_snow():
#     arr = np.arange(5)
#     ans = False
#
#     assert ans == enough_snow(arr, clear, water, snow, snow_thresh)
#
#     arr[1:] = snow
#     ans = True
#     assert ans == enough_snow(arr, clear, water, snow, snow_thresh)
#
#
# def test_filter_median_green():
#     arr = np.arange(10)
#     ans = np.array([True, True, True, True, True,
#                     True, True, True, False, False])
#
#     assert np.array_equal(ans, filter_median_green(arr, 3))
#
#
# def test_duplicate_values():
#     arr = np.array([1, 2, 2, 3, 4, 5, 5])
#     ans = np.array([True, True, False, True, True,
#                     True, False], dtype=bool)
#
#     assert np.array_equal(ans, mask_duplicate_values(arr))
