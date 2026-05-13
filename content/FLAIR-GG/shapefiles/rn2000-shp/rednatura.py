import geopandas as gpd
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot_shapefile(shapefile_path, title="Shapefile Plot"):
    # Read shapefile
    gdf = gpd.read_file(shapefile_path)
    gdf_plants = gdf[gdf["TIPO"].isin(["A", "B"])]

    # Print basic info
    print("CRS:", gdf_plants.crs)
    print("Number of features:", len(gdf_plants))

    # Plot
    gdf_plants.plot(edgecolor="black", facecolor="lightblue", figsize=(10, 8))
    plt.title(title)
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()


def plot_natura2000_types(shapefile_path):
    """
    Plots Natura 2000 sites in Spain grouped by directive type:
    - Habitats Directive (A+B)
    - Birds Directive (C)
    """
    # Load shapefile
    gdf = gpd.read_file(shapefile_path)

    # Group TIPO into human-readable directives
    def directive_group(tipo):
        if tipo in ["A", "B"]:
            return "Habitats Directive (A+B)"
        elif tipo == "C":
            return "Birds Directive (C)"
        else:
            return "Other"

    gdf["Directive"] = gdf["TIPO"].apply(directive_group)

    # Define colors
    color_map = {
        "Habitats Directive (A+B)": "green",
        "Birds Directive (C)": "blue",
        "Other": "grey"
    }

    # Plot
    fig, ax = plt.subplots(figsize=(10, 8))
    for group, data in gdf.groupby("Directive"):
        data.plot(ax=ax, facecolor=color_map.get(group, "grey"), edgecolor="black")

    # Create a proper legend
    patches = [mpatches.Patch(color=color, label=label) 
               for label, color in color_map.items() if label in gdf["Directive"].unique()]
    plt.legend(handles=patches, title="Natura 2000 Directives")

    plt.title("Natura 2000 Sites in Spain")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.show()




def inspect_shapefile(path):
    gdf = gpd.read_file(path)
    print("CRS:", gdf.crs)
    print("Number of features:", len(gdf))
    print("\nColumns (fields):")
    print(gdf.columns)
    print("\nField types:")
    print(gdf.dtypes)
    print("\nFirst few rows:")
    print(gdf.head())
    # Also, show statistics for numeric fields
    print("\nDescriptive stats for numeric fields:")
    print(gdf.describe())

    # Optionally, check unique values in certain fields
    for field in ["tipo", "figura", "categoria", "nombre", "biogeog"]:  # guess some names
        if field in gdf.columns:
            print(f"\nUnique values in {field}:")
            print(gdf[field].unique())

    return gdf

if __name__ == "__main__":
    # Replace with your shapefile path
    shapefile_path = "Es_Lic_SCI_Zepa_SPA_Medalpatl_202412.shp"
    plot_shapefile(shapefile_path)
    # plot_natura2000_types(shapefile_path)

    path = shapefile_path
    # gdf = inspect_shapefile(path)


    # gdf.drop(columns="geometry").to_csv("rn2000.csv", index=False)