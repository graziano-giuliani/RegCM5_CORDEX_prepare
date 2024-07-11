

obs = readAsciiTable("input_Figure6d.txt", 2, "float", (/0,0/))
obslon2 = obs(:,0)
obslat = obs(:,1)

obslon = where(obslon2.lt.0, obslon2+360., obslon2)


xlat = fspan(-60,60,121) 
xlon = fspan(0,360,361)

obser = new((/121,361/),integer)
obser = 0

;dera = new((/121,361/),integer)
;dera = 0

;dmpi = new((/121,361/),integer)
;dmpi = 0

;dnor = new((/121,361/),integer)
;dnor = 0

;dhad = new((/121,361/),integer)
;dhad = 0

;jlat = ind_nearest_coord (eralat, xlat, 0)
;ilon = ind_nearest_coord (eralon, xlon, 0)

jlat2 = ind_nearest_coord (obslat, xlat, 0)
ilon2 = ind_nearest_coord (obslon, xlon, 0)

;jlat0 = ind_nearest_coord (mpilat, xlat, 0)
;ilon0 = ind_nearest_coord (mpilon, xlon, 0)

;jlat1 = ind_nearest_coord (hadlat, xlat, 0)
;ilon1 = ind_nearest_coord (hadlon, xlon, 0)

;jlat3 = ind_nearest_coord (norlat, xlat, 0)
;ilon3 = ind_nearest_coord (norlon, xlon, 0)

;do k=0,(dimsizes(jlat))-1
;
;   dera(jlat(k),ilon(k)) = (dera(jlat(k),ilon(k)))+1
;
;end do

;delete(k)

do k=0,(dimsizes(jlat2))-1

   obser(jlat2(k),ilon2(k)) = (obser(jlat2(k),ilon2(k)))+1

end do

;delete(k)
;
;do k=0,(dimsizes(jlat0))-1
;
;   dmpi(jlat0(k),ilon0(k)) = (dmpi(jlat0(k),ilon0(k)))+1
;   
;end do
;
;delete(k)
;
;do k=0,(dimsizes(jlat1))-1
;
;   dhad(jlat1(k),ilon1(k)) = (dhad(jlat1(k),ilon1(k)))+1
;
;end do
;
;delete(k)
;
;do k=0,(dimsizes(jlat3))-1
;
;   dnor(jlat3(k),ilon3(k)) = (dnor(jlat3(k),ilon3(k)))+1
;   
;end do
;
;delete(k)
;
;ensh = (dnor + dhad + dmpi)/3. 
;ensh!1="lon"
;ensh!0="lat"
;ensh&lat=xlat
;ensh&lon=xlon
;ensh&lat@units="degrees_north"
;ensh&lon@units="degrees_east"
;
;dera!1="lon"
;dera!0="lat"
;dera&lat=xlat
;dera&lon=xlon
;dera&lat@units="degrees_north"
;dera&lon@units="degrees_east"
;
obser!1="lon"
obser!0="lat"
obser&lat=xlat
obser&lon=xlon
obser&lat@units="degrees_north"
obser&lon@units="degrees_east"

;-----------------------------------------------------

wks = gsn_open_wks("pdf" ,"map_tcdensity_global-RegCM5-EAScut")                ; open a ps file 
gsn_define_colormap(wks,"WhiteBlueGreenYellowRed")        ; choose colormap 
plot = new(3,graphic)
 
res                  = True     ; plot mods desired 
res@gsnDraw          = False              ; Don't draw plot
res@gsnFrame         = False

res@cnFillOn         = True               ; color Fill 
res@cnFillMode       = "RasterFill"       ; Raster Mode
res@cnLinesOn        = False             ; Turn off contour lines
res@mpFillOn         = False
res@cnLineLabelsOn   = False              ; no contour labels
res@cnInfoLabelOn    = False              ; no contour info label

res@mpDataBaseVersion      = "MediumRes"        ; better map outlines
res@pmTickMarkDisplayMode  = "Always"           ; turn on tickmarks

;res@gsnSpreadColors  = True     ; use full range of color map 

res@gsnStringFontHeightF      = 0.018              ; smaller title
res@gsnLeftStringOrthogonalPosF = -0.005              ;
res@gsnRightStringOrthogonalPosF = -0.005
res@tmXBLabelFontHeightF = 0.016                 ; resize tick labels
res@tmYLLabelFontHeightF = 0.016
 
res@gsnAddCyclic     = False    ; data already has cyclic point 
res@tmYROn           = False            ; Turn off right tickmarks.
res@tmXTOn           = False            ; Turn off top tickmarks.

res@mpLimitMode          = "LatLon"           ; choose region of map  
res@mpMinLatF            =   -60.      ; range to zoom in on 
res@mpMaxLatF            =   60. 
res@mpMinLonF            =    0. 
res@mpMaxLonF            =  360. 

res@mpGridAndLimbOn        = False               ; turn on grid lines

res@lbOrientation =   "vertical"
res@lbLabelFontHeightF   = 0.02

res@cnLevelSelectionMode   = "ExplicitLevels"
;res@cnLevels               = (/0.001,5,10,15,20,25,30,35,40,45,50/)
res@cnLevels               = (/1,2,3,4,5,6,7,8,9,10,15,20,25,30/)
;res@cnLevelSelectionMode = "ManualLevels"   ; manually specify contour levels
;res@cnMinLevelValF       = 0.             ; min level
;res@cnMaxLevelValF       = 60.             ; max level
;res@cnLevelSpacingF      =  5.             ; contour interval
res@lbLabelBarOn        = False

res@gsnLeftString   = "Tropical cyclone track density RegCM5 (2000-2009)"
plot(0) = gsn_csm_contour_map_ce(wks,obser, res) 

;res@gsnLeftString   = "Tropical cyclone track density RegCM ERA-INT (2000-2009)"
;plot(1) = gsn_csm_contour_map_ce(wks,dera, res)

;res@gsnLeftString   = "Tropical cyclone track density RegCM ensemble (2000-2009)"
;plot(2) = gsn_csm_contour_map_ce(wks,ensh, res)

;---------------------------------------------
; create panel
;---------------------------------------------
  pres                  = True
  pres@gsnPaperOrientation = "auto"
  pres@gsnMaximize = True
  pres@gsnPanelLabelBar    = True                ; add common colorbar
  pres@lbOrientation        = "Horizontal"   ; vertical label bar
;  gsn_panel(wks,plot,(/3,1/),pres)
  gsn_panel(wks,plot,(/1,1/),pres)
 
