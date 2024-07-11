load "trimPNG.ncl"

begin
	;-- env
	path0 = getenv("path0")
	ilev = getenv("plev")
	fig_format = getenv("fig_format")

	;-- check plev
	plev_opt = (/100, 150, 200, 250, 300, 400, 500, 600, 700, 850, 925, 1000/)
	if_plev = ind(plev_opt .eq. ilev)
	if ismissing(if_plev)
		print("plev options: 100, 150, 200, 250, 300, 400, 500, 600, 700, 850, 925, 1000.")
		return
	end if

	;-- plotting
	outn   = path0+"/Wind_"+ilev+"hPa_v5"
	wks = gsn_open_wks(fig_format,outn)
	plots = new(4,graphic)
	tstr = "abcdefg"
	tstr := stringtochar(tstr)

	;-- season
	season = (/"DJF", "JJA"/)
	ns = dimsizes(season)
	
	;-- loop over season
	do i = 0, ns-1

		;--
		s = season(i)

		;-- range				  850				500						200
		if s .eq. "JJA"
			vmax1 = (/15.0, 15.0, 10.0, 26.0, 30.0, 20.0, 60.0, 75.0, 80.0, 30.0, 75.0, 50.0/)
			vmin1 = (/ 1.0,  1.0,  1.0,  2.0,  2.0,  2.0,  2.5,  5.0,  5.0,  2.5,  5.0,  5.0/)
			vref = (/ 10.0, 10.0, 20.0, 15.0, 20.0, 35.0, 30.0, 45.0, 45.0, 60.0, 45.0, 35.0/)
		else if s .eq. "DJF"
			vmax1 = (/15.0, 15.0, 10.0, 26.0, 30.0, 20.0, 60.0, 75.0, 80.0, 30.0, 75.0, 50.0/)
			vmin1 = (/ 1.0,  1.0,  1.0,  2.0,  2.0,  2.0,  3.0,  5.0,  5.0,  2.5,  5.0,  5.0/)
			vref = (/ 10.0, 10.0, 20.0, 15.0, 20.0, 35.0, 30.0, 45.0, 45.0, 60.0, 45.0, 35.0/)
		else
			vmax1 = (/15.0, 15.0, 10.0, 26.0, 30.0, 45.0, 60.0, 75.0, 80.0, 80.0, 75.0, 50.0/)
			vmin1 = (/ 1.0,  1.0,  1.0,  2.0,  2.0,  3.0,  5.0,  5.0,  5.0,  5.0,  5.0,  5.0/)
			;vref = (/10.0, 10.0, 5.0, 15.0, 20.0, 25.0, 30.0, 45.0, 45.0, 50.0, 45.0, 35.0/)
		end if
		end if
		vstp1 = vmin1
		;vref = 4.0 ; 5.0

		;-- fname
		uofname = path0+"/../data/ERA5_uwnd_RegCM5_"+s+"_mean.nc"
		vofname = path0+"/../data/ERA5_vwnd_RegCM5_"+s+"_mean.nc"
		urfname = path0+"/../data/Global_ua_RegCM5_"+s+"_mean.nc"
		vrfname = path0+"/../data/Global_va_RegCM5_"+s+"_mean.nc"
		
		;-- read file
		uof = addfile(uofname, "r")
		vof = addfile(vofname, "r")
		urf = addfile(urfname, "r")
		vrf = addfile(vrfname, "r")

		;-- read level
		level = uof->level
		lev_id2 = ind(level .eq. ilev)
		plev = urf->plev
		lev_id = ind(plev .eq. ilev)
		;-- read ua va
		uo = uof->ua(0, lev_id2, :, :)
		vo = vof->va(0, lev_id2, :, :)
		ur = urf->ua(lev_id, :, :)
		vr = vrf->va(lev_id, :, :)

		;-- mask out missing data from RCM
		uo = where(ismissing(ur), uo@_FillValue, uo)
		vo = where(ismissing(vr), vo@_FillValue, vo)

		;-- calc wind speed
		spo = wind_speed(uo, vo)
		;uo = uo/spo
		;vo = vo/spo
		spr = wind_speed(ur, vr)
		;ur = ur/spr
		;vr = vr/spr

		;***********************
		; plot
		;***********************
		res            = True                    ; plot mods desired
		res@gsnDraw             = False              ; don't draw yet
		res@gsnFrame            = False              ; don't advance frame yet

	;	res@tfDoNDCOverlay         = True      ; do not transform
		res@mpFillOn               = False

		res@mpGeophysicalLineColor = "black"     ; color of continental outlines
		res@mpPerimOn              = True      ; draw box around map
		res@mpGridLineDashPattern  = 5         ; lat/lon lines as dashed

		res@gsnAddCyclic           = True     ; regional data don't add

		res@pmTickMarkDisplayMode  = "Always"  ;
		res@mpGridAndLimbOn        = False               ; turn on grid lines

		res@lbLabelBarOn        = False ; True ; False
		res@lbBoxMinorExtentF = 0.15
	;	res@lbBoxMajorExtentF = 1.0
		res@lbLabelFontHeightF   = 0.015
	;	res@lbTitleFontHeightF   = 0.012             ; make title smaller
	;	res@lbTitleString    = "m/s"
	;	res@lbTitlePosition      = "Right"
	;	res@lbTitleDirection = "Across"
		res@lbTopMarginF = -0.05

		res@tmYROn = False            ; Turn off right tickmarks.
		res@tmXTOn = False            ; Turn off top tickmarks.
		res@tmYLOn = False
		res@tmXBOn = False

	;	offsetR = 0.010
	;	offsetL = 0.00
	;	offsetRe = offsetR
	;	offsetLe = offsetR
	;	res@gsnLeftStringOrthogonalPosF  = offsetL
	;	res@gsnRightStringOrthogonalPosF = offsetR

	;	res@sfXArray = lon
	;	res@sfYArray = lat

		vcres                     = res
		vcres@vcLevelSelectionMode     = "ManualLevels"
	;	vcres@lbLabelStride       = 2         ; plot every other colar bar label
		vcres@vcRefAnnoOrthogonalPosF = -1.0
		vcres@vcRefLengthF            = 0.050            ; ref vec length
		vcres@vcGlyphStyle            = "CurlyVector" ; "LineArrow" ; 
		vcres@vcMinDistanceF          = 0.010 ; 0.008
		vcres@vcLineArrowThicknessF = 1.7 ; 1.5; 1;2
		vcres@vcLineArrowHeadMaxSizeF = 0.004 ; Default: 0.05 (LineArrow), 0.012 (CurlyVector)
		vcres@vcLineArrowHeadMinSizeF = 0.004 ; Default: 0.005  
		vcres@vcRefAnnoOn = False

		;-- colormap, reference vector
		cmap = read_colormap_file("precip3_16lev")
		vcres@vcLevelPalette = cmap(1:16, :)
		vcres@vcMinLevelValF           = vmin1(lev_id)
		vcres@vcMaxLevelValF           = vmax1(lev_id)
		vcres@vcLevelSpacingF          = vstp1(lev_id)
		vcres@vcRefMagnitudeF         = vref(lev_id)              ; make vectors larger

		;-- strings
		vcres@gsnLeftString     = ""
		vcres@gsnRightString    = "" ; "m/s"

		;-- plot ERA5
		if s .eq. "DJF"
			pid = 0
		else
			pid = 2
		end if
		vcres@gsnCenterString = "("+tstr(pid)+") Global " + ilev + " hPa Wind " + s + " ERA5"
		plots(pid)=gsn_csm_vector_scalar_map_ce(wks,uo,vo,spo,vcres)

		;-- plot RegCM5
		if s .eq. "DJF"
			pid = 1
		else
			pid = 3
		end if
		vcres@gsnCenterString = "("+tstr(pid)+ ") Global " + ilev + " hPa Wind " + s + " RegCM5"
		plots(pid)=gsn_csm_vector_scalar_map_ce(wks,ur,vr,spr,vcres)
	end do

	;---------------------------------------------
	; create panel
	;---------------------------------------------
	pres                      = True
	pres@gsnPanelLabelBar    = True
	pres@lbLabelFontHeightF   = 0.01
	pres@lbTitleFontHeightF   = 0.01             ; make title smaller
	pres@lbTitleString    = "m/s"
	pres@lbTitlePosition      = "Right" ; "Center"
	pres@lbTitleDirection = "Across"
	pres@gsnMaximize = True

	gsn_panel(wks,plots,(/2, 2/),pres)
	trimPNG(outn+"."+fig_format)
end
