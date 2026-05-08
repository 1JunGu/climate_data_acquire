import os
from datetime import datetime, timedelta
import subprocess

def download_data(start_date, end_date, base_dir):
    base_url = "https://data.gesdisc.earthdata.nasa.gov/data/GPM_L3/GPM_3IMERGDF.07/{year}/{month}/3B-DAY.MS.MRG.3IMERG.{date}-S000000-E235959.V07B.nc4"
    
    current_date = start_date
    while current_date <= end_date:
        year = current_date.strftime("%Y")
        month = current_date.strftime("%m")
        date = current_date.strftime("%Y%m%d")
        
        url = base_url.format(year=year, month=month, date=date)
        
        # Create year directory if it doesn't exist
        year_dir = os.path.join(base_dir, year)
        os.makedirs(year_dir, exist_ok=True)
        
        # Download file using wget with cookies
        wget_command = [
            "wget",
            "--load-cookies", "~/.urs_cookies",
            "--save-cookies", "~/.urs_cookies",
            "--keep-session-cookies",
            "-P", year_dir,
            url
        ]
        subprocess.run(wget_command)
        
        current_date += timedelta(days=1)

# Example usage
start_date = datetime(2019, 6, 10)
end_date = datetime(2019, 7, 10)
base_dir = "./IMERG_Day"

download_data(start_date, end_date, base_dir)
