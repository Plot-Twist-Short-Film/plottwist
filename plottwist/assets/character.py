#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module that contains definitions for character assets in Plot Twist
"""

from __future__ import print_function, division, absolute_import

__author__ = "Tomas Poveda"
__license__ = "MIT"
__maintainer__ = "Tomas Poveda"
__email__ = "tpovedatd@gmail.com"

from plottwist.core import asset


class PlotTwistCharacter(asset.PlotTwistAsset, object):
    def __init__(self, project, asset_data):
        super(PlotTwistCharacter, self).__init__(project=project, asset_data=asset_data)
