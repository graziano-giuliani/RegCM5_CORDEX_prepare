#!/usr/bin/env python
# coding: utf-8

import sys
import glob

light_blue = "#f2f8fa"
dark_blue = "#bde0ef"
dark_red = "#ffd7a0"
light_red = "#fff3df"

ocean = light_blue
land = light_red

imgpth = './images'
imgsize = 0.4 # inches
xalpha = 1.0 # larger less transparent

base = sys.argv[1]
season = base[-3:]
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

gp = 'IPCC-WGI-reference-regions-v4.shp'
regionshapes = gpd.read_file(gp)

remap = regionshapes.loc[lambda s: s.Type != 'Ocean'].to_crs('EPSG:4326')

## Change the EPSG in geoconv to adjust the projection conversion
geoconv = gpd.GeoDataFrame.to_crs(remap, ccrs.Robinson())
centers = np.asarray([ x for x in geoconv.centroid ])
list_arrays = [ np.array((geom.xy[0][0], geom.xy[1][0])) for geom in centers ]

img = [ ]
acro = [ ]
legenda=Image.open('exemplo_clw.png')


for rcod in remap.Acronym:
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
        list_arrays[i]=[-7760832.0632548, -651195.07906457]
    if acro[i]=='SWS':
        list_arrays[i]=[-6743568.58844822, -3769606.14102048]
    if acro[i]=='SCA':
        list_arrays[i]=[-8300682.06862156,  1180692.87014061]
    if acro[i]=='MDG':
        list_arrays[i]=[ 4843471.77346599, -2108565.78658505]
    if acro[i]=='WSAF':
        list_arrays[i]=[ 1118407.23574649, -2446797.83554867]
    if acro[i]=='CAR':
        list_arrays[i]=[-6537306.24237058,  1976177.2895233 ]
    if acro[i]=='ENA':
        list_arrays[i]=[-6184294.93791933,  4213911.70882605]
    if acro[i]=='CNA':
        list_arrays[i]=[-8139332.99902502,  4598858.07632454]
    if acro[i]=='NES':
        list_arrays[i]=[-3444123.66405135, -1066358.04223574]
    if acro[i]=='SES':
        list_arrays[i]=[-5057972.72197529, -3258362.44165917]
    if acro[i]=='SAS':
        list_arrays[i]=[7373713.32084525, 1831886.75032472] 
    if acro[i]=='WCE':
        list_arrays[i]=[2856997.26683688, 5566938.45482863]
    if acro[i]=='WCA':
        list_arrays[i]=[5063598.69849336, 4422035.47609929]
    if acro[i]=='ARP':
        list_arrays[i]=[4343154.34063271, 2798619.0420713 ]
    if acro[i]=='NEAF':
        list_arrays[i]=[3686153.84678033 , 1258299.97365805]
    if acro[i]=='SAH':
        list_arrays[i]=[ 1718178.94254739, 2364718.27256082]
    if acro[i]=='NAU':
        list_arrays[i]=[13387862.03462767, -1103077.86640377]
    if acro[i]=='SAU':
        list_arrays[i]=[11841419.47834757, -5009798.35032037]
    if acro[i]=='NZ':
        list_arrays[i]=[14558293.42422992, -4750008.48157433]
    if acro[i]=='ECA':
        list_arrays[i]=[8115728.57968411, 3394961.87852045]
    if acro[i]=='SAS':
        list_arrays[i]= [6873713.32084525, 1531886.75032472]
    if acro[i]=='TIB':
        list_arrays[i]= [8370076.67336481, 2964997.51237719]
    if acro[i]=='NCA':
        list_arrays[i]= [-9663098.01701045,  2332197.64801253]
    if acro[i]=='NEN':
        list_arrays[i]= [-5900725.08301593 , 6262936.12622698]
    if acro[i]=='NWN':
        list_arrays[i]=[-9703908.5934842,   6406014.33259522]
    if acro[i]=='SAM':
        list_arrays[i]=[-5663984.28704498, -1869859.26566404]
    if acro[i]=='SES':
        list_arrays[i]=[-4057972.72197529, -3258362.44165917]
    if acro[i]=='ESAF':
        list_arrays[i]=[ 3021548.90761941, -2687751.08830015]
    if acro[i]=='SEAF':
        list_arrays[i]=[3467216.72745506, -611269.857155  ]
    if acro[i]=='ARP':
        list_arrays[i]=[4843154.34063271, 2398619.0420713]
    if acro[i]=='NEAF':
        list_arrays[i]=[3186153.84678033, 1258299.97365805]
    if acro[i]=='SSA':
        list_arrays[i]=[-4953559.0192668, -5181998.4810157]
    if acro[i]=='MED':
        list_arrays[i]=[1320185.72077745, 4297719.46626139]
    if acro[i]=='NEU':
        list_arrays[i]=[ 819993.02441789, 6274297.76319928]
    if acro[i]=='SEA':
       list_arrays[i]=[10420476.34931033,   369006.20019558]
        


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
    ax1_location=[ 8643471.77346599, -3750008.48157433]
    for i,p in enumerate(img):
        if p is not None:
            ax0[i] = inset_axes(ax,
                                width = imgsize,
                                height = imgsize,
                                bbox_transform = ax.transData,
                                bbox_to_anchor=list_arrays[i],
                                loc=position[acro[i]])
            ax0[i].imshow(p, alpha = xalpha)
            ax0[i].axis('off')
            ax0[i].set_title(acro[i],fontsize=4, loc='right', y=0.8,fontweight="bold")#,labelpad=0)
        if acro[i]=='NWN':
            ax1 = inset_axes(ax,
                             width = imgsize*1.75,
                             height = imgsize*1.75,
                             bbox_transform = ax.transData,
                             bbox_to_anchor=ax1_location,
                             loc=position[acro[i]])
            ax1.plot(300, 70, 'bo', markersize=2)
            ax1.plot(300, 170, 'ro', markersize=2)
            ax1.plot(300, 270, color='lime', marker='o',markersize=2)
            ax1.imshow(legenda, alpha = xalpha)
            ticks_y = [20,180,340,500,660,820]
            labels_y = [0, 200, 400, 600,800,1000]
            ax1.set_yticks(ticks_y, labels_y,fontsize=5)
            a=133
            ticks_x = [30,30+a,30+2*a,30+3*a,30+4*a,30+5*a,30+6*a]
            labels_x = [0,5,10,15,20,25,30]
            
            ax1.set_xticks([])#ticks_x, labels_x,fontsize=5)
            ax1.set_xlabel('Cloud Liquid Water (mg/kg)',fontsize=5,labelpad=2,weight="bold")
            ax1.set_ylabel('Pressure level (hPa)',fontsize=5,labelpad=0,weight="bold")
            ax1.annotate('ERA 5', xy=(350, 95),fontsize=5)
            ax1.annotate('RegCM5', xy=(350, 195),fontsize=5)
            ax1.annotate('RegCM4', xy=(350, 295),fontsize=5)
            if season=='DJF':
                ax1.annotate(season, xy=(40, 790),fontsize=8, bbox=dict(facecolor='white', edgecolor='black', pad=2.0))
            else:
                ax1.annotate(season, xy=(40, 790),fontsize=8, bbox=dict(facecolor='white', edgecolor='black', pad=2.0))
    plt.savefig(base+'.png',bbox_inches='tight',dpi=800)

plot_map_colored(ocean, land)
