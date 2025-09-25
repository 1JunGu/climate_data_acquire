import os
import requests
from datetime import datetime, timedelta
import json

BASE_URL = "https://weather.uwyo.edu/"

def get_available_stations(date: datetime):
    #dt_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:00:00"
    dt_str = date.strftime("%Y-%m-%d %H:00:00")
    url = f"{BASE_URL}/wsgi/sounding_json?datetime={dt_str}"
    resp = requests.get(url)
    if resp.status_code == 200:
        ##write to file
        #with open("stations.json", "w", encoding="utf-8") as f:
        #    json.dump(resp.json()["stations"], f, ensure_ascii=False, indent=4)
        return resp.json()["stations"]
    else:
        print(f"Failed to get stations for {dt_str}")
        return []

def filter_stations_within_region(stations, minlat, maxlat, minlon, maxlon):
    filtered = []
    for st in stations:
        lat = float(st.get("lat", 0))
        lon = float(st.get("lon", 0))
        if minlat <= lat <= maxlat and minlon <= lon <= maxlon:
            print(f"Station {st['stationid']} name: {st['name']} at ({lat}, {lon}) is within the region.")
            filtered.append(st)
    return filtered

def download_sounding_data(datetime: datetime, stid: str, src: str, out_dir: str) -> bool:
    #dt_str = f"{year}-{month:02d}-{day:02d} {hour:02d}:00:00"
    dt_str = datetime.strftime("%Y-%m-%d %H:00:00")
    url = f"{BASE_URL}/wsgi/sounding"
    params = {
        "datetime": dt_str,
        "id": stid,
        "src": src,
        "type": "TEXT:CSV"
    }
    resp = requests.get(url, params=params)
    if resp.status_code == 200:
        filename = f"{datetime.strftime('%Y%m%d_%H')}_{stid}.csv"
        with open(f"{out_dir}/{filename}", "w") as f:
            f.write(resp.text)
        return True
    return False

start_date = datetime(2023, 7, 27, 0)
end_date = datetime(2023, 7, 28, 21)
#generate dates list with 3-hour interval
date_list = []
current_date = start_date   
while current_date <= end_date:
    date_list.append(current_date)
    current_date += timedelta(hours=3)

for dt in date_list:
    selected_date = dt
    stations = get_available_stations(selected_date)
    stations_filtered = filter_stations_within_region(stations, 28, 45, 105, 130)
    #make dir containing data
    if not os.path.exists(selected_date.strftime("%Y%m%d_%H")):
        os.makedirs(selected_date.strftime("%Y%m%d_%H"))
    for st in stations_filtered:
        if st["src"] in ["BUFR", "TEMP"]:
            print(f"Downloading data for station {st['stationid']} from source {st['src']}")
            isSuccess = download_sounding_data(selected_date, st["stationid"], st["src"], selected_date.strftime("%Y%m%d_%H"))
            if isSuccess:
                pass
            else:
                print(f"❌Failed to download data for station {st['stationid']}")
