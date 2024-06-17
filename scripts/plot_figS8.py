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
import resource

def main():

	warnings.filterwarnings(action='ignore', message='Mean of empty slice')
	
	wdthres=0.1

	#'ITA','GER','FRA','SWI',

	regions=['NOR','SWE','UK','GER','CARPAT','FRA','EURO4M','SWI','ITA','SPA']
	
	
	fig = plt.figure(figsize=(28,34))

	file_OBS=Dataset('../data/regrid_daily_EOBS_hist_2000-2004_tas.nc')
	file_REG=Dataset('../data/regrid_daily_REGCM5_CP_hist_2000-2004_tas_ALL.nc')
	file_REG12=Dataset('../data/regrid_daily_REGCM5_12km_hist_2000-2004_tas_ALL.nc')
	file_ERA5=Dataset('../data/regrid_daily_ERA5_hist_2000-2004_tas_ALL.nc')

	
	if 'GER' in regions:
		##### CODE FOR GER #####
		print(datetime.now(),'reading in GER temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_REGNIE_2000-2004.nc')
				
		maxbin=181
		
		latmin=300
		latmax=700
		lonmin=1000
		lonmax=1400
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
		
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')
		
		matplotlib.rcParams.update({'font.size': 20})
	
		ax5= fig.add_subplot(4,3,5)
		alpha=1.0

		ax5.set_facecolor('xkcd:light grey')	
		ax5.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='RegCM5 CP')	
		ax5.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='RegCM5 12k')
		ax5.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax5.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='OBS')
		plt.grid(color='w')
		#ax5.set_yscale('log')
		#ax.set_xscale('log')
		ax5.set_ylabel('proportions', fontsize=18)
		ax5.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax5.set_title('Germany', fontsize=24)
		ax5.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(30), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(30), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(30), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(30), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_GER_daily.png', bbox_inches='tight', dpi=200) 
	
	if 'UK' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in UK temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_ENG-REGR_2000-2004.nc')
			
		maxbin=181
		
		latmin=500
		latmax=800
		lonmin=500
		lonmax=1000
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
		
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0
		
		print('plotting')
		
		ax4= fig.add_subplot(4,3,4)
		alpha=1.0

		ax4.set_facecolor('xkcd:light grey')	
		ax4.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax4.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax4.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax4.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax4.set_yscale('log')
		#ax.set_xscale('log')
		ax4.set_ylabel('proportions', fontsize=18)
		ax4.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax4.set_title('United Kingdom', fontsize=24)
		ax4.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_UK_daily.png', bbox_inches='tight', dpi=200) 	
	if 'NOR' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in NORWAY temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_NORWAY-METNO_2000-2004.nc')

		maxbin=181
		
		latmin=800
		latmax=1000
		lonmin=1000
		lonmax=1300
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		REG_hist_lat=file_REG['lat'][latmin:latmax]
		REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
				
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')
		
		ax2= fig.add_subplot(4,3,2)	
		alpha=1.0

		ax2.set_facecolor('xkcd:light grey')	
		ax2.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax2.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax2.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax2.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax2.set_yscale('log')
		#ax.set_xscale('log')
		ax2.set_ylabel('proportions', fontsize=18)
		ax2.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax2.set_title('Norway', fontsize=24)
		ax2.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_NORWAY_daily.png', bbox_inches='tight', dpi=200) 
		
	if 'CARPAT' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in CARPAT temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_CARPAT_2000-2004.nc')

		maxbin=181
		
		latmin=200
		latmax=700
		lonmin=1200
		lonmax=1900
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
	
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')
		
		ax6= fig.add_subplot(4,3,6)
		alpha=1.0

		ax6.set_facecolor('xkcd:light grey')	
		ax6.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax6.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax6.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax6.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax6.set_yscale('log')
		#ax.set_xscale('log')
		ax6.set_ylabel('proportions', fontsize=18)
		ax6.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax6.set_title('Carpatians', fontsize=24)
		ax6.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_CARPAT_daily.png', bbox_inches='tight', dpi=200) 
	
	if 'EURO4M' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in EURO4M temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_EURO4M_2000-2004.nc')

		maxbin=181
		
		latmin=300
		latmax=500
		lonmin=800
		lonmax=1500
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
		
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=00	
		
		print('plotting')
		
		ax8= fig.add_subplot(4,3,8)
		alpha=1.0

		ax8.set_facecolor('xkcd:light grey')	
		ax8.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax8.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax8.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax8.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax8.set_yscale('log')
		#ax.set_xscale('log')
		ax8.set_ylabel('proportions', fontsize=18)
		ax8.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax8.set_title('Alps', fontsize=24)
		ax8.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_EURO4M_daily.png', bbox_inches='tight', dpi=200) 
	
	if 'SPA' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in SPAIN temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_SPAIN02_2000-2004.nc')

		maxbin=181
		
		latmin=100
		latmax=400
		lonmin=400
		lonmax=1000
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop

		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')

		ax10= fig.add_subplot(4,3,10)
		alpha=1.0

		ax10.set_facecolor('xkcd:light grey')	
		ax10.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax10.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax10.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax10.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax10.set_yscale('log')
		#ax.set_xscale('log')
		ax10.set_ylabel('proportions', fontsize=18)
		ax10.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax10.set_title('Spain', fontsize=24)
		ax10.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_SPAIN_daily.png', bbox_inches='tight', dpi=200) 

	if 'SWE' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in SWEDEN temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_SWEDEN_2000-2004.nc')

		maxbin=181
		
		latmin=700
		latmax=1000
		lonmin=1200
		lonmax=1700
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop
	
		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')

		ax3= fig.add_subplot(4,3,3)
		alpha=1.0

		ax3.set_facecolor('xkcd:light grey')	
		ax3.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax3.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax3.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax3.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax3.set_yscale('log')
		#ax.set_xscale('log')
		ax3.set_ylabel('proportions', fontsize=18)
		ax3.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax3.set_title('Sweden', fontsize=24)
		ax3.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_SWEDEN_daily.png', bbox_inches='tight', dpi=200) 

	if 'FRA' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in FRANCE temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_COMEPHORE_2000-2004.nc')

		maxbin=181
				
		latmin=200
		latmax=1000
		lonmin=400
		lonmax=1200
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop

		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')

		ax7= fig.add_subplot(4,3,7)
		alpha=1.0

		ax7.set_facecolor('xkcd:light grey')	
		ax7.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax7.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax7.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax7.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax7.set_yscale('log')
		#ax.set_xscale('log')
		ax7.set_ylabel('proportions', fontsize=18)
		ax7.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax7.set_title('France', fontsize=24)
		ax7.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_FRA_daily.png', bbox_inches='tight', dpi=200) 

	if 'SWI' in regions:
		##### CODE FOR SWI #####
		print(datetime.now(),'reading in Switzerland temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_RdisaggH_2003-2007.nc')

		maxbin=181
						
		latmin=300
		latmax=500
		lonmin=800
		lonmax=1200
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop

		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')
		
		ax9= fig.add_subplot(4,3,9)
		alpha=1.0

		ax9.set_facecolor('xkcd:light grey')	
		ax9.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='REGCM5')	
		ax9.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='REG 12k')
		ax9.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax9.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='COMEPHORE')
		plt.grid(color='w')
		#ax9.set_yscale('log')
		#ax.set_xscale('log')
		ax9.set_ylabel('proportions', fontsize=18)
		ax9.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax9.set_title('Switzerland', fontsize=24)
		ax9.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		#h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		#h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		#h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		#h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_SWI_daily.png', bbox_inches='tight', dpi=200) 

	if 'ITA' in regions:
		##### CODE FOR FRA #####
		print(datetime.now(),'reading in ITALY temp dataset')
		file_OBS_pr=Dataset('../data/regrid_daily_GRIPHO_2001-2005.nc')

		maxbin=181
								
		latmin=150
		latmax=550
		lonmin=1000
		lonmax=1600
		
		print(datetime.now(),'read file OBS')		
		hist=file_OBS_pr['pr_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		mask_index=np.where(hist[1,:,:]<=0)
		hist=file_OBS['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		hist[:,mask_index[0],mask_index[1]]=np.nan
		hist=np.nansum(np.nansum(hist, axis=2),axis=1)
			
		print(datetime.now(),'read file RegCM5 CP')
		REG_hist=file_REG['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG_hist=np.nansum(np.nansum(REG_hist, axis=2),axis=1)			
		
		print(datetime.now(),'read file RegCM 12km')
		REG12_hist=file_REG12['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]
		print('mask_out_value')
		REG12_hist[:,mask_index[0],mask_index[1]]=np.nan
		REG12_hist=np.nansum(np.nansum(REG12_hist, axis=2),axis=1)		
		
		print(datetime.now(),'read file ERA5')
		ERA5_hist=file_ERA5['temp_hist'][:maxbin,latmin:latmax,lonmin:lonmax]					
		print('mask_out_value')
		ERA5_hist[:,mask_index[0],mask_index[1]]=np.nan
		ERA5_hist=np.nansum(np.nansum(ERA5_hist, axis=2),axis=1)				
		
		#REG_hist_lat=file_REG['lat'][latmin:latmax]
		#REG_hist_lon=file_REG['lon'][lonmin:lonmax]
		
		#extent=[-12,40,35,70]
		#fig = plt.figure(figsize=(9,11))
		#ax0= fig.add_subplot(1,2,1, projection=ccrs.LambertConformal(central_longitude=9.75, central_latitude= 49.68))
		#ax0.set_extent(extent)
		#ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		#ax0.coastlines(resolution='50m', linewidth=1)

		#print('plotting Precip int diff map')
		#cmap = nclcmaps.cmap('MPL_BrBG')
		#cs=ax0.contourf(REG_hist_lon[:],REG_hist_lat[:],REG_hist[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap)
		#print(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss)
		#plt.show()
		#stop

		nbins=181
		bins=np.linspace(-40,50,nbins)
				
		amount_array=bins
		#amount_array[0]=0	
		
		print('plotting')
		
		ax11= fig.add_subplot(4,3,11)
		alpha=1.0

		ax11.set_facecolor('xkcd:light grey')	
		ax11.plot(amount_array[0:maxbin]-1.15, REG_hist[0:maxbin]/np.nansum(REG_hist), '-', c='orange', alpha=alpha, markeredgecolor='orange', label='RegCM5 CP')	
		ax11.plot(amount_array[0:maxbin]-1.15, REG12_hist[0:maxbin]/np.nansum(REG12_hist), '-', c='red', alpha=alpha, markeredgecolor='red', label='RegCM5 12km')
		ax11.plot(amount_array[0:maxbin]-1.15, ERA5_hist[0:maxbin]/np.nansum(ERA5_hist), '-', c='blue', alpha=alpha, markeredgecolor='blue', label='ERA5')
		ax11.plot(amount_array[1:maxbin], hist[1:maxbin]/np.nansum(hist[1:maxbin]), '-', c='black', alpha=alpha, markeredgecolor='black', label='Observations')
		plt.grid(color='w')
		#ax11.set_yscale('log')
		#ax.set_xscale('log')
		ax11.set_ylabel('proportions', fontsize=18)
		ax11.set_xlabel('daily temperature ($^\circ$C)', fontsize=18)
		ax11.set_title('Italy', fontsize=24)
		ax11.tick_params(labelsize=18)

		# Create dummy Line2D objects for legend
		h1 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='orange', linestyle='None')
		h2 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='red', linestyle='None')
		h3 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='blue', linestyle='None')
		h4 = Line2D([0], [0], marker='o', markersize=np.sqrt(20), color='black', linestyle='None')
		# Plot legend.
		#plt.legend([h1, h2, h3, h4], ['RegCM5 CP','RegCM5 12km','ERA5','OBS'], loc=1, markerscale=2, scatterpoints=1, fontsize=18, handletextpad=0.1)
				
		#plt.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_ITA_daily.png', bbox_inches='tight', dpi=200) 

		#figsize = (3, 3)
		#fig_leg = plt.figure(figsize=figsize)
		ax_leg = fig.add_subplot(4,3,12)
		# add the legend from the previous axes
		ax_leg.legend(*ax11.get_legend_handles_labels(), loc='center')
		# hide the axes frame and the x/y labels
		ax_leg.axis('off')
		#fig_leg.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/legend.png', bbox_inches='tight', dpi=200)
	
		ax2.annotate("a)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax3.annotate("b)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax4.annotate("c)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax5.annotate("d)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax6.annotate("e)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax7.annotate("f)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax8.annotate("g)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax9.annotate("h)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax10.annotate("i)", xy=(0.05, 0.05), xycoords="axes fraction")
		ax11.annotate("j)", xy=(0.05, 0.05), xycoords="axes fraction")
	
		ax0 = fig.add_subplot(4,3,1)
		ax0.axis('off')
		ax0.annotate("PDFs of daily temperature \nBin size: 0.5 $^\circ$C", xy=(0.2, 0.4), xycoords="axes fraction", fontsize=22)
		
	#fig.savefig('/marconi_work/ICT23_ESP/jdeleeuw/plots/hist/hist_ALL_daily_temp.jpeg', bbox_inches='tight', dpi=200) 
	fig.savefig('../plots/Fig_S8.jpeg', bbox_inches='tight', dpi=200) 
	
	
main()
