import pandas as pd
import geopandas as geopandas
import osmnx as ox
import folium


def initmap():
    style = {'color': '#F7DC6F', 'weight':'1'}
    m = folium.Map([59.328197, 18.0351706], zoom_start=15)
    return m


def loadgarbagebins(garbfile):
    dataframe = pd.read_excel(garbfile,encoding = 'ISO-8859-1',sheet_name='Blad1', axis = 1)#, index_col=0,header=[1])
    return dataframe


def genpoints(df, m):
    n = 0
    tooltip = 'Garbage bin'
   
    for row in df.iterrows():
        s1 = str(row[1]['OBJECT_ID'])
        s2 = row[1]['MAIN_ATTR0']
        s3 = row[1]['Fabrikat']
        s4 = str(row[1]['Färg'])
        s = s1 + "<br>" + s2 + "<br>" + s3 + "<br>" + s4

        lat = row[1]['lat']
        lon = row[1]['lon']
        folium.Marker([lat, lon], popup=s, tooltip=tooltip).add_to(m)

    m.save("garbage.html")


def main():
    df = loadgarbagebins("./Skräpkorgar.xlsx")
    m = initmap()
    genpoints(df, m)


if __name__ == "__main__":
    main()