import math
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import cartopy.crs as ccrs
import cartopy
import cartopy.feature as cfeature
from netCDF4 import Dataset
from matplotlib.colors import LogNorm

from math import *

year='2000'
month='06'
zoom='yes'		# 'yes' to plot the insert of the figure

file_ERA5=Dataset('../data/pr_'+year+'_'+month+'.nc')
lat_ERA5=np.array(file_ERA5['latitude'][:])
lon_ERA5=np.array(file_ERA5['longitude'])
lon_grid_ERA5,lat_grid_ERA5=np.meshgrid(lon_ERA5,lat_ERA5)

daystart=7

for j in range(2):
 j=j+daystart
 if j < 9:
	  readname='../data/WP3_yellowS_SHF.'+year+month+'0'+str(j+1)+'00.nc'
 if j >=9:
	  readname='../data/WP3_yellowS_SHF.'+year+month+str(j+1)+'00.nc'
 file_RegCM=Dataset(readname,mode='r')
 pr_RegCM=np.array(file_RegCM['pr'])
 if j==daystart:
   lat_RegCM=np.array(file_RegCM['xlat'])
   lon_RegCM=np.array(file_RegCM['xlon'])
   
   lat_RegCM_r=np.array(file_RegCM['rlat'])
   lon_RegCM_r=np.array(file_RegCM['rlon'])

   lon_RegCM_rt,lat_RegCM_rt=np.meshgrid(lon_RegCM_r,lat_RegCM_r)
	 
   pr_RegCM_boundary=np.zeros(np.shape(pr_RegCM)[1:])

   indices=np.where(lon_RegCM_rt<=lon_RegCM_r[29])
   pr_RegCM_boundary[indices]=100
  
   indices=np.where(lon_RegCM_rt>=lon_RegCM_r[-29])
   pr_RegCM_boundary[indices]=100

   indices=np.where(lat_RegCM_rt<=lat_RegCM_r[29])
   pr_RegCM_boundary[indices]=100

   indices=np.where(lat_RegCM_rt>=lat_RegCM_r[-29])
   pr_RegCM_boundary[indices]=100

   pr_RegCM_boundary[pr_RegCM_boundary==0]=-10 
 for i in range(24):
  print('day ',j+1,'hour ',i)
  if j < 9:
	  if i <= 9:
		  savename='Fig7_precip_'+year+month+'0'+str(j+1)+'0'+str(i)+'.png'
		  title_name=year+'/'+month+'/0'+str(j+1)+' 0'+str(i) + ':00 UTC'
	  if i >9:
		  savename='Fig7_precip_'+year+month+'0'+str(j+1)+str(i)+'.png'
		  title_name=year+'/'+month+'/0'+str(j+1)+' '+str(i) + ':00 UTC'
  if j >=9:
	  if i <= 9:
		  savename='Fig7_precip_'+year+month+str(j+1)+'0'+str(i)+'.png'
		  title_name=year+'/'+month+'/'+str(j+1)+' 0'+str(i)+ ':00 UTC'
	  if i >9:
		  savename='Fig7_precip_'+year+month+str(j+1)+str(i)+'.png'
		  title_name=year+'/'+month+'/'+str(j+1)+' '+str(i) + ':00 UTC'
 
  pr_ERA5=np.array(file_ERA5['tp'][i+j*24,:,:])
  pr_ERA5[450:,:]=np.nan
  pr_ERA5[:,400:1100]=np.nan

  fig = plt.figure(figsize=(8,5))
   
  if zoom=='no':
  	extent=[-40,55,15,70]
  	cbar_ax = fig.add_axes([0.15, 0.01, 0.7, 0.05])	
  if zoom=='yes':
  	extent=[10,25,36,44]
  
  pr_ERA5[pr_ERA5[:,:]*1000<=0.1]=np.nan
  pr_RegCM[pr_RegCM[:,:,:]*3600<=0.1]=np.nan
  
  pr_ERA5[200:220,0:100]=-999
  pr_ERA5[200:220,-45:]=-999
  pr_ERA5[180:200,0:108]=-999
  pr_ERA5[180:200,-50:]=-999  
  pr_ERA5[160:180,0:114]=-999
  pr_ERA5[160:180,-60:]=-999
  pr_ERA5[140:160,0:123]=-999
  pr_ERA5[140:160,-70:]=-999
  pr_ERA5[110:140,0:135]=-999
  pr_ERA5[110:140,-80:]=-999
  pr_ERA5[104:110,0:100]=-999
  pr_ERA5[104:110,-40:]=-999
  
  if zoom=='yes':
  	pr_ERA5[:,:]=np.nan
  
  ax=plt.axes(projection=ccrs.Orthographic(central_longitude=9.75, central_latitude= 49.68))
  ax.set_extent(extent)
  ax.gridlines(draw_labels=True, dms=False,x_inline=False,y_inline=False)
  ax.add_feature(cfeature.LAND.with_scale('50m'))
  ax.coastlines(resolution='50m', linewidth=1)
  clevels=[0.0,0.5,1.0,1.5,2,2.5,3,3.5,4,4.5,5]
  print('plotting ERA5')
  cs=ax.contourf(lon_grid_ERA5[:,:],lat_grid_ERA5[:,:],pr_ERA5[:,:]*1000, transform=ccrs.PlateCarree(), cmap=matplotlib.cm.BuPu, extend='max', levels=clevels)
  print('plotting RegCM5')
  cs=ax.contourf(lon_RegCM[:,:],lat_RegCM[:,:],pr_RegCM[i,:,:]*3600, transform=ccrs.PlateCarree(), cmap=matplotlib.cm.BuPu, extend='max',levels=clevels)
  if zoom=='no':
  	cs2=ax.contourf(lon_RegCM[:,:],lat_RegCM[:,:],pr_RegCM_boundary[:,:], transform=ccrs.PlateCarree(), cmap=matplotlib.cm.Greys, extend='max',levels=clevels, alpha=0.3)
  	plt.colorbar(cs, cax=cbar_ax, label='mm hr$^{-1}$', orientation='horizontal');
  plt.title(title_name)
  print('saving the figure zoom_', savename)
  if zoom=='yes':
  	plt.savefig('../plots/zoom_'+savename, bbox_inches='tight', dpi=200) 
  if zoom=='no':
  	plt.savefig('../plots/'+savename, bbox_inches='tight', dpi=200)
  plt.clf()



