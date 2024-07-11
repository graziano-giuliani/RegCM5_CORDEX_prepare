# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 09:40:19 2023

@author: Chen Lu
"""

import os
import numpy as np
import matplotlib.pyplot as plt

# environment variables
path0 = '.'
# subregs = 'ESB RFE ECA TIB EAS'
# subregs = 'ESB'
# ys = '2000-2009'
# snum = 'EastAsia'

# arrays
domains = ['SouthAmerica', 'EastAsia', 'SouthAsia', 'CentralAmerica', 'Australasia', 'NorthAmerica', 'Europe', 'Africa', 'SouthEastAsia']
#domains = ['CentralAmerica']
#domains = ['Europe']
#domains = ['Africa']
#domains = ['SouthEastAsia']

# index for mask
# [tas, tasmax, tasmin], [pr], [pr_frq], [pr_int], [p99]
idx = [[0, 1, 2], [3], [4], [5], [6]]
vns = [8, 5, 45, 2, 20]
cmaps = ['RdBu_r', 'BrBG', 'BrBG', 'BrBG', 'BrBG']
nid = len(idx)

# loop through domains
for snum in domains: 
    ys = '2000-2009'
    # subregions
    if snum == 'Europe':
        subregs = 'MED NEU WCE'
        ys = '1980-2010'
    if snum == 'NorthAmerica': 
        subregs = 'NWN NEN WNA CNA ENA NCA'
    if snum == 'CentralAmerica':
        subregs = 'NCA SCA CAR'
    if snum == 'SouthAmerica':
        subregs = 'NWS NSA SAM NES SES SWS SSA'
    if snum == 'Africa':
        subregs = 'SAH WAF CAF NEAF SEAF ARP WSAF ESAF MDG'
    if snum == 'SouthAsia':
        subregs = 'WCA ECA TIB SAS ARP'
    if snum == 'EastAsia':
        subregs = 'ESB RFE ECA TIB EAS'
    if snum == 'SouthEastAsia':
        subregs = 'SEA'
    if snum == 'Australasia':
        subregs = 'NAU CAU EAU SAU NZ'
    if snum == 'Mediterranean':
        subregs = 'CARPAT SPAIN02 EURO4M COMEPHORE RdisaggH GRIPHO'
    if snum == 'Medi':
        subregs = 'CARPAT EURO4M COMEPHORE GRIPHO'
    if snum == 'Medi3':
        subregs = 'CARPAT SPAIN02 EURO4M COMEPHORE RdisaggH GRIPHO'
    if snum == 'SEEurope':
        subregs = 'COMEPHORE GRIPHO'
        
    # fnames
    try:
        os.mkdir(os.path.join(path0,'plots_v1_v2'))
    except:
        pass
    subregs = subregs.split(' ')
    for subreg in subregs: 
        print('plotting '+snum)
        # fname
        ofname = os.path.join(path0,'txt_files',snum + '_pixels_' + subreg + '_obs_' + ys + '.txt')
        mfname = os.path.join(path0,'txt_files',snum + '_pixels_' + subreg + '_mod_' + ys + '.txt')
        outfname = os.path.join(path0,'plots_v1_v2',snum + '_pixels_' + subreg + '_' + ys + '.png')
    
        # read txt file
        ao = np.loadtxt(ofname)
        am = np.loadtxt(mfname)
    
        # calculate bias
        ar = am - ao
        # print(ar)
        nrow = ar.shape[0]
        ncol = ar.shape[1]
    
        # postproc extreme indices
        col_ext = [7]
        for c in col_ext:
            ar[1:nrow, c-1] = ar[0, c-1]
        
        # pixel plot
        fig, ax = plt.subplots()
        
        # loop over idx
        for i in range(0, nid):
            ids = np.array(idx[i])
            m = np.ones_like(ar)
            m[:, ids] = 0
            arm = np.ma.masked_array(ar, m)
            # plot
            p0 = ax.imshow(arm, cmap = cmaps[i])
            p0.set_clim(vmin = -vns[i], vmax = vns[i])
        
        # remove axis ticks
        plt.axis('off')
    
        # save figure (remove the white paddings)
        plt.savefig(outfname, bbox_inches='tight', pad_inches = 0)
        plt.close()
