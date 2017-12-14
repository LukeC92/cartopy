"""
Demonstrate autoscaling of coastlines
---------------------------------------------
This example demonstrates the effect of setting the scale of a
NaturalEarthFeature to 'auto', in this case for coastlines.
This is done by defining a coastlines feature with the autoscaling argument
and plotting the object on three subplots, each at a different extent,
which in turn automatically scales the coastlines feature accordingly.
"""
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.pyplot as plt


def main():
    # Create coastlines feature with autoscaling
    coastline = cfeature.NaturalEarthFeature('physical', 'coastline', 'auto',
                                             edgecolor='black',
                                             facecolor='none')

    # Specify axes projection
    projection = ccrs.PlateCarree()

    # Define some extents (in degrees)
    extents = ((-5, -8, 56, 59),
               (-12, 8, 40, 60),
               (-25, 35, 12, 70))

    # Create a figure
    fig = plt.figure()

    for plot in range(1, 4):
        # Add GeoAxes object
        ax = fig.add_subplot(1, 3, plot,
                             projection=projection)

        # Add coastlines (without specifying resolution)
        ax.add_feature(coastline)

        # Set the extent (can be done after or before adding coastlines)
        ax.set_extent(extents[plot-1])

    # Display plot
    plt.show()


if __name__ == "__main__":

    main()
