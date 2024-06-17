import math
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import matplotlib
import numpy as np
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from netCDF4 import Dataset
from matplotlib.colors import LogNorm
from datetime import datetime, timedelta, date
import xarray as xr
import warnings
import netCDF4
import nclcmaps
import sys
from mpl_toolkits.axes_grid1.inset_locator import inset_axes

def main():

	warnings.filterwarnings(action='ignore', message='Mean of empty slice')
	
	wdthres=0.1

	#'ITA','GER','FRA','SWI',UK

	regions=['UK', 'REGCM5','REGCM5_12','ERA5']

	# Managing the data for each individual location:
	
	file_ITA=Dataset('../data/regrid_GRIPHO_2001.nc')
	amount_array=np.array(file_ITA['bin_values'][:])
	
	amount_array[0]=0.1
	
	amount_array_zoom=np.linspace(0,1,11)
		
	if 'ITA' in regions:
		##### CODE FOR ITA #####
		print(datetime.now(),'reading in ITA precip dataset')
		file_ITA=Dataset('../data/regrid_GRIPHO_2001.nc')
		OBS_lat_ITA=np.array(file_ITA['lat'][:])
		OBS_lon_ITA=np.array(file_ITA['lon'][:])
		OBS_pr_hist_ITA=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA[OBS_pr_hist_ITA<0]=np.nan
		estimate_array_ITA=np.nansum(np.nansum(OBS_pr_hist_ITA,axis=1),axis=1)
		file_ITA=Dataset('../data/regrid_GRIPHO_2001_zoom.nc')
		OBS_pr_hist_ITA_zoom=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA_zoom[OBS_pr_hist_ITA_zoom<0]=np.nan
		estimate_array_ITA_zoom=np.nansum(np.nansum(OBS_pr_hist_ITA_zoom,axis=1),axis=1)
		print('reading 2002')
		file_ITA=Dataset('../data/regrid_GRIPHO_2002.nc')
		OBS_pr_hist_ITA=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA[OBS_pr_hist_ITA<0]=np.nan
		estimate_array_ITA=estimate_array_ITA+np.nansum(np.nansum(OBS_pr_hist_ITA,axis=1),axis=1)
		file_ITA=Dataset('../data/regrid_GRIPHO_2002_zoom.nc')
		OBS_pr_hist_ITA_zoom=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA_zoom[OBS_pr_hist_ITA_zoom<0]=np.nan
		estimate_array_ITA_zoom=estimate_array_ITA_zoom+np.nansum(np.nansum(OBS_pr_hist_ITA_zoom,axis=1),axis=1)
		print('reading 2003')
		file_ITA=Dataset('../data/regrid_GRIPHO_2003.nc')
		OBS_pr_hist_ITA=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA[OBS_pr_hist_ITA<0]=np.nan
		estimate_array_ITA=estimate_array_ITA+np.nansum(np.nansum(OBS_pr_hist_ITA,axis=1),axis=1)
		file_ITA=Dataset('../data/regrid_GRIPHO_2003_zoom.nc')
		OBS_pr_hist_ITA_zoom=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA_zoom[OBS_pr_hist_ITA_zoom<0]=np.nan
		estimate_array_ITA_zoom=estimate_array_ITA_zoom+np.nansum(np.nansum(OBS_pr_hist_ITA_zoom,axis=1),axis=1)
		print('reading 2004')
		file_ITA=Dataset('../data/regrid_GRIPHO_2004.nc')
		OBS_pr_hist_ITA=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA[OBS_pr_hist_ITA<0]=np.nan
		estimate_array_ITA=estimate_array_ITA+np.nansum(np.nansum(OBS_pr_hist_ITA,axis=1),axis=1)
		file_ITA=Dataset('../data/regrid_GRIPHO_2004_zoom.nc')
		OBS_pr_hist_ITA_zoom=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA_zoom[OBS_pr_hist_ITA_zoom<0]=np.nan
		estimate_array_ITA_zoom=estimate_array_ITA_zoom+np.nansum(np.nansum(OBS_pr_hist_ITA_zoom,axis=1),axis=1)
		print('reading 2005')
		file_ITA=Dataset('../data/regrid_GRIPHO_2005.nc')
		OBS_pr_hist_ITA=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA[OBS_pr_hist_ITA<0]=np.nan
		estimate_array_ITA=estimate_array_ITA+np.nansum(np.nansum(OBS_pr_hist_ITA,axis=1),axis=1)
		file_ITA=Dataset('../data/regrid_GRIPHO_2005_zoom.nc')
		OBS_pr_hist_ITA_zoom=np.array(file_ITA['pr_hist'][:,:,:])
		OBS_pr_hist_ITA_zoom[OBS_pr_hist_ITA_zoom<0]=np.nan
		estimate_array_ITA_zoom=estimate_array_ITA_zoom+np.nansum(np.nansum(OBS_pr_hist_ITA_zoom,axis=1),axis=1)


	if 'SWI' in regions:
		##### CODE FOR SWI #####
		print(datetime.now(),'reading in SWI precip dataset')
		file_SWI=Dataset('../data/regrid_RdisaggH_2003.nc')
		OBS_lat_SWI=np.array(file_SWI['lat'][:])
		OBS_lon_SWI=np.array(file_SWI['lon'][:])
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI=np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		file_SWI=Dataset('../data/regrid_RdisaggH_2003_zoom.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI_zoom=np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		print('reading 2004')
		file_SWI=Dataset('../data/regrid_RdisaggH_2004.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		estimate_array_SWI=estimate_array_SWI+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		file_SWI=Dataset('../data/regrid_RdisaggH_2004_zoom.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI_zoom=estimate_array_SWI_zoom+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		print('reading 2005')
		file_SWI=Dataset('../data/regrid_RdisaggH_2005.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		estimate_array_SWI=estimate_array_SWI+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		file_SWI=Dataset('../data/regrid_RdisaggH_2005_zoom.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI_zoom=estimate_array_SWI_zoom+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		print('reading 2006')
		file_SWI=Dataset('../data/regrid_RdisaggH_2006.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		estimate_array_SWI=estimate_array_SWI+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		file_SWI=Dataset('../data/regrid_RdisaggH_2006_zoom.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI_zoom=estimate_array_SWI_zoom+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		print('reading 2007')
		file_SWI=Dataset('../data/regrid_RdisaggH_2007.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		estimate_array_SWI=estimate_array_SWI+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)
		file_SWI=Dataset('../data/regrid_RdisaggH_2007_zoom.nc')
		OBS_pr_hist_SWI=np.array(file_SWI['pr_hist'][:,:,:])
		OBS_pr_hist_SWI[OBS_pr_hist_SWI<0]=np.nan
		OBS_pr_hist_SWI[OBS_pr_hist_SWI>10**5]=np.nan
		estimate_array_SWI_zoom=estimate_array_SWI_zoom+np.nansum(np.nansum(OBS_pr_hist_SWI,axis=1),axis=1)


	if 'GER' in regions:
		##### CODE FOR GER #####
		print(datetime.now(),'reading in GER precip dataset')
		file_GER=Dataset('../data/regrid_RADKLIM_2005.nc')
		OBS_lat_GER=np.array(file_GER['lat'][:])
		OBS_lon_GER=np.array(file_GER['lon'][:])
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER=np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		file_GER=Dataset('../data/regrid_RADKLIM_2005_zoom.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER_zoom=np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		print('reading 2004')		
		file_GER=Dataset('../data/regrid_RADKLIM_2004.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER=estimate_array_GER+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		file_GER=Dataset('../data/regrid_RADKLIM_2004_zoom.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER_zoom=estimate_array_GER_zoom+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		print('reading 2003')
		file_GER=Dataset('../data/regrid_RADKLIM_2003.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER=estimate_array_GER+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		file_GER=Dataset('../data/regrid_RADKLIM_2003_zoom.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER_zoom=estimate_array_GER_zoom+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		print('reading 2002')
		file_GER=Dataset('../data/regrid_RADKLIM_2002.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER=estimate_array_GER+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		file_GER=Dataset('../data/regrid_RADKLIM_2002_zoom.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER_zoom=estimate_array_GER_zoom+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		print('reading 2001')
		file_GER=Dataset('../data/regrid_RADKLIM_2001.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER=estimate_array_GER+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
		file_GER=Dataset('../data/regrid_RADKLIM_2001_zoom.nc')
		OBS_pr_hist_GER=np.array(file_GER['pr_hist'][:,:,:])
		OBS_pr_hist_GER[OBS_pr_hist_GER<0]=np.nan
		OBS_pr_hist_GER[OBS_pr_hist_GER>10**5]=np.nan
		estimate_array_GER_zoom=estimate_array_GER_zoom+np.nansum(np.nansum(OBS_pr_hist_GER,axis=1),axis=1)
	
	if 'FRA' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in FRA precip dataset')
		file_FRA=Dataset('../data/regrid_COMPHORE_2004.nc')
		OBS_lat_FRA=np.array(file_FRA['lat'][:])
		OBS_lon_FRA=np.array(file_FRA['lon'][:])
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA=np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		file_FRA=Dataset('../data/regrid_COMPHORE_2004_zoom.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA_zoom=np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		print('reading 2003')
		file_FRA=Dataset('../data/regrid_COMPHORE_2003.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA=estimate_array_FRA+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		file_FRA=Dataset('../data/regrid_COMPHORE_2003_zoom.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA_zoom=estimate_array_FRA_zoom+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)		
		print('reading 2002')
		file_FRA=Dataset('../data/regrid_COMPHORE_2002.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA=estimate_array_FRA+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		file_FRA=Dataset('../data/regrid_COMPHORE_2002_zoom.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA_zoom=estimate_array_FRA_zoom+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		print('reading 2001')
		file_FRA=Dataset('../data/regrid_COMPHORE_2001.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA=estimate_array_FRA+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		file_FRA=Dataset('../data/regrid_COMPHORE_2001_zoom.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA_zoom=estimate_array_FRA_zoom+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)		
		print('reading 2000')
		file_FRA=Dataset('../data/regrid_COMPHORE_2000.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA=estimate_array_FRA+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
		file_FRA=Dataset('../data/regrid_COMPHORE_2000_zoom.nc')
		OBS_pr_hist_FRA=np.array(file_FRA['pr_hist'][:,:,:])
		OBS_pr_hist_FRA[OBS_pr_hist_FRA<0]=np.nan
		OBS_pr_hist_FRA[OBS_pr_hist_FRA>10**5]=np.nan
		estimate_array_FRA_zoom=estimate_array_FRA_zoom+np.nansum(np.nansum(OBS_pr_hist_FRA,axis=1),axis=1)
	
	if 'UK' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in UK precip dataset')
		file_UK=Dataset('../data/regrid_CEH-GEAR_2004.nc')
		OBS_lat_UK=np.array(file_UK['lat'][:])
		OBS_lon_UK=np.array(file_UK['lon'][:])
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK=np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)
		file_UK=Dataset('../data/regrid_CEH-GEAR_2004_zoom.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK_zoom=np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)		
		print('reading 2003')
		file_UK=Dataset('../data/regrid_CEH-GEAR_2003.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK=estimate_array_UK+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)
		file_UK=Dataset('../data/regrid_CEH-GEAR_2003_zoom.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK_zoom=estimate_array_UK_zoom+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)
		print('reading 2002')
		file_UK=Dataset('../data/regrid_CEH-GEAR_2002.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK=estimate_array_UK+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)
		file_UK=Dataset('../data/regrid_CEH-GEAR_2002_zoom.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK_zoom=estimate_array_UK_zoom+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)		
		print('reading 2001')
		file_UK=Dataset('../data/regrid_CEH-GEAR_2001.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK=estimate_array_UK+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)
		file_UK=Dataset('../data/regrid_CEH-GEAR_2001_zoom.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK_zoom=estimate_array_UK_zoom+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)		
		print('reading 2000')
		file_UK=Dataset('../data/regrid_CEH-GEAR_2000.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK=estimate_array_UK+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)	
		file_UK=Dataset('../data/regrid_CEH-GEAR_2000_zoom.nc')
		OBS_pr_hist_UK=np.array(file_UK['pr_hist'][:,:,:])
		OBS_pr_hist_UK[OBS_pr_hist_UK<0]=np.nan
		OBS_pr_hist_UK[OBS_pr_hist_UK>10**5]=np.nan
		estimate_array_UK_zoom=estimate_array_UK_zoom+np.nansum(np.nansum(OBS_pr_hist_UK,axis=1),axis=1)	

	
	if 'ITA' in regions:
		index=np.where(np.nansum(OBS_pr_hist_ITA, axis=0)<=0)
	if 'SWI' in regions:
		index=np.where(np.nansum(OBS_pr_hist_SWI, axis=0)<=0)
	if 'GER' in regions:
		index=np.where(np.nansum(OBS_pr_hist_GER, axis=0)<=0)
	if 'FRA' in regions:
		index=np.where(np.nansum(OBS_pr_hist_FRA, axis=0)<=0)
	if 'UK' in regions:
		index=np.where(np.nansum(OBS_pr_hist_UK, axis=0)<=0)

	if 'REGCM5' in regions:
		##### CODE FOR REGCM5 #####
		print(datetime.now(),'reading in REGCM5 precip dataset')
		path= '../data/'
		file_REGCM5=Dataset(path+'regrid_REGCM5_2000.nc')
		OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
		OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array=np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_hist_2000_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_zoom=np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)
		print('reading 2001')
		file_REGCM5=Dataset(path+'regrid_REGCM5_2001.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan		
		estimate_array=estimate_array+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_hist_2001_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_zoom=estimate_array_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)
		print('reading 2002')
		file_REGCM5=Dataset(path+'regrid_REGCM5_2002.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array=estimate_array+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_hist_2002_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_zoom=estimate_array_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)
		print('reading 2003')
		file_REGCM5=Dataset(path+'regrid_REGCM5_2003.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array=estimate_array+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_hist_2003_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_zoom=estimate_array_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)
		print('reading 2004')
		file_REGCM5=Dataset(path+'regrid_REGCM5_2004.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array=estimate_array+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_hist_2004_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_zoom=estimate_array_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)

	if 'REGCM5_12' in regions:
		##### CODE FOR REGCM5 #####
		print(datetime.now(),'reading in REGCM5 12km precip dataset')
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2000.nc')
		OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
		OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array_12k=np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2000_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_12k_zoom=np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)
		print('reading 2001')
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2001.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan		
		estimate_array_12k=estimate_array_12k+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2001_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_12k_zoom=estimate_array_12k_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)		
		print('reading 2002')
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2002.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array_12k=estimate_array_12k+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2002_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_12k_zoom=estimate_array_12k_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)            
		print('reading 2003')
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2003.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array_12k=estimate_array_12k+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2003_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_12k_zoom=estimate_array_12k_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)            
		print('reading 2004')
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2004.nc')
		OBS_pr_hist_REGCM5=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5[OBS_pr_hist_REGCM5<0]=np.nan
		OBS_pr_hist_REGCM5[:,index[0],index[1]]=np.nan
		estimate_array_12k=estimate_array_12k+np.nansum(np.nansum(OBS_pr_hist_REGCM5,axis=1),axis=1)
		file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hist_2004_zoom.nc')
		OBS_pr_hist_REGCM5_zoom=np.array(file_REGCM5['pr_hist'][:,:,:])
		OBS_pr_hist_REGCM5_zoom[OBS_pr_hist_REGCM5_zoom<0]=np.nan
		OBS_pr_hist_REGCM5_zoom[:,index[0],index[1]]=np.nan
		estimate_array_12k_zoom=estimate_array_12k_zoom+np.nansum(np.nansum(OBS_pr_hist_REGCM5_zoom,axis=1),axis=1)            

	if 'ERA5' in regions:
		##### CODE FOR REGCM5 #####
		print(datetime.now(),'reading in ERA5 precip dataset')
		file_ERA5=Dataset('../data/regrid_ERA5_2004.nc')
		OBS_lat_ERA5=np.array(file_ERA5['lat'][:])
		OBS_lon_ERA5=np.array(file_ERA5['lon'][:])
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5=np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		file_ERA5=Dataset('../data/regrid_ERA5_2004_zoom.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5_zoom=np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		print('reading 2003')
		file_ERA5=Dataset('../data/regrid_ERA5_2003.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan		
		estimate_array_ERA5=estimate_array_ERA5+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		file_ERA5=Dataset('../data/regrid_ERA5_2003_zoom.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5_zoom=estimate_array_ERA5_zoom+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		print('reading 2002')
		file_ERA5=Dataset('../data/regrid_ERA5_2002.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5=estimate_array_ERA5+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		file_ERA5=Dataset('../data/regrid_ERA5_2002_zoom.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5_zoom=estimate_array_ERA5_zoom+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		print('reading 2001')
		file_ERA5=Dataset('../data/regrid_ERA5_2001.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5=estimate_array_ERA5+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		file_ERA5=Dataset('../data/regrid_ERA5_2001_zoom.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5_zoom=estimate_array_ERA5_zoom+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)		
		print('reading 2000')
		file_ERA5=Dataset('../data/regrid_ERA5_2000.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5=estimate_array_ERA5+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
		file_ERA5=Dataset('../data/regrid_ERA5_2000_zoom.nc')
		OBS_pr_hist_ERA5=np.array(file_ERA5['pr_hist'][:,:,:])
		OBS_pr_hist_ERA5[OBS_pr_hist_ERA5<0]=np.nan
		OBS_pr_hist_ERA5[:,index[0],index[1]]=np.nan
		estimate_array_ERA5_zoom=estimate_array_ERA5_zoom+np.nansum(np.nansum(OBS_pr_hist_ERA5,axis=1),axis=1)
	
	matplotlib.rcParams.update({'font.size': 22})
	
	fig = plt.figure(figsize=(8,8))
	ax = plt.gca()
	
	if 'REGCM5' in regions:	
		esum=np.nansum(estimate_array)
		estimate_array=estimate_array/esum
		esum=np.nansum(estimate_array_12k)
		estimate_array_zoom=estimate_array_zoom/esum
		estimate_array_zoom[0]=estimate_array[0]		
	if 'REGCM5_12' in regions:
		esum=np.nansum(estimate_array_12k)
		estimate_array_12k=estimate_array_12k/esum
		estimate_array_12k_zoom=estimate_array_12k_zoom/esum
		estimate_array_12k_zoom[0]=estimate_array_12k[0]
	if 'ITA' in regions:
		esum=np.nansum(estimate_array_ITA)
		estimate_array_ITA=estimate_array_ITA/esum
		estimate_array_ITA_zoom=estimate_array_ITA_zoom/esum
		estimate_array_ITA_zoom[0]=estimate_array_ITA[0]
	if 'SWI' in regions:	
		esum=np.nansum(estimate_array_SWI)
		estimate_array_SWI=estimate_array_SWI/esum
		estimate_array_SWI_zoom=estimate_array_SWI_zoom/esum
		estimate_array_SWI_zoom[0]=estimate_array_SWI[0]
	if 'ERA5' in regions:		
		esum=np.nansum(estimate_array_ERA5)
		estimate_array_ERA5=estimate_array_ERA5/esum
		estimate_array_ERA5_zoom=estimate_array_ERA5_zoom/esum
		estimate_array_ERA5_zoom[0]=estimate_array_ERA5[0]
	if 'GER' in regions:
		esum=np.nansum(estimate_array_GER)
		estimate_array_GER=estimate_array_GER/esum
		estimate_array_GER_zoom=estimate_array_GER_zoom/esum
		estimate_array_GER_zoom[0]=estimate_array_GER[0]
	if 'FRA' in regions:
		esum=np.nansum(estimate_array_FRA)
		estimate_array_FRA=estimate_array_FRA/esum
		estimate_array_FRA_zoom=estimate_array_FRA_zoom/esum
		estimate_array_FRA_zoom[0]=estimate_array_FRA[0]
	if 'UK' in regions:
		esum=np.nansum(estimate_array_UK)
		estimate_array_UK=estimate_array_UK/esum
		estimate_array_UK_zoom=estimate_array_UK_zoom/esum
		estimate_array_UK_zoom[0]=estimate_array_UK[0]		
		
	print('plotting')
	
	alpha=1.0
	
	ax.set_facecolor('xkcd:light grey')
	if 'REGCM5' in regions:	
		ax.plot(amount_array, estimate_array, 'o', c='orange', markeredgecolor='orange', label='REGCM5 CP')
	if 'REGCM5_12' in regions:	
		ax.plot(amount_array, estimate_array_12k, 'o', c='red', markeredgecolor='red', label='REGCM5 12km')	
	if 'ITA' in regions:
		ax.plot(amount_array, estimate_array_ITA, 'o', c='black', markeredgecolor='black', label='GRIPHO')
	if 'SWI' in regions:
		ax.plot(amount_array, estimate_array_SWI, 'o', c='black', markeredgecolor='black', label='RdisaggH')
	if 'ERA5' in regions:
		ax.plot(amount_array, estimate_array_ERA5, 'o', c='blue', markeredgecolor='blue', label='ERA5')	
	if 'GER' in regions:
		ax.plot(amount_array, estimate_array_GER, 'o', c='black', markeredgecolor='black', label='RADKLIM')
	if 'FRA' in regions:
		ax.plot(amount_array, estimate_array_FRA, 'o', c='black', markeredgecolor='black', label='COMEPHORE')
	if 'UK' in regions:
		ax.plot(amount_array, estimate_array_UK, 'o', c='black', markeredgecolor='black', label='CEH-GEAR')
	
	plt.grid(color='w')

	# Create dummy Line2D objects for legend
	h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
	h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
	h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
	h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
	
	# Plot legend.
	plt.legend([h1, h2, h3, h4], ['RegCM5 CP', 'RegCM5 12km', 'ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
	
	matplotlib.rcParams.update({'font.size': 12})
	
	axins2 = inset_axes(ax, width="30%", height="30%", loc=3, borderpad=3)
	axins2.set_facecolor('xkcd:light grey')
	
	if 'REGCM5' in regions:	
		axins2.plot(amount_array_zoom[1:], estimate_array_zoom[1:], 'o', c='orange', markeredgecolor='orange', label='REGCM5 CP')
	if 'REGCM5_12' in regions:	
		axins2.plot(amount_array_zoom[1:], estimate_array_12k_zoom[1:], 'o', c='red', markeredgecolor='red', label='REGCM5 12km')	
	if 'ITA' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_ITA_zoom[1:], 'o', c='black', markeredgecolor='black', label='GRIPHO')
	if 'SWI' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_SWI_zoom[1:], 'o', c='black', markeredgecolor='black', label='RdisaggH')
	if 'ERA5' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_ERA5_zoom[1:], 'o', c='blue', markeredgecolor='blue', label='ERA5')	
	if 'GER' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_GER_zoom[1:], 'o', c='black', markeredgecolor='black', label='RADKLIM')
	if 'FRA' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_FRA_zoom[1:], 'o', c='black', markeredgecolor='black', label='COMEPHORE')
	if 'UK' in regions:
		axins2.plot(amount_array_zoom[1:], estimate_array_UK_zoom[1:], 'o', c='black', markeredgecolor='black', label='CEH-GEAR')
	axins2.set_yscale('log')
	axins2.set_xscale('log')
	
	plt.grid(color='white')
	ax.set_yscale('log')
	ax.set_xscale('log')
	ax.set_ylabel('proportions', fontsize=18)
	ax.set_xlabel('precipitation intensity (mm/hr)', fontsize=18)
	
	#axins2.set_ylabel('proportions', fontsize=12)
	#axins2.set_xlabel('precipitation intensity (mm/hr)', fontsize=12)
	if 'ITA' in regions:
		ax.set_title('Italy', fontsize=24)
	if 'FRA' in regions:
		ax.set_title('France', fontsize=24)
	if 'GER' in regions:
		ax.set_title('Germany', fontsize=24)
	if 'SWI' in regions:
		ax.set_title('Switzerland', fontsize=24)
	if 'UK' in regions:
		ax.set_title('Great Britain', fontsize=24)
	ax.tick_params(labelsize=18)
	

	
	if 'ITA' in regions:	
		plt.savefig('../plots/Fig11_ITA.png', bbox_inches='tight', dpi=200) 
	if 'SWI' in regions:	
		plt.savefig('../plots/Fig11_SWI.png', bbox_inches='tight', dpi=200) 
	if 'FRA' in regions:	
		plt.savefig('../plots/Fig11_FRA.png', bbox_inches='tight', dpi=200) 
	if 'GER' in regions:	
		plt.savefig('../plots/Fig11_GER.png', bbox_inches='tight', dpi=200) 
	if 'UK' in regions:	
		plt.savefig('../plots/Fig11_UK.png', bbox_inches='tight', dpi=200) 
	

main()
