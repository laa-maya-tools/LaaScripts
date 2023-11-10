global coordTags = #("X", "Y", "Z")

global remaps = #(
	#("Samus_C01_Xtra_Cannon", "cannon_R0_ctl"),
	#("Samus_L01_Xtra_Elbow_CTL", "arm_L0_mid_ctl"),
	#("Samus_L01_Xtra_Knee_CTL", "leg_L0_mid_ctl"),
	#("Samus_R01_Xtra_Elbow_CTL", "arm_R0_mid_ctl", #(-1, -2, 3)),
	#("Samus_R01_Xtra_Knee_CTL", "leg_R0_mid_ctl"),
	#("Samus_DC_FXMuzzle_Weapon_CTL", "DC_FXMuzzle_CTL"),
	
	#("zebesian_bip_L_Thigh", "leg_L1_fk0_ctl"),
	#("zebesian_bip_L_Calf", "leg_L1_fk1_ctl"),
	#("zebesian_bip_L_Foot", "leg_L1_fk2_ctl"),
	#("zebesian_bip_L_Toe0", "foot_L1_fk0_ctl"),
	#("zebesian_bip_L_Toe01", "Toe_L2_fk0_ctl", #(1, -2, -3)),
	#("zebesian_bip_L_Toe02", "Toe_L3_fk0_ctl", #(1, -2, -3)),
	#("zebesian_bip_R_Thigh", "leg_R1_fk0_ctl"),
	#("zebesian_bip_R_Calf", "leg_R1_fk1_ctl"),
	#("zebesian_bip_R_Foot", "leg_R1_fk2_ctl"),
	#("zebesian_bip_R_Toe0", "foot_R1_fk0_ctl"),
	#("zebesian_bip_R_Toe01", "Toe_R2_fk0_ctl", #(-1, 2, -3)),
	#("zebesian_bip_R_Toe02", "Toe_R3_fk0_ctl", #(-1, 2, -3)),
	#("zebesian_bip_C_Collar", "collar_C0_ctl"),
	#("zebesian_DC_Shot", "DC_Shot_CTL"),
	#("zebesian_DC_FXMuzzle", "DC_FXMuzzle_CTL")
)

global globalProcessScripts = #(
	"\\GAME\\Tools\\MayaTools\\internal\\ImportAnimationFromMax\\Zebessian\\ClawAnimationFix.ms"
)

-- Logging struct to record messages
struct MessageLogger
(
	messages = #(),
	infos = #(),
	errors = #(),
	warnings = #(),
	
	fn logInfo message =
	(
		format message
		format "\n"
		
		logSystem.logEntry message info:true
		
		append this.infos message
		append this.messages message
	),
	
	fn logWarning message =
	(
		format "WARNING: "
		format message
		format "\n"
		
		logSystem.logEntry message warning:true
		
		append this.warnings message
		append this.messages message
	),
	
	fn logError message =
	(
		format "ERROR: "
		format message
		format "\n"
		
		logSystem.logEntry message error:true
		
		append this.errors message
		append this.messages message
	),
	
	fn clearLogger =
	(
		messages = #()
		infos = #()
		errors = #()
		warnings = #()
	),
	
	fn appendLogger otherLogger =
	(
		append this.messages otherLogger.messages
		append this.infos otherLogger.infos
		append this.errors otherLogger.errors
		append this.warnings otherLogger.warnings
	)
)
global logger = MessageLogger()

-- Checks if an object is a biped node or not.
fn IsBipedObject obj =
(
	bipedControllerClasses = #(BipSlave_Control, Vertical_Horizontal_Turn, Footsteps)
	(finditem  bipedControllerClasses (classof obj.controller)) !=0
)

-- Checks if an object is a biped prop.
fn IsProp obj =
(
	obj == (biped.getNode obj.controller #prop1) or obj == (biped.getNode obj.controller #prop2) or obj == (biped.getNode obj.controller #prop3)
)

-- Returns the parent of the node. If the node has a LinkConstraint, returns the node it's linked to.
fn GetNodeParent node =
(
	if classOf node.controller == Link_Constraint then
	(
		if node.controller.getNumTargets() > 0 then
			return node.controller.getNode 1
		else
			return undefined
	)
	else if classOf node.controller == BipSlave_Control  and IsProp node then
	(
		if (biped.getCurrentLayer node.controller) != 0 then
			biped.setCurrentLayer node.controller 0
		
		if node.controller.keys.count == 0 then
			return undefined
		else
		(
			local posParent = unsupplied
			local rotParent = unsupplied
			for i = 1 to node.controller.keys.count do
			(
				local key = biped.getKey node.controller i
				local p = case key.posSpace of
				(
					0: undefined
					1: biped.getNode node.controller #vertical
					2: biped.getNode node.controller #rArm link:4
					3: biped.getNode node.controller #lArm link:4
				)
				local r = case key.rotSpace of
				(
					0: undefined
					1: biped.getNode node.controller #vertical
					2: biped.getNode node.controller #rArm link:4
					3: biped.getNode node.controller #lArm link:4
				)
				if posParent != unsupplied and posParent != p then
					logger.logWarning ("Inconsistent prop space for " + node.name + ": position space was " + posParent as string +", but is " + p as string + " at frame " + key.time as string)
				else
					posParent = p
				if rotParent != unsupplied and rotParent != r then
					logger.logWarning ("Inconsistent prop space for " + node.name + ": rotation space was " + rotParent as string +", but is " + r as string + " at frame " + key.time as string)
				else
					rotParent = r
			)
			return #(posParent, rotParent)
		)
	)
	else
	(
		return node.parent
	)
)

-- Gets the keyable subcontroller.
fn GetKeyableController controller listClass:undefined =
(
	while classOf controller == listClass and controller.count > 0 do
		controller = controller[controller.active].controller
	while classOf controller == Float_Limit do 
		controller = controller.GetLimitedControl()
	controller
)

-- Gets all the keys from an object.
fn GetNodeKeys obj =
(
	if IsBipedObject obj then
		if classOf obj.controller == Vertical_Horizontal_Turn then
		(
			local keys = #()
			
			join keys obj.controller.horizontal.controller.keys
			join keys obj.controller.vertical.controller.keys
			join keys obj.controller.turning.controller.keys
			
			keys
		)
		else
			obj.controller.keys
	else
	(
		local keys = #()
		
		local posController = GetKeyableController obj.position.controller listClass:Position_List
		join keys posController.keys
		
		local rotController = GetKeyableController obj.rotation.controller listClass:Rotation_List
		join keys rotController.keys
		
		local scaController = GetKeyableController obj.scale.controller listClass:Scale_List
		join keys scaController.keys
		
		keys
	)
)

-- Checks if an object has a transformation key at the specified time.
fn HasKeyAtTime obj t =
(
	if IsBipedObject obj then
		if classOf obj.controller == Vertical_Horizontal_Turn then
		(
			if (getKeyIndex obj.controller.vertical.controller t) != 0 then
				true
			else if (getKeyIndex obj.controller.horizontal.controller t) != 0 then
				true
			else if (getKeyIndex obj.controller.turning.controller t) != 0 then
				true
			else
				false
		)
		else
			(getKeyIndex obj.controller t) != 0
	else
	(
		if (getKeyIndex (GetKeyableController obj.position.controller listClass:Position_List) t) != 0 then
			true
		else if (getKeyIndex (GetKeyableController obj.rotation.controller listClass:Rotation_List) t) != 0 then
			true
		else if (getKeyIndex (GetKeyableController obj.scale.controller listClass:Scale_List) t) != 0 then
			true
		else
			false
	)
)

-- Returns the ikBlend alue of the provided limb or undefined if the lim is not keyed on the current frame.
fn GetIKState bipedLimb useDefaultValueInsteadOfUndefined:false =
(
	if bipedLimb == undefined then
		undefined
	else
	(
		local keyIndex = getKeyIndex bipedLimb.controller currentTime
		if keyIndex != 0 then
			(biped.getKey bipedLimb.controller keyIndex).ikBlend
		else if useDefaultValueInsteadOfUndefined then
			0.0	-- The default value is FK
		else
			undefined
	)
)

-- Converts a point into an array with 3 elements.
fn PointToArray p =
(
	#(p.x, p.y, p.z)
)

-- Utility function to turn single values or arrays into strings.
fn AsString val =
(
	if val == undefined then
		""
	else if classOf val == Point3 then
		"[" + (val.x as string) + "," + (val.y as string) + "," + (val.z as string) + "]"
	else if classOf val == color then
		"[" + (val.r as string) + "," + (val.g as string) + "," + (val.b as string) + "]"
	else
		val as string
)

-- Expands the animation range to the one determined by the minimum and maximum key times of the provided nodes.
fn ExpandAnimationRangeToAnimation objs =
(
	local start = undefined
	local end = undefined
	for obj in objs do
	(
		local keys = GetNodeKeys obj.node
		if keys.count > 0 then
		(
			local keyTimes = for key in keys collect key.time
			local earliestKeyTime = amin keyTimes
			local latestKeyTime = amax keyTimes
			if start== undefined or start > earliestKeyTime then
				start = earliestKeyTime
			if end== undefined or end < latestKeyTime then
				end = latestKeyTime
		)
	)
	if start != undefined and end != undefined then
	(
		if start == end then
			end += 1
		animationrange = interval start end
	)
)

-- Stores all the information for a keyframe's tangent.
struct KeyTangent
(
	inTangentType,
	outTangentType,
	inTangent = undefined,
	outTangent = undefined,
	inTangentLength = undefined,
	outTangentLength = undefined,
	
	fn invertTangent =
	(
		if inTangent != undefined then
			inTangent *= -1
		if outTangent != undefined then
			outTangent *= -1
	),
	
	fn createFromBezier key controller keyIndex factor:1.0 =
	(
		local tangents = if classOf key.inTangent == Point3 then
			for i=1 to 3 collect KeyTangent key.inTangentType key.outTangentType key.inTangent[i] key.outTangent[i] key.inTangentLength[i] key.outTangentLength[i]
		else
			#(KeyTangent key.inTangentType key.outTangentType key.inTangent key.outTangent key.inTangentLength key.outTangentLength)
		
		for tangent in tangents do
		(
			if tangent.inTangentType == #custom then
			(
				tangent.inTangent = KeyTangent.tangentToAngle tangent.inTangent factor:factor
				if keyIndex > 1 then
					tangent.inTangentLength = KeyTangent.tangentToLength tangent.inTangentLength tangent.inTangent key.time.frame (getKey controller (keyIndex - 1)).time.frame
				else
					tangent.inTangentLength = 0
			)
			if tangent.outTangentType == #custom then
			(
				tangent.outTangent = KeyTangent.tangentToAngle tangent.outTangent factor:factor
				if keyIndex < controller.keys.count  then
					tangent.outTangentLength = KeyTangent.tangentToLength tangent.outTangentLength tangent.outTangent key.time.frame (getKey controller (keyIndex + 1)).time.frame
				else
					tangent.outTangentLength = 0
			)
		)
		
		if tangents.count == 1 then
			tangents = tangents[1]
		
		tangents
	),
	
	fn createFromTCB key controller keyIndex property:undefined =
	(
		local tangentType = #custom
		if key.tension == 25 and key.continuity == 25 and key.bias == 25 then
			tangentType = #smooth
		else if key.continuity == 0 and key.tension == 25 and key.bias == 25 then
			tangentType = #linear
		else if key.tension == 50 then
			tangentType = #slow
		else if key.tension == 0 and key.bias == 25 then
			tangentType = #fast
		
		local currentValue = KeyTangent.getControllerValue key controller property
		
		local tangents = if tangentType != #custom then
		(
			if classOf currentValue == Quat then
			(
				currentValue = currentValue as EulerAngles
				currentValue = [currentValue.x, currentValue.y,currentValue.z]
			)
			
			for i = 1 to currentValue.count collect
				KeyTangent tangentType tangentType
		)
		else
		(
			local currentFrame = key.time.frame
			
			local previousValue = undefined
			local previousFrame = undefined
			if keyIndex > 1 then
			(
				local previousKey = biped.getKey controller (keyIndex - 1)
				previousValue = KeyTangent.getControllerValue previousKey controller property
				previousFrame = previousKey.time.frame
			)
			
			local nextValue = undefined
			local nextFrame = undefined
			if keyIndex < controller.keys.count then
			(
				local nextKey = biped.getKey controller (keyIndex + 1)
				nextValue = KeyTangent.getControllerValue nextKey controller property
				nextFrame = nextKey.time.frame
			)
			
			if previousValue == undefined and nextValue == undefined then
			(
				if classOf currentValue == Quat then
				(
					currentValue = currentValue as EulerAngles
					currentValue = [currentValue.x, currentValue.y,currentValue.z]
				)
				
				for i = 1 to currentValue.count collect
					KeyTangent #auto #auto
			)
			else
			(
				if previousValue == undefined then
				(
					previousValue = currentValue
					previousFrame = (2 * currentFrame - nextFrame)
				)
				if nextValue == undefined then
				(
					nextValue = currentValue
					nextFrame = (2 * currentFrame - previousFrame)
				)
				
				local deltaPreviousValue = undefined
				local deltaNextValue = undefined
				if classOf currentValue == Quat then
				(
					deltaPreviousValue = (currentValue * inverse previousValue) as EulerAngles
					deltaPreviousValue = [deltaPreviousValue.x, deltaPreviousValue.y, deltaPreviousValue.z]
					deltaNextValue = (nextValue * inverse currentValue) as EulerAngles
					deltaNextValue = [deltaNextValue.x, deltaNextValue.y, deltaNextValue.z]
					currentValue = currentValue as EulerAngles
					currentValue = [currentValue.x, currentValue.y, currentValue.z]
				)
				else
				(
					deltaPreviousValue = #()
					deltaNextValue = #()
					for i = 1 to currentValue.count do
					(
						append deltaPreviousValue (currentValue[i] - previousValue[i])
						append deltaNextValue (nextValue[i] - currentValue[i])
					)
				)
				local deltaTime = nextFrame - previousFrame
				
				for i = 1 to currentValue.count collect
				(
					local t = key.tension / 25.0 - 1
					local c = key.continuity / 25.0 - 1
					local b = key.bias / 25.0 - 1
					
					local ts = (1-t)*(1-c)*(1+b) * deltaPreviousValue[i] + (1-t)*(1+c)*(1-b) * deltaNextValue[i]
					local td = (1-t)*(1+c)*(1+b) * deltaPreviousValue[i]+ (1-t)*(1-c)*(1-b) * deltaNextValue[i]
					
					local inTangent = -atan2 ts deltaTime
					local outTangent = atan2 td deltaTime
					
					KeyTangent #custom #custom inTangent outTangent
				)
			)
		)
		
		if tangents.count == 1 then
			tangents = tangents[1]
		
		tangents
	),
	
	fn getControllerValue key controller property =
	(
		local val = at time key.time getProperty controller.value property
		if classOf val != Quat and classOf val != Point3 then
			val = #(val)
		val
	),
	
	fn tangentToAngle val factor:1.0 =
	(
		factor * atan2 val 0.1875
	),
	
	fn tangentToLength lengthFactor tangentAngle time1 time2 =
	(
		lengthFactor * abs(time1 - time2) / (cos tangentAngle)
	),
	
	fn asXml xmlElement =
	(
		xmlElement.setAttribute "inTangentType" (AsString inTangentType)
		xmlElement.setAttribute "outTangentType" (AsString outTangentType)
		if inTangentType == #custom then
		(
			if inTangent != undefined then
				xmlElement.setAttribute "inTangent" (AsString inTangent)
			if inTangentLength != undefined then
				xmlElement.setAttribute "inTangentLength" (AsString inTangentLength)
		)
		if outTangentType == #custom then
		(
			if outTangent != undefined then
				xmlElement.setAttribute "outTangent" (AsString outTangent)
			if outTangentLength != undefined then
				xmlElement.setAttribute "outTangentLength" (AsString outTangentLength)
		)
	)
)

-- A posture for a node. Contains the transformation info of this node.
struct NodeTransform
(
	-- Reference to the MaxNode struct the posture is refering to.
	node,
	
	-- Transformations of the posture.
	-- An undefined value means there is no key on that component.
	position = #(undefined, undefined, undefined),
	rotation = #(undefined, undefined, undefined),
	scale = #(undefined, undefined, undefined),
	
	positionTangent = #(undefined, undefined, undefined),
	rotationTangent = #(undefined, undefined, undefined),
	scaleTangent = #(undefined, undefined, undefined),
	
	-- We need all the components exported, wheter or not they have a key.
	-- Stores wheter they have a key or not.
	positionKeyed = #(False, False, False),
	rotationKeyed = #(False, False, False),
	scaleKeyed = #(False, False, False),
	
	fn create obj forceKey:false defaultTangentType:#auto =
	(
		local nodeTrf = NodeTransform obj
		
		if obj.exportPosition or obj.exportRotation or obj.exportScale then
		(
			local trf = obj.getTransform()
			local keyIndex = 0
			local controller = undefined
			if obj.isBiped then
			(
				if classOf obj.node.controller == Vertical_Horizontal_Turn then
				(
					if obj.exportPosition then
					(
						nodeTrf.position = trf.position
						if (keyIndex = getKeyIndex (controller = obj.node.controller.horizontal.controller) currentTime) != 0 or forceKey  then
						(
							nodeTrf.positionKeyed[1] = True
							nodeTrf.positionKeyed[2] = True
							
							if keyIndex != 0 then
							(
								local key = biped.getKey controller keyIndex
								-- NOTE: The biped root has no parents, and as such it's X and Y translation coordinates will be swaped (since this is the conversion used for Maya).
								-- We need to apply this swap to the tangents as well.
								nodeTrf.positionTangent[2] = KeyTangent.createFromTCB key controller keyIndex property:"position.x"
								nodeTrf.positionTangent[1] = KeyTangent.createFromTCB key controller keyIndex property:"position.y"
								nodeTrf.positionTangent[1].invertTangent()
							)
							else
							(
								nodeTrf.positionTangent[1] = nodeTrf.positionTangent[2] = KeyTangent #smooth #smooth
							)
						)
						if (keyIndex = getKeyIndex (controller = obj.node.controller.vertical.controller) currentTime) != 0 or forceKey  then
						(
							nodeTrf.positionKeyed[3] = True
							
							if keyIndex != 0 then
							(
								local key = biped.getKey controller keyIndex
								nodeTrf.positionTangent[3] = KeyTangent.createFromTCB key controller keyIndex property:"position.z"
							)
							else
							(
								nodeTrf.positionTangent[3] = KeyTangent #smooth #smooth
							)
						)
					)
					if obj.exportRotation then
						if (keyIndex = getKeyIndex (controller = obj.node.controller.turning.controller) currentTime) != 0 or forceKey then
						(
							nodeTrf.rotation = PointToArray (trf.rotation as EulerAngles)
							nodeTrf.rotationKeyed = #(True, True, True)
							
							if keyIndex != 0 then
							(
								local key = biped.getKey controller keyIndex
								nodeTrf.rotationTangent = KeyTangent.createFromTCB key controller keyIndex property:"rotation"
							)
							else
							(
								local tangent = KeyTangent #smooth #smooth
								nodeTrf.rotationTangent = #(tangent, tangent, tangent)
							)
						)
				)
				else if (keyIndex = getKeyIndex (controller = obj.node.controller) currentTime) != 0 or forceKey then
				(
					if obj.exportPosition then
					(
						nodeTrf.position = PointToArray trf.position
						nodeTrf.positionKeyed = #(True, True, True)
						
						if keyIndex != 0 then
						(
							local key = biped.getKey controller keyIndex
							nodeTrf.positionTangent = KeyTangent.createFromTCB key controller keyIndex property:"position"
						)
						else
						(
							local tangent = KeyTangent #smooth #smooth
							nodeTrf.positionTangent = #(tangent, tangent, tangent)
						)
					)
					if obj.exportRotation then
					(
						nodeTrf.rotation = PointToArray (trf.rotation as EulerAngles)
						nodeTrf.rotationKeyed = #(True, True, True)
						
						if keyIndex != 0 then
						(
							local key = biped.getKey controller keyIndex
							nodeTrf.rotationTangent = KeyTangent.createFromTCB key controller keyIndex property:"rotation"
						)
						else
						(
							local tangent = KeyTangent #smooth #smooth
							nodeTrf.rotationTangent = #(tangent, tangent, tangent)
						)
					)
					if obj.exportScale then
					(
						nodeTrf.scale = PointToArray trf.scale
						nodeTrf.scaleKeyed = #(True, True, True)
						
						if keyIndex != 0 then
						(
							local key = biped.getKey controller keyIndex
							nodeTrf.scaleTangent = KeyTangent.createFromTCB key controller keyIndex property:"scale"
						)
						else
						(
							local tangent = KeyTangent #smooth #smooth
							nodeTrf.scaleTangent = #(tangent, tangent, tangent)
						)
					)
				)
			)
			else
			(
				if obj.exportPosition then
				(
					nodeTrf.position = trf.position
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.posXController) currentTime) != 0 or forceKey then
					(
						nodeTrf.positionKeyed[1] = True
						
						if keyIndex != 0 then
						(
							local key = getKey controller keyIndex
							nodeTrf.positionTangent[1] = KeyTangent.createFromBezier key controller keyIndex
						)
						else
						(
							nodeTrf.positionTangent[1] = KeyTangent defaultTangentType defaultTangentType
						)
					)
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.posYController) currentTime) != 0 or forceKey then
					(
						nodeTrf.positionKeyed[2] = True
						
						if keyIndex != 0 then
						(
							local key = getKey controller keyIndex
							nodeTrf.positionTangent[2] = KeyTangent.createFromBezier key controller keyIndex
						)
						else
						(
							nodeTrf.positionTangent[2] = KeyTangent defaultTangentType defaultTangentType
						)
					)
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.posZController) currentTime) != 0 or forceKey then
					(
						nodeTrf.positionKeyed[3] = True
						
						if keyIndex != 0 then
						(
							local key = getKey controller keyIndex
							nodeTrf.positionTangent[3] = KeyTangent.createFromBezier key controller keyIndex
						)
						else
						(
							nodeTrf.positionTangent[3] = KeyTangent defaultTangentType defaultTangentType
						)
					)
					if obj.parent == undefined then
					(
						-- Since the position of unparented controls is rotated 90º around the X axis, the Z and Y axis switch their keyframes
						local temp = nodeTrf.positionKeyed[2]
						nodeTrf.positionKeyed[2] = nodeTrf.positionKeyed[3]
						nodeTrf.positionKeyed[3] = temp
					)
				)
				if obj.exportRotation then
				(
					nodeTrf.rotation = PointToArray (trf.rotation as EulerAngles)
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.rotXController) currentTime) != 0 then
					(
						local key = getKey controller keyIndex
						nodeTrf.rotationTangent[1] = KeyTangent.createFromBezier key controller keyIndex
						nodeTrf.rotationKeyed[1] = True
					)
					else if forceKey then
					(
						nodeTrf.rotationTangent[1] = KeyTangent defaultTangentType defaultTangentType
						nodeTrf.rotationKeyed[1] = True
					)
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.rotYController) currentTime) != 0 then
					(
						local key = getKey controller keyIndex
						nodeTrf.rotationTangent[2] = KeyTangent.createFromBezier key controller keyIndex
						nodeTrf.rotationKeyed[2] = True
					)
					else if forceKey then
					(
						nodeTrf.rotationTangent[2] = KeyTangent defaultTangentType defaultTangentType
						nodeTrf.rotationKeyed[2] = True
					)
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.rotZController) currentTime) != 0 then
					(
						local key = getKey controller keyIndex
						nodeTrf.rotationTangent[3] = KeyTangent.createFromBezier key controller keyIndex
						nodeTrf.rotationKeyed[3] = True
					)
					else if forceKey then
					(
						nodeTrf.rotationTangent[3] = KeyTangent defaultTangentType defaultTangentType
						nodeTrf.rotationKeyed[3] = True
					)
				)
				if obj.exportScale then
				(
					if (keyIndex = getKeyIndex (controller = nodeTrf.node.scaController) currentTime) != 0 or forceKey then
					(
						nodeTrf.scale = PointToArray trf.scale
						nodeTrf.scaleKeyed = #(True, True, True)
						
						if keyIndex != 0 then
						(
							local key = getKey controller keyIndex
							nodeTrf.scaleTangent = KeyTangent.createFromBezier key controller keyIndex
						)
						else
						(
							local tangent = KeyTangent defaultTangentType defaultTangentType
							nodeTrf.scaleTangent = #(tangent, tangent, tangent)
						)
					)
				)
			)
		)
		
		nodeTrf
	),
	
	fn isEmpty arr:unsupplied =
	(
		if arr == unsupplied then
			arr = positionKeyed + rotationKeyed + scaleKeyed
		(finditem arr True) == 0
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "NodeTransform"
		root.setAttribute "nodeName" (node.getName())
		
		if not isEmpty arr:positionKeyed then
			for i=1 to position.count do
			(
				local element = xmlDoc.createElement ("Position" + coordTags[i])
				element.innerText = AsString position[i]
				element.setAttribute "keyed" (AsString positionKeyed[i])
				if positionTangent[i] != undefined then
					positionTangent[i].asXml element
				root.appendChild element
			)

		if not isEmpty arr:rotationKeyed then
			for i=1 to rotation.count do
			(
				local element = xmlDoc.createElement ("Rotation" + coordTags[i])
				element.innerText = AsString rotation[i]
				element.setAttribute "keyed" (AsString rotationKeyed[i])
				if rotationTangent[i] != undefined then
					rotationTangent[i].asXml element
				root.appendChild element
			)

		if not isEmpty arr:scaleKeyed then
			for i=1 to scale.count do
			(
				local element = xmlDoc.createElement ("Scale" + coordTags[i])
				element.innerText = AsString scale[i]
				element.setAttribute "keyed" (AsString scaleKeyed[i])
				if scaleTangent[i] != undefined then
					scaleTangent[i].asXml element
				root.appendChild element
			)
		
		root
	)
)

-- Struct to store parameters that should be transfered from Max to Maya
struct Param
(
	sourceNode,
	
	subAnimIndices,
	
	outputAttribute,
	
	inputRange = #(0, 1),
	outputRange = #(0, 1),
	clampRange = True,
	
	animationData = #(),
	beforeOutOfRangeType = undefined,
	afterOutOfRangeType = undefined,
	
	fn isValid =
	(
		local s = getNodeByName sourceNode
		if not isValidNode s then
			return False
		for i in subAnimIndices do
			if i > s.numSubs then
				return False
			else
				s = s[i]
		return True
	),
	
	fn remapValue val clampRange:True =
	(
		if clampRange then
		(
			if inputRange[1] > inputRange[2] then
				val = amin #(inputRange[1], amax #(inputRange[2], val))
			else
				val = amin #(inputRange[2], amax #(inputRange[1], val))
		)
		
		factor = (val as float - inputRange[1]) / (inputRange[2] - inputRange[1])
		
		factor * (outputRange[2] - outputRange[1]) + outputRange[1]
	),
	
	fn storeAnimation =
	(
		local n = getNodeByName sourceNode
		local s = n
		for i in subAnimIndices do
			s = s[i]
		
		local keys = s.keys
		if keys != undefined then
		(
			local factor = (outputRange[2] - outputRange[1]) as float / (inputRange[2] - inputRange[1])
			animationData = for i = 1 to keys.count collect at time keys[i].time 
			(
				local tangent = KeyTangent.createFromBezier keys[i] s.controller i factor:factor
				#(keys[i].time, remapValue s.value clampRange:clampRange, tangent)
			)
			
			beforeOutOfRangeType = getBeforeORT s.controller
			afterOutOfRangeType = getAfterORT s.controller
		)
	),
	
	fn hasAnimation =
	(
		animationData.count != 0
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "Parameter"
		root.setAttribute "attribute" outputAttribute
		if beforeOutOfRangeType != undefined and beforeOutOfRangeType != #constant then	-- We ignore when the controller is set to constant, since it is the default type both on Max and Maya
			root.setAttribute "beforeOutOfRangeType" beforeOutOfRangeType
		if afterOutOfRangeType != undefined and afterOutOfRangeType != #constant then	-- We ignore when the controller is set to constant, since it is the default type both on Max and Maya
			root.setAttribute "afterOutOfRangeType" afterOutOfRangeType
	
		for data in animationData do
		(
			local element = xmlDoc.createElement "Keyframe"
			element.innerText = AsString data[2]
			element.setAttribute "time" (AsString data[1].frame)
			if data[3] != undefined then
				data[3].asXml element
			root.appendChild element
		)
	
		root
	)
)

global params = #(
	Param "zebesian_R01_ArmBlade_Retractor_CTL" #(3, 1, 2, 1, 1) "armUI_R0_ctl.bladeLength" inputRange:#(-80, 0) outputRange:#(0, 1) clampRange:True
)

-- A posture of the animation at a specific time. Contains the posture of each node whith keys at that time.
struct AnimationPosture
(
	-- Time of the posture.
	time,
	
	-- List of nodes which have key at the posture time and their transformation.
	nodeTransforms = #(),
	
	-- Used for biped, indicates if the posture has a limb on IK or FK.
	--An undefined value means the limb doesn't have a key on that frame and should be ignored.
	rightArmIK = undefined,
	leftArmIK = undefined,
	rightLegIK = undefined,
	leftLegIK = undefined,
	
	fn isEmpty =
	(
		nodeTransforms.count == 0
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "AnimationPosture"
		root.setAttribute "time" (AsString time.frame)
		
		if rightArmIK != undefined then root.setAttribute "rightArmIK" (AsString rightArmIK)
		if leftArmIK != undefined then root.setAttribute "leftArmIK" (AsString leftArmIK)
		if rightLegIK != undefined then root.setAttribute "rightLegIK" (AsString rightLegIK)
		if leftLegIK != undefined then root.setAttribute "leftLegIK" (AsString leftLegIK)
		
		for nodeTrf in nodeTransforms do
			root.appendChild (nodeTrf.asXml xmlDoc)
		
		root
	)
)

-- Structure that represents a layer. It contains all the animation for all the nodes on that layer.
struct LayerAnimation
(
	-- Name of the layer
	layerName,
	
	-- Layers that should be active in order to recreate this layer
	requiredLayers = #(),
	
	-- List of all the postures, ordered by time.
	animationPostures = #(),
	
	-- List of Out-of-Range-Types for each node.
	outOfRangeTypes = #(),
	
	fn getIKLimbStateAtTime charAnim limb t =
	(
		local ikStates = #(0, 0, 0, 0)	-- The default state is FK (0 blend weight)
		for posture in animationPostures while posture.time <= t do
		(
			if posture.rightArmIK != undefined then
				ikStates[1] = posture.rightArmIK
			if posture.leftArmIK != undefined then
				ikStates[2] = posture.leftArmIK
			if posture.rightLegIK != undefined then
				ikStates[3] = posture.rightLegIK
			if posture.leftLegIK != undefined then
				ikStates[4] = posture.leftLegIK
		)
		
		if limb == charAnim.rightArmNode then
			ikStates[1]
		else if limb == charAnim.leftArmNode then
			ikStates[2]
		else if limb == charAnim.rightLegNode then
			ikStates[3]
		else if limb == charAnim.leftLegNode then
			ikStates[4]
		else
			undefined
	),
	
	fn create layerName nodes charAnim isBiped:False requiredLayers:#() =
	(
		local layerAnim = LayerAnimation layerName requiredLayers
		
		-- Sets the animation range to the nodes' animation range.
		ExpandAnimationRangeToAnimation nodes
		
		if not isBiped then
		(
			for obj in nodes do
			(
				obj.updateCachedControllers()
				
				local positionBeforeORT = #(undefined, undefined, undefined)
				local positionAfterORT = #(undefined, undefined, undefined)
				local rotationBeforeORT = #(undefined, undefined, undefined)
				local rotationAfterORT = #(undefined, undefined, undefined)
				local scaleBeforeORT = undefined
				local scaleAfterORT = undefined
				if obj.exportPosition then
				(
					positionBeforeORT[1] = getBeforeORT obj.posXController
					positionBeforeORT[2] = getBeforeORT obj.posYController
					positionBeforeORT[3] = getBeforeORT obj.posZController
					positionAfterORT[1] = getAfterORT obj.posXController
					positionAfterORT[2] = getAfterORT obj.posYController
					positionAfterORT[3] = getAfterORT obj.posZController
				)
				if obj.exportRotation then
				(
					rotationBeforeORT[1] = getBeforeORT obj.rotXController
					rotationBeforeORT[2] = getBeforeORT obj.rotYController
					rotationBeforeORT[3] = getBeforeORT obj.rotZController
					rotationAfterORT[1] = getAfterORT obj.rotXController
					rotationAfterORT[2] = getAfterORT obj.rotYController
					rotationAfterORT[3] = getAfterORT obj.rotZController
				)
				if obj.exportScale then
				(
					scaleBeforeORT = getBeforeORT obj.scaController
					scaleAfterORT = getAfterORT obj.scaController
				)
				
				append layerAnim.outOfRangeTypes #(obj, positionBeforeORT, positionAfterORT, rotationBeforeORT, rotationAfterORT, scaleBeforeORT, scaleAfterORT)
			)
		)
		
		-- Creates a posture for each frame.
		for j = animationrange.start to animationrange.end collect at time j
		(
			local posture = AnimationPosture j
			
			local forceRightArmKey = False
			local forceLeftArmKey = False
			local forceRightLegKey = False
			local forceLeftLegKey = False
			if isBiped then
			(
				--Checks if it should force keys on limbs.
				if (charAnim.bipedLayerAnimations.count > 0) and (HasKeyAtTime charAnim.bip currentTime) then	-- If this is a layer other than the base one and there is a key on the root...
				(
					-- Force the key if the limb is currently on IK mode
					forceRightArmKey = (charAnim.bipedLayerAnimations[1].getIKLimbStateAtTime charAnim charAnim.rightArmNode currentTime) > 0
					forceLeftArmKey = (charAnim.bipedLayerAnimations[1].getIKLimbStateAtTime charAnim charAnim.leftArmNode currentTime) > 0
					forceRightLegKey = (charAnim.bipedLayerAnimations[1].getIKLimbStateAtTime charAnim charAnim.rightLegNode currentTime) > 0
					forceLeftLegKey = (charAnim.bipedLayerAnimations[1].getIKLimbStateAtTime charAnim charAnim.leftLegNode currentTime) > 0
				)
				
				-- Stores the IK state for each limb.
				posture.rightArmIK = GetIKState charAnim.rightArmNode useDefaultValueInsteadOfUndefined:forceRightArmKey
				posture.leftArmIK = GetIKState charAnim.leftArmNode useDefaultValueInsteadOfUndefined:forceLeftArmKey
				posture.rightLegIK = GetIKState charAnim.rightLegNode useDefaultValueInsteadOfUndefined:forceRightLegKey
				posture.leftLegIK = GetIKState charAnim.leftLegNode useDefaultValueInsteadOfUndefined:forceLeftLegKey
			)
			
			-- Retrieves the transformation for each of the nodes.
			for obj in nodes do
			(
				local forceKey = if obj.ikLimb == undefined then
					False
				else if obj.ikLimb == charAnim.rightArmNode then
					forceRightArmKey
				else if obj.ikLimb == charAnim.leftArmNode then
					forceLeftArmKey
				else if obj.ikLimb == charAnim.rightLegNode then
					forceRightLegKey
				else if obj.ikLimb == charAnim.leftLegNode then
					forceLeftLegKey
				
				local nodeTrf = NodeTransform.create obj forceKey:forceKey
				
				-- Only stores it if there is actual transformation data.
				if not nodeTrf.isEmpty() then
					append posture.nodeTransforms nodeTrf
			)
			
			-- If the posture contains any data, stores it.
			if not posture.isEmpty() then
				append layerAnim.animationPostures posture
		)
		
		-- return
		layerAnim
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "LayerAnimation"
		root.setAttribute "layerName" layerName
		
		if requiredLayers.count > 0 then
		(
			local requiredLayersElement = xmlDoc.createElement "RequiredLayers"
			root.appendChild requiredLayersElement
			for requiredLayer in requiredLayers do
			(
				local requiredLayerElement = xmlDoc.createElement "RequiredLayer"
				requiredLayersElement.appendChild requiredLayerElement
				requiredLayerElement.innerText = requiredLayer
			)
		)
		
		local outOfRangeTypesElement = xmlDoc.createElement "OutOfRangeTypes"
		root.appendChild outOfRangeTypesElement
		local ortAttrs = #(#("startTranslateX", "startTranslateY", "startTranslateZ"), #("endTranslateX", "endTranslateY", "endTranslateZ"), #("startRotateX", "startRotateY", "startRotateZ"), #("endRotateX", "endRotateY", "endRotateZ"), "startScale", "endScale")
		for ort in outOfRangeTypes do
		(
			local ortElement = xmlDoc.createElement "OutOfRangeType"
			ortElement.setAttribute "nodeName" (ort[1].getName())
			
			local usefull = False
			for i = 2 to 5 do
				for j = 1 to 3 do
				(
					local t = ort[i][j]
					if t != undefined and t != #constant then	-- We ignore when the controller is set to constant, since it is the default type both on Max and Maya
					(
						ortElement.setAttribute ortAttrs[i-1][j] t
						usefull = True
					)
				)
			for i = 6 to 7 do
			(
				local t = ort[i]
				if t != undefined and t != #linear then
				(
					ortElement.setAttribute ortAttrs[i-1] t
					usefull = True
				)
			)
			
			if usefull then
				outOfRangeTypesElement.appendChild ortElement
		)
		
		local animationPosturesElement = xmlDoc.createElement "AnimationPostures"
		root.appendChild animationPosturesElement
		for posture in animationPostures do
			animationPosturesElement.appendChild (posture.asXml xmlDoc)
		
		root
	)
)

-- Stores a normal node and the necessary information to export it correctly.
struct MaxNode
(
	-- Reference to the node.
	node,
	isBiped,
	
	-- The MaxNode parent of this node.
	-- Usefull to specify if there are LinkConstraints or discrepancies within the source and target rigs.
	parent,
	parentForRotation, 	-- Some nodes may have a different parent for their rotation (like the biped Props).
	
	-- Wether or not the node should be reparented on Maya to it's Max parent.
	reparent,
	
	-- An identifier for the limb this node is part of.
	ikLimb,
	
	-- Remaps the node name.
	-- Some nodes won't have the same name on Maya.
	nameRemap,
	forceRemap = False,	-- This flag is used to look for global remaps if none is specified
	
	-- Remaps of the axis.
	-- Some nodes won't have the same axis on Maya.
	axisRemap = #(1,2,3),
	
	-- Wether or not to store the base transform
	storeBaseTransform,
	
	-- Which transformation components should be exported. By default, only export rotation.
	exportPosition,
	exportRotation,
	exportScale,
	
	-- Quick access to the node's postion/rotation/scale - x/y/z controllers.
	posController,
	posXController,
	posYController,
	posZController,
	
	rotController,
	rotXController,
	rotYController,
	rotZController,
	
	scaController,
	
	-- Stores the base transformation for the node, used if there are no animation keys
	baseTransform = undefined,
	
	fn updateCachedControllers =
	(
		if this.exportPosition then
		(
			this.posController = GetKeyableController node.position.controller listClass:Position_List
			if (classOf this.posController) != Position_XYZ then
			(
				this.exportPosition = False
				logger.logWarning ("The object [" + this.node.name + "] has an invalid position controller.")
			)
			else
			(
				this.posXController = GetKeyableController this.posController.x_position.controller listClass:Float_List
				this.posYController = GetKeyableController this.posController.y_position.controller listClass:Float_List
				this.posZController = GetKeyableController this.posController.z_position.controller listClass:Float_List
			)
		)
		
		if this.exportRotation then
		(
			this.rotController = GetKeyableController node.rotation.controller listClass:Rotation_List
			if (classOf this.rotController) != Euler_XYZ then
			(
				this.exportRotation = False
				logger.logWarning ("The object [" + this.node.name + "] has an invalid rotation controller.")
			)
			else
			(
				this.rotXController = GetKeyableController this.rotController.x_rotation.controller listClass:Float_List
				this.rotYController = GetKeyableController this.rotController.y_rotation.controller listClass:Float_List
				this.rotZController = GetKeyableController this.rotController.z_rotation.controller listClass:Float_List
			)
		)
		
		if this.exportScale then
		(
			this.scaController = GetKeyableController node.scale.controller listClass:Scale_List
			if (classOf this.scaController) != Bezier_Scale then
			(
				this.exportScale = False
				logger.logWarning ("The object [" + this.node.name + "] has an invalid scale controller.")
			)
		)
	),
	
	fn lookForParent maxNodeList =
	(
		local parentNode = GetNodeParent this.node
		if classOf parentNode == Array then
		(
			this.parent = MaxNode.getMaxNodeFromList parentNode[1] maxNodeList
			this.parentForRotation = MaxNode.getMaxNodeFromList parentNode[2] maxNodeList
		)
		else
		(
			this.parent = MaxNode.getMaxNodeFromList parentNode maxNodeList
			this.parentForRotation = this.parent
		)
	),
	
	fn storeTransform =
	(
		at time 0
		(
			if not isBiped then
				this.updateCachedControllers()
			this.baseTransform = NodeTransform.create this forceKey:True defaultTangentType:#smooth	-- We use smooth tangents in this case to avoid affecting the animation as much as possible
		)
	),
	
	fn create node maxNodeList:#() parent:unsupplied reparent:False ikLimb:undefined nameRemap:undefined forceRemap:true axisRemap:#(1, 2, 3) storeBaseTransform:False exportPosition:False exportRotation:True exportScale:False =
	(
		if nameRemap == undefined or not forceRemap then
		(
			newNameRemap = undefined
			for remap in remaps where remap[1] == node.name while newNameRemap == undefined do
			(
				newNameRemap = remap[2]
				if remap.count >= 3 then
					axisRemap = remap[3]
			)
			if newNameRemap != undefined then
				nameRemap = newNameRemap
		)
		
		local parentForRotation = unsupplied
		if parent != unsupplied then
		(
			if classOf parent == Array then
			(
				parentForRotation = parent[2]
				parent = parent[1]
			)
			else
			(
				parentForRotation = parent
			)
		)
		
		local isBiped = IsBipedObject node
		
		local obj = MaxNode node isBiped parent parentForRotation reparent ikLimb nameRemap forceRemap axisRemap storeBaseTransform exportPosition exportRotation exportScale
		
		if parent == unsupplied then
			obj.lookForParent maxNodeList
		
		if storeBaseTransform then 
			obj.storeTransform()		
		
		if maxNodeList != undefined then
			append maxNodeList obj
		
		obj
	),
	
	fn createFromStoredName maxNodeList:#() =
	(
		local n = getNodeByName node
		if isValidNode n then
		(
			local p = unsupplied
			if parent != undefined then
				local parentNode  = getNodeByName parent
				if isValidNode parentNode then
					for mn in maxNodeList where mn.node == parentNode while p == unsupplied do
						p = mn
			
			MaxNode.create n maxNodeList:maxNodeList parent:p reparent:this.reparent nameRemap:this.nameRemap forceRemap:this.forceRemap axisRemap:this.axisRemap storeBaseTransform:this.storeBaseTransform exportPosition:this.exportPosition exportRotation:this.exportRotation exportScale:this.exportScale
		)
		else
			undefined
	),
	
	fn getMaxNodeFromList obj list =
	(
		local targetNode = undefined
		for maxNode in list while targetNode == undefined do
			if maxNode.node == obj then
				targetNode = maxNode
		targetNode
	),
	
	fn getName =
	(
		if nameRemap != undefined then
			nameRemap
		else
			node.name
	),
	
	fn sign val =
	(
		if val > 0 then 1 else if val < 0 then -1 else 0
	),
	
	fn swapAxis val remap =
	(
		local newVal = copy val
		val = #(val[1], val[2], val[3])
		newVal[1] = val[abs remap[1]] * sign remap[1]
		newVal[2] = val[abs remap[2]] * sign remap[2]
		newVal[3] = val[abs remap[3]] * sign remap[3]
		newVal
	),
	
	fn getTransform =
	(
		local trf = swapAxis node.transform axisRemap
		local pos = trf.row4
		if parentForRotation != undefined then
			trf = trf * inverse (swapAxis parentForRotation.node.transform parentForRotation.axisRemap)
		else
			trf.rotation = trf.rotation * AngleAxis 90 [1,0,0]
		if parent != undefined then
		(
			trf.row4 = pos * inverse (swapAxis parent.node.transform parent.axisRemap)
			--trf.row4 = swapAxis trf.row4 axisRemap	-- Creo que esto es innecesario, en Maya ya compensamos la posición en base a la rotación inicial con respecto al padre
		)
		else
		(
			if isBiped then
				trf.row4 = pos * (AngleAxis -90 [0,0,1]) as Quat
			else
				trf.row4 = pos * (AngleAxis 90 [1,0,0]) as Quat
		)
		
		trf
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "Node"
		
		root.setAttribute "nodeName" (getName())
		
		if parent != undefined then
			root.setAttribute "parentName" (parent.getName())
		if parentForRotation != undefined then
			root.setAttribute "parentForRotationName" (parentForRotation.getName())
		root.setAttribute "reparent" (AsString reparent)
		
		root.setAttribute "exportPosition" (AsString exportPosition)
		root.setAttribute "exportRotation" (AsString exportRotation)
		root.setAttribute "exportScale" (AsString exportScale)
		
		if baseTransform != undefined then
			root.appendChild (baseTransform.asXml xmlDoc)
		
		root
	)
)

global normalNodes = #(
	MaxNode "zebesian_R01_ArmBlade_Main_CTL" parent:"zebesian_bip_R_Forearm" nameRemap:"armbladeMain_R0_ctl" storeBaseTransform:True exportPosition:False exportRotation:True exportScale:False,
	MaxNode "zebesian_R01_ArmBlade_01_CTL" nameRemap:"armblade_R0_fk0_ctl" axisRemap:#(-1, -2, 3) storeBaseTransform:True exportPosition:True exportRotation:True exportScale:False,
	MaxNode "zebesian_R01_ArmBlade_02_CTL" nameRemap:"armblade_R0_fk1_ctl" axisRemap:#(-1, 2, -3) storeBaseTransform:True exportPosition:True exportRotation:True exportScale:False
)

-- Main class which stores all the data from a character's animation.
struct CharacterAnimation
(
	-- Refrence to the character's InfoChar.
	infoChar,
	
	-- List of nodes. Used to store information relevant to the nodes.
	-- The list is sorted descending to hierarchy, so the animation is both copied and pasted in the right order.
	bipedNodes = #(),
	normalNodes = #(),
	
	-- List of parameters. Used to store how to transfer parametric information.
	params = #(),
	
	-- Used for biped, stores the limbs to retrieve the IK state on each frame of the animation.
	--An undefined value means there is not such limb.
	bip = undefined,
	rightArmNode = undefined,
	leftArmNode = undefined,
	rightLegNode = undefined,
	leftLegNode = undefined,
	
	-- List of layers, both for biped and normal nodes. The elements of this lists contains the actual animation.
	bipedLayerAnimations = #(),
	normalLayerAnimations = #(),
	
	-- Combines two animation postures into a new one. Used to combine biped and normal layer animations.
	fn CombineAnimationPostures postureA postureB =
	(
		local newPosture = AnimationPosture postureA.time
		
		-- It naively assumes there are not shared nodes.
		join newPosture.nodeTransforms postureA.nodeTransforms
		join newPosture.nodeTransforms postureB.nodeTransforms
		
		newPosture.rightArmIK = if postureA.rightArmIK != undefined then postureA.rightArmIK else postureB.rightArmIK
		newPosture.leftArmIK = if postureA.leftArmIK != undefined then postureA.leftArmIK else postureB.leftArmIK
		newPosture.rightLegIK = if postureA.rightLegIK != undefined then postureA.rightLegIK else postureB.rightLegIK
		newPosture.leftLegIK = if postureA.leftLegIK != undefined then postureA.leftLegIK else postureB.leftLegIK
		
		newPosture
	),

	-- Combines two animation layers into a new one. Used to combine biped and normal layer animations.
	fn CombineLayerAnimations layerA layerB =
	(
		local newLayer = LayerAnimation layerA.layerName
		
		newLayer.requiredLayers = for l in layerA.requiredLayers collect l
		for l in layerB.requiredLayers do
			appendIfUnique newLayer.requiredLayers l
		
		newLayer.outOfRangeTypes = layerA.outOfRangeTypes + layerB.outOfRangeTypes
		
		if layerA.animationPostures.count == 0 then
			newLayer.animationPostures = layerB.animationPostures
		else if layerB.animationPostures.count == 0 then
			newLayer.animationPostures = layerA.animationPostures
		else
		(
			local j = 1
			for i = 1 to layerA.animationPostures.count do
			(
				while j <= layerB.animationPostures.count and layerB.animationPostures[j].time < layerA.animationPostures[i].time do
				(
					append newLayer.animationPostures layerB.animationPostures[j]
					j += 1
				)
				if j <= layerB.animationPostures.count and layerB.animationPostures[j].time == layerA.animationPostures[i].time then
				(
					append newLayer.animationPostures (CombineAnimationPostures layerB.animationPostures[j] layerA.animationPostures[i])
					j += 1
				)
				else
					append newLayer.animationPostures layerA.animationPostures[i]
			)
		)
		
		newLayer
	),
	
	fn asXml xmlDoc =
	(
		local root = xmlDoc.createElement "CharacterAnimation"
		root.setAttribute "characterName" infoChar.sCharName
		
		local charLayers = infoChar.GetAllAnimLayerInfo()
		local animPresets = (infoChar.GetAllAnimPresetStruct()).animPresets
		if animPresets != undefined and animPresets.count > 0 then
		(
			local animPresetsElement = xmlDoc.createElement "AnimPresets"
			root.appendChild animPresetsElement
			for animPreset in animPresets do
			(
				local animPresetElement = xmlDoc.createElement "AnimPreset"
				animPresetsElement.appendChild animPresetElement
				
				animPresetElement.setAttribute "nameParts" (AsString animPreset.nameParts)
				animPresetElement.setAttribute "path" (AsString animPreset.path)
				animPresetElement.setAttribute "enabled" (AsString animPreset.enabled)
				animPresetElement.setAttribute "color" (AsString animPreset.color)
				animPresetElement.setAttribute "start" (AsString animPreset.frameStart)
				animPresetElement.setAttribute "end" (AsString animPreset.frameEnd)
				animPresetElement.setAttribute "pose" (AsString animPreset.pose)
				animPresetElement.setAttribute "loop" (AsString animPreset.loop)
				
				local activeLayersElement = xmlDoc.createElement "ActiveLayers"
				animPresetElement.appendChild activeLayersElement
				for activeLayer in animPreset.activeLayers where (findItem charLayers activeLayer) != 0 do
				(
					local activeLayerElement = xmlDoc.createElement "ActiveLayer"
					activeLayerElement.innerText = activeLayer
					activeLayersElement.appendChild activeLayerElement
				)
			)
		)
		
		local nodes = #()
		join nodes bipedNodes
		join nodes normalNodes
		if nodes.count > 0 then
		(
			local nodesElement = xmlDoc.createElement "Nodes"
			root.appendChild nodesElement
			
			for node in nodes do
				nodesElement.appendChild (node.asXml xmlDoc)
		)
		
		local layers = #()
		local uncombinedNormalLayers = for l in normalLayerAnimations collect l
		for bipedLayer in bipedLayerAnimations do
		(
			local layerMatch = false
			for i=1 to uncombinedNormalLayers.count while not layerMatch do
				if bipedLayer.layerName == uncombinedNormalLayers[i].layerName then
				(
					append layers (CombineLayerAnimations bipedLayer uncombinedNormalLayers[i])
					
					deleteItem uncombinedNormalLayers i
					layerMatch = true
				)
			
			if not layerMatch then
				append layers bipedLayer
		)
		join layers uncombinedNormalLayers
		if layers.count > 0 then
		(
			local layersElement = xmlDoc.createElement "LayerAnimations"
			root.appendChild layersElement
			
			for layer in layers do
				layersElement.appendChild (layer.asXml xmlDoc)
		)
		
		if params.count > 0 then
		(
			local paramsElement = xmlDoc.createElement "Parameters"
			root.appendChild paramsElement
			
			for param in params do
				paramsElement.appendChild (param.asXml xmlDoc)
		)
		
		root
	)
)

-- Retrieves all the nodes from the biped as a list of MaxNode.
-- This list is already sorted by hierarchy.
fn GetBipedNodes charAnim maxNodeList:#() =
(
	-- Gets the structure containing all the biped nodes organized by chain.
	local bip = charAnim.bip
	local bipNodes = getBipNodes bip
	
	-- ZEBESIAN TWEAK
	local isZebesian = bip.name == "zebesian_bip"
	
	-- Adds the biped's nodes in order.
	local sortedBipedObjects = #()
	
	local bipMaxNode = MaxNode.create bipNodes.bipNode maxNodeList:maxNodeList nameRemap:"body_C0_ctl" parent:undefined exportPosition:True
	append sortedBipedObjects bipMaxNode
	
	append sortedBipedObjects (MaxNode.create bipNodes.pelvis maxNodeList:maxNodeList nameRemap:"pelvis_C0_ctl")
	
	append sortedBipedObjects (MaxNode.create bipNodes.spine[1] parent:bipMaxNode maxNodeList:maxNodeList nameRemap:("spine_C0_fk0_ctl"))
	for i = 2 to bipNodes.spine.count - 1 do append sortedBipedObjects (MaxNode.create bipNodes.spine[i] maxNodeList:maxNodeList nameRemap:("spine_C0_fk"+ (i-1) as string +"_ctl"))
	local lastSpineMaxNode = MaxNode.create bipNodes.spine[bipNodes.spine.count] maxNodeList:maxNodeList nameRemap:("spine_C0_fk"+ (bipNodes.spine.count-1) as string +"_ctl")
	append sortedBipedObjects lastSpineMaxNode
	
	for i = 1 to bipNodes.neck.count do append sortedBipedObjects (MaxNode.create bipNodes.neck[i] maxNodeList:maxNodeList nameRemap:("neck_C0_fk"+ (i-1) as string +"_ctl") axisRemap:#(3, 1, 2))
	append sortedBipedObjects (MaxNode.create bipNodes.head parent:bipMaxNode maxNodeList:maxNodeList nameRemap:"neck_C0_head_ctl" axisRemap:#(3, 1, 2))
	
	if bipNodes.lArm != undefined then
	(
		append sortedBipedObjects (MaxNode.create bipNodes.lArm[1] parent:lastSpineMaxNode ikLimb:charAnim.leftArmNode maxNodeList:maxNodeList nameRemap:"shoulder_L0_ctl")
		append sortedBipedObjects (MaxNode.create bipNodes.lArm[2] parent:bipMaxNode ikLimb:charAnim.leftArmNode maxNodeList:maxNodeList nameRemap:"arm_L0_fk0_ctl")
		for i = 3 to bipNodes.lArm.count - 1 do append sortedBipedObjects (MaxNode.create bipNodes.lArm[i] ikLimb:charAnim.leftArmNode maxNodeList:maxNodeList nameRemap:("arm_L0_fk"+ (i-2) as string +"_ctl"))
		append sortedBipedObjects (MaxNode.create bipNodes.lArm[bipNodes.lArm.count] ikLimb:charAnim.leftArmNode maxNodeList:maxNodeList nameRemap:("arm_L0_fk"+ (bipNodes.lArm.count-2) as string +"_ctl")  axisRemap:(if isZebesian then #(1 ,2, 3) else #(1, 3, -2)))
		for i = 1 to bipNodes.lFingers.count do append sortedBipedObjects (MaxNode.create bipNodes.lFingers[i] ikLimb:charAnim.leftArmNode maxNodeList:maxNodeList nameRemap:("finger_L"+ ((i-1)/bip.controller.fingerLinks) as string +"_fk"+ ((mod (i-1) bip.controller.fingerLinks) as integer) as string +"_ctl"))
	)
	
	if bipNodes.rArm != undefined then
	(
		append sortedBipedObjects (MaxNode.create bipNodes.rArm[1] parent:lastSpineMaxNode ikLimb:charAnim.rightArmNode maxNodeList:maxNodeList nameRemap:"shoulder_R0_ctl" axisRemap:#(-1, -2, 3))
		append sortedBipedObjects (MaxNode.create bipNodes.rArm[2] parent:bipMaxNode ikLimb:charAnim.rightArmNode maxNodeList:maxNodeList nameRemap:"arm_R0_fk0_ctl" axisRemap:#(-1, -2, 3))
		for i = 3 to bipNodes.rArm.count - 1 do append sortedBipedObjects (MaxNode.create bipNodes.rArm[i] ikLimb:charAnim.rightArmNode maxNodeList:maxNodeList nameRemap:("arm_R0_fk"+ (i-2) as string +"_ctl") axisRemap:#(-1, -2, 3))
		append sortedBipedObjects (MaxNode.create bipNodes.rArm[bipNodes.rArm.count] ikLimb:charAnim.rightArmNode maxNodeList:maxNodeList nameRemap:("arm_R0_fk"+ (bipNodes.rArm.count-2) as string +"_ctl"))	-- The right hand doesn't actually have any axis difference
		for i = 1 to bipNodes.rFingers.count do append sortedBipedObjects (MaxNode.create bipNodes.rFingers[i] ikLimb:charAnim.rightArmNode maxNodeList:maxNodeList nameRemap:("finger_R"+ ((i-1)/bip.controller.fingerLinks) as string +"_fk"+ ((mod (i-1) bip.controller.fingerLinks) as integer) as string +"_ctl") axisRemap:#(-1, -2, 3))
	)
	
	if bipNodes.lLeg != undefined then
	(
		append sortedBipedObjects (MaxNode.create bipNodes.lLeg[1] parent:bipMaxNode ikLimb:charAnim.leftLegNode maxNodeList:maxNodeList nameRemap:("leg_L0_fk0_ctl") forceRemap:false)
		for i = 2 to bipNodes.lLeg.count - 1 do append sortedBipedObjects (MaxNode.create bipNodes.lLeg[i] ikLimb:charAnim.leftLegNode maxNodeList:maxNodeList nameRemap:("leg_L0_fk"+ (i-1) as string +"_ctl") forceRemap:false)
		append sortedBipedObjects (MaxNode.create bipNodes.lLeg[bipNodes.lLeg.count] ikLimb:charAnim.leftLegNode maxNodeList:maxNodeList nameRemap:("leg_L0_fk"+ (bipNodes.lLeg.count-1) as string +"_ctl") forceRemap:false axisRemap:#(2, -1, 3))
		for i = 1 to bipNodes.lToes.count do append sortedBipedObjects (MaxNode.create bipNodes.lToes[i] ikLimb:charAnim.leftLegNode maxNodeList:maxNodeList nameRemap:("foot_L"+ ((i-1)/bip.controller.toeLinks) as string +"_fk"+ ((mod (i-1) bip.controller.toeLinks) as integer) as string +"_ctl") forceRemap:false)
	)
	
	if bipNodes.rLeg != undefined then
	(
		append sortedBipedObjects (MaxNode.create bipNodes.rLeg[1] parent:bipMaxNode ikLimb:charAnim.rightLegNode maxNodeList:maxNodeList nameRemap:("leg_R0_fk0_ctl") forceRemap:false axisRemap:#(-1, -2, 3))
		for i = 2 to bipNodes.rLeg.count - 1 do append sortedBipedObjects (MaxNode.create bipNodes.rLeg[i] ikLimb:charAnim.rightLegNode maxNodeList:maxNodeList nameRemap:("leg_R0_fk"+ (i-1) as string +"_ctl") forceRemap:false axisRemap:#(-1, -2, 3))
		append sortedBipedObjects (MaxNode.create bipNodes.rLeg[bipNodes.rLeg.count] ikLimb:charAnim.rightLegNode maxNodeList:maxNodeList nameRemap:("leg_R0_fk"+ (bipNodes.rLeg.count-1) as string +"_ctl") forceRemap:false axisRemap:#(-2, 1, 3))
		for i = 1 to bipNodes.rToes.count do append sortedBipedObjects (MaxNode.create bipNodes.rToes[i] ikLimb:charAnim.rightLegNode maxNodeList:maxNodeList nameRemap:("foot_R"+ ((i-1)/bip.controller.toeLinks) as string +"_fk"+ ((mod (i-1) bip.controller.toeLinks) as integer) as string +"_ctl") forceRemap:false axisRemap:#(-1, -2, 3))
	)
	
	for xtraChain in bipNodes.xtras do
		for i = 1 to xtraChain.count do append sortedBipedObjects (MaxNode.create xtraChain[i] maxNodeList:maxNodeList exportPosition:True)
	if bipNodes.tail != undefined then
		for i = 1 to bipNodes.tail.count do append sortedBipedObjects (MaxNode.create bipNodes.tail[i] maxNodeList:maxNodeList)
	if bipNodes.pony1 != undefined then
		for i = 1 to bipNodes.pony1.count do append sortedBipedObjects (MaxNode.create bipNodes.pony1[i] maxNodeList:maxNodeList)
	if bipNodes.pony2 != undefined then
		for i = 1 to bipNodes.pony2.count do append sortedBipedObjects (MaxNode.create bipNodes.pony2[i] maxNodeList:maxNodeList)
	
	if bipNodes.prop1 != undefined and bipNodes.prop1[1] != undefined then append sortedBipedObjects (MaxNode.create bipNodes.prop1[1] maxNodeList:maxNodeList reparent:true nameRemap:"Prop1_C0_ctl" storeBaseTransform:True exportPosition:True)
	if bipNodes.prop2 != undefined and bipNodes.prop2[1] != undefined then append sortedBipedObjects (MaxNode.create bipNodes.prop2[1] maxNodeList:maxNodeList reparent:true nameRemap:"Prop2_C0_ctl" storeBaseTransform:True exportPosition:True)
	if bipNodes.prop3 != undefined and bipNodes.prop3[1] != undefined then append sortedBipedObjects (MaxNode.create bipNodes.prop3[1] maxNodeList:maxNodeList reparent:true nameRemap:"Prop3_C0_ctl" storeBaseTransform:True exportPosition:True)
	
	return sortedBipedObjects
)

-- Returns which layers are required to be active in order to properly apply the animation for a layer.
-- This information is infered based on the animation presets configured on the infoChar.
fn GetRequiredLayers infoChar layerName =
(
	local charLayers = infoChar.GetAllAnimLayerInfo()
	local layerIndex = findItem charLayers layerName
	charLayers = for i = 1 to layerIndex - 1 collect charLayers[i]
	
	local requiredLayers = #()
	local excludedLayers = #()
	local animPresets = (infoChar.GetAllAnimPresetStruct()).animPresets
	for animPreset in animPresets where (findItem animPreset.activeLayers layerName) != 0 do
		for layer in charLayers do
			if (findItem animPreset.activeLayers layer) != 0 then
			(
				if (findItem requiredLayers layer) == 0 then
				(
					append requiredLayers layer
					if (findItem excludedLayers layer) != 0 then
						logger.logWarning ("The layer [" + layerName + "] has inconsistent dependencies on the layer [" + layer + "]!")
				)
			)
			else
			(
				if (findItem excludedLayers layer) == 0 then
				(
					append excludedLayers layer
					if (findItem requiredLayers layer) != 0 then
						logger.logWarning ("The layer [" + layerName + "] has inconsistent dependencies on the layer [" + layer + "]!")
				)
			)
	
	requiredLayers
)

-- Returns a CharacterAnimation struct containing all the animation data for the character.
fn GetCharacterAnimation infoChar =
(
	-- Multiple bipeds are not currently supported.
	if infoChar.aBip.count > 1 then
		logger.logWarning ("Multiple bipeds are not supported. Only the first one will be exported.")
	
	-- Creates the structure that will hold all the data.
	local charAnim = CharacterAnimation infoChar
	
	-- If there is a biped on the scene, retrieves all it's nodes.
	if infoChar.aBip.count >= 1 then
	(
		charAnim.bip = infoChar.aBip[1].node.controller.rootNode
		
		-- Resets the InPlace mode
		charAnim.bip.controller.inPlaceMode = False
		
		charAnim.rightArmNode = biped.getNode charAnim.bip.controller #rarm
		charAnim.leftArmNode = biped.getNode charAnim.bip.controller #larm
		charAnim.rightLegNode = biped.getNode charAnim.bip.controller #rleg
		charAnim.leftLegNode = biped.getNode charAnim.bip.controller #lleg
		
		charAnim.bipedNodes = GetBipedNodes charAnim
	)
	
	-- Adds all the normal nodes.
	local maxNodes = #()
	for normalNode in normalNodes do
	(
		local n = normalNode.createFromStoredName maxNodeList:(maxNodes + charAnim.bipedNodes)
		if n != undefined then
			append maxNodes n
	)
	charAnim.normalNodes = maxNodes
	
	-- Adds the DC controls to the list.
	-- NOTE: InfoChar doesn't currently provide all the character's controls. As such, only the DC controls' animation is retrieved.
	-- In order to do this, first looks for the character's DC_Root node, then it's control and finally all the nodes on it's layer.
	local dcRoot = undefined
	for exportBone in infoChar.aExpBn while dcRoot == undefined do
		if exportBone.node.name == "DC_Root" then
			dcRoot = exportBone.node
	if dcRoot == undefined then
		logger.logWarning ("The character doesn't have a DC_Root node.")
	else if classOf dcRoot.position.controller != Position_Constraint then
		logger.logWarning ("The DC_Root node doesn't have a PositionConstraint controller.")
	else
	(
		-- Finds the DC_Root control and then retrieves all the nodes on it's layer.
		local dcRootController = dcRoot.position.controller.getNode 1
		local dcControls = #()
		dcRootController.layer.nodes &dcControls
		
		-- Creates the MaxNode objects.
		local prefix = (infoChar.sCharName) + "_"
		local maxNodeList = for maxNode in charAnim.bipedNodes collect maxNode
		maxNodeList += charAnim.normalNodes
		local maxNodes = for dc in dcControls collect MaxNode.create dc reparent:True nameRemap:(substituteString dc.name prefix "") forceRemap:false maxNodeList:maxNodeList storeBaseTransform:False exportPosition:True	axisRemap:#(1, 3, -2)	-- We don't make them store their base transform yet since we need them all to be created before doing that
		
		-- The DC's might be linked to another DC's, so we need to make them look for their parent once again.
		maxNodeList += maxNodes
		for dc in maxNodes do
		(
			dc.lookForParent maxNodeList
			dc.storeTransform()
		)
		
		-- Sorts the list based on hierarchy.
		for i = 1 to maxNodes.count do
		(
			local idx = i
			for j = i+1 to maxNodes.count do
			(
				if maxNodes[idx].parent != undefined and maxNodes[idx].parent.node == maxNodes[j].node then
				(
					local temp = maxNodes[idx]
					deleteItem maxNodes idx
					insertItem temp maxNodes j
					idx = j
				)
			)
		)
		
		join charAnim.normalNodes maxNodes
	)
	
	-- Retrieves the animation data from the biped.
	if charAnim.bip != undefined then
	(
		charAnim.bipedLayerAnimations = #()
		for i = 0 to biped.numLayers charAnim.bip.controller collect
		(			
			-- Sets the current biped layer and enables it.
			biped.setCurrentLayer charAnim.bip.controller i
			biped.setLayerActive charAnim.bip.controller i true
			
			-- Updates the IKs from the base layer in case there is a retarget
			if i != 0 then
				biped.retargetToBaseLayer charAnim.bip.controller false
			
			-- Retrieves the layer's animation.
			local layerName = biped.getLayerName charAnim.bip.controller i
			local requiredLayers = GetRequiredLayers infoChar layerName
			infoChar.SetActiveAnimLayer (requiredLayers + #(layerName))
			local layerAnim = LayerAnimation.create layerName charAnim.bipedNodes charAnim isBiped:True requiredLayers:requiredLayers
			append charAnim.bipedLayerAnimations layerAnim
			
			windows.processPostedMessages()
		)
	)
	
	-- Retrieves the animation data from the normal nodes.
	if charAnim.normalNodes.count > 0 then
	(
		-- Retrieves the list of normal layers for the character.
		local layers = #("Original")
		local layerSetIndex = 0
		if AnimationLayersRollout != undefined then
		(
			layerSetIndex = AnimationLayersRollout.GetLayerSetIndexFromName infoChar.sCharName
			if layerSetIndex != 0 then
			(
				layers = AnimationLayersRollout.GetLayerNamesFromLayerSet layerSetIndex
				layers[1] = "Original"	-- We use Original as the base layer name to be consistent with Biped
			)
		)
		
		charAnim.normalLayerAnimations = for i=1 to layers.count collect
		(			
			-- Sets the current layer
			if layerSetIndex != 0 then
			(
				AnimationLayersRollout.SelectLayer i layerSetIndex:layerSetIndex
				AnimationLayersRollout.SetLayerVisibility layerSetIndex i true
			)
			
			-- Retrieves the layer's animation.
			local layerAnim = LayerAnimation.create layers[i] charAnim.normalNodes charAnim
			windows.processPostedMessages()
			layerAnim
		)
	)
	
	-- Retrieves the animation data for the parameters.
	for param in params where param.isValid() do
	(
		-- AnimationLayers are unsupported for parameters, so we just store the values on the Param struct
		param.storeAnimation()
		
		-- Only stores the param if it has animation
		if param.hasAnimation() then
			append charAnim.params param
		
		windows.processPostedMessages()
	)
	
	return charAnim
)

-- Saves a character animation into a custom xml file.
fn SaveCharacterAnimation charAnim filePath =
(
	local xmlDoc = dotNetObject "System.Xml.XmlDocument"
	
	xmlDoc.appendChild (charAnim.asXml xmlDoc)
	
	xmlDoc.save filePath
)

fn ExportCharacterAnimation infoChar filePath processScripts:globalProcessScripts =
(
	local projectDir = getCtrPipelineDir "PRJ"
	for processScript  in processScripts do
		fileIn (projectDir + processScript)
	
	local charAnim = GetCharacterAnimation infoChar
	SaveCharacterAnimation charAnim filePath
)

fn ExportAllCharacterAnimations filePath:undefined =
(	
	local infoChars = getClassInstances MSE_InfoChar
	if infoChars.count == 0 then
	(
		logger.logError ("There are no characters on the scene!")
		return ok
	)
	
	if filePath == undefined then
	(
		filePath = getSaveFileName caption:"Copy Biped Animation" filename:(substituteString maxFileName ".max" ".mxca") types:"Max Character Animation (*.mxca)|*mxca" historyCategory:"MaxCharacterAnimationHistory" 
		if filePath == undefined then
			return ok
	)
	
	if not matchPattern filePath pattern:"*.mxca" then
		filePath += ".mxca"
	
	if infoChars.count == 1 then
		ExportCharacterAnimation infoChars[1] filePath
	else
		for infoChar in infoChars do ExportCharacterAnimation infoChar (substituteString filePath ".mxca" ("_" + infoChar.sCharName + ".mxca"))
)

fn BatchExport files:unsupplied outputFolder:unsupplied finalLog:true processScripts:globalProcessScripts =
(
	if files == unsupplied then
	(
		local fileBrowser = DotNetObject "System.Windows.Forms.OpenFileDialog"
		fileBrowser.multiSelect = true
		fileBrowser.title = "Select Files to Export"
		fileBrowser.initialDirectory = maxFilePath
		fileBrowser.filter = "Max Files (*.max)|*max"
		local result = fileBrowser.ShowDialog()
		if result.Equals result.OK then
			files = fileBrowser.fileNames
		else
			return ok
	)
	
	if outputFolder == unsupplied then
	(
		local splitPath = filterString files[1] "\\"
		deleteItem splitPath splitPath.count
		local initialDir = ""
		for p in splitPath do
			initialDir += p + "\\"
		
		outputFolder = getSavePath caption:"Select Export Folder" initialDir:initialDir
		if outputFolder == undefined then
			return ok
	)
	
	if outputFolder[outputFolder.count] != "\\" then
		outputFolder += "\\"
	
	local currentLogFile = logSystem.getNetLogFileName() 
	local currentLogger = logger
	logSystem.logName (outputFolder + "log.txt")
	logSystem.longevity = #forever 
	logSystem.quietMode = True
	
	local processLogger = MessageLogger()
	local logs = #()
	
	processLogger.logInfo  "---------------------------"
	processLogger.logInfo "Batch Export"
	processLogger.logInfo "---------------------------"
	
	local actorName = undefined
	for file in files do
	(
		local fileExportLogger = MessageLogger()
		logger = fileExportLogger
		append logs #(file, fileExportLogger)
		
		try
		(			
			fileExportLogger.logInfo ("Opening file: " + file)
			local loadSuccessfull = loadMaxFile file quiet:true
			if loadSuccessfull then
			(
				local infoChars = getClassInstances MSE_InfoChar
				if infoChars.count == 0 then
				(
					fileExportLogger.logError "There are no InfoChars on the scene! Skipping..."
				)
				else if infoChars.count > 0 then
				(
					if actorName == undefined then
						actorName = infoChars[1].sCharName
						processLogger.logInfo ("Actor Found: " + actorName)
					
					local actorInfoChars = for infoChar in infoChars where infoChar.sCharName == actorName collect infoChar
					if actorInfoChars.count == 0 then
					(
						fileExportLogger.logError ("There are no InfoChars for " + actorName + " on the scene! Skipping...")
					)
					else
					(
						if actorInfoChars.count > 1 then
						(
							fileExportLogger.logWarning ("There are multiple InfoChars for " + actorName + "! Only the first one will be exported.")
						)
						if infoChars.count != actorInfoChars.count then
						(
							fileExportLogger.logWarning ("There are InfoChars for characters other than " + actorName + "! Only the " + actorName + " InfoChar will be exported.")
						)
						
						try
						(
							fileExportLogger.logInfo "Exporting Animation..."
							
							local infoChar = actorInfoChars[1]
							local filePath = outputFolder + (substituteString maxFileName ".max" ".mxca")
							ExportCharacterAnimation infoChar filePath processScripts:processScripts
							
							fileExportLogger.logInfo "File exported successfully!"
						)
						catch
						(
							fileExportLogger.logError ("An error occurred when exporting file: " + file + "\n" + getCurrentException())
						)
						
						gc()
					)
				)
			)
			else
			(
				fileExportLogger.logError ("Unable to open file: " + file)
			)
		)
		catch
		(
			fileExportLogger.logError ("Unexpected error when exporting file: " + file + "\n" + getCurrentException())
		)
		
		processLogger.appendLogger fileExportLogger
		processLogger.logInfo  "---------------------------"
	)
	
	processLogger.logInfo "Export Finished"
	processLogger.logInfo  "---------------------------"
	
	if finalLog then
	(
		local finalLogger = MessageLogger()

		local headerPrinted = False
		for fileLog in logs do
		(
			try
			(
				local file = fileLog[1]
				local logger = fileLog[2]
				if logger.warnings.count > 0 then
				(
					if not headerPrinted then
					(
						finalLogger.logInfo "The following files produced WARNINGS when exporting:"
						finalLogger.logInfo  "---------------------------"
						headerPrinted = true
					)
					
					processLogger.logInfo file
					for warning in logger.warnings do
						finalLogger.logWarning warning
					finalLogger.logInfo  "---------------------------"
				)
			)
			catch
			(
				processLogger.logError ("Unexpected error when logging the final results!")
			)
		)

		headerPrinted = False
		for fileLog in logs do
		(
			try
			(
				local file = fileLog[1]
				local logger = fileLog[2]
				if logger.errors.count > 0 then
				(
					if not headerPrinted then
					(
						finalLogger.logInfo "The following files produced ERRORS when exporting:"
						finalLogger.logInfo  "---------------------------"
						headerPrinted = true
					)
					
					processLogger.logInfo file
					for error in logger.errors do
						finalLogger.logError error
					finalLogger.logInfo  "---------------------------"
				)
			)
			catch
			(
				processLogger.logError ("Unexpected error when logging the final results!")
			)
		)

		processLogger.appendLogger finalLogger
	)
	
	logger = currentLogger
	logSystem.logName currentLogFile
	logSystem.quietMode = False

	shellLaunch outputFolder ""
	
	return ok
)
