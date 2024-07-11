#!/usr/bin/env python
# coding: utf-8

# Run me like this: python3 Global_plot_Fig1.py pixels
# after running the script in Global_plot_pixel_part_Figure2

import sys
import glob

light_blue = "#f2f8fa"
dark_blue = "#bde0ef"
dark_red = "#ffd7a0"
light_red = "#fff3df"

ocean = light_blue
land = light_red

imgpth = './Global_plot_pixel_part_Figure2/plots_v1_v2'
imgsize = 0.4 # inches
xalpha = 1.0 # larger less transparent

base = sys.argv[1]
gsearch = imgpth+'/*'+base+'*.png'
flist = glob.glob(gsearch)

if len(flist) == 0:
    print('No files matching pattern '+gsearch)
    sys.exit(-1)

# Supported values arei:
#   'upper right', 'upper left', 'lower left', 'lower right', 'right',
#   'center left', 'center right', 'lower center', 'upper center', 'center'
position = {
"GIC" : 'center',
"NWN" : 'center',
"NEN" : 'center',
"WNA" : 'center',
"CNA" : 'center',
"ENA" : 'center',
"NCA" : 'center',
"SCA" : 'center',
"CAR" : 'center',
"NWS" : 'center',
"NSA" : 'center',
"NES" : 'center',
"SAM" : 'center',
"SWS" : 'center',
"SES" : 'center',
"SSA" : 'center',
"NEU" : 'center',
"WCE" : 'center',
"EEU" : 'center',
"MED" : 'center',
"SAH" : 'center',
"WAF" : 'center',
"CAF" : 'center',
"NEAF" : 'center',
"SEAF" : 'center',
"WSAF" : 'center',
"ESAF" : 'center',
"MDG" : 'center',
"RAR" : 'center',
"WSB" : 'center',
"ESB" : 'center',
"RFE" : 'center',
"WCA" : 'center',
"ECA" : 'lower right',
"TIB" : 'center',
"EAS" : 'center',
"ARP" : 'center',
"SAS" : 'center',
"SEA" : 'center',
"NAU" : 'center',
"CAU" : 'center',
"EAU" : 'center',
"SAU" : 'center',
"NZ" : 'center',
"EAN" : 'center',
"WAN" : 'center',
"ARO" : 'center',
"NPO" : 'center',
"EPO" : 'center',
"SPO" : 'center',
"NAO" : 'center',
"EAO" : 'center',
"SAO" : 'center',
"ARS" : 'center',
"BOB" : 'center',
"EIO" : 'center',
"SIO" : 'center',
"SOO" : 'center'}

import cartopy.crs as ccrs
import matplotlib.pyplot as plt
import mplotutils as mpu
import regionmask
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
import numpy as np
import matplotlib.patheffects as pe
from shapely.geometry import Point, Polygon
import geopandas as gpd
from PIL import Image
import matplotlib.patches as patches

gp='IPCC-WGI-reference-regions-v4.shp'
regionshapes = gpd.read_file(gp)

remap = regionshapes.loc[lambda s: s.Type != 'Ocean'].to_crs('EPSG:4326')

## Change the EPSG in geoconv to adjust the projection conversion
geoconv = gpd.GeoDataFrame.to_crs(remap, ccrs.Robinson())
centers = np.asarray([ x for x in geoconv.centroid ])
list_arrays = [ np.array((geom.xy[0][0], geom.xy[1][0])) for geom in centers ]

img = [ ]
acro = [ ]
legenda=Image.open('legenda-new.png')
global_pixels=Image.open('Global_pixels.png')

a=-1
for rcod in remap.Acronym:
    a=a+1
    itex = [rcod in x for x in flist]
    if any(itex):
        indx = [i for i, x in enumerate(itex) if x][0]
        img.append(np.asarray(Image.open(flist[indx])))
        acro.append(rcod)
    else:
        img.append(None)
        acro.append(None)
        
for i in range(np.size(acro)):
    if acro[i]=='NWS':
        list_arrays[i]=[-6740832.0632548, -281195.07906457] 
    if acro[i]=='SWS':
        list_arrays[i]=[-6743568.58844822, -3269606.14102048]
    if acro[i]=='NSA':
        list_arrays[i]=[-4775374.97880105,   189939.76624508]
    if acro[i]=='MDG':
        list_arrays[i]=[ 4843471.77346599, -2108565.78658505]
    if acro[i]=='WSAF':
        list_arrays[i]=[ 1118407.23574649, -2446797.83554867]
    if acro[i]=='CAR':
        list_arrays[i]=[-6537306.24237058,  1976177.2895233 ]
    if acro[i]=='ENA':
        list_arrays[i]=[-6184294.93791933,  4213911.70882605]
    if acro[i]=='CNA':
        list_arrays[i]=[-8139332.99902502,  4198858.07632454]
    if acro[i]=='ECA':
        list_arrays[i]=[9115728.57968411, 3394961.87852045]
    if acro[i]=='SAS':
        list_arrays[i]= [7373713.32084525, 1831886.75032472]
    if acro[i]=='TIB':
        list_arrays[i]= [7870076.67336481, 3164997.51237719]
    if acro[i]=='SAU':
        list_arrays[i]= [11841419.47834757, -4509798.35032037]
    if acro[i]=='CAU':
        list_arrays[i]=[11763105.49758399, -2985635.21268542]
    if acro[i]=='SAM':
        list_arrays[i]=[-5663984.28704498, -1769859.26566404]
    if acro[i]=='SEAF':
        list_arrays[i]=[3467216.72745506, -511269.857155  ]
    if acro[i]=='SEA':
       list_arrays[i]=[10120476.34931033,   369006.20019558]
    if acro[i]=='SES':
        list_arrays[i]=[-4557972.72197529, -3058362.44165917]
    if acro[i]=='NES':
        list_arrays[i]=[-3444123.66405135, -1066358.04223574]


actualvalues=np.ones((4,7))
actualvalues[0,:]=[0.0,-0.3,0.5,0.2,3.0,-0.1,0.8] 
actualvalues[1,:]=[-0.2,-0.6,0.4,0.2,3.8,0.0,0.0]
actualvalues[2,:]=[0.0,-0.3,0.5,0.1,4.1,0.1,0.0]
actualvalues[3,:]=[0.0,-0.3,0.6,0.2,3.5,0.0,0.0]
    
def plot_map_colored(color_light, color_dark):
    text_kws = dict(bbox=dict(color="none"),
                    path_effects=[pe.withStroke(linewidth=2, foreground="w")],
                    color="#67000d",
                    fontsize=8,
                    )
    f, ax = plt.subplots(1, 1, subplot_kw=dict(projection=ccrs.Robinson()))

    regionmask.defined_regions.ar6.land.plot(
        ax=ax, # text_kws=text_kws,
        label='abbrev',
        add_label=False,
        add_land=True,
        land_kws=dict(color=color_dark, zorder=0.9),
        add_ocean=True,
        ocean_kws=dict(color=color_light, zorder=0.9),
        line_kws=dict(lw=0.25),
    )
    ax.set_extent([-115, 166, -59, 72], crs=ccrs.PlateCarree())
    mpu.set_map_layout(ax)
    side = 0.01
    plt.subplots_adjust(wspace = 0.075,
                        left = side,
                        right = 1 - side,
                        bottom = 0.02,
                        top = 0.98)
 
    ## Here is the part I added
    ax0 = [None]*len(img)
    ax1=[None]
    ax1_location=[ 7343471.77346599, -4250008.48157433]
    ax2_location=[ -9193471, -3100008.48157433]
    for i,p in enumerate(img):
        if p is not None:
            ax0[i] = inset_axes(ax,
                                width = imgsize,
                                height = imgsize,
                                bbox_transform = ax.transData,
                                bbox_to_anchor=list_arrays[i],
                                loc=position[acro[i]])
            ax0[i].imshow(p, alpha = xalpha)
            ax0[i].set_xticks([])
            ax0[i].set_yticks([])
            for spine in ax0[i].spines.values():
                spine.set_edgecolor('gray')
                spine.set_linewidth(1)


            ax0[i].set_title(acro[i],fontsize=5, loc='right', y=0.7,fontweight="bold")#,labelpad=0)
        if acro[i]=='NZ':
            ax1 = inset_axes(ax,
                             width = imgsize*2.7,
                             height = imgsize*2.7,
                             bbox_transform = ax.transData,
                             bbox_to_anchor=ax1_location,
                             loc=position[acro[i]])
            ax1.imshow(global_pixels, alpha = xalpha)
            a=50
            a1=[30,30+a,30+a*2,30+a*3]
            b=48
            b1=[7.5,7.5+b,7.5+b*2,7.5+b*3,7.5+b*4,7.5+b*5,7.5+b*6]
            for i in range(4):
                for j in range(6):
                    ax1.annotate(actualvalues[i,j], xy=( b1[j],a1[i]),fontsize=4,weight="bold")
            ax1.annotate(actualvalues[0,6], xy=( b1[6],105),fontsize=4,weight="bold")        
            ticks_y = [25, 75, 125, 175]
            labels_y = ['DJF', 'MAM', 'JJA', 'SON']
            ax1.set_yticks(ticks_y, labels_y)
            ticks_x = [10,70,115, 170, 215,260, 310]
            labels_x = ['$T_{mean}$', '$T_{max}$','$T_{min}$','$Pr$','$frq$','$int$','$P99$']
            ax1.set_xticks(ticks_x, labels_x,fontsize=5)
            ax1.set_title('GLOBAL',fontsize=5, loc='right', y=0.9,fontweight="bold")#,labelpad=0)
    ax2 = inset_axes(ax,
                     width = imgsize*3.5,
                     height = imgsize*3.5,
                     bbox_transform = ax.transData,
                     bbox_to_anchor=ax2_location,
                     loc=position[acro[1]])
    ax2.imshow(legenda, alpha = xalpha)
    ax2.axis('off')
    plt.savefig('Figure1.eps',bbox_inches='tight',dpi=800)

plot_map_colored(ocean, land)
