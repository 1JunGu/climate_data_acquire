import cdsapi
import os
import sys
import multiprocessing
import pandas as pd
import calendar

def retrieve_era5_data(dataset, variables, year, month, day, time, file_path, pl_list=None):
    print(f'dataset: {dataset} year : {year} month: {month} day: {day} file_path: {file_path}')
    if dataset == 'sl':
        name = 'reanalysis-era5-single-levels'
        progress_flag=False
        params = {
                'product_type': 'reanalysis',
                'format': 'grib',
                'variable': variables,
                'year': year,
                'month': month,
                'day': day,
                'time': time,
        }
    elif dataset == 'pl':
        if pl_list is None:
            raise ValueError('please provide a list of pressure levels')
        name = 'reanalysis-era5-pressure-levels'
        progress_flag=False
        params = {
                'product_type': 'reanalysis',
                'format': 'grib',
                'variable': variables,
                'year': year,
                'month': month,
                'day': day,
                'time': time,
                'pressure_level': pl_list,
        }
    else:
        #raise error
        raise ValueError('please enter a valid dataset name (sl or pl)')
    c = cdsapi.Client(progress=progress_flag)
    c.retrieve(name, params, file_path)

# Main program
#name of Tropical Cyclone
dir_name='2305Doksuri'
#initial time of the forecast List
init_time=['2023-07-27T19:00:00','2023-07-27T23:00:00']
#period of surface
start_date = '2023-07-26'
end_date = '2023-08-03'

#create a directory named dir_name
if not os.path.exists(dir_name):
    os.makedirs(dir_name)

#create a queue to pass to processes
queue = multiprocessing.Queue()

#create a list to hold our processes
jobs = []

#Download the data for init_final
for init_hour in pd.date_range(start=init_time[0], end=init_time[1], freq='h'):
    init_hour_str = init_hour.strftime("%Y-%m-%dT%H:%M:%S")
    print(init_hour_str)
    print(type(init_hour_str))
    init_year = init_hour_str[:4]
    init_month = init_hour_str[5:7]
    init_day = init_hour_str[8:10]
    init_hour = init_hour_str[11:16]

    pl_var_list=['geopotential', 'relative_humidity', 'temperature','u_component_of_wind', 'v_component_of_wind']
    pl_list=[
                '1', '2', '3',
                '5', '7', '10',
                '20', '30', '50',
                '70', '100', '125',
                '150', '175', '200',
                '225', '250', '300',
                '350', '400', '450',
                '500', '550', '600',
                '650', '700', '750',
                '775', '800', '825',
                '850', '875', '900',
                '925', '950', '975',
                '1000',
            ]
    file_path = os.path.join(dir_name, f'pl_{init_year}_{init_month}_{init_day}_{init_hour}.grib')
    p = multiprocessing.Process(target=retrieve_era5_data, args=('pl', pl_var_list, init_year, init_month, init_day, init_hour, file_path, pl_list))
    jobs.append(p)
    p.start()

    sl_var_list=[
                '10m_u_component_of_wind', '10m_v_component_of_wind', '2m_dewpoint_temperature',
                '2m_temperature', 'land_sea_mask', 'mean_sea_level_pressure',
                'sea_ice_cover', 'sea_surface_temperature', 'skin_temperature',
                'snow_depth', 'soil_temperature_level_1', 'soil_temperature_level_2',
                'soil_temperature_level_3', 'soil_temperature_level_4', 'surface_pressure',
                'volumetric_soil_water_layer_1', 'volumetric_soil_water_layer_2', 'volumetric_soil_water_layer_3',
                'volumetric_soil_water_layer_4',
                ]
    file_path = os.path.join(dir_name, f'sl_{init_year}_{init_month}_{init_day}_{init_hour}.grib')
    p = multiprocessing.Process(target=retrieve_era5_data, args=('sl', sl_var_list, init_year, init_month, init_day, init_hour, file_path))
    jobs.append(p)
    p.start()

#Download the data for surface_update
#sfc_var_list = ['land_sea_mask', 'sea_ice_cover', 'sea_surface_temperature']
#
#time_list = [
#    '00:00', '01:00', '02:00', '03:00',
#    '04:00', '05:00', '06:00', '07:00',
#    '08:00', '09:00', '10:00', '11:00',
#    '12:00', '13:00', '14:00', '15:00',
#    '16:00', '17:00', '18:00', '19:00',
#    '20:00', '21:00', '22:00', '23:00',
#]
#
#start_year = start_date[:4]
#start_month = start_date[5:7]
#end_year = end_date[:4]
#end_month = end_date[5:7]
#
#if start_year == end_year and start_month == end_month:
#    # Retrieve data for a single month
#    day_list = pd.date_range(start_date, end_date, freq='D').strftime('%d').tolist()
#    file_path = os.path.join(dir_name, f'sfc_{start_date}-{end_date}.grib')
#    #retrieve_era5_data(sfc_var_list, start_year, start_month, day_list, time_list, file_path)
#    p = multiprocessing.Process(target=retrieve_era5_data, args=('sl', sfc_var_list, start_year, start_month, day_list, time_list, file_path))
#    jobs.append(p)
#    p.start()
#else:
#    # Retrieve data for multiple months
#    ## Retrieve data for the first month
#    last_day = calendar.monthrange(int(start_year), int(start_month))[1]
#    day_list = pd.date_range(start_date, f'{start_year}-{start_month}-{last_day}', freq='D').strftime('%d').tolist()
#    file_path = os.path.join(dir_name, f'sfc_{start_date}-{start_year}-{start_month}-{last_day}.grib')
#    #retrieve_era5_data(sfc_var_list, start_year, start_month, day_list, time_list, file_path)
#    p = multiprocessing.Process(target=retrieve_era5_data, args=('sl',sfc_var_list, start_year, start_month, day_list, time_list, file_path))
#    jobs.append(p)
#    p.start()
#
#    # Retrieve data for the months in between
#    for year_month in pd.date_range(start=f'{start_year}-{int(start_month)+1:02}', end=f'{end_year}-{int(end_month)-1:02}', freq='MS'):
#        year_month_str = year_month.strftime('%Y-%m')
#        last_day = calendar.monthrange(int(year_month_str[:4]), int(year_month_str[5:7]))[1]
#        day_list = pd.date_range(f'{year_month_str}-01', f'{year_month_str}-{last_day}', freq='D').strftime('%d').tolist()
#        file_path = os.path.join(dir_name, f'sfc_{year_month_str}.grib')
#        #retrieve_era5_data(sfc_var_list, year_month_str[:4], year_month_str[5:7], day_list, time_list, file_path)
#        p = multiprocessing.Process(target=retrieve_era5_data, args=('sl',sfc_var_list, year_month_str[:4], year_month_str[5:7], day_list, time_list, file_path))
#        jobs.append(p)
#        p.start()
#
#    # Retrieve data for the last month
#    day_list = pd.date_range(f'{end_year}-{end_month}-01', end_date, freq='D').strftime('%d').tolist()
#    file_path = os.path.join(dir_name, f'sfc_{end_year}-{end_month}-01-{end_date}.grib')
#    p = multiprocessing.Process(target=retrieve_era5_data, args=('sl',sfc_var_list, end_year, end_month, day_list, time_list, file_path))
#    jobs.append(p)
#    p.start()
#wait for all processes to finish
print("All Requests finished !")
for p in jobs:
    p.join(timeout=None)
print(f'All data downloaded to {dir_name}')
#os.system(f'tar cvzf  {dir_name}.tar.gz {dir_name}')
