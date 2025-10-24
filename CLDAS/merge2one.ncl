begin
    dq = str_get_dq()
    date_cmd   = "date +" + dq + "%a %b %d %H:%M:%S %Z %Y" + dq
    wcStrt = systemfunc(date_cmd)
    ;---Processing----------------
    finames = systemfunc("ls |grep P_CLDAS |grep -v 0728")
    fi = addfiles(finames,"r")
    ListSetType(fi, "join")
    lat = fi[0]->LAT
    lon = fi[0]->LON
    rain = fi[0:71]->PRCP
    rain!0 = "hours"
    printVarSummary(rain)
    rain_3day = dim_sum_n_Wrap(rain, 0)
    rain_3day@units  ="mm/3day"
    rain_3day@long_name = "3-day accumulated precipitation"
    ;setfileoption("nc", "Format", "LargeFile")
    fiout = addfile("../../Figure1/CLDAS_Doksuri.nc","c")
    fiout->rain = rain
    fiout->rain_3day = rain_3day
    ;-----------------------------
    wallClockElapseTime(wcStrt, "Processing", 0)
    wcStrtGraphics = systemfunc(date_cmd)
    ;---Graphics------------------
    wallClockElapseTime(wcStrtGraphics, "Graphics", 0)
    wallClockElapseTime(wcStrt, "Processing and Graphics", 0)
end
