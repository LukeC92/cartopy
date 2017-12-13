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

import cartopy.feature as cfeature


class TestFeatures(object):
    def test_change_scale(self):
        # Check that features can easily be retrieved with a different scale.
        new_lakes = cfeature.LAKES.with_scale('10m')
        assert new_lakes.scale == '10m'
        assert new_lakes.kwargs == cfeature.LAKES.kwargs
        assert new_lakes.category == cfeature.LAKES.category
        assert new_lakes.name == cfeature.LAKES.name
    
    def test_autoscale_keyword(self):
        # Check that autoscale variants can be passed as the scale argument
        new_borders = cfeature.NaturalEarthFeature('cultural',
                                                   'admin_0_boundary_lines_land',
                                                   'auto', 
                                                   edgecolor='black',
                                                   facecolor='none')
        
        new_coastline = cfeature.NaturalEarthFeature('physical',
                                                     'coastline',
                                                     'a',
                                                     edgecolor='black',
                                                     facecolor='none')
        assert new_borders.scale == 'auto'
        assert new_borders.autoscale == True
        assert new_borders.scale == 'a'
        assert new_borders.autoscale == True

                
    def test_autoscale_default(self):
        # Check that autoscaling not used by default
        new_lakes = cfeature.LAKES
        
        assert new_lakes.scale == '110m'
        assert new_lakes.autoscale == False
        
    def test_autoscale_function(self):
        # Check that scale changes with extent when autoscale==True
        
        new_borders = cfeature.NaturalEarthFeature('cultural',
                                                   'admin_0_boundary_lines_land',
                                                   'auto', 
                                                   edgecolor='black',
                                                   facecolor='none')
        
        extent = (-6, -8, 56, 59)
        
        new_scale = new_borders._scale_from_extent(extent)
        
        assert new_borders.scale == 'auto'
        assert new_scale == '10m'
        
        