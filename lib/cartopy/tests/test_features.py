# (C) British Crown Copyright 2017, Met Office
#
# This file is part of cartopy.
#
# cartopy is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# cartopy is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with cartopy.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)

import numpy as np
import matplotlib.pyplot as plt
import cartopy.feature as cfeature
import cartopy.crs as ccrs

COLORS = {'land': np.array((240, 240, 220)) / 256.,
          'land_alt1': np.array((220, 220, 220)) / 256.,
          'water': np.array((152, 183, 226)) / 256.}

small_extent = (-6, -8, 56, 59)
medium_extent = (-20, 20, 20, 60)
large_extent = (-40, 40, 0, 80)

autoscale_borders = cfeature.NaturalEarthFeature(
   'cultural', 'admin_0_boundary_lines_land',
   'autoscale', edgecolor='black', facecolor='none')

a_coastline = cfeature.NaturalEarthFeature('physical', 'coastline',
                                             'a', edgecolor='black',
                                             facecolor='none')

auto_land = cfeature.NaturalEarthFeature('physical', 'land',
                                        'auto', edgecolor='face',
                                         facecolor=COLORS['land'])

default_lakes = cfeature.LAKES

ten_borders = cfeature.NaturalEarthFeature(
   'cultural', 'admin_0_boundary_lines_land',
   '10m', edgecolor='black', facecolor='none')

fifty_coastline = cfeature.NaturalEarthFeature('physical', 'coastline',
                                             '50m', edgecolor='black',
                                             facecolor='none')

hundredten_land = cfeature.NaturalEarthFeature('physical', 'land',
                                        '110m', edgecolor='face',
                                         facecolor=COLORS['land'])

class TestFeatures(object):
    def test_change_scale(self):
        # Check that features can easily be retrieved with a different
        # scale.
        new_lakes = cfeature.LAKES.with_scale('10m')
        assert new_lakes.scale == '10m'
        assert new_lakes.kwargs == cfeature.LAKES.kwargs
        assert new_lakes.category == cfeature.LAKES.category
        assert new_lakes.name == cfeature.LAKES.name

    def test_autoscale_keyword(self):
        # Check that autoscale variants can be passed as the scale
        # argument

        assert autoscale_borders.scale == 'autoscale'
        assert autoscale_borders.autoscale == True
        assert a_coastline.scale == 'a'
        assert a_coastline.autoscale == True
        assert auto_land.scale == 'auto'
        assert auto_land.autoscale == True

    def test_autoscale_default(self):
        # Check that autoscaling not used by default
        assert default_lakes.scale == '110m'
        assert default_lakes.autoscale == False
        assert ten_borders.scale == '10m'
        assert ten_borders.autoscale == False
        assert fifty_coastline.scale == '50m'
        assert fifty_coastline.autoscale == False
        assert hundredten_land.scale == '110m'
        assert hundredten_land.autoscale == False

    def test_scale_from_small_extent(self):
        # Check that scale changes with extent when autoscale==True
        new_scale = auto_land._scale_from_extent(small_extent)
        assert auto_land.scale == 'auto'
        assert new_scale == '10m'

    def test_scale_from_medium_extent(self):
        # Check that scale changes with extent when autoscale==True
        new_scale = auto_land._scale_from_extent(medium_extent)
        assert auto_land.scale == 'auto'
        assert new_scale == '50m'

    def test_scale_from_large_extent(self):
        # Check that scale changes with extent when autoscale==True
        new_scale = auto_land._scale_from_extent(large_extent)
        assert auto_land.scale == 'auto'
        assert new_scale == '110m'

    def test_autoscale_small_draw(self):
        # Check that scale changes with extent when autoscale==True
        auto_land.intersecting_geometries(small_extent)
#        ax = plt.axes(projection=ccrs.PlateCarree())
#        ax.add_feature(auto_land)
#        ax.set_extent(small_extent)
#        ax.draw()
        #new_scale = auto_land._scale_from_extent(small_extent)
        assert auto_land.scale == '10m'
