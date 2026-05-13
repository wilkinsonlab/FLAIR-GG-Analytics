import rasterio
from rasterio.plot import show

# Path to your precipitation raster
raster_path = "w001001.adf"

# Open and inspect
with rasterio.open(raster_path) as src:
    print("=== Raster metadata ===")
    print(f"File: {raster_path}")
    print(f"CRS: {src.crs}")
    print(f"Width, Height: {src.width} x {src.height}")
    print(f"Number of bands: {src.count}")
    print(f"Resolution: {src.res}")
    print(f"Bounds: {src.bounds}")
    print(f"Nodata value: {src.nodata}")
    
    # Optional: quick visualization of first band
    show(src.read(1), title="Precipitation (first band)")

    # Optional: basic statistics of first band
    band1 = src.read(1, masked=True)
    print(f"Mean precipitation (masked): {band1.mean():.2f}")
    print(f"Min: {band1.min()}, Max: {band1.max()}")
