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
	
	#READING IN THE OBSERVATIONAL DAILY DATASETS
	
	path_OBS='../data/'
	path_REGCM='../data/'
	path_EOBS='../data/'
	
	#ITALY
	file_OBS_ITA_DJF=Dataset(path_OBS+'regrid_daily_GRIPHO_period_1_5_DJF_Pstats.nc')
	file_OBS_ITA_MAM=Dataset(path_OBS+'regrid_daily_GRIPHO_period_1_5_MAM_Pstats.nc')
	file_OBS_ITA_JJA=Dataset(path_OBS+'regrid_daily_GRIPHO_period_1_5_JJA_Pstats.nc')
	file_OBS_ITA_SON=Dataset(path_OBS+'regrid_daily_GRIPHO_period_1_5_SON_Pstats.nc')

	#SPAIN
	file_OBS_SPA_DJF=Dataset(path_OBS+'regrid_daily_SPAIN02_period_1_5_DJF_Pstats.nc')
	file_OBS_SPA_MAM=Dataset(path_OBS+'regrid_daily_SPAIN02_period_1_5_MAM_Pstats.nc')
	file_OBS_SPA_JJA=Dataset(path_OBS+'regrid_daily_SPAIN02_period_1_5_JJA_Pstats.nc')
	file_OBS_SPA_SON=Dataset(path_OBS+'regrid_daily_SPAIN02_period_1_5_SON_Pstats.nc')
	
	#FRANCE
	file_OBS_FRA_DJF=Dataset(path_OBS+'regrid_daily_COMEPHORE_period_1_5_DJF_Pstats.nc')
	file_OBS_FRA_MAM=Dataset(path_OBS+'regrid_daily_COMEPHORE_period_1_5_MAM_Pstats.nc')
	file_OBS_FRA_JJA=Dataset(path_OBS+'regrid_daily_COMEPHORE_period_1_5_JJA_Pstats.nc')
	file_OBS_FRA_SON=Dataset(path_OBS+'regrid_daily_COMEPHORE_period_1_5_SON_Pstats.nc')
	
	#ALPS
	file_OBS_ALP_DJF=Dataset(path_OBS+'regrid_daily_EURO4M_period_1_5_DJF_Pstats.nc')
	file_OBS_ALP_MAM=Dataset(path_OBS+'regrid_daily_EURO4M_period_1_5_MAM_Pstats.nc')
	file_OBS_ALP_JJA=Dataset(path_OBS+'regrid_daily_EURO4M_period_1_5_JJA_Pstats.nc')
	file_OBS_ALP_SON=Dataset(path_OBS+'regrid_daily_EURO4M_period_1_5_SON_Pstats.nc')
	
	#CARPAT
	file_OBS_CAR_DJF=Dataset(path_OBS+'regrid_daily_CARPAT_period_1_5_DJF_Pstats.nc')
	file_OBS_CAR_MAM=Dataset(path_OBS+'regrid_daily_CARPAT_period_1_5_MAM_Pstats.nc')
	file_OBS_CAR_JJA=Dataset(path_OBS+'regrid_daily_CARPAT_period_1_5_JJA_Pstats.nc')
	file_OBS_CAR_SON=Dataset(path_OBS+'regrid_daily_CARPAT_period_1_5_SON_Pstats.nc')
	
	#GERMANY
	file_OBS_GER_DJF=Dataset(path_OBS+'regrid_daily_REGNIE_period_1_5_DJF_Pstats.nc')
	file_OBS_GER_MAM=Dataset(path_OBS+'regrid_daily_REGNIE_period_1_5_MAM_Pstats.nc')
	file_OBS_GER_JJA=Dataset(path_OBS+'regrid_daily_REGNIE_period_1_5_JJA_Pstats.nc')
	file_OBS_GER_SON=Dataset(path_OBS+'regrid_daily_REGNIE_period_1_5_SON_Pstats.nc')
	
	#UK
	file_OBS_UK_DJF=Dataset(path_OBS+'regrid_daily_ENG-REGR_period_1_5_DJF_Pstats.nc')
	file_OBS_UK_MAM=Dataset(path_OBS+'regrid_daily_ENG-REGR_period_1_5_MAM_Pstats.nc')
	file_OBS_UK_JJA=Dataset(path_OBS+'regrid_daily_ENG-REGR_period_1_5_JJA_Pstats.nc')
	file_OBS_UK_SON=Dataset(path_OBS+'regrid_daily_ENG-REGR_period_1_5_SON_Pstats.nc')
	
	#SWEDEN
	file_OBS_SWE_DJF=Dataset(path_OBS+'regrid_daily_SWEDEN_period_1_5_DJF_Pstats.nc')
	file_OBS_SWE_MAM=Dataset(path_OBS+'regrid_daily_SWEDEN_period_1_5_MAM_Pstats.nc')
	file_OBS_SWE_JJA=Dataset(path_OBS+'regrid_daily_SWEDEN_period_1_5_JJA_Pstats.nc')
	file_OBS_SWE_SON=Dataset(path_OBS+'regrid_daily_SWEDEN_period_1_5_SON_Pstats.nc')
	
	#NORWAY
	file_OBS_NOR_DJF=Dataset(path_OBS+'regrid_daily_NORWAY-METNO_period_1_5_DJF_Pstats.nc')
	file_OBS_NOR_MAM=Dataset(path_OBS+'regrid_daily_NORWAY-METNO_period_1_5_MAM_Pstats.nc')
	file_OBS_NOR_JJA=Dataset(path_OBS+'regrid_daily_NORWAY-METNO_period_1_5_JJA_Pstats.nc')
	file_OBS_NOR_SON=Dataset(path_OBS+'regrid_daily_NORWAY-METNO_period_1_5_SON_Pstats.nc')				
	
	OBS_lat_ITA=np.array(file_OBS_ITA_DJF['lat'][:])
	OBS_lon_ITA=np.array(file_OBS_ITA_DJF['lon'][:])
	
	OBS_pr_ITA=np.array(file_OBS_ITA_DJF['pr_avg'][:])
	
	#creating the empty files to fill in with the OBS data
	OBS_arr_pr_TOT_int=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))	
	OBS_arr_pr_TOT_frq=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	OBS_arr_pr_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	OBS_arr_tas_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	
	non_data_mask=np.ones((np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	
	ITA_mask=np.where(np.array(file_OBS_ITA_DJF['pr_avg'][:])<=0,0,1)
	SPA_mask=np.where(np.array(file_OBS_SPA_DJF['pr_avg'][:])<=0,0,1)
	FRA_mask=np.where(np.array(file_OBS_FRA_DJF['pr_avg'][:])<=0,0,1)
	GER_mask=np.where(np.array(file_OBS_GER_DJF['pr_avg'][:])<=0,0,1)
	CAR_mask=np.where(np.array(file_OBS_CAR_DJF['pr_avg'][:])<=0,0,1)
	ALP_mask=np.where(np.array(file_OBS_ALP_DJF['pr_avg'][:])<=0,0,1)
	UK_mask=np.where(np.array(file_OBS_UK_DJF['pr_avg'][:])<=0,0,1)
	NOR_mask=np.where(np.array(file_OBS_NOR_DJF['pr_avg'][:])<=0,0,1)
	SWE_mask=np.where(np.array(file_OBS_SWE_DJF['pr_avg'][:])<=0,0,1)
	
	total_mask=ITA_mask+GER_mask+FRA_mask+UK_mask+CAR_mask+ALP_mask+NOR_mask+SWE_mask+SPA_mask
	
	OBS_arr_pr_TOT_avg[0,:,:]=np.array(file_OBS_ITA_DJF['pr_avg'][:])*ITA_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_CAR_DJF['pr_avg'][:])*CAR_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_GER_DJF['pr_avg'][:])*GER_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_SPA_DJF['pr_avg'][:])*SPA_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_FRA_DJF['pr_avg'][:])*FRA_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_UK_DJF['pr_avg'][:])*UK_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_ALP_DJF['pr_avg'][:])*ALP_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_NOR_DJF['pr_avg'][:])*NOR_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]+np.array(file_OBS_SWE_DJF['pr_avg'][:])*SWE_mask
	OBS_arr_pr_TOT_avg[0,:,:]=OBS_arr_pr_TOT_avg[0,:,:]/total_mask
	
	OBS_arr_pr_TOT_int[0,:,:]=np.array(file_OBS_ITA_DJF['pr_int'][:])*ITA_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_CAR_DJF['pr_int'][:])*CAR_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_GER_DJF['pr_int'][:])*GER_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_SPA_DJF['pr_int'][:])*SPA_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_FRA_DJF['pr_int'][:])*FRA_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_UK_DJF['pr_int'][:])*UK_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_ALP_DJF['pr_int'][:])*ALP_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_NOR_DJF['pr_int'][:])*NOR_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]+np.array(file_OBS_SWE_DJF['pr_int'][:])*SWE_mask
	OBS_arr_pr_TOT_int[0,:,:]=OBS_arr_pr_TOT_int[0,:,:]/total_mask

	OBS_arr_pr_TOT_frq[0,:,:]=np.array(file_OBS_ITA_DJF['pr_frq'][:])*ITA_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_CAR_DJF['pr_frq'][:])*CAR_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_GER_DJF['pr_frq'][:])*GER_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_SPA_DJF['pr_frq'][:])*SPA_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_FRA_DJF['pr_frq'][:])*FRA_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_UK_DJF['pr_frq'][:])*UK_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_ALP_DJF['pr_frq'][:])*ALP_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_NOR_DJF['pr_frq'][:])*NOR_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]+np.array(file_OBS_SWE_DJF['pr_frq'][:])*SWE_mask
	OBS_arr_pr_TOT_frq[0,:,:]=OBS_arr_pr_TOT_frq[0,:,:]/total_mask	

	OBS_arr_pr_TOT_avg[1,:,:]=np.array(file_OBS_ITA_MAM['pr_avg'][:])*ITA_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_CAR_MAM['pr_avg'][:])*CAR_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_GER_MAM['pr_avg'][:])*GER_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_SPA_MAM['pr_avg'][:])*SPA_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_FRA_MAM['pr_avg'][:])*FRA_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_UK_MAM['pr_avg'][:])*UK_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_ALP_MAM['pr_avg'][:])*ALP_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_NOR_MAM['pr_avg'][:])*NOR_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]+np.array(file_OBS_SWE_MAM['pr_avg'][:])*SWE_mask
	OBS_arr_pr_TOT_avg[1,:,:]=OBS_arr_pr_TOT_avg[1,:,:]/total_mask
	
	OBS_arr_pr_TOT_int[1,:,:]=np.array(file_OBS_ITA_MAM['pr_int'][:])*ITA_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_CAR_MAM['pr_int'][:])*CAR_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_GER_MAM['pr_int'][:])*GER_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_SPA_MAM['pr_int'][:])*SPA_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_FRA_MAM['pr_int'][:])*FRA_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_UK_MAM['pr_int'][:])*UK_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_ALP_MAM['pr_int'][:])*ALP_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_NOR_MAM['pr_int'][:])*NOR_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]+np.array(file_OBS_SWE_MAM['pr_int'][:])*SWE_mask
	OBS_arr_pr_TOT_int[1,:,:]=OBS_arr_pr_TOT_int[1,:,:]/total_mask

	OBS_arr_pr_TOT_frq[1,:,:]=np.array(file_OBS_ITA_MAM['pr_frq'][:])*ITA_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_CAR_MAM['pr_frq'][:])*CAR_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_GER_MAM['pr_frq'][:])*GER_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_SPA_MAM['pr_frq'][:])*SPA_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_FRA_MAM['pr_frq'][:])*FRA_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_UK_MAM['pr_frq'][:])*UK_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_ALP_MAM['pr_frq'][:])*ALP_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_NOR_MAM['pr_frq'][:])*NOR_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]+np.array(file_OBS_SWE_MAM['pr_frq'][:])*SWE_mask
	OBS_arr_pr_TOT_frq[1,:,:]=OBS_arr_pr_TOT_frq[1,:,:]/total_mask	

	OBS_arr_pr_TOT_avg[2,:,:]=np.array(file_OBS_ITA_JJA['pr_avg'][:])*ITA_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_CAR_JJA['pr_avg'][:])*CAR_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_GER_JJA['pr_avg'][:])*GER_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_SPA_JJA['pr_avg'][:])*SPA_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_FRA_JJA['pr_avg'][:])*FRA_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_UK_JJA['pr_avg'][:])*UK_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_ALP_JJA['pr_avg'][:])*ALP_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_NOR_JJA['pr_avg'][:])*NOR_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]+np.array(file_OBS_SWE_JJA['pr_avg'][:])*SWE_mask
	OBS_arr_pr_TOT_avg[2,:,:]=OBS_arr_pr_TOT_avg[2,:,:]/total_mask
	
	OBS_arr_pr_TOT_int[2,:,:]=np.array(file_OBS_ITA_JJA['pr_int'][:])*ITA_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_CAR_JJA['pr_int'][:])*CAR_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_GER_JJA['pr_int'][:])*GER_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_SPA_JJA['pr_int'][:])*SPA_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_FRA_JJA['pr_int'][:])*FRA_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_UK_JJA['pr_int'][:])*UK_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_ALP_JJA['pr_int'][:])*ALP_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_NOR_JJA['pr_int'][:])*NOR_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]+np.array(file_OBS_SWE_JJA['pr_int'][:])*SWE_mask
	OBS_arr_pr_TOT_int[2,:,:]=OBS_arr_pr_TOT_int[2,:,:]/total_mask

	OBS_arr_pr_TOT_frq[2,:,:]=np.array(file_OBS_ITA_JJA['pr_frq'][:])*ITA_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_CAR_JJA['pr_frq'][:])*CAR_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_GER_JJA['pr_frq'][:])*GER_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_SPA_JJA['pr_frq'][:])*SPA_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_FRA_JJA['pr_frq'][:])*FRA_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_UK_JJA['pr_frq'][:])*UK_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_ALP_JJA['pr_frq'][:])*ALP_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_NOR_JJA['pr_frq'][:])*NOR_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]+np.array(file_OBS_SWE_JJA['pr_frq'][:])*SWE_mask
	OBS_arr_pr_TOT_frq[2,:,:]=OBS_arr_pr_TOT_frq[2,:,:]/total_mask	

	OBS_arr_pr_TOT_avg[3,:,:]=np.array(file_OBS_ITA_SON['pr_avg'][:])*ITA_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_CAR_SON['pr_avg'][:])*CAR_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_GER_SON['pr_avg'][:])*GER_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_SPA_SON['pr_avg'][:])*SPA_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_FRA_SON['pr_avg'][:])*FRA_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_UK_SON['pr_avg'][:])*UK_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_ALP_SON['pr_avg'][:])*ALP_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_NOR_SON['pr_avg'][:])*NOR_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]+np.array(file_OBS_SWE_SON['pr_avg'][:])*SWE_mask
	OBS_arr_pr_TOT_avg[3,:,:]=OBS_arr_pr_TOT_avg[3,:,:]/total_mask
	
	OBS_arr_pr_TOT_int[3,:,:]=np.array(file_OBS_ITA_SON['pr_int'][:])*ITA_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_CAR_SON['pr_int'][:])*CAR_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_GER_SON['pr_int'][:])*GER_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_SPA_SON['pr_int'][:])*SPA_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_FRA_SON['pr_int'][:])*FRA_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_UK_SON['pr_int'][:])*UK_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_ALP_SON['pr_int'][:])*ALP_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_NOR_SON['pr_int'][:])*NOR_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]+np.array(file_OBS_SWE_SON['pr_int'][:])*SWE_mask
	OBS_arr_pr_TOT_int[3,:,:]=OBS_arr_pr_TOT_int[3,:,:]/total_mask

	OBS_arr_pr_TOT_frq[3,:,:]=np.array(file_OBS_ITA_SON['pr_frq'][:])*ITA_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_CAR_SON['pr_frq'][:])*CAR_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_GER_SON['pr_frq'][:])*GER_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_SPA_SON['pr_frq'][:])*SPA_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_FRA_SON['pr_frq'][:])*FRA_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_UK_SON['pr_frq'][:])*UK_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_ALP_SON['pr_frq'][:])*ALP_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_NOR_SON['pr_frq'][:])*NOR_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]+np.array(file_OBS_SWE_SON['pr_frq'][:])*SWE_mask
	OBS_arr_pr_TOT_frq[3,:,:]=OBS_arr_pr_TOT_frq[3,:,:]/total_mask	
	
	#READING IN THE REGCM5 CP DAILY DATASETS
	
	total_mask=np.array(total_mask)
	
	total_mask[np.where(total_mask>0)]=1
	#total_mask[np.where(total_mask==0)]=np.nan
	
	index=np.where(total_mask!=1)
	non_data_mask[index]=999
	
	file_precip_REGCM5_CP_DJF=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_DJF_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_CP_MAM=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_MAM_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_CP_JJA=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_JJA_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_CP_SON=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_SON_2000-2004_pr_thres_1.nc')

	REGCM5_CP_arr_pr_TOT_int=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))	
	REGCM5_CP_arr_pr_TOT_frq=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	REGCM5_CP_arr_pr_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	REGCM5_CP_arr_tas_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))

	REGCM5_CP_arr_pr_TOT_avg[0,:,:]=np.array(file_precip_REGCM5_CP_DJF['pr_avg'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_avg[1,:,:]=np.array(file_precip_REGCM5_CP_MAM['pr_avg'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_avg[2,:,:]=np.array(file_precip_REGCM5_CP_JJA['pr_avg'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_avg[3,:,:]=np.array(file_precip_REGCM5_CP_SON['pr_avg'][:])*total_mask
		
	REGCM5_CP_arr_pr_TOT_int[0,:,:]=np.array(file_precip_REGCM5_CP_DJF['pr_int'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_int[1,:,:]=np.array(file_precip_REGCM5_CP_MAM['pr_int'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_int[2,:,:]=np.array(file_precip_REGCM5_CP_JJA['pr_int'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_int[3,:,:]=np.array(file_precip_REGCM5_CP_SON['pr_int'][:])*total_mask

	REGCM5_CP_arr_pr_TOT_frq[0,:,:]=np.array(file_precip_REGCM5_CP_DJF['pr_frq'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_frq[1,:,:]=np.array(file_precip_REGCM5_CP_MAM['pr_frq'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_frq[2,:,:]=np.array(file_precip_REGCM5_CP_JJA['pr_frq'][:])*total_mask
	REGCM5_CP_arr_pr_TOT_frq[3,:,:]=np.array(file_precip_REGCM5_CP_SON['pr_frq'][:])*total_mask

	file_temp_REGCM5_CP_DJF=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_DJF_2000-2004_temp.nc')
	file_temp_REGCM5_CP_MAM=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_MAM_2000-2004_temp.nc')
	file_temp_REGCM5_CP_JJA=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_JJA_2000-2004_temp.nc')
	file_temp_REGCM5_CP_SON=Dataset(path_REGCM+'regrid_daily_REGCM5_CP_SON_2000-2004_temp.nc')
	
	REGCM5_CP_arr_tas_TOT_avg[0,:,:]=np.array(file_temp_REGCM5_CP_DJF['tas_avg'][:])
	REGCM5_CP_arr_tas_TOT_avg[1,:,:]=np.array(file_temp_REGCM5_CP_MAM['tas_avg'][:])
	REGCM5_CP_arr_tas_TOT_avg[2,:,:]=np.array(file_temp_REGCM5_CP_JJA['tas_avg'][:])
	REGCM5_CP_arr_tas_TOT_avg[3,:,:]=np.array(file_temp_REGCM5_CP_SON['tas_avg'][:])


	#READING IN THE REGCM5 12km DAILY DATASETS

	file_precip_REGCM5_12km_DJF=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_DJF_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_12km_MAM=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_MAM_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_12km_JJA=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_JJA_2000-2004_pr_thres_1.nc')
	file_precip_REGCM5_12km_SON=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_SON_2000-2004_pr_thres_1.nc')

	REGCM5_12km_arr_pr_TOT_int=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))	
	REGCM5_12km_arr_pr_TOT_frq=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	REGCM5_12km_arr_pr_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))
	REGCM5_12km_arr_tas_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))

	REGCM5_12km_arr_pr_TOT_avg[0,:,:]=np.array(file_precip_REGCM5_12km_DJF['pr_avg'][:]*24)
	REGCM5_12km_arr_pr_TOT_avg[1,:,:]=np.array(file_precip_REGCM5_12km_MAM['pr_avg'][:]*24)
	REGCM5_12km_arr_pr_TOT_avg[2,:,:]=np.array(file_precip_REGCM5_12km_JJA['pr_avg'][:]*24)
	REGCM5_12km_arr_pr_TOT_avg[3,:,:]=np.array(file_precip_REGCM5_12km_SON['pr_avg'][:]*24)
	
	REGCM5_12km_arr_pr_TOT_int[0,:,:]=np.array(file_precip_REGCM5_12km_DJF['pr_int'][:]*24)
	REGCM5_12km_arr_pr_TOT_int[1,:,:]=np.array(file_precip_REGCM5_12km_MAM['pr_int'][:]*24)
	REGCM5_12km_arr_pr_TOT_int[2,:,:]=np.array(file_precip_REGCM5_12km_JJA['pr_int'][:]*24)
	REGCM5_12km_arr_pr_TOT_int[3,:,:]=np.array(file_precip_REGCM5_12km_SON['pr_int'][:]*24)

	REGCM5_12km_arr_pr_TOT_frq[0,:,:]=np.array(file_precip_REGCM5_12km_DJF['pr_frq'][:])
	REGCM5_12km_arr_pr_TOT_frq[1,:,:]=np.array(file_precip_REGCM5_12km_MAM['pr_frq'][:])
	REGCM5_12km_arr_pr_TOT_frq[2,:,:]=np.array(file_precip_REGCM5_12km_JJA['pr_frq'][:])
	REGCM5_12km_arr_pr_TOT_frq[3,:,:]=np.array(file_precip_REGCM5_12km_SON['pr_frq'][:])

	file_temp_REGCM5_12km_DJF=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_DJF_2000-2004_temp.nc')
	file_temp_REGCM5_12km_MAM=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_MAM_2000-2004_temp.nc')
	file_temp_REGCM5_12km_JJA=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_JJA_2000-2004_temp.nc')
	file_temp_REGCM5_12km_SON=Dataset(path_REGCM+'regrid_daily_REGCM5_12km_SON_2000-2004_temp.nc')
	
	REGCM5_12km_arr_tas_TOT_avg[0,:,:]=np.array(file_temp_REGCM5_12km_DJF['tas_avg'][:])
	REGCM5_12km_arr_tas_TOT_avg[1,:,:]=np.array(file_temp_REGCM5_12km_MAM['tas_avg'][:])
	REGCM5_12km_arr_tas_TOT_avg[2,:,:]=np.array(file_temp_REGCM5_12km_JJA['tas_avg'][:])
	REGCM5_12km_arr_tas_TOT_avg[3,:,:]=np.array(file_temp_REGCM5_12km_SON['tas_avg'][:])
	
	#READING IN THE P99 DAILY dataset
	
	file_precip_bias_P99=Dataset('../data/P99_total_incl.nc')
	
	data=np.array(file_precip_bias_P99['P99_OBS'][:,:])
	P99_lat=np.array(file_precip_bias_P99['lat'][:])
	P99_lon=np.array(file_precip_bias_P99['lon'][:])
	diff_arr_TOT_P99=np.zeros((4,np.shape(data)[0],np.shape(data)[1]))
	diff_arr_TOT12_P99=np.zeros((4,np.shape(data)[0],np.shape(data)[1]))
	
	diff_arr_TOT_P99[0,:,:]=np.array(file_precip_bias_P99['P99_REG'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT_P99[1,:,:]=np.array(file_precip_bias_P99['P99_REG'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT_P99[2,:,:]=np.array(file_precip_bias_P99['P99_REG'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT_P99[3,:,:]=np.array(file_precip_bias_P99['P99_REG'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])

	diff_arr_TOT12_P99[0,:,:]=np.array(file_precip_bias_P99['P99_REG12'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT12_P99[1,:,:]=np.array(file_precip_bias_P99['P99_REG12'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT12_P99[2,:,:]=np.array(file_precip_bias_P99['P99_REG12'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])
	diff_arr_TOT12_P99[3,:,:]=np.array(file_precip_bias_P99['P99_REG12'][:,:])-np.array(file_precip_bias_P99['P99_OBS'][:,:])


	#READING IN THE EOBS DAILY DATASETS

	file_tas_EOBS_DJF=Dataset(path_EOBS+'regrid_daily_EOBS_DJF_2000-2004_temp.nc')
	file_tas_EOBS_MAM=Dataset(path_EOBS+'regrid_daily_EOBS_MAM_2000-2004_temp.nc')
	file_tas_EOBS_JJA=Dataset(path_EOBS+'regrid_daily_EOBS_JJA_2000-2004_temp.nc')
	file_tas_EOBS_SON=Dataset(path_EOBS+'regrid_daily_EOBS_SON_2000-2004_temp.nc')
	
	#landmask_file=Dataset(path_EOBS+'landmask_highres.nc')
	
	#landmask=landmask_file['lsm'][0,:,:]

	EOBS_arr_tas_TOT_avg=np.zeros((4,np.shape(OBS_pr_ITA)[0],np.shape(OBS_pr_ITA)[1]))

	EOBS_arr_tas_TOT_avg[0,:,:]=np.array(file_tas_EOBS_DJF['tas_avg'][:]+274.15)
	EOBS_arr_tas_TOT_avg[1,:,:]=np.array(file_tas_EOBS_MAM['tas_avg'][:]+274.15)
	EOBS_arr_tas_TOT_avg[2,:,:]=np.array(file_tas_EOBS_JJA['tas_avg'][:]+274.15)
	EOBS_arr_tas_TOT_avg[3,:,:]=np.array(file_tas_EOBS_SON['tas_avg'][:]+274.15)
	
	landmask=np.where(EOBS_arr_tas_TOT_avg[0,:,:]>3000,0,1)
	
	# masking out sea for the temperature fields
	REGCM5_CP_arr_tas_TOT_avg[0,:,:]=REGCM5_CP_arr_tas_TOT_avg[0,:,:]*landmask
	REGCM5_CP_arr_tas_TOT_avg[1,:,:]=REGCM5_CP_arr_tas_TOT_avg[1,:,:]*landmask
	REGCM5_CP_arr_tas_TOT_avg[2,:,:]=REGCM5_CP_arr_tas_TOT_avg[2,:,:]*landmask
	REGCM5_CP_arr_tas_TOT_avg[3,:,:]=REGCM5_CP_arr_tas_TOT_avg[3,:,:]*landmask
	
	REGCM5_12km_arr_tas_TOT_avg[0,:,:]=REGCM5_12km_arr_tas_TOT_avg[0,:,:]*landmask
	REGCM5_12km_arr_tas_TOT_avg[1,:,:]=REGCM5_12km_arr_tas_TOT_avg[1,:,:]*landmask
	REGCM5_12km_arr_tas_TOT_avg[2,:,:]=REGCM5_12km_arr_tas_TOT_avg[2,:,:]*landmask
	REGCM5_12km_arr_tas_TOT_avg[3,:,:]=REGCM5_12km_arr_tas_TOT_avg[3,:,:]*landmask
	
	REGCM5_CP_arr_tas_TOT_avg[REGCM5_CP_arr_tas_TOT_avg==0]=np.nan
	
	EOBS_arr_tas_TOT_avg[0,:,:]=EOBS_arr_tas_TOT_avg[0,:,:]*landmask
	EOBS_arr_tas_TOT_avg[1,:,:]=EOBS_arr_tas_TOT_avg[1,:,:]*landmask
	EOBS_arr_tas_TOT_avg[2,:,:]=EOBS_arr_tas_TOT_avg[2,:,:]*landmask
	EOBS_arr_tas_TOT_avg[3,:,:]=EOBS_arr_tas_TOT_avg[3,:,:]*landmask

	non_data_mask=non_data_mask*landmask
	
	non_data_mask[non_data_mask!=999]=np.nan	
	######### CREATING THE FIGURE

	panel_b='false'
	coastline_width=0.5
	cmap_grey = 'Greys'
	
	if panel_b=='true':

		print(datetime.now(),'plotting the data')

		cmap = nclcmaps.cmap('MPL_BrBG')
		cmap_grey = 'Greys'
		clevels1=[-5,-4,-3,-2,-1,-0.5,0.5,1,2,3,4,5]
		clevels2=[-10,-8,-6,-4,-2,-0.5,0.5,2,4,6,8,10]	
		clevels3=[-50,-40,-30,-20,-10,-5,5,10,20,30,40,50]	

		clevels1_plot=['True','False','True','False','True','False','True','True','False','True','False','True','False','True']
		clevels2_plot=[-25,-15,-5,-1,1,5,15,25]
		#clevels3_plot=[-25,-15,-5,-1,1,5,15,25]
		clevels3_plot=[-12,-8,-4,-0.5,0.5,4,8,12]	
		extent=[-15,30,33,65]

		# Plotting all the subplots here:  

		#### FIRST ROW (DJF)

		fig = plt.figure(figsize=(11,11))

		ax0= fig.add_subplot(4,4,1, projection=ccrs.PlateCarree())
		ax0.set_extent(extent)
		ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax0.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],non_data_mask[:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		cs=ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_int[0,:-20,:]-OBS_arr_pr_TOT_int[0,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)


		ax0.set_title('RegCM5 CP')

		ax0.annotate("DJF", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
		ax0.annotate("Precipitation intensity", xy=(0.6, 1.3), xycoords="axes fraction", size='large')

		ax1= fig.add_subplot(4,4,2, projection=ccrs.PlateCarree())
		ax1.set_extent(extent)
		ax1.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax1.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_int[0,:,:]-OBS_arr_pr_TOT_int[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
		ax1.set_title('RegCM5 12km')	
		ax1.annotate("Bias (RegCM5-OBS)", xy=(0.55, 1.5), xycoords="axes fraction", size='x-large')

		ax2= fig.add_subplot(4,4,3, projection=ccrs.PlateCarree())
		ax2.set_extent(extent)
		ax2.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax2.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax2.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],(REGCM5_CP_arr_pr_TOT_frq[0,:-20,:]-OBS_arr_pr_TOT_frq[0,:-20,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
		ax2.set_title('RegCM5 CP')
		ax2.annotate("Precipitation frequency", xy=(0.55, 1.3), xycoords="axes fraction", size='large')

		ax3= fig.add_subplot(4,4,4, projection=ccrs.PlateCarree())
		ax3.set_extent(extent)
		ax3.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax3.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],(REGCM5_12km_arr_pr_TOT_frq[0,:,:]-OBS_arr_pr_TOT_frq[0,:,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
		ax3.set_title('RegCM5 12km')	

		#### SECOND ROW (MAM)

		ax4= fig.add_subplot(4,4,5, projection=ccrs.PlateCarree())
		ax4.set_extent(extent)
		ax4.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax4.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_int[1,:-20,:]-OBS_arr_pr_TOT_int[1,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax4.annotate("MAM", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax5= fig.add_subplot(4,4,6, projection=ccrs.PlateCarree())
		ax5.set_extent(extent)
		ax5.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax5.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax5.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_int[1,:,:]-OBS_arr_pr_TOT_int[1,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax6= fig.add_subplot(4,4,7, projection=ccrs.PlateCarree())
		ax6.set_extent(extent)
		ax6.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax6.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],(REGCM5_CP_arr_pr_TOT_frq[1,:-20,:]-OBS_arr_pr_TOT_frq[1,:-20,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)

		ax7= fig.add_subplot(4,4,8, projection=ccrs.PlateCarree())
		ax7.set_extent(extent)
		ax7.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax7.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],(REGCM5_12km_arr_pr_TOT_frq[1,:,:]-OBS_arr_pr_TOT_frq[1,:,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)	

		#### Third ROW (JJA)

		ax8= fig.add_subplot(4,4,9, projection=ccrs.PlateCarree())
		ax8.set_extent(extent)
		ax8.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax8.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax8.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_int[2,:-20,:]-OBS_arr_pr_TOT_int[2,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax8.annotate("JJA", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax9= fig.add_subplot(4,4,10, projection=ccrs.PlateCarree())
		ax9.set_extent(extent)
		ax9.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax9.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_int[2,:,:]-OBS_arr_pr_TOT_int[2,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax10= fig.add_subplot(4,4,11, projection=ccrs.PlateCarree())
		ax10.set_extent(extent)
		ax10.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax10.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],(REGCM5_CP_arr_pr_TOT_frq[2,:-20,:]-OBS_arr_pr_TOT_frq[2,:-20,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)

		ax11= fig.add_subplot(4,4,12, projection=ccrs.PlateCarree())
		ax11.set_extent(extent)
		ax11.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax11.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax11.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],(REGCM5_12km_arr_pr_TOT_frq[2,:,:]-OBS_arr_pr_TOT_frq[2,:,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)	

		#### Fourth ROW (SON)

		ax12= fig.add_subplot(4,4,13, projection=ccrs.PlateCarree())
		ax12.set_extent(extent)
		ax12.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax12.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax12.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_int[3,:-20,:]-OBS_arr_pr_TOT_int[3,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax12.annotate("SON", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax13= fig.add_subplot(4,4,14, projection=ccrs.PlateCarree())
		ax13.set_extent(extent)
		ax13.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax13.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax13.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_int[3,:,:]-OBS_arr_pr_TOT_int[3,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax14= fig.add_subplot(4,4,15, projection=ccrs.PlateCarree())
		ax14.set_extent(extent)
		ax14.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax14.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax14.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],(REGCM5_CP_arr_pr_TOT_frq[3,:-20,:]-OBS_arr_pr_TOT_frq[3,:-20,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)

		ax15= fig.add_subplot(4,4,16, projection=ccrs.PlateCarree())
		ax15.set_extent(extent)
		ax15.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax15.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax15.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],(REGCM5_12km_arr_pr_TOT_frq[3,:,:]-OBS_arr_pr_TOT_frq[3,:,:])*100, transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)	

		print('plotting colorbars')

		fig.subplots_adjust(wspace=0.05, hspace=0.05)

		cbar_ax = fig.add_axes([0.22,  0.08, 0.20, 0.015])
		cbar_ax2 = fig.add_axes([0.60, 0.08, 0.20, 0.015])

		cbar=plt.colorbar(cs, cax=cbar_ax, label='mm/day',orientation='horizontal');
		cbar.set_ticks(clevels1)
		cbar.ax.tick_params(rotation=60)

		tl = cbar.ax.get_xticklabels()

		# set the alignment for the first and the last
		for kk in range(12):
			tl[kk].set_horizontalalignment('right')


		cbar2=plt.colorbar(cs1, cax=cbar_ax2, label='%',orientation='horizontal');
		cbar2.set_ticks(clevels3)
		cbar2.ax.tick_params(rotation=60)

		tl = cbar2.ax.get_xticklabels()

		# set the alignment for the first and the last
		for kk in range(12):
			tl[kk].set_horizontalalignment('right')


		#cbar3=plt.colorbar(cs2, cax=cbar_ax3, label='mm/day',orientation='horizontal');
		#cbar3.set_ticks(clevels3)
		#cbar3.ax.tick_params(rotation=90)

		print('plotting annotations')

		ax0.annotate("a)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax1.annotate("b)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax2.annotate("c)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax3.annotate("d)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax4.annotate("e)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax5.annotate("f)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax6.annotate("g)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax7.annotate("h)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax8.annotate("i)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax9.annotate("j)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax10.annotate("k)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax11.annotate("l)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax12.annotate("m)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax13.annotate("n)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax14.annotate("o)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax15.annotate("p)", xy=(0.1, 0.9), xycoords="axes fraction")
		
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
		ax12.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax13.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax14.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax15.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
				
		print('saving the figure')
		
		plt.savefig('../plots/Fig_8_panel_b.jpeg', bbox_inches='tight', dpi=200) 

	###### P99 Figure
	
	panel_c='false'
	coastline_width=0.5
	extent=[-15,30,33,65]
	
	if panel_c=='true':

		cmap = nclcmaps.cmap('MPL_BrBG')	
		clevels3=[-50,-40,-30,-20,-10,-5,5,10,20,30,40,50]
		
		# Plotting all the subplots here:  

		#### FIRST ROW (Annual)

		fig = plt.figure(figsize=(8,3))
		ax0= fig.add_subplot(1,2,1, projection=ccrs.PlateCarree())
		ax0.set_extent(extent)
		ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax0.coastlines(resolution='50m', linewidth=coastline_width)
		cs=ax0.contourf(P99_lon,P99_lat,diff_arr_TOT_P99[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
		ax0.set_title('RegCM5 CP')

		ax2= fig.add_subplot(1,2,2,projection=ccrs.PlateCarree())
		ax2.set_extent(extent)
		ax2.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax2.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting P99 map')
		cs=ax2.contourf(P99_lon,P99_lat,diff_arr_TOT12_P99[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels3)
		ax2.set_title('RegCM5 12km')

		fig.subplots_adjust(wspace=0.05, hspace=0.05)

		cbar_ax = fig.add_axes([0.95,  0.08, 0.015, 0.8])

		cbar=plt.colorbar(cs, cax=cbar_ax, label='mm/day',orientation='vertical');
		cbar.set_ticks(clevels3)

		ax0.annotate("a)", xy=(0.12, 0.9), xycoords="axes fraction")
		ax2.annotate("b)", xy=(0.12, 0.9), xycoords="axes fraction")
		
		ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax2.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])


		print('saving the figure')

		plt.savefig('../plots/Fig_8_panel_c.jpeg', bbox_inches='tight', dpi=200) 
	
	############# CREATING THE MEAN TEMP - PRECIP figure	
	
	panel_a='true'
	
	if panel_a=='true':

		clevels1=[-10,-8,-6,-4,-2,-0.5,0.5,2,4,6,8,10]
		clevels2=[-10,-8,-6,-4,-2,-1,1,2,4,6,8,10]	
		
		no_data_mask=np.where(np.abs(REGCM5_CP_arr_tas_TOT_avg[0,:,:]-EOBS_arr_tas_TOT_avg[0,:,:])>20,0,1)
		
		no_data_mask=np.array(no_data_mask)
		
		# Plotting all the subplots here:  

		cmap_TEMP='bwr'


		######### CREATING THE FIGURE

		print(datetime.now(),'plotting the data')

		cmap = nclcmaps.cmap('MPL_BrBG')

		# Plotting all the subplots here:  

		#### FIRST ROW (DJF)

		fig = plt.figure(figsize=(11,11))

		ax0= fig.add_subplot(4,4,1, projection=ccrs.PlateCarree())
		ax0.set_extent(extent)
		ax0.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax0.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_avg[0,:-20,:]-OBS_arr_pr_TOT_avg[0,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
		ax0.set_title('RegCM5 CP')

		ax0.annotate("DJF", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')
		ax0.annotate("Mean Precipitation", xy=(0.7, 1.3), xycoords="axes fraction", size='large')

		ax1= fig.add_subplot(4,4,2, projection=ccrs.PlateCarree())
		ax1.set_extent(extent)
		ax1.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax1.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_avg[0,:,:]-OBS_arr_pr_TOT_avg[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)
		ax1.set_title('RegCM5 12km')	
		ax1.annotate("Bias (RegCM5-OBS)", xy=(0.55, 1.5), xycoords="axes fraction", size='x-large')

		ax2= fig.add_subplot(4,4,3, projection=ccrs.PlateCarree())
		ax2.set_extent(extent)
		ax2.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax2.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax2.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_CP_arr_tas_TOT_avg[0,:,:]*no_data_mask-EOBS_arr_tas_TOT_avg[0,:,:]*no_data_mask, transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)
		ax2.set_title('RegCM5 CP')
		ax2.annotate("Mean Temperature", xy=(0.6, 1.3), xycoords="axes fraction", size='large')

		ax3= fig.add_subplot(4,4,4, projection=ccrs.PlateCarree())
		ax3.set_extent(extent)
		ax3.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax3.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_tas_TOT_avg[0,:,:]-EOBS_arr_tas_TOT_avg[0,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)
		ax3.set_title('RegCM5 12km')	

		#### SECOND ROW (MAM)

		ax4= fig.add_subplot(4,4,5, projection=ccrs.PlateCarree())
		ax4.set_extent(extent)
		ax4.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax4.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_avg[1,:-20,:]-OBS_arr_pr_TOT_avg[1,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax4.annotate("MAM", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax5= fig.add_subplot(4,4,6, projection=ccrs.PlateCarree())
		ax5.set_extent(extent)
		ax5.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax5.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax5.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_avg[1,:,:]-OBS_arr_pr_TOT_avg[1,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax6= fig.add_subplot(4,4,7, projection=ccrs.PlateCarree())
		ax6.set_extent(extent)
		ax6.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax6.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_CP_arr_tas_TOT_avg[1,:,:]*no_data_mask-EOBS_arr_tas_TOT_avg[1,:,:]*no_data_mask, transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)

		ax7= fig.add_subplot(4,4,8, projection=ccrs.PlateCarree())
		ax7.set_extent(extent)
		ax7.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax7.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_tas_TOT_avg[1,:,:]-EOBS_arr_tas_TOT_avg[1,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)

		#### Third ROW (JJA)

		ax8= fig.add_subplot(4,4,9, projection=ccrs.PlateCarree())
		ax8.set_extent(extent)
		ax8.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax8.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax8.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_avg[2,:-20,:]-OBS_arr_pr_TOT_avg[2,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax8.annotate("JJA", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax9= fig.add_subplot(4,4,10, projection=ccrs.PlateCarree())
		ax9.set_extent(extent)
		ax9.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax9.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_avg[2,:,:]-OBS_arr_pr_TOT_avg[2,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax10= fig.add_subplot(4,4,11, projection=ccrs.PlateCarree())
		ax10.set_extent(extent)
		ax10.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax10.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_CP_arr_tas_TOT_avg[2,:,:]*no_data_mask-EOBS_arr_tas_TOT_avg[2,:,:]*no_data_mask, transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)

		ax11= fig.add_subplot(4,4,12, projection=ccrs.PlateCarree())
		ax11.set_extent(extent)
		ax11.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax11.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax11.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_tas_TOT_avg[2,:,:]-EOBS_arr_tas_TOT_avg[2,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)	

		#### Fourth ROW (SON)

		ax12= fig.add_subplot(4,4,13, projection=ccrs.PlateCarree())
		ax12.set_extent(extent)
		ax12.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax12.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax12.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:-20],REGCM5_CP_arr_pr_TOT_avg[3,:-20,:]-OBS_arr_pr_TOT_avg[3,:-20,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax12.annotate("SON", xy=(-0.3, 0.5), xycoords="axes fraction", size='large')

		ax13= fig.add_subplot(4,4,14, projection=ccrs.PlateCarree())
		ax13.set_extent(extent)
		ax13.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax13.coastlines(resolution='50m', linewidth=coastline_width)

		print('plotting Precip int diff map')

		cs=ax13.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_pr_TOT_avg[3,:,:]-OBS_arr_pr_TOT_avg[3,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap, levels=clevels1)

		ax14= fig.add_subplot(4,4,15, projection=ccrs.PlateCarree())
		ax14.set_extent(extent)
		ax14.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax14.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax14.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_CP_arr_tas_TOT_avg[3,:,:]*no_data_mask-EOBS_arr_tas_TOT_avg[3,:,:]*no_data_mask, transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)

		ax15= fig.add_subplot(4,4,16, projection=ccrs.PlateCarree())
		ax15.set_extent(extent)
		ax15.gridlines(draw_labels=False, dms=False,x_inline=False,y_inline=False)
		ax15.coastlines(resolution='50m', linewidth=coastline_width)
		print('plotting Precip frq diff map')
		cs1=ax15.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],REGCM5_12km_arr_tas_TOT_avg[3,:,:]-EOBS_arr_tas_TOT_avg[3,:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_TEMP, levels=clevels2)

		print('plotting colorbars')

		fig.subplots_adjust(wspace=0.05, hspace=0.05)

		cbar_ax = fig.add_axes([0.22,  0.08, 0.20, 0.015])
		cbar_ax2 = fig.add_axes([0.60, 0.08, 0.20, 0.015])

		cbar=plt.colorbar(cs, cax=cbar_ax, label='mm/day',orientation='horizontal');
		cbar.set_ticks(clevels1)
		cbar.ax.tick_params(rotation=60)

		tl = cbar.ax.get_xticklabels()

		# set the alignment for the first and the last
		for kk in range(12):
			tl[kk].set_horizontalalignment('right')


		cbar2=plt.colorbar(cs1, cax=cbar_ax2, label='$^\circ$Celsius',orientation='horizontal');
		cbar2.set_ticks(clevels2)
		cbar2.ax.tick_params(rotation=60)

		tl = cbar2.ax.get_xticklabels()

		# set the alignment for the first and the last
		for kk in range(12):
			tl[kk].set_horizontalalignment('right')


		#cbar3=plt.colorbar(cs2, cax=cbar_ax3, label='mm/day',orientation='horizontal');
		#cbar3.set_ticks(clevels3)
		#cbar3.ax.tick_params(rotation=90)

		print('plotting annotations')

		ax0.annotate("a)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax1.annotate("b)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax2.annotate("c)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax3.annotate("d)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax4.annotate("e)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax5.annotate("f)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax6.annotate("g)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax7.annotate("h)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax8.annotate("i)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax9.annotate("j)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax10.annotate("k)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax11.annotate("l)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax12.annotate("m)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax13.annotate("n)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax14.annotate("o)", xy=(0.1, 0.9), xycoords="axes fraction")
		ax15.annotate("p)", xy=(0.1, 0.9), xycoords="axes fraction")

		print('adding the grey background color')
				
		no_data_mask[no_data_mask==0]=999
				
		ax0.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax1.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax2.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],no_data_mask[:,:], transform=ccrs.PlateCarree(), cmap=cmap_grey, levels=[2,999])
		#ax3.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax4.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax5.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax6.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],no_data_mask[:,:], transform=ccrs.PlateCarree(), cmap=cmap_grey, levels=[2,999])
		#ax7.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax8.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax9.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax10.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],no_data_mask[:,:], transform=ccrs.PlateCarree(), cmap=cmap_grey, levels=[2,999])
		#ax11.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax12.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax13.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
		ax14.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],no_data_mask[:,:], transform=ccrs.PlateCarree(), cmap=cmap_grey, levels=[2,999])
		#ax15.contourf(OBS_lon_ITA[:],OBS_lat_ITA[:],non_data_mask[:,:], transform=ccrs.PlateCarree(), extend='both', cmap=cmap_grey, levels=[1,999])
				

		print('saving the figure')

		plt.savefig('../plots/Fig_8_panel_a.jpeg', bbox_inches='tight', dpi=200) 
		
main()
