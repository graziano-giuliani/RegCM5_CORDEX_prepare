# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:13:24 2024

@author: Chen Lu
"""

import os
import matplotlib.pyplot as plt
import numpy as np
import skill_metrics as sm

# environment variables
path0 = '.'
#subregs = 'ESB RFE ECA TIB EAS'
#obs = 'APHRO'
#vname = 'pr'
#snum = 'EastAsia'
#conf = 'NoTo'

# domain
domains = ['SouthAmerica', 'EastAsia', 'SouthAsia', 'CentralAmerica', 'Australasia', 
            'NorthAmerica', 'Europe', 'Africa', 'SouthEastAsia']
#domains = ['EastAsia']
#domains = ['SouthEastAsia']
#domains = ['CentralAmerica']
# domains = ['Africa']
# do1mains = ['Europe']

# variable
# vns = ['pr', 'tas']
vns = ['pr', 'tas', 'tasmax', 'tasmin', 'clt']
#vns = ['pr']
#vns = ['tas', 'tasmax', 'tasmin']

# loop over domains
for snum in domains: 
    # loop over variables
    for vname in vns:
        # observations
        if vname == 'pr':
            observations = 'ERA5 CRU CPC GPCC MSWEP'
        else :
            observations = 'ERA5 CRU'
        
        # subregions
        if snum == 'Europe':
            subregs = 'MED NEU WCE'
            if vname == 'pr':
                #observations = 'ERA5 CRU CPC GPCC MSWEP HIRES EOBS'
                observations = 'ERA5 CRU CPC GPCC MSWEP EOBS'
            if vname == 'tas':
                observations = 'ERA5 CRU EOBS'
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
            if vname == 'pr':
                observations = 'ERA5 CRU CPC GPCC MSWEP APHRO CN05.1'
            if vname == 'tas':
                observations = 'ERA5 CRU APHRO CN05.1'
            #observations = 'APHRO'
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
        
        # split
        observations = observations.split(' ')
        
        try:
            os.mkdir(os.path.join(path0,'figures_masked'))
        except:
            pass
        # loop over observations
        for obs in observations:
            # fname
            fname1 = os.path.join(path0,'txt_files',snum + '_' + obs + '_' + vname + '_cc.txt')
            fname2 = os.path.join(path0,'txt_files',snum + '_' + obs + '_' + vname + '_ratio.txt')
            fname3 = os.path.join(path0,'txt_files',snum + '_' + obs + '_' + vname + '_rmse.txt')
            outfname = os.path.join(path0,'figures_masked',snum + '_taylor_' + vname + '_' + obs + '.png')
            
            # read txt file
            cc = np.loadtxt(fname1)
            ratio = np.loadtxt(fname2)
            rmse = np.loadtxt(fname3)
            
            # to matrix
            cc = np.matrix(cc)
            ratio = np.matrix(ratio)
            rmse = np.matrix(rmse)
            
            # correction for APHRO and CN05.1
            #subregs = 'ESB RFE ECA TIB EAS'
            #subregs = 'ECA TIB EAS'
            # 以下条件只能在aphro和cn05.1在观测数据集的最后两个时成立，
            # 不然之后的观测数据集的subregs则都是错的。
            if obs == 'APHRO' or obs == 'CN05.1':
                # subregs = 'ECA TIB EAS'
                # cc = cc[0:3, :]
                # ratio = ratio[0:3, :]
                # rmse = rmse[0:3, :]
                cc[0:2, :] = -1 # <== 强行不画ESB和RFE
            
            #
            nr = cc.shape[0]
            nc = cc.shape[1]
            
            # ## PLOT STYLE ################################################################# #
            
            FONT_FAMILY = 'Times New Roman'
            FONT_SIZE = 12
            
            # specify some styles for the correlation component
            COLS_COR = {
                'grid': '#DDDDDD',
                'tick_labels': '#000000',
                'title': '#000000'
            }
            
            # specify some styles for the standard deviation
            COLS_STD = {
                'grid': '#DDDDDD',
                'tick_labels': '#000000',
                'ticks': '#DDDDDD',
                'title': '#000000'
            }
            
            # specify some styles for the root mean square deviation
            STYLES_RMS = {
                'color': '#AAAADD',
                'linestyle': '--'
            }
            
            #
            #subreg_color = ['#e3342f', '#f6993f', '#ffed4a', '#38c172', '#4dc0b5', 
            #                '#3490dc', '#6574cd', '#9561e2', '#f66d9b']
            subreg_color = ['#cd5582', '#ec6b2d', '#e1be6a', '#40b0a6', '#6d8ef7', 
                            '#a5c8dd', '#6e579a', '#a38e89', '#e89a7a']
            
            season_marker = ['o', '^', 'D', 'v'] #, 's', '*', 'p', 'h']
            
            # ##  ################################################################# #
            #
            # update figures global properties
            #plt.rcParams.update({'font.size': FONT_SIZE, 'font.family': FONT_FAMILY})
            plt.rcParams.update({'font.size': FONT_SIZE})
            plt.figure(num=1, figsize=(4, 3))
            
            sm.taylor_diagram(np.array((1, 2)), 
                              np.array((0, 0)), 
                              np.array((1, 1)), 
                              markersymbol = '.',
                              markercolors = {
                                  "face": '#DDDDDD',
                                  "edge": '#DDDDDD'
                                  },
                              markersize = 9, # 9
                              colscor = COLS_COR,
                              colsstd = COLS_STD,
                              colframe='#DDDDDD',
                              styleOBS = ':',
                              colOBS = '#000000',
                              titleSTD = 'off',
                              titleCOR = 'off',
                              tickRMS = [0.0],
                              tickCOR = [0.1, 0.3, 0.5, 0.7, 0.8, 0.9, 0.95, 0.99, 1.0],
                              showlabelsRMS = 'off',
                              titleRMS = 'off')
                    
            # loop over row/subregion
            for i in range(0, nr):
                # loop over col/season
                for j in range(0, nc):
                    sm.taylor_diagram(np.array((1, ratio[i, j])), 
                                      np.array((0, rmse[i, j])), 
                                      np.array((1, cc[i, j])), 
                                      markersymbol = season_marker[j],
                                      markercolors = {
                                          "face": subreg_color[i],
                                          "edge": subreg_color[i]
                                          },
                                      alpha = 1.0, # 0.5
                                      markersize = 5, # 9
                                      overlay = 'on')
            
            #plt.show()
            # save figure (remove the white paddings)
            plt.savefig(outfname, bbox_inches='tight', pad_inches = 0)
            plt.close()
