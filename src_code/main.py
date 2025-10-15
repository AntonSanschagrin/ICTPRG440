# main.py
# Author: Chan Yee
# Date: October 2025
# Description: Script to view and reproject vector spatial data for NSW
# -------------------------------------------------------------------

import geopandas as gpd

# Function 1: Read spatial vector data
def read_vector_data(file_path: str) -> gpd.GeoDataFrame:
    """
    Reads vector spatial data and returns a GeoDataFrame object.
    Parameters:
        file_path (str): Path to the vector file (e.g. shapefile or KML)
    Returns:
        gpd.GeoDataFrame: GeoDataFrame containing spatial data
    """
    try:
        gdf = gpd.read_file(file_path)
        print("✅ File successfully read.")
        return gdf
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None


# Function 2: Display attribute table row by row
def display_attributes(gdf: gpd.GeoDataFrame) -> None:
    """
    Displays attribute table row by row using a loop.
    Parameters:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame
    Returns:
        None
    """
    if gdf is None:
        print("⚠️ No data to display.")
        return

    print("\n--- Attribute Table ---")
    for index, row in gdf.iterrows():     # Looping through each record
        print(f"Row {index}: {row}")
    print("------------------------")


# Function 3: Reproject data and save as shapefile
def reproject_and_save(gdf: gpd.GeoDataFrame, epsg_code: int, output_path: str) -> None:
    """
    Reprojects vector data to a new coordinate system and saves output.
    Parameters:
        gdf (gpd.GeoDataFrame): Input GeoDataFrame
        epsg_code (int): Target EPSG code (e.g. 32756 for GDA2020 MGA Zone 56)
        output_path (str): Path for saving the projected shapefile
    Returns:
        None
    """
    try:
        projected = gdf.to_crs(epsg=epsg_code)
        projected.to_file(output_path)
        print(f"✅ Reprojected data saved to: {output_path}")
    except Exception as e:
        print(f"❌ Error during reprojection: {e}")


# ---------------- MAIN SCRIPT ----------------
if __name__ == "__main__":
    input_file = "spatial_data_original/Sydney_landmarks.kml"  # change filename if needed
    output_file = "spatial_data_projected/Sydney_landmarks_proj.shp"

    # Step 1: Read data
    data = read_vector_data(input_file)

    # Step 2: Display attributes
    display_attributes(data)

    # Step 3: Reproject (WGS84 -> GDA2020 / MGA Zone 56)
    reproject_and_save(data, 32756, output_file)

    print("🎯 Task 2 completed successfully!")

