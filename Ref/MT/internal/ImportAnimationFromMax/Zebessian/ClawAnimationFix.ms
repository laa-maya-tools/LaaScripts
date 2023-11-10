fn clawAnimationFix =
(
	local infoChar = getNodeByName "zebesian_infoChar"
	local finger1 = getNodeByName"zebesian_bip_L_Finger0"
	local finger2 = getNodeByName"zebesian_bip_L_Finger1"
	local claw1 = getNodeByName "zebesian_bip_L_Finger0_Xtra"
	local claw2 = getNodeByName "zebesian_bip_L_Finger1_Xtra"
	
	format "* Zebessian Claw Fix *\n"
	if infoChar == undefined  then
	(
		format "Unable to find Zebessian InfoChar!\n"
		return False
	)
	if finger1 == undefined or finger2 == undefined then
	(
		format "Unable to find Zebessian claw controls!\n"
		return False
	)
	if claw1 == undefined or claw2 == undefined then
	(
		format "Unable to find Zebessian claw extra controls!\n"
		return False
	)
	
	local animPresets = (infoChar.GetAllAnimPresetStruct()).animPresets
	
	local bip = claw1.controller.rootNode.controller
	local i = 0
	while i <= biped.numLayers bip do
	(
		biped.setCurrentLayer bip i
		biped.setLayerActive bip i true
		
		local claw1KeyTimes = for key in  claw1.controller.keys collect key.time
		local claw2KeyTimes = for key in  claw2.controller.keys collect key.time
		if claw1KeyTimes.count > 0 or claw2KeyTimes.count > 0 then
		(
			local claw1Transforms = for keyTime in claw1KeyTimes collect at time keyTime claw1.transform
			local claw2Transforms = for keyTime in claw2KeyTimes collect at time keyTime claw2.transform
			
			local currentLayerName = biped.getLayerName bip i
			local clawLayerName = currentLayerName + "_claws"
			
			biped.deleteKeys claw1.controller
			biped.deleteKeys claw2.controller
			
			biped.createLayer bip (i + 1) clawLayerName
			
			for j = 1 to claw1KeyTimes.count do at time claw1KeyTimes[j] with animate on
				finger1.transform = claw1Transforms[j]
			for j = 1 to claw2KeyTimes.count do at time claw2KeyTimes[j] with animate on
				finger2.transform = claw2Transforms[j]
			
			for animPreset in animPresets where (findItem animPreset.activeLayers currentLayerName) != 0 do
			(
				append animPreset.activeLayers clawLayerName
				infoChar.SetAnimPresetByStruct animPreset
			)
			
			if i != 0 then
				biped.setLayerActive bip i false
			i += 1
		)
		
		if i != 0 then
			biped.setLayerActive bip i false
		i += 1
	)
	
	format "Zebessian Claw Fix Success\n"
	return True
)

clawAnimationFix()