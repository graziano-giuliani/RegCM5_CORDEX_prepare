import math
import matplotlib.pyplot as plt
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
from matplotlib.lines import Line2D

def main():

	warnings.filterwarnings(action='ignore', message='Mean of empty slice')
	
	wdthres='01'
	season='JJA'
	
	#########READING IN THE daily cycle data
	
	path='../data/'
	
	UK_daily_mean_file=Dataset('../data/UK_total_'+season+'.nc')
	UK_daily_mean=UK_daily_mean_file['P_mean'][:]
	UK_daily_int=UK_daily_mean_file['P_int'][:]
	UK_daily_frq=UK_daily_mean_file['P_frq'][:]
	UK_daily_P99=UK_daily_mean_file['P99'][:]
	UK_daily_P999=UK_daily_mean_file['P999'][:]
	
	UK_pre=Dataset('../data/regrid_CEH-GEAR_hr1_MAM_thres_01.nc')
	UK_mask_file=UK_pre['pr_frq'][:,:]
	
	UK_lat=UK_pre['lat'][:]
	UK_lon=UK_pre['lon'][:]
	
	index_UK=np.where(UK_mask_file[:,:]>=0)
	UK_mask_single=np.zeros((np.shape(UK_mask_file[:,:])))
	UK_mask=np.zeros((24,np.shape(UK_mask_file[:,:])[0],np.shape(UK_mask_file[:,:])[1]))
	UK_mask_single[index_UK]=1
	for i in range(24):
		UK_mask[i,:,:]=UK_mask_single
	UK_mask[UK_mask==0]=np.nan
		
	FRA_daily_mean_file=Dataset(path+'pr_COMEPHORE_1hr_2000-2004_'+season+'_MeanDiurnalCycle.nc')
	FRA_daily_int_file=Dataset(path+'pr_COMEPHORE_1hr_2000-2004_'+season+'_INTDiurnalCycle.nc')
	FRA_daily_frq_file=Dataset(path+'pr_COMEPHORE_1hr_2000-2004_'+season+'_WetFreqDiurnalCycle.nc')
	FRA_daily_P99_file=Dataset(path+'pr_COMEPHORE_1hr_2000-2004_'+season+'_pctl99DiurnalCycle.nc')
	FRA_daily_P999_file=Dataset(path+'pr_COMEPHORE_1hr_2000-2004_'+season+'_pctl999DiurnalCycle.nc')
	
	FRA_daily_mean=FRA_daily_mean_file['pr'][:,:,:]
	FRA_daily_int=FRA_daily_int_file['pr'][:,0,:,:]
	FRA_daily_frq=FRA_daily_frq_file['pr'][:,0,:,:]
	FRA_daily_P99=FRA_daily_P99_file['pr'][:,:,:]
	FRA_daily_P999=FRA_daily_P999_file['pr'][:,:,:]

	index_FRA=np.where(FRA_daily_mean[:,:,:]>=0)
	FRA_mask=np.zeros((np.shape(FRA_daily_mean[:,:,:])))
	FRA_mask[index_FRA]=1
	FRA_mask[FRA_mask==0]=np.nan
	
	GER_daily_mean_file=Dataset(path+'pr_RADKLIM_1hr_2001-2005_'+season+'_MeanDiurnalCycle.nc')
	GER_daily_int_file=Dataset(path+'pr_RADKLIM_1hr_2001-2005_'+season+'_INTDiurnalCycle.nc')
	GER_daily_frq_file=Dataset(path+'pr_RADKLIM_1hr_2001-2005_'+season+'_WetFreqDiurnalCycle.nc')
	GER_daily_P99_file=Dataset(path+'pr_RADKLIM_1hr_2001-2005_'+season+'_pctl99DiurnalCycle.nc')
	GER_daily_P999_file=Dataset(path+'pr_RADKLIM_1hr_2001-2005_'+season+'_pctl999DiurnalCycle.nc')
	
	GER_daily_mean=GER_daily_mean_file['pr'][:,:,:]
	GER_daily_int=GER_daily_int_file['pr'][:,0,:,:]
	GER_daily_frq=GER_daily_frq_file['pr'][:,0,:,:]
	GER_daily_P99=GER_daily_P99_file['pr'][:,:,:]
	GER_daily_P999=GER_daily_P999_file['pr'][:,:,:]

	index_GER=np.where(GER_daily_mean[:,:,:]>10)
	GER_mask=np.ones((np.shape(GER_daily_mean[:,:,:])))
	GER_mask[index_GER]=0
	GER_mask[GER_mask==0]=np.nan
	
	SWI_daily_mean_file=Dataset(path+'pr_RdisaggH_1hr_2003-2007_'+season+'_MeanDiurnalCycle.nc')
	SWI_daily_int_file=Dataset(path+'pr_RdisaggH_1hr_2003-2007_'+season+'_INTDiurnalCycle.nc')
	SWI_daily_frq_file=Dataset(path+'pr_RdisaggH_1hr_2003-2007_'+season+'_WetFreqDiurnalCycle.nc')
	SWI_daily_P99_file=Dataset(path+'pr_RdisaggH_1hr_2003-2007_'+season+'_pctl99DiurnalCycle.nc')
	SWI_daily_P999_file=Dataset(path+'pr_RdisaggH_1hr_2003-2007_'+season+'_pctl999DiurnalCycle.nc')
	
	SWI_daily_mean=SWI_daily_mean_file['pr'][:,:,:]
	SWI_daily_int=SWI_daily_int_file['pr'][:,0,:,:]
	SWI_daily_frq=SWI_daily_frq_file['pr'][:,0,:,:]
	SWI_daily_P99=SWI_daily_P99_file['pr'][:,:,:]
	SWI_daily_P999=SWI_daily_P999_file['pr'][:,:,:]

	index_SWI=np.where(SWI_daily_mean[:,:,:]>=0)
	SWI_mask=np.zeros((np.shape(SWI_daily_mean[:,:,:])))
	SWI_mask[index_SWI]=1
	SWI_mask[SWI_mask==0]=np.nan

	ITA_daily_mean_file=Dataset(path+'pr_GRIPHO_1hr_2001-2005_'+season+'_MeanDiurnalCycle.nc')
	ITA_daily_int_file=Dataset(path+'pr_GRIPHO_1hr_2001-2005_'+season+'_INTDiurnalCycle.nc')
	ITA_daily_frq_file=Dataset(path+'pr_GRIPHO_1hr_2001-2005_'+season+'_WetFreqDiurnalCycle.nc')
	ITA_daily_P99_file=Dataset(path+'pr_GRIPHO_1hr_2001-2005_'+season+'_pctl99DiurnalCycle.nc')
	ITA_daily_P999_file=Dataset(path+'pr_GRIPHO_1hr_2001-2005_'+season+'_pctl999DiurnalCycle.nc')
	
	ITA_daily_mean=ITA_daily_mean_file['pr'][:,:,:]
	ITA_daily_int=ITA_daily_int_file['pr'][:,0,:,:]
	ITA_daily_frq=ITA_daily_frq_file['pr'][:,0,:,:]
	ITA_daily_P99=ITA_daily_P99_file['pr'][:,:,:]
	ITA_daily_P999=ITA_daily_P999_file['pr'][:,:,:]

	index_ITA=np.where(ITA_daily_mean[:,:,:]>=0)
	ITA_mask=np.zeros((np.shape(ITA_daily_mean[:,:,:])))
	ITA_mask[index_ITA]=1
	ITA_mask[ITA_mask==0]=np.nan
	
	REGCM5_daily_mean_file=Dataset(path+'pr_WP3_yellowS_3km_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_MeanDiurnalCycle.nc')
	REGCM5_daily_int_file=Dataset(path+'pr_WP3_yellowS_3km_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_INTDiurnalCycle.nc')
	REGCM5_daily_frq_file=Dataset(path+'pr_WP3_yellowS_3km_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_WetFreqDiurnalCycle.nc')
	REGCM5_daily_P99_file=Dataset(path+'pr_WP3_yellowS_3km_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_pctl99DiurnalCycle.nc')
	REGCM5_daily_P999_file=Dataset(path+'pr_WP3_yellowS_3km_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_pctl999DiurnalCycle.nc')
	
	REGCM5_daily_mean=REGCM5_daily_mean_file['pr'][:,:,:]
	REGCM5_daily_int=REGCM5_daily_int_file['pr'][:,0,:,:]
	REGCM5_daily_frq=REGCM5_daily_frq_file['pr'][:,0,:,:]
	REGCM5_daily_P99=REGCM5_daily_P99_file['pr'][:,:,:]
	REGCM5_daily_P999=REGCM5_daily_P999_file['pr'][:,:,:]	
	
	REGCM512_daily_mean_file=Dataset(path+'pr_EUR-11_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_MeanDiurnalCycle.nc')
	REGCM512_daily_int_file=Dataset(path+'pr_EUR-11_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_INTDiurnalCycle.nc')
	REGCM512_daily_frq_file=Dataset(path+'pr_EUR-11_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_WetFreqDiurnalCycle.nc')
	REGCM512_daily_P99_file=Dataset(path+'pr_EUR-11_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_pctl99DiurnalCycle.nc')
	REGCM512_daily_P999_file=Dataset(path+'pr_EUR-11_evaluation_ICTP-RegCM5_1hr_2000-2004_'+season+'_pctl999DiurnalCycle.nc')

	REGCM512_daily_mean=REGCM512_daily_mean_file['pr'][:,:,:]
	REGCM512_daily_int=REGCM512_daily_int_file['pr'][:,0,:,:]
	REGCM512_daily_frq=REGCM512_daily_frq_file['pr'][:,0,:,:]
	REGCM512_daily_P99=REGCM512_daily_P99_file['pr'][:,:,:]
	REGCM512_daily_P999=REGCM512_daily_P999_file['pr'][:,:,:]	
	
	ERA5_daily_mean_file=Dataset(path+'pr_evaluation_ERA5_1hr_2000-2004_'+season+'_MeanDiurnalCycle.nc')
	ERA5_daily_int_file=Dataset(path+'pr_evaluation_ERA5_1hr_2000-2004_'+season+'_INTDiurnalCycle.nc')
	ERA5_daily_frq_file=Dataset(path+'pr_evaluation_ERA5_1hr_2000-2004_'+season+'_WetFreqDiurnalCycle.nc')
	ERA5_daily_P99_file=Dataset(path+'pr_evaluation_ERA5_1hr_2000-2004_'+season+'_pctl99DiurnalCycle.nc')
	ERA5_daily_P999_file=Dataset(path+'pr_evaluation_ERA5_1hr_2000-2004_'+season+'_pctl999DiurnalCycle.nc')	
	
	ERA5_daily_mean=ERA5_daily_mean_file['tp'][:,:,:]
	ERA5_daily_int=ERA5_daily_int_file['tp'][:,0,:,:]
	ERA5_daily_frq=ERA5_daily_frq_file['tp'][:,0,:,:]
	ERA5_daily_P99=ERA5_daily_P99_file['tp'][:,:,:]
	ERA5_daily_P999=ERA5_daily_P999_file['tp'][:,:,:]
	
	time=range(25)
	time=time[1:]
	
	fig = plt.figure(figsize=(15,10))
	matplotlib.rcParams.update({'font.size': 12})
	ax0= fig.add_subplot(5,5,1)
	ax0.set_facecolor('xkcd:light grey')
	ax0.plot(time, UK_daily_mean, color='k', label='OBS')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM5_daily_mean*UK_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM512_daily_mean*UK_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax0.plot(time, np.nanmean(np.nanmean(ERA5_daily_mean*UK_mask, axis=1),axis=1), color='b', label='ERA5')
	ax0.xaxis.set_ticks(np.arange(0, 25, 6))
	ax0.yaxis.set_ticks(np.arange(0, 0.21, 0.05))
	ax0.xaxis.set_ticklabels([])
	
	plt.grid(color='w')
	#ax0.set_ylabel('mm/hr', fontsize=12)
	#ax0.set_xlabel('Time [hr]', fontsize=12)
	ax0.set_title('Mean \n Precipitation (mm/hr)')
	ax0.annotate("Great Britain", xy=(-0.5, 0.05), xycoords="axes fraction", size='large', rotation=90)
	
	ax1= fig.add_subplot(5,5,2)
	ax1.set_facecolor('xkcd:light grey')
	ax1.plot(time, UK_daily_int, color='k', label='OBS')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM5_daily_int*UK_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM512_daily_int*UK_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax1.plot(time, np.nanmean(np.nanmean(ERA5_daily_int*UK_mask, axis=1),axis=1), color='b', label='ERA5')
	plt.grid(color='w')
	#ax1.set_ylabel('mm/hr', fontsize=12)
	#ax1.set_xlabel('Time [hr]', fontsize=12)
	ax1.set_title('Precipitation \n intensity (mm/hr)')
	ax1.xaxis.set_ticks(np.arange(0, 25, 6))
	ax1.yaxis.set_ticks(np.arange(0, 2.1, 0.5))
	ax1.xaxis.set_ticklabels([])
	
	ax2= fig.add_subplot(5,5,3)
	ax2.set_facecolor('xkcd:light grey')
	ax2.plot(time, UK_daily_frq, color='k', label='OBS')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM5_daily_frq*UK_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM512_daily_frq*UK_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax2.plot(time, np.nanmean(np.nanmean(ERA5_daily_frq*UK_mask, axis=1),axis=1), color='b', label='ERA5')
	plt.grid(color='w')
	#ax2.set_ylabel('fraction', fontsize=12)
	#ax2.set_xlabel('Time [hr]', fontsize=12)
	ax2.set_title('Precipitation frequency')
	ax2.xaxis.set_ticks(np.arange(0, 25, 6))
	ax2.yaxis.set_ticks(np.arange(0, 0.31, 0.1))
	ax2.xaxis.set_ticklabels([])
	ax2.annotate("Diurnal cycles MAM", xy=(0.1, 1.5), xycoords="axes fraction", size='x-large')
	
	ax3= fig.add_subplot(5,5,4)
	ax3.set_facecolor('xkcd:light grey')
	ax3.plot(time, UK_daily_P99, color='k', label='OBS')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P99*UK_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P99*UK_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax3.plot(time, np.nanmean(np.nanmean(ERA5_daily_P99*UK_mask, axis=1),axis=1), color='b', label='ERA5')
	plt.grid(color='w')
	#ax3.set_ylabel('mm/hr', fontsize=12)
	#ax3.set_xlabel('Time [hr]', fontsize=12)
	ax3.set_title('P99 (mm/hr)')
	ax3.xaxis.set_ticks(np.arange(0, 25, 6))
	ax3.yaxis.set_ticks(np.arange(0, 5.1, 1))
	ax3.xaxis.set_ticklabels([])
	
	ax4= fig.add_subplot(5,5,5)
	ax4.set_facecolor('xkcd:light grey')
	ax4.plot(time, UK_daily_P999, color='k', label='OBS')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P999*UK_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P999*UK_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax4.plot(time, np.nanmean(np.nanmean(ERA5_daily_P999*UK_mask, axis=1),axis=1), color='b', label='ERA5')
	#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=2, scatterpoints=1, fontsize=12, handletextpad=0.5)
	plt.grid(color='w')
	#ax4.set_ylabel('mm/hr', fontsize=12)
	#ax4.set_xlabel('Time [hr]', fontsize=12)
	ax4.set_title('P99.9 (mm/hr)')
	ax4.xaxis.set_ticks(np.arange(0, 25, 6))
	ax4.yaxis.set_ticks(np.arange(0, 16, 5))
	ax4.xaxis.set_ticklabels([])
	
	####### FRA
	
	ax0= fig.add_subplot(5,5,6)
	ax0.set_facecolor('xkcd:light grey')
	ax0.plot(time, np.nanmean(np.nanmean(FRA_daily_mean*FRA_mask, axis=1),axis=1), color='k', label='OBS')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM5_daily_mean*FRA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM512_daily_mean*FRA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax0.plot(time, np.nanmean(np.nanmean(ERA5_daily_mean*FRA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax0.xaxis.set_ticks(np.arange(0, 25, 6))
	ax0.yaxis.set_ticks(np.arange(0, 0.2, 0.05))
	ax0.xaxis.set_ticklabels([])
	
	plt.grid(color='w')
	#ax0.set_ylabel('mm/hr', fontsize=12)
	#ax0.set_xlabel('Time [hr]', fontsize=12)
	ax0.annotate("France", xy=(-0.5, 0.3), xycoords="axes fraction", size='large', rotation=90)
	
	ax1= fig.add_subplot(5,5,7)
	ax1.set_facecolor('xkcd:light grey')
	ax1.plot(time, np.nanmean(np.nanmean(FRA_daily_int*FRA_mask, axis=1),axis=1), color='k', label='OBS')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM5_daily_int*FRA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM512_daily_int*FRA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax1.plot(time, np.nanmean(np.nanmean(ERA5_daily_int*FRA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax1.xaxis.set_ticks(np.arange(0, 25, 6))
	ax1.yaxis.set_ticks(np.arange(0, 2.1, 0.5))
	ax1.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax1.set_ylabel('mm/hr', fontsize=12)
	
	ax2= fig.add_subplot(5,5,8)
	ax2.set_facecolor('xkcd:light grey')
	ax2.plot(time, np.nanmean(np.nanmean(FRA_daily_frq*FRA_mask, axis=1),axis=1), color='k', label='OBS')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM5_daily_frq*FRA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM512_daily_frq*FRA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax2.plot(time, np.nanmean(np.nanmean(ERA5_daily_frq*FRA_mask, axis=1),axis=1), color='b', label='ERA5')
	plt.grid(color='w')
	ax2.xaxis.set_ticks(np.arange(0, 25, 6))
	ax2.yaxis.set_ticks(np.arange(0, 0.31, 0.1))
	ax2.xaxis.set_ticklabels([])
	#ax2.set_ylabel('fraction', fontsize=12)
	#ax2.set_xlabel('Time [hr]', fontsize=12)
	
	ax3= fig.add_subplot(5,5,9)
	ax3.set_facecolor('xkcd:light grey')
	ax3.plot(time, np.nanmean(np.nanmean(FRA_daily_P99*FRA_mask, axis=1),axis=1), color='k', label='OBS')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P99*FRA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P99*FRA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax3.plot(time, np.nanmean(np.nanmean(ERA5_daily_P99*FRA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax3.xaxis.set_ticks(np.arange(0, 25, 6))
	ax3.yaxis.set_ticks(np.arange(0, 5.1, 1))
	ax3.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax3.set_ylabel('mm/hr', fontsize=12)
	#ax3.set_xlabel('Time [hr]', fontsize=12)
	
	ax4= fig.add_subplot(5,5,10)
	ax4.set_facecolor('xkcd:light grey')
	ax4.plot(time, np.nanmean(np.nanmean(FRA_daily_P999*FRA_mask, axis=1),axis=1), color='k', label='OBS')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P999*FRA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P999*FRA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax4.plot(time, np.nanmean(np.nanmean(ERA5_daily_P999*FRA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax4.xaxis.set_ticks(np.arange(0, 25, 6))
	ax4.yaxis.set_ticks(np.arange(0, 16, 5))
	ax4.xaxis.set_ticklabels([])
	#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=2, scatterpoints=1, fontsize=12, handletextpad=0.5)
	plt.grid(color='w')
	#ax4.set_ylabel('mm/hr', fontsize=12)
	
	####### GER
	
	ax0= fig.add_subplot(5,5,11)
	ax0.set_facecolor('xkcd:light grey')
	ax0.plot(time, np.nanmean(np.nanmean(GER_daily_mean*GER_mask, axis=1),axis=1), color='k', label='OBS')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM5_daily_mean*GER_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM512_daily_mean*GER_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax0.plot(time, np.nanmean(np.nanmean(ERA5_daily_mean*GER_mask, axis=1),axis=1), color='b', label='ERA5')
	ax0.xaxis.set_ticks(np.arange(0, 25, 6))
	ax0.yaxis.set_ticks(np.arange(0, 0.16, 0.05))
	ax0.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax0.set_ylabel('mm/hr', fontsize=12)
	#ax0.set_xlabel('Time [hr]', fontsize=12)
	ax0.annotate("Germany", xy=(-0.5, 0.15), xycoords="axes fraction", size='large', rotation=90)
	
	ax1= fig.add_subplot(5,5,12)
	ax1.set_facecolor('xkcd:light grey')
	ax1.plot(time, np.nanmean(np.nanmean(GER_daily_int*GER_mask, axis=1),axis=1), color='k', label='OBS')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM5_daily_int*GER_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM512_daily_int*GER_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax1.plot(time, np.nanmean(np.nanmean(ERA5_daily_int*GER_mask, axis=1),axis=1), color='b', label='ERA5')
	ax1.xaxis.set_ticks(np.arange(0, 25, 6))
	ax1.yaxis.set_ticks(np.arange(0, 2.1, 0.5))
	ax1.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax1.set_ylabel('mm/hr', fontsize=12)
	
	ax2= fig.add_subplot(5,5,13)
	ax2.set_facecolor('xkcd:light grey')
	ax2.plot(time, np.nanmean(np.nanmean(GER_daily_frq*GER_mask, axis=1),axis=1), color='k', label='OBS')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM5_daily_frq*GER_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM512_daily_frq*GER_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax2.plot(time, np.nanmean(np.nanmean(ERA5_daily_frq*GER_mask, axis=1),axis=1), color='b', label='ERA5')
	ax2.xaxis.set_ticks(np.arange(0, 25, 6))
	ax2.yaxis.set_ticks(np.arange(0, 0.31, 0.1))
	ax2.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax2.set_ylabel('fraction', fontsize=12)
	#ax2.set_xlabel('Time [hr]', fontsize=12)
	
	ax3= fig.add_subplot(5,5,14)
	ax3.set_facecolor('xkcd:light grey')
	ax3.plot(time, np.nanmean(np.nanmean(GER_daily_P99*GER_mask, axis=1),axis=1), color='k', label='OBS')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P99*GER_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P99*GER_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax3.plot(time, np.nanmean(np.nanmean(ERA5_daily_P99*GER_mask, axis=1),axis=1), color='b', label='ERA5')
	ax3.xaxis.set_ticks(np.arange(0, 25, 6))
	ax3.yaxis.set_ticks(np.arange(0, 5.1, 1))
	ax3.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax3.set_ylabel('mm/hr', fontsize=12)
	#ax3.set_xlabel('Time [hr]', fontsize=12)
	
	ax4= fig.add_subplot(5,5,15)
	ax4.set_facecolor('xkcd:light grey')
	ax4.plot(time, np.nanmean(np.nanmean(GER_daily_P999*GER_mask, axis=1),axis=1), color='k', label='OBS')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P999*GER_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P999*GER_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax4.plot(time, np.nanmean(np.nanmean(ERA5_daily_P999*GER_mask, axis=1),axis=1), color='b', label='ERA5')
	ax4.xaxis.set_ticks(np.arange(0, 25, 6))
	ax4.yaxis.set_ticks(np.arange(0, 16, 5))
	ax4.xaxis.set_ticklabels([])
	plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=2, scatterpoints=1, fontsize=12, handletextpad=0.5)
	plt.grid(color='w')
	#ax4.set_ylabel('mm/hr', fontsize=12)
	
	####### SWI
	
	ax0= fig.add_subplot(5,5,16)
	ax0.set_facecolor('xkcd:light grey')
	ax0.plot(time, np.nanmean(np.nanmean(SWI_daily_mean*SWI_mask, axis=1),axis=1), color='k', label='OBS')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM5_daily_mean*SWI_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM512_daily_mean*SWI_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax0.plot(time, np.nanmean(np.nanmean(ERA5_daily_mean*SWI_mask, axis=1),axis=1), color='b', label='ERA5')
	ax0.xaxis.set_ticks(np.arange(0, 25, 6))
	ax0.yaxis.set_ticks(np.arange(0, 0.46, 0.1))
	ax0.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax0.set_ylabel('mm/hr', fontsize=12)
	#ax0.set_xlabel('Time [hr]', fontsize=12)
	ax0.annotate("Switzerland", xy=(-0.5, 0.1), xycoords="axes fraction", size='large', rotation=90)
	
	ax1= fig.add_subplot(5,5,17)
	ax1.set_facecolor('xkcd:light grey')
	ax1.plot(time, np.nanmean(np.nanmean(SWI_daily_int*SWI_mask, axis=1),axis=1), color='k', label='OBS')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM5_daily_int*SWI_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM512_daily_int*SWI_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax1.plot(time, np.nanmean(np.nanmean(ERA5_daily_int*SWI_mask, axis=1),axis=1), color='b', label='ERA5')
	ax1.xaxis.set_ticks(np.arange(0, 25, 6))
	ax1.yaxis.set_ticks(np.arange(0, 2.1, 0.5))
	ax1.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax1.set_ylabel('mm/hr', fontsize=12)
	
	ax2= fig.add_subplot(5,5,18)
	ax2.set_facecolor('xkcd:light grey')
	ax2.plot(time, np.nanmean(np.nanmean(SWI_daily_frq*SWI_mask, axis=1),axis=1), color='k', label='OBS')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM5_daily_frq*SWI_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM512_daily_frq*SWI_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax2.plot(time, np.nanmean(np.nanmean(ERA5_daily_frq*SWI_mask, axis=1),axis=1), color='b', label='ERA5')
	ax2.xaxis.set_ticks(np.arange(0, 25, 6))
	ax2.yaxis.set_ticks(np.arange(0, 0.41, 0.1))
	ax2.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax2.set_ylabel('fraction', fontsize=12)
	#ax2.set_xlabel('Time [hr]', fontsize=12)
	
	ax3= fig.add_subplot(5,5,19)
	ax3.set_facecolor('xkcd:light grey')
	ax3.plot(time, np.nanmean(np.nanmean(SWI_daily_P99*SWI_mask, axis=1),axis=1), color='k', label='OBS')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P99*SWI_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P99*SWI_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax3.plot(time, np.nanmean(np.nanmean(ERA5_daily_P99*SWI_mask, axis=1),axis=1), color='b', label='ERA5')
	ax3.xaxis.set_ticks(np.arange(0, 25, 6))
	ax3.yaxis.set_ticks(np.arange(0, 6.1, 1))
	ax3.xaxis.set_ticklabels([])
	plt.grid(color='w')
	#ax3.set_ylabel('mm/hr', fontsize=12)
	#ax3.set_xlabel('Time [hr]', fontsize=12)
	
	ax4= fig.add_subplot(5,5,20)
	ax4.set_facecolor('xkcd:light grey')
	ax4.plot(time, np.nanmean(np.nanmean(SWI_daily_P999*SWI_mask, axis=1),axis=1), color='k', label='OBS')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P999*SWI_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P999*SWI_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax4.plot(time, np.nanmean(np.nanmean(ERA5_daily_P999*SWI_mask, axis=1),axis=1), color='b', label='ERA5')
	ax4.xaxis.set_ticks(np.arange(0, 25, 6))
	ax4.yaxis.set_ticks(np.arange(0, 16, 5))
	ax4.xaxis.set_ticklabels([])
	#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=2, scatterpoints=1, fontsize=12, handletextpad=0.5)
	plt.grid(color='w')
	#ax4.set_ylabel('mm/hr', fontsize=12)		
	
	####### ITA
	
	ax0= fig.add_subplot(5,5,21)
	ax0.set_facecolor('xkcd:light grey')
	ax0.plot(time, np.nanmean(np.nanmean(ITA_daily_mean*ITA_mask, axis=1),axis=1), color='k', label='OBS')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM5_daily_mean*ITA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax0.plot(time, np.nanmean(np.nanmean(REGCM512_daily_mean*ITA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax0.plot(time, np.nanmean(np.nanmean(ERA5_daily_mean*ITA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax0.xaxis.set_ticks(np.arange(0, 25, 6))
	ax0.yaxis.set_ticks(np.arange(0, 0.26, 0.05))
	plt.grid(color='w')
	#ax0.set_ylabel('mm/hr', fontsize=12)
	ax0.set_xlabel('Time [hr]', fontsize=12)
	ax0.annotate("Italy", xy=(-0.5, 0.4), xycoords="axes fraction", size='large', rotation=90)
	
	ax1= fig.add_subplot(5,5,22)
	ax1.set_facecolor('xkcd:light grey')
	ax1.plot(time, np.nanmean(np.nanmean(ITA_daily_int*ITA_mask, axis=1),axis=1), color='k', label='OBS')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM5_daily_int*ITA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax1.plot(time, np.nanmean(np.nanmean(REGCM512_daily_int*ITA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax1.plot(time, np.nanmean(np.nanmean(ERA5_daily_int*ITA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax1.xaxis.set_ticks(np.arange(0, 25, 6))
	ax1.yaxis.set_ticks(np.arange(0, 2.1, 0.5))
	plt.grid(color='w')
	ax1.set_xlabel('Time [hr]', fontsize=12)
	#ax1.set_ylabel('mm/hr', fontsize=12)
	
	ax2= fig.add_subplot(5,5,23)
	ax2.set_facecolor('xkcd:light grey')
	ax2.plot(time, np.nanmean(np.nanmean(ITA_daily_frq*ITA_mask, axis=1),axis=1), color='k', label='OBS')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM5_daily_frq*ITA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax2.plot(time, np.nanmean(np.nanmean(REGCM512_daily_frq*ITA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax2.plot(time, np.nanmean(np.nanmean(ERA5_daily_frq*ITA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax2.xaxis.set_ticks(np.arange(0, 25, 6))
	ax2.yaxis.set_ticks(np.arange(0, 0.31, 0.1))
	plt.grid(color='w')
	#ax2.set_ylabel('fraction', fontsize=12)
	ax2.set_xlabel('Time [hr]', fontsize=12)
	
	ax3= fig.add_subplot(5,5,24)
	ax3.set_facecolor('xkcd:light grey')
	ax3.plot(time, np.nanmean(np.nanmean(ITA_daily_P99*ITA_mask, axis=1),axis=1), color='k', label='OBS')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P99*ITA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax3.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P99*ITA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax3.plot(time, np.nanmean(np.nanmean(ERA5_daily_P99*ITA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax3.xaxis.set_ticks(np.arange(0, 25, 6))
	ax3.yaxis.set_ticks(np.arange(0, 5.1, 1))
	plt.grid(color='w')
	#ax3.set_ylabel('mm/hr', fontsize=12)
	ax3.set_xlabel('Time [hr]', fontsize=12)
	
	ax4= fig.add_subplot(5,5,25)
	ax4.set_facecolor('xkcd:light grey')
	ax4.plot(time, np.nanmean(np.nanmean(ITA_daily_P999*ITA_mask, axis=1),axis=1), color='k', label='OBS')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM5_daily_P999*ITA_mask, axis=1),axis=1),color='orange', label='RegCM5 CP')
	ax4.plot(time, np.nanmean(np.nanmean(REGCM512_daily_P999*ITA_mask, axis=1),axis=1), color='red', label='RegCM5 12km')
	ax4.plot(time, np.nanmean(np.nanmean(ERA5_daily_P999*ITA_mask, axis=1),axis=1), color='b', label='ERA5')
	ax4.xaxis.set_ticks(np.arange(0, 25, 6))
	ax4.yaxis.set_ticks(np.arange(0, 16, 5))
	#plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), markerscale=2, scatterpoints=1, fontsize=12, handletextpad=0.5)
	plt.grid(color='w')
	ax4.set_xlabel('Time [hr]', fontsize=12)
	#ax4.set_ylabel('mm/hr', fontsize=12)	
	
	if season=='JJA':
		plt.savefig('../plots/Fig12.jpeg', bbox_inches='tight', dpi=200) 
	if season!='JJA':
		plt.savefig('../plots/FigS10_'+season+'.jpeg', bbox_inches='tight', dpi=200) 
	
main()
