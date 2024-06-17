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

def main():

	warnings.filterwarnings(action='ignore', message='Mean of empty slice')
	
	#season=str(sys.argv[1])
	
	seasons=['DJF','MAM','JJA','SON']
	
	index_season=0

	wdthres='01'
	
	coastline_width=0.5
	
	#'ITA','GER','FRA','SWI',

	regions=['UK','ITA','GER','FRA','SWI','REGCM5_12km']		# change REGCM5 into REGCM_12km is you want to plot obs vs EUR-11 simulation

	file_OBS_ITA=Dataset('../data/regrid_GRIPHO_hr1_'+'JJA'+'_thres_'+wdthres+'.nc')
	OBS_lat_ITA=np.array(file_OBS_ITA['pr_int'][:])
	diff_arr_ITA_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_GER_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_FRA_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_SWI_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_UK_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	
	diff_arr_ITA_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_GER_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_FRA_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_SWI_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))
	diff_arr_UK_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))	
	
	diff_arr_TOT_int=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))	
	diff_arr_TOT_frq=np.zeros((4,np.shape(OBS_lat_ITA)[0],np.shape(OBS_lat_ITA)[1]))	
	
	for season in seasons:
		print('reading in: ',  season)

		# Managing the data for each individual location:

		#### CODE FOR ITALY ####

		if 'ITA' in regions:
			print(datetime.now(),'reading in ITA precip dataset')
			#hourly data ITA (available 2001/01/01 up to 2004/04/30)
			file_OBS_ITA=Dataset('../data/regrid_GRIPHO_hr1_'+season+'_thres_'+wdthres+'.nc')
			OBS_lat_ITA=np.array(file_OBS_ITA['lat'][:])
			OBS_lon_ITA=np.array(file_OBS_ITA['lon'][:])
			OBS_pr_int_ITA=np.array(file_OBS_ITA['pr_int'][:,:])
			OBS_pr_frq_ITA=np.array(file_OBS_ITA['pr_frq'][:,:])
			ITA_mask=np.where(np.array(OBS_pr_int_ITA[:,:])<=0,0,1)
			ITA_mask2=np.where(np.array(OBS_pr_int_ITA[:,:])>1000,0,1)

		if 'GER' in regions:
			##### CODE FOR GERMANY #####
			print(datetime.now(),'reading in GER precip dataset')
			#hourly data GER (available 2001/01/01 up to 2004/04/30)
			file_OBS_GER=Dataset('../data/regrid_RADKLIM_hr1_'+season+'_thres_'+wdthres+'.nc')
			OBS_lat_GER=np.array(file_OBS_GER['lat'][:])
			OBS_lon_GER=np.array(file_OBS_GER['lon'][:])
			OBS_pr_int_GER=np.array(file_OBS_GER['pr_int'][:,:])
			OBS_pr_frq_GER=np.array(file_OBS_GER['pr_frq'][:,:])
			GER_mask=np.where(np.array(OBS_pr_int_GER[:,:])<=0,0,1)
			GER_mask2=np.where(np.array(OBS_pr_int_ITA[:,:])>1000,0,1)

		if 'FRA' in regions:
			##### CODE FOR FRANCE #####
			print(datetime.now(),'reading in FRA precip dataset')
			#hourly data FRA
			file_OBS_FRA=Dataset('../data/regrid_COMEPHORE_hr1_'+season+'_thres_'+wdthres+'.nc')
			OBS_lat_FRA=np.array(file_OBS_FRA['lat'][:])
			OBS_lon_FRA=np.array(file_OBS_FRA['lon'][:])
			OBS_pr_int_FRA=np.array(file_OBS_FRA['pr_int'][:,:])
			OBS_pr_frq_FRA=np.array(file_OBS_FRA['pr_frq'][:,:])
			FRA_mask=np.where(np.array(OBS_pr_int_FRA[:,:])<=0,0,1)
			FRA_mask2=np.where(np.array(OBS_pr_int_ITA[:,:])>1000,0,1)

		if 'SWI' in regions:
			##### CODE FOR SWITZERLAND #####
			print(datetime.now(),'reading in SWI precip dataset')
			#file_OBS_SWI=Dataset('/marconi_work/ICT23_ESP/jciarlo0/obs/eur-hires/pr_RdisaggH_1hr_2003-2010.nc')
			file_OBS_SWI=Dataset('../data/regrid_RdisaggH_hr1_'+season+'_thres_'+wdthres+'.nc')
			OBS_lat_SWI=np.array(file_OBS_SWI['lat'][:])
			OBS_lon_SWI=np.array(file_OBS_SWI['lon'][:])
			OBS_pr_int_SWI=np.array(file_OBS_SWI['pr_int'][:,:])
			OBS_pr_frq_SWI=np.array(file_OBS_SWI['pr_frq'][:,:])
			SWI_mask=np.where(np.array(OBS_pr_int_SWI[:,:])<=0,0,1)
			SWI_mask2=np.where(np.array(OBS_pr_int_ITA[:,:])>1000,0,1)

		if 'UK' in regions:
			##### CODE FOR SWITZERLAND #####
			print(datetime.now(),'reading in UK precip dataset')
			file_OBS_UK=Dataset('../data/regrid_CEH-GEAR_hr1_'+season+'_thres_'+wdthres+'.nc')
			OBS_lat_UK=np.array(file_OBS_UK['lat'][:])
			OBS_lon_UK=np.array(file_OBS_UK['lon'][:])
			OBS_pr_int_UK=np.array(file_OBS_UK['pr_int'][:,:])
			OBS_pr_frq_UK=np.array(file_OBS_UK['pr_frq'][:,:])
			UK_mask=np.where(np.array(OBS_pr_int_UK[:,:])<=0,0,1)
			UK_mask2=np.where(np.array(OBS_pr_int_ITA[:,:])>1000,0,1)
			
		if 'REGCM5' in regions:
			##### CODE FOR REGCM5 #####
			print(datetime.now(),'reading in REGCM5 precip dataset')
			file_REGCM5=Dataset('../data/regrid_hourly_REGCM5_CP_'+season+'_2000-2004_pr_thres_'+wdthres+'.nc')
			OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
			OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])						
			OBS_pr_int_REGCM5=np.array(file_REGCM5['pr_int'][:,:])
			OBS_pr_frq_REGCM5=np.array(file_REGCM5['pr_frq'][:,:])
			OBS_pr_int_REGCM5[np.abs(OBS_pr_int_REGCM5) > 10**4]=np.nan

		total_mask=ITA_mask+GER_mask+FRA_mask+UK_mask+SWI_mask+ITA_mask2+GER_mask2+FRA_mask2+UK_mask2+SWI_mask2
		non_data_mask=np.ones((np.shape(OBS_pr_int_ITA)[0],np.shape(OBS_pr_int_ITA)[1]))
		total_mask=np.array(total_mask)

		total_mask[np.where(total_mask>0)]=1
		#total_mask[np.where(total_mask==0)]=np.nan

		index=np.where(total_mask!=1)
		non_data_mask[index]=999
		#non_data_mask=non_data_mask*landmask
		non_data_mask[non_data_mask!=999]=np.nan
				
		if 'REGCM5_12km' in regions:
			##### CODE FOR REGCM5 #####
			print(datetime.now(),'reading in REGCM5 12km precip dataset')
			if season=='DJF':
				index=0
			if season=='MAM':
				index=1
			if season=='JJA':
				index=2	
			if season=='SON':
				index=3
			if wdthres=='01':		
				file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hourly_2000-2004_INT.nc')
				OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
				OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
				OBS_pr_int_REGCM5=np.array(file_REGCM5['pr'][index,0,:,:])
				file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hourly_2000-2004_FREQ.nc')
				OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
				OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
				OBS_pr_frq_REGCM5=np.array(file_REGCM5['pr'][index,0,:,:])/24
				OBS_pr_int_REGCM5[np.abs(OBS_pr_int_REGCM5) > 10**4]=np.nan
			if wdthres=='05':		
				file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hourly_2000-2004_INT05.nc')
				OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
				OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
				OBS_pr_int_REGCM5=np.array(file_REGCM5['pr'][index,0,:,:])
				file_REGCM5=Dataset('../data/regrid_REGCM5_12km_hourly_2000-2004_FREQ05.nc')
				OBS_lat_REGCM5=np.array(file_REGCM5['lat'][:])
				OBS_lon_REGCM5=np.array(file_REGCM5['lon'][:])
				OBS_pr_frq_REGCM5=np.array(file_REGCM5['pr'][index,0,:,:])/24
				OBS_pr_int_REGCM5[np.abs(OBS_pr_int_REGCM5) > 10**4]=np.nan

		if 'UK' in regions:
			diff_arr_ITA_int[index_season,:,:]=OBS_pr_int_ITA[:,:]-OBS_pr_int_REGCM5[:,:]
			diff_arr_ITA_frq[index_season,:,:]=OBS_pr_frq_ITA[:,:]/24-OBS_pr_frq_REGCM5[:,:]
		if 'GER' in regions:
			diff_arr_GER_int[index_season,:,:]=OBS_pr_int_GER[:,:]-OBS_pr_int_REGCM5[:,:]
			diff_arr_GER_frq[index_season,:,:]=OBS_pr_frq_GER[:,:]/24-OBS_pr_frq_REGCM5[:,:]
		if 'FRA' in regions:
			diff_arr_FRA_int[index_season,:,:]=OBS_pr_int_FRA[:,:]-OBS_pr_int_REGCM5[:,:]
			diff_arr_FRA_frq[index_season,:,:]=OBS_pr_frq_FRA[:,:]/24-OBS_pr_frq_REGCM5[:,:]
		if 'SWI' in regions:
			diff_arr_SWI_int[index_season,:,:]=OBS_pr_int_SWI[:,:]-OBS_pr_int_REGCM5[:,:]
			diff_arr_SWI_frq[index_season,:,:]=OBS_pr_frq_SWI[:,:]/24-OBS_pr_frq_REGCM5[:,:]
		if 'UK' in regions:
			diff_arr_UK_int[index_season,:,:]=OBS_pr_int_UK[:,:]-OBS_pr_int_REGCM5[:,:]
			diff_arr_UK_frq[index_season,:,:]=OBS_pr_frq_UK[:,:]/24-OBS_pr_frq_REGCM5[:,:]
			
		print(np.nanmax(diff_arr_UK_frq[index_season,:,:]))
		
		OBS_pr_int_UK[OBS_pr_int_UK<-10**(10)]=np.nan
		OBS_pr_int_FRA[OBS_pr_int_FRA<-10**(10)]=np.nan
		OBS_pr_int_GER[OBS_pr_int_GER<-10**(10)]=np.nan
		OBS_pr_int_SWI[OBS_pr_int_SWI<-10**(10)]=np.nan
		OBS_pr_int_ITA[OBS_pr_int_ITA<-10**(10)]=np.nan
		
		OBS_pr_int_UK[OBS_pr_int_UK>10**(10)]=np.nan
		OBS_pr_int_FRA[OBS_pr_int_FRA>10**(10)]=np.nan
		OBS_pr_int_GER[OBS_pr_int_GER>10**(10)]=np.nan
		OBS_pr_int_SWI[OBS_pr_int_SWI>10**(10)]=np.nan
		OBS_pr_int_ITA[OBS_pr_int_ITA>10**(10)]=np.nan
		
		A_notnanmask_UK=np.ones(np.shape(OBS_pr_int_UK));A_notnanmask_UK[np.isnan(OBS_pr_int_UK)]=0;
		A_notnanmask_FRA=np.ones(np.shape(OBS_pr_int_FRA));A_notnanmask_FRA[np.isnan(OBS_pr_int_FRA)]=0;
		A_notnanmask_GER=np.ones(np.shape(OBS_pr_int_GER));A_notnanmask_GER[np.isnan(OBS_pr_int_GER)]=0;
		A_notnanmask_SWI=np.ones(np.shape(OBS_pr_int_SWI));A_notnanmask_SWI[np.isnan(OBS_pr_int_SWI)]=0;
		A_notnanmask_ITA=np.ones(np.shape(OBS_pr_int_ITA));A_notnanmask_ITA[np.isnan(OBS_pr_int_ITA)]=0;
		
		A_notnanmask_TOT=(A_notnanmask_UK+A_notnanmask_FRA+A_notnanmask_GER+A_notnanmask_SWI+A_notnanmask_ITA)
		
		non_data_mask[A_notnanmask_TOT==0]=999
		
		OBS_pr_int_ITA[np.isnan(OBS_pr_int_ITA)]=0
		OBS_pr_int_FRA[np.isnan(OBS_pr_int_FRA)]=0
		OBS_pr_int_GER[np.isnan(OBS_pr_int_GER)]=0
		OBS_pr_int_SWI[np.isnan(OBS_pr_int_SWI)]=0
		OBS_pr_int_UK[np.isnan(OBS_pr_int_UK)]=0
		
		OBS_pr_frq_ITA[np.isnan(OBS_pr_frq_ITA)]=0
		OBS_pr_frq_FRA[np.isnan(OBS_pr_frq_FRA)]=0
		OBS_pr_frq_GER[np.isnan(OBS_pr_frq_GER)]=0
		OBS_pr_frq_SWI[np.isnan(OBS_pr_frq_SWI)]=0
		OBS_pr_frq_UK[np.isnan(OBS_pr_frq_UK)]=0
		
		OBS_pr_int_tot=(OBS_pr_int_ITA*A_notnanmask_ITA+OBS_pr_int_GER*A_notnanmask_GER+OBS_pr_int_FRA*A_notnanmask_FRA+OBS_pr_int_SWI*A_notnanmask_SWI+OBS_pr_int_UK*A_notnanmask_UK)/(A_notnanmask_TOT)
		OBS_pr_frq_tot=(OBS_pr_frq_ITA*A_notnanmask_ITA+OBS_pr_frq_GER*A_notnanmask_GER+OBS_pr_frq_FRA*A_notnanmask_FRA+OBS_pr_frq_SWI*A_notnanmask_SWI+OBS_pr_frq_UK*A_notnanmask_UK)/(A_notnanmask_TOT)
				
		diff_arr_TOT_int[index_season,:,:]=OBS_pr_int_tot[:,:]-OBS_pr_int_REGCM5[:,:]
		diff_arr_TOT_frq[index_season,:,:]=OBS_pr_frq_tot[:,:]/24-OBS_pr_frq_REGCM5[:,:]
		
		print('reading in P999')
		file2data=Dataset('../data/P999_obs_'+season+'_thres_'+'01'+'.nc','r')
		if season=='DJF':
			P999_OBS_DJF=np.array(file2data['P999'][:,:])
		if season=='MAM':
			P999_OBS_MAM=np.array(file2data['P999'][:,:])
		if season=='JJA':
			P999_OBS_JJA=np.array(file2data['P999'][:,:])
		if season=='SON':
			P999_OBS_SON=np.array(file2data['P999'][:,:])
		
		
		if 'REGCM5' in regions:
			file2data=Dataset('../data/regrid_hourly_REGCM5_CP_'+season+'_2000-2004_pr_thres_'+wdthres+'.nc','r')
			if season=='DJF':
				P999_MOD_DJF=np.array(file2data['pr_P999'][:,:])
			if season=='MAM':
				P999_MOD_MAM=np.array(file2data['pr_P999'][:,:])
			if season=='JJA':
				P999_MOD_JJA=np.array(file2data['pr_P999'][:,:])
			if season=='SON':
				P999_MOD_SON=np.array(file2data['pr_P999'][:,:])
		
		if 'REGCM5_12km' in regions:
			file2data=Dataset('../data/regrid_REGCM5_12km_2000-2004_P999.nc','r')
			P999_MOD_DJF=np.array(file2data['pr'][0,:,:])
			P999_MOD_MAM=np.array(file2data['pr'][1,:,:])
			P999_MOD_JJA=np.array(file2data['pr'][2,:,:])
			P999_MOD_SON=np.array(file2data['pr'][3,:,:])
		
		index_season+=1 
	
	P999_bias_DJF=P999_MOD_DJF-P999_OBS_DJF
	P999_bias_MAM=P999_MOD_MAM-P999_OBS_MAM
	P999_bias_JJA=P999_MOD_JJA-P999_OBS_JJA
	P999_bias_SON=P999_MOD_SON-P999_OBS_SON
	
	P999_bias_DJF[P999_bias_DJF<-10**(10)]=np.nan
	P999_bias_MAM[P999_bias_MAM<-10**(10)]=np.nan
	P999_bias_JJA[P999_bias_JJA<-10**(10)]=np.nan
	P999_bias_SON[P999_bias_SON<-10**(10)]=np.nan
	
	P999_bias_DJF[A_notnanmask_TOT==0]=np.nan
	P999_bias_MAM[A_notnanmask_TOT==0]=np.nan
	P999_bias_JJA[A_notnanmask_TOT==0]=np.nan
	P999_bias_SON[A_notnanmask_TOT==0]=np.nan
	
	P999_bias_DJF[P999_bias_DJF>10**(10)]=np.nan
	P999_bias_MAM[P999_bias_MAM>10**(10)]=np.nan
	P999_bias_JJA[P999_bias_JJA>10**(10)]=np.nan
	P999_bias_SON[P999_bias_SON>10**(10)]=np.nan
	
	diff_arr_TOT_int[diff_arr_TOT_int<-10**(10)]=np.nan
	diff_arr_TOT_frq[diff_arr_TOT_frq<-10**(10)]=np.nan
	diff_arr_TOT_int[diff_arr_TOT_int>10**(10)]=np.nan
	diff_arr_TOT_frq[diff_arr_TOT_frq>10**(10)]=np.nan
	
	diff_arr_ITA_int[diff_arr_ITA_int<-10**(10)]=np.nan
	diff_arr_GER_int[diff_arr_GER_int<-10**(10)]=np.nan
	diff_arr_FRA_int[diff_arr_FRA_int<-10**(10)]=np.nan
	diff_arr_SWI_int[diff_arr_SWI_int<-10**(10)]=np.nan
	diff_arr_UK_int[diff_arr_UK_int<-10**(10)]=np.nan

	diff_arr_ITA_int[diff_arr_ITA_int>10**(10)]=np.nan
	diff_arr_GER_int[diff_arr_GER_int>10**(10)]=np.nan
	diff_arr_FRA_int[diff_arr_FRA_int>10**(10)]=np.nan
	diff_arr_SWI_int[diff_arr_SWI_int>10**(10)]=np.nan
	diff_arr_UK_int[diff_arr_UK_int>10**(10)]=np.nan
	
	diff_arr_ITA_frq[diff_arr_ITA_frq<-10**(10)]=np.nan
	diff_arr_GER_frq[diff_arr_GER_frq<-10**(10)]=np.nan
	diff_arr_FRA_frq[diff_arr_FRA_frq<-10**(10)]=np.nan
	diff_arr_SWI_frq[diff_arr_SWI_frq<-10**(10)]=np.nan
	diff_arr_UK_frq[diff_arr_UK_frq<-10**(10)]=np.nan

	diff_arr_ITA_frq[diff_arr_ITA_frq>10**(10)]=np.nan
	diff_arr_GER_frq[diff_arr_GER_frq>10**(10)]=np.nan
	diff_arr_FRA_frq[diff_arr_FRA_frq>10**(10)]=np.nan
	diff_arr_SWI_frq[diff_arr_SWI_frq>10**(10)]=np.nan
	diff_arr_UK_frq[diff_arr_UK_frq>10**(10)]=np.nan
	
	print(datetime.now(),'plotting the data')

	cmap = nclcmaps.cmap('MPL_BrBG')
	clevels1=[-1,-0.8,-0.6,-0.4,-0.2,-0.1,0.1,0.2,0.4,0.6,0.8,1]
	clevels2=[-25,-20,-15,-10,-5,-1,1,5,10,15,20,25]
	clevels3=[-10,-8,-6,-4,-2,-0.5,0.5,2,4,6,8,10]	
	
	clevels1_plot=['True','False','True','False','True','False','True','True','False','True','False','True','False','True']
	clevels2_plot=[-25,-15,-5,-1,1,5,15,25]
	clevels3_plot=[-12,-8,-4,-0.5,0.5,4,8,12]	
	#extent=[-12,20,35,60]
	extent=[-12,20,35,60]
	
	# Plotting all the subplots here:  
	
	#### FIRST ROW (DJF)
	cmap_grey = 'Greys'
	fig = plt.figure(figsize=(9,11))
	ax0= fig.add_subplot(4,3,1, projection=ccrs.PlateCarree())
	ax0.set_extent(extent)
	ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax0.coastlines(resolution='50m', linewidth=coastline_width)
	
	print('plotting Precip int diff map')
	
	cs=ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'ITA' in regions:
	#	cs=ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'GER' in regions:
	#	cs=ax0.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'FRA' in regions:
	#	cs=ax0.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'SWI' in regions:
	#	cs=ax0.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'UK' in regions:
	#	cs=ax0.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_int[0,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	ax0.set_title('Precipitation intensity')
	
	ax0.annotate("DJF", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
	
	ax1= fig.add_subplot(4,3,2, projection=ccrs.PlateCarree())
	ax1.set_extent(extent)
	ax1.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax1.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip frq diff map')
	cs1=ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_frq[0,:,:]*-100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'ITA' in regions:
	#	cs=ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_frq[0,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'GER' in regions:
	#	cs=ax1.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_frq[0,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'FRA' in regions:
	#	cs=ax1.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_frq[0,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'SWI' in regions:
	#	cs=ax1.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_frq[0,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'UK' in regions:
	#	cs=ax1.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_frq[0,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	if 'REGCM5_12km' in regions:
		ax1.set_title('Bias (RegCM5 12km-OBS) \n \n Precipitation frequency')
	if 'REGCM5' in regions:
		ax1.set_title('Bias (RegCM5 CP-OBS) \n \n Precipitation frequency')
	
	ax2= fig.add_subplot(4,3,3, projection=ccrs.PlateCarree())
	ax2.set_extent(extent)
	ax2.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax2.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting P999 map')
	cs2=ax2.contourf(OBS_lon_ITA,OBS_lat_ITA,P999_bias_DJF, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
	ax2.set_title('P99.9')

	#### SECOND ROW (MAM)
	
	ax3= fig.add_subplot(4,3,4, projection=ccrs.PlateCarree())
	ax3.set_extent(extent)
	ax3.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax3.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip int diff map')
	cs=ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'ITA' in regions:
	#	cs=ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'GER' in regions:
	#	cs=ax3.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'FRA' in regions:
	#	cs=ax3.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'SWI' in regions:
	#	cs=ax3.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'UK' in regions:
	#	cs=ax3.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_int[1,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	ax3.annotate("MAM", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
	
	ax4= fig.add_subplot(4,3,5, projection=ccrs.PlateCarree())
	ax4.set_extent(extent)
	ax4.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax4.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip frq diff map')
	cs1=ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_frq[1,:,:]*-100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'ITA' in regions:
	#	cs=ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_frq[1,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'GER' in regions:
	#	cs=ax4.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_frq[1,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'FRA' in regions:
	#	cs=ax4.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_frq[1,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'SWI' in regions:
	#	cs=ax4.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_frq[1,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'UK' in regions:
	#	cs=ax4.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_frq[1,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)

	ax5= fig.add_subplot(4,3,6, projection=ccrs.PlateCarree())
	ax5.set_extent(extent)
	ax5.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax5.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting P999 map')
	cs2=ax5.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],P999_bias_MAM, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)

	#### Third ROW (JJA)
	
	ax6= fig.add_subplot(4,3,7, projection=ccrs.PlateCarree())
	ax6.set_extent(extent)
	ax6.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax6.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip int diff map')
	cs=ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'ITA' in regions:
	#	cs=ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'GER' in regions:
	#	cs=ax6.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'FRA' in regions:
	#	cs=ax6.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'SWI' in regions:
	#	cs=ax6.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'UK' in regions:
	#	cs=ax6.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_int[2,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	ax6.annotate("JJA", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
	
	ax7= fig.add_subplot(4,3,8, projection=ccrs.PlateCarree())
	ax7.set_extent(extent)
	ax7.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax7.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip frq diff map')
	cs1=ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_frq[2,:,:]*-100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'ITA' in regions:
	#	cs=ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_frq[2,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'GER' in regions:
	#	cs=ax7.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_frq[2,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'FRA' in regions:
	#	cs=ax7.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_frq[2,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'SWI' in regions:
	#	cs=ax7.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_frq[2,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'UK' in regions:
	#	cs=ax7.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_frq[2,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)

	ax8= fig.add_subplot(4,3,9, projection=ccrs.PlateCarree())
	ax8.set_extent(extent)
	ax8.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax8.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting P999 map')
	cs=ax8.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],P999_bias_JJA, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)

	#### Fourth ROW (SON)
	
	ax9= fig.add_subplot(4,3,10, projection=ccrs.PlateCarree())
	ax9.set_extent(extent)
	ax9.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax9.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip int diff map')
	cs=ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'ITA' in regions:
	#	cs=ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'GER' in regions:
	#	cs=ax9.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'FRA' in regions:
	#	cs=ax9.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'SWI' in regions:
	#	cs=ax9.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	#if 'UK' in regions:
	#	cs=ax9.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_int[3,:,:]*-1, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
	ax9.annotate("SON", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
	
	ax10= fig.add_subplot(4,3,11, projection=ccrs.PlateCarree())
	ax10.set_extent(extent)
	ax10.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax10.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting Precip frq diff map')
	cs1=ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_TOT_frq[3,:,:]*-100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'ITA' in regions:
	#	cs1=ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],diff_arr_ITA_frq[3,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'GER' in regions:
	#	cs1=ax10.contourf(OBS_lon_GER[:],OBS_lat_GER[:],diff_arr_GER_frq[3,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'FRA' in regions:
	#	cs1=ax10.contourf(OBS_lon_FRA[:],OBS_lat_FRA[:],diff_arr_FRA_frq[3,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'SWI' in regions:
	#	cs1=ax10.contourf(OBS_lon_SWI[:],OBS_lat_SWI[:],diff_arr_SWI_frq[3,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)
	#if 'UK' in regions:
	#	cs1=ax10.contourf(OBS_lon_UK[:],OBS_lat_UK[:],diff_arr_UK_frq[3,:,:]*-100/24, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels2)

	ax11= fig.add_subplot(4,3,12, projection=ccrs.PlateCarree())
	ax11.set_extent(extent)
	ax11.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
	ax11.coastlines(resolution='50m', linewidth=coastline_width)
	print('plotting P999 map')
	cs2=ax11.contourf(OBS_lon_ITA[50:],OBS_lat_ITA[:],P999_bias_SON[:,50:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
	
	print('plotting colorbars')
	
	fig.subplots_adjust(wspace=0.05, hspace=0.05)
	
	cbar_ax = fig.add_axes([0.15,  0.08, 0.20, 0.015])
	cbar_ax2 = fig.add_axes([0.415, 0.08, 0.20, 0.015])
	cbar_ax3 = fig.add_axes([0.675, 0.08, 0.20, 0.015])
	
	cbar=plt.colorbar(cs, cax=cbar_ax, label='\n mm/hour',orientation='horizontal');
	cbar.set_ticks(clevels1)
	cbar.ax.tick_params(rotation=90)
	
	cbar2=plt.colorbar(cs1, cax=cbar_ax2, label='%',orientation='horizontal');
	cbar2.set_ticks(clevels2)
	cbar2.ax.tick_params(rotation=90)
	
	cbar3=plt.colorbar(cs2, cax=cbar_ax3, label='mm/hour',orientation='horizontal');
	cbar3.set_ticks(clevels3)
	cbar3.ax.tick_params(rotation=90)
	
	print('plotting annotations')
	
	ax0.annotate("a)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax1.annotate("b)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax2.annotate("c)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax3.annotate("d)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax4.annotate("e)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax5.annotate("f)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax6.annotate("g)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax7.annotate("h)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax8.annotate("i)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax9.annotate("j)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax10.annotate("k)", xy=(0.91, 0.05), xycoords="axes fraction")
	ax11.annotate("l)", xy=(0.91, 0.05), xycoords="axes fraction")

	print('adding the grey background color')

	ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax2.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax5.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax8.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
	ax11.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])


		
	print('saving the figure')
	
	if 'REGCM5_12km' in regions:
		if wdthres=='01':
			plt.savefig('../plots/FigS9_panel_b.jpeg', bbox_inches='tight', dpi=200)
		if wdthres=='05':
			plt.savefig('../plots/Fig10_panel_b.jpeg', bbox_inches='tight', dpi=200)	 
	if 'REGCM5' in regions:
		if wdthres=='01':
			plt.savefig('../plots/FigS9_panel_a.jpeg', bbox_inches='tight', dpi=200)
		if wdthres=='05':
			plt.savefig('../plots/Fig10_panel_a.jpeg', bbox_inches='tight', dpi=200)	 
	

main()
