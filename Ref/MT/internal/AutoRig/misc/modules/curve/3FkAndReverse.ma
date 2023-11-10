//Maya ASCII 2020 scene
//Name: 3FkAndReverse.ma
//Last modified: Mon, Jul 18, 2022 04:25:00 PM
//Codeset: 1252
file -rdi 1 -ns "Main" -rfn "MainRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 1 -ns "Rev" -rfn "RevRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -r -ns "Main" -dr 1 -rfn "MainRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -r -ns "Rev" -dr 1 -rfn "RevRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "8845B0F1-4BDC-E04A-A843-699A0464FD86";
createNode transform -s -n "persp";
	rename -uid "8CD630A7-499E-4718-8761-F0ADAB366494";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 21.53265148971122 12.27112253367261 30.06010882255428 ;
	setAttr ".r" -type "double3" -15.338352729616764 39.400000000001384 1.0289945948215235e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0E28CED5-40F8-D9B2-F283-9C918C3FEE30";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 37.497772516979097;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "73BE527B-401A-9C4A-0630-58928C2BD3E5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -2.7644549103228946 1000.1 -1.3756772593300761 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "40758B38-4A85-51E7-937E-17B30C11B961";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 25.219510884170894;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "11F1322C-4C03-6D1A-7BE2-6B8DD47B04AA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -3.6167432429127691 4.5841561946234908 1000.1031825519401 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "050A230B-4411-4C24-D6E3-8A9316705DA9";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1031825519401;
	setAttr ".ow" 31.480153698912016;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "03091BE6-4D66-0CED-4A5D-F086AF689B2F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 3.1384753970586359 1.5571909996420863 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "162695FD-4776-A12A-918A-39967B503A3C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 26.557443491816045;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Sys_00_grp";
	rename -uid "38B0ABEF-4C4A-0846-0CC8-7981ED3C809D";
	setAttr ".v" no;
createNode transform -n "SplLinear_00_crv" -p "Sys_00_grp";
	rename -uid "14514565-494E-AA17-974E-57985B03A192";
createNode nurbsCurve -n "SplLinear_00_crvShape" -p "SplLinear_00_crv";
	rename -uid "6F0A7719-4353-24DF-ECEB-D9804747325F";
	setAttr -k off ".v";
	setAttr -s 3 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		0 -4.4408920985006262e-16 0
		0 5 0
		0 10 0
		;
createNode transform -n "SplQuadratic_00_crv" -p "Sys_00_grp";
	rename -uid "38A601B8-460B-0D6D-3075-2F9F28F84A13";
createNode nurbsCurve -n "SplQuadratic_00_crvShape" -p "SplQuadratic_00_crv";
	rename -uid "7C22463B-440E-C9A1-5A77-DEB3C4FD6EFB";
	setAttr -k off ".v";
	setAttr -s 3 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		0 -4.4408920985006262e-16 0
		0 5 0
		0 10 0
		;
createNode fosterParent -n "MainRNfosterParent1";
	rename -uid "4D957E6B-44F3-B90B-E90B-74AAC1ACFB40";
createNode transform -n "SplRev_02_mstc" -p "MainRNfosterParent1";
	rename -uid "06E079F4-4258-7DC7-D7D6-A38F7D984252";
	addAttr -w false -s false -h true -sn "_deletable_" -ln "_deletable_" -dv 1 -min 
		0 -max 1 -at "bool";
createNode transform -n "Rev:TplTpl_00_hrch" -p "MainRNfosterParent1";
	rename -uid "F3E3BC7B-417A-B0AF-20CC-1EAABA97382B";
	setAttr ".v" no;
createNode fosterParent -n "RevRNfosterParent1";
	rename -uid "41640AC0-4EA5-FBF2-A8B6-29BF03E0E138";
createNode parentConstraint -n "FkTpl_00_root_parentConstraint1" -p "RevRNfosterParent1";
	rename -uid "0ADE008B-4B4C-8F3A-F843-13B0B70A8868";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkTpl_02_rootW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -10 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "FkTpl_01_root_parentConstraint1" -p "RevRNfosterParent1";
	rename -uid "65B83969-4492-3CE9-4000-0FA6D8E07B85";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkTpl_01_rootW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 -5 5 ;
	setAttr ".rst" -type "double3" 0 0 5 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "FkTpl_02_root_parentConstraint1" -p "RevRNfosterParent1";
	rename -uid "C476182F-429F-3CB8-E50F-BAAD417F57CE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkTpl_00_rootW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".tg[0].tot" -type "double3" 0 0 10 ;
	setAttr ".rst" -type "double3" 0 0 5 ;
	setAttr -k on ".w0";
createNode transform -n "Spl_02_loc" -p "RevRNfosterParent1";
	rename -uid "6803CAEC-46CA-D35D-8998-F4B92B528298";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Spl_02_locShape" -p "Spl_02_loc";
	rename -uid "1A644A8E-4DCB-FDFB-20DD-C7A315457C70";
	setAttr -k off ".v" no;
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "SplRev_01_mstc" -p "RevRNfosterParent1";
	rename -uid "A815D880-431C-033D-D6D4-33BCFDD081D2";
	addAttr -w false -s false -h true -sn "_deletable_" -ln "_deletable_" -dv 1 -min 
		0 -max 1 -at "bool";
createNode parentConstraint -n "SplRevMstc_01_prc" -p "SplRev_01_mstc";
	rename -uid "F4A57E93-4D34-C700-59C0-3EAB57313C3C";
	addAttr -w false -s false -h true -sn "_deletable_" -ln "_deletable_" -dv 1 -min 
		0 -max 1 -at "bool";
createNode parentConstraint -n "Rev:Fk_01_root_parentConstraint1" -p "RevRNfosterParent1";
	rename -uid "FD6C6065-4C56-196E-A747-1DA904E90090";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplRev_01_mstcW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 -5 0 ;
	setAttr -k on ".w0";
createNode transform -n "Spl_01_loc" -p "RevRNfosterParent1";
	rename -uid "61A3A773-4788-CA07-05B4-0E944179C789";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Spl_01_locShape" -p "Spl_01_loc";
	rename -uid "D6796FD3-41CF-B005-ED2B-B9BCC88CF47F";
	setAttr -k off ".v" no;
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode transform -n "SplRev_00_mstc" -p "RevRNfosterParent1";
	rename -uid "9799C16C-4819-0784-5F58-848171534FFB";
	addAttr -w false -s false -h true -sn "_deletable_" -ln "_deletable_" -dv 1 -min 
		0 -max 1 -at "bool";
createNode parentConstraint -n "SplRevMstc_00_prc" -p "SplRev_00_mstc";
	rename -uid "9D722FCA-4D19-2DBA-70F8-E19BD684065C";
	addAttr -w false -s false -h true -sn "_deletable_" -ln "_deletable_" -dv 1 -min 
		0 -max 1 -at "bool";
createNode parentConstraint -n "Rev:Fk_02_root_parentConstraint1" -p "RevRNfosterParent1";
	rename -uid "7D0538BF-4E8A-E279-78E4-3D8648DF0724";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplRev_00_mstcW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr -k off ".tx";
	setAttr -k off ".ty";
	setAttr -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -k off ".sx";
	setAttr -k off ".sy";
	setAttr -k off ".sz";
	setAttr ".erp" yes;
	setAttr ".rst" -type "double3" 0 -5 0 ;
	setAttr -k on ".w0";
createNode transform -n "Spl_00_loc" -p "RevRNfosterParent1";
	rename -uid "FAE5FC4E-4C51-AF71-D252-0F926AE55FC1";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Spl_00_locShape" -p "Spl_00_loc";
	rename -uid "69262011-4D00-34F2-56CE-DFBA62E8B4B7";
	setAttr -k off ".v" no;
	setAttr ".los" -type "double3" 0.25 0.25 0.25 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "21BA693C-4966-7647-7DA5-ECAED4C13A48";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "2EAC49F7-4133-03C2-FDE7-7ABE1E50D95B";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "ED8A6424-451D-654A-DA0A-26BF5B8EC43C";
createNode displayLayerManager -n "layerManager";
	rename -uid "1B4F04F0-43D2-E116-FC52-9F93F3D761D3";
createNode displayLayer -n "defaultLayer";
	rename -uid "2B6B19EA-43DB-595E-754B-1F88F425A5D4";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "F96FF215-4402-42B3-B2EE-419F9F6ACB25";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "404520E2-4500-95B9-5E7D-6ABE1FDBE8FD";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "0AADCFD6-4149-4F77-342A-2FBADDD7C91D";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1195\n            -height 702\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n"
		+ "            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n"
		+ "            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n"
		+ "            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n"
		+ "                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n"
		+ "                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n"
		+ "                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n"
		+ "\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n"
		+ "                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n"
		+ "                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n"
		+ "                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 0\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n"
		+ "\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -editorChanged \"updateModelPanelBar\" \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n"
		+ "                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n"
		+ "                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n"
		+ "                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n"
		+ "            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1195\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1195\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "1B0EF228-4785-DEB8-10E7-ECBB0BF1D4EA";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode controller -n "SplRev_00_tag";
	rename -uid "EE431800-4D73-D33A-633E-B28CC23B7C2F";
createNode reference -n "MainRN";
	rename -uid "7B147137-4051-7133-10C9-FDB64C8A71EE";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
	setAttr -s 33 ".phl";
	setAttr ".phl[30]" 0;
	setAttr ".phl[56]" 0;
	setAttr ".phl[57]" 0;
	setAttr ".phl[58]" 0;
	setAttr ".phl[59]" 0;
	setAttr ".phl[60]" 0;
	setAttr ".phl[61]" 0;
	setAttr ".phl[62]" 0;
	setAttr ".phl[63]" 0;
	setAttr ".phl[64]" 0;
	setAttr ".phl[65]" 0;
	setAttr ".phl[66]" 0;
	setAttr ".phl[67]" 0;
	setAttr ".phl[68]" 0;
	setAttr ".phl[69]" 0;
	setAttr ".phl[70]" 0;
	setAttr ".phl[71]" 0;
	setAttr ".phl[72]" 0;
	setAttr ".phl[73]" 0;
	setAttr ".phl[74]" 0;
	setAttr ".phl[75]" 0;
	setAttr ".phl[76]" 0;
	setAttr ".phl[77]" 0;
	setAttr ".phl[78]" 0;
	setAttr ".phl[79]" 0;
	setAttr ".phl[80]" 0;
	setAttr ".phl[81]" 0;
	setAttr ".phl[82]" 0;
	setAttr ".phl[83]" 0;
	setAttr ".phl[84]" 0;
	setAttr ".phl[85]" 0;
	setAttr ".phl[86]" 0;
	setAttr ".phl[87]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"MainRN"
		"MainRN" 2
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root|Main:FkTpl_03_jnt.message" 
		"MainRN.placeHolderList[30]" ""
		5 3 "MainRN" "Main:TemplateSet.message" "MainRN.placeHolderList[56]" 
		""
		"MainRN" 33
		0 "|MainRNfosterParent1|Rev:TplTpl_00_hrch" "|Main:Tpl_00_tpl" "-s -r "
		0 "|MainRNfosterParent1|SplRev_02_mstc" "|Main:input_00_link|Main:Fk_00_root|Main:Fk_00_ctr|Main:Fk_01_root|Main:Fk_01_ctr|Main:Fk_02_root|Main:Fk_02_ctr" 
		"-s -r "
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.translate" "MainRN.placeHolderList[57]" 
		""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.rotatePivot" "MainRN.placeHolderList[58]" 
		""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.rotatePivotTranslate" 
		"MainRN.placeHolderList[59]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.rotate" "MainRN.placeHolderList[60]" 
		""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.rotateOrder" "MainRN.placeHolderList[61]" 
		""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root.parentMatrix" "MainRN.placeHolderList[62]" 
		""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.scale" 
		"MainRN.placeHolderList[63]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.translate" 
		"MainRN.placeHolderList[64]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.rotatePivot" 
		"MainRN.placeHolderList[65]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.rotatePivotTranslate" 
		"MainRN.placeHolderList[66]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.rotate" 
		"MainRN.placeHolderList[67]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.rotateOrder" 
		"MainRN.placeHolderList[68]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root.parentMatrix" 
		"MainRN.placeHolderList[69]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.scale" 
		"MainRN.placeHolderList[70]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.translate" 
		"MainRN.placeHolderList[71]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.rotatePivot" 
		"MainRN.placeHolderList[72]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.rotatePivotTranslate" 
		"MainRN.placeHolderList[73]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.rotate" 
		"MainRN.placeHolderList[74]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.rotateOrder" 
		"MainRN.placeHolderList[75]" ""
		5 3 "MainRN" "|Main:Tpl_00_tpl|Main:FkTpl_00_root|Main:FkTpl_01_root|Main:FkTpl_02_root.parentMatrix" 
		"MainRN.placeHolderList[76]" ""
		5 3 "MainRN" "|Main:input_00_link.instObjGroups" "MainRN.placeHolderList[77]" 
		""
		5 3 "MainRN" "|Main:input_00_link|Main:Fk_00_root|Main:Fk_00_ctr.worldMatrix" 
		"MainRN.placeHolderList[78]" ""
		5 3 "MainRN" "|Main:input_00_link|Main:Fk_00_root|Main:Fk_00_ctr|Main:Fk_01_root|Main:Fk_01_ctr.worldMatrix" 
		"MainRN.placeHolderList[79]" ""
		5 3 "MainRN" "|Main:input_00_link|Main:Fk_00_root|Main:Fk_00_ctr|Main:Fk_01_root|Main:Fk_01_ctr.worldInverseMatrix" 
		"MainRN.placeHolderList[80]" ""
		5 3 "MainRN" "|Main:input_00_link|Main:Fk_00_root|Main:Fk_00_ctr|Main:Fk_01_root|Main:Fk_01_ctr|Main:Fk_02_root|Main:Fk_02_ctr.worldInverseMatrix" 
		"MainRN.placeHolderList[81]" ""
		5 3 "MainRN" "Main:ControlsSet.message" "MainRN.placeHolderList[82]" 
		""
		5 3 "MainRN" "Main:SkinJointsSet.message" "MainRN.placeHolderList[83]" 
		""
		5 2 "MainRN" "Main:MetadataTemplate._postExecution[0]" "MainRN.placeHolderList[84]" 
		""
		5 3 "MainRN" "Main:LinkSet.message" "MainRN.placeHolderList[85]" ""
		5 1 "MainRN" "|Main:Fk_00_jnt|Main:Fk_01_jnt|Main:Fk_02_jnt.message" 
		"MainRN.placeHolderList[86]" ""
		5 1 "MainRN" "Main:MetadataTemplate.message" "MainRN.placeHolderList[87]" 
		"";
lockNode -l 1 ;
createNode reference -n "RevRN";
	rename -uid "FA981822-4F01-38EF-4B8C-588D1E0B78EC";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma{1}";
	setAttr -s 56 ".phl";
	setAttr ".phl[35]" 0;
	setAttr ".phl[86]" 0;
	setAttr ".phl[87]" 0;
	setAttr ".phl[88]" 0;
	setAttr ".phl[89]" 0;
	setAttr ".phl[90]" 0;
	setAttr ".phl[91]" 0;
	setAttr ".phl[92]" 0;
	setAttr ".phl[93]" 0;
	setAttr ".phl[94]" 0;
	setAttr ".phl[95]" 0;
	setAttr ".phl[96]" 0;
	setAttr ".phl[97]" 0;
	setAttr ".phl[98]" 0;
	setAttr ".phl[99]" 0;
	setAttr ".phl[100]" 0;
	setAttr ".phl[101]" 0;
	setAttr ".phl[102]" 0;
	setAttr ".phl[103]" 0;
	setAttr ".phl[104]" 0;
	setAttr ".phl[105]" 0;
	setAttr ".phl[106]" 0;
	setAttr ".phl[107]" 0;
	setAttr ".phl[108]" 0;
	setAttr ".phl[109]" 0;
	setAttr ".phl[110]" 0;
	setAttr ".phl[111]" 0;
	setAttr ".phl[112]" 0;
	setAttr ".phl[113]" 0;
	setAttr ".phl[114]" 0;
	setAttr ".phl[115]" 0;
	setAttr ".phl[116]" 0;
	setAttr ".phl[117]" 0;
	setAttr ".phl[118]" 0;
	setAttr ".phl[119]" 0;
	setAttr ".phl[120]" 0;
	setAttr ".phl[121]" 0;
	setAttr ".phl[122]" 0;
	setAttr ".phl[123]" 0;
	setAttr ".phl[124]" 0;
	setAttr ".phl[125]" 0;
	setAttr ".phl[126]" 0;
	setAttr ".phl[127]" 0;
	setAttr ".phl[128]" 0;
	setAttr ".phl[129]" 0;
	setAttr ".phl[130]" 0;
	setAttr ".phl[131]" 0;
	setAttr ".phl[132]" 0;
	setAttr ".phl[133]" 0;
	setAttr ".phl[134]" 0;
	setAttr ".phl[135]" 0;
	setAttr ".phl[136]" 0;
	setAttr ".phl[137]" 0;
	setAttr ".phl[138]" 0;
	setAttr ".phl[139]" 0;
	setAttr ".phl[140]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"RevRN"
		"RevRN" 2
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root|Rev:FkTpl_03_jnt.message" 
		"RevRN.placeHolderList[35]" ""
		5 3 "RevRN" "Rev:TemplateSet.message" "RevRN.placeHolderList[86]" ""
		
		"RevRN" 66
		0 "|Rev:input_00_link" "|MainRNfosterParent1|SplRev_02_mstc" "-s -r "
		0 "|Rev:Tpl_00_tpl" "|MainRNfosterParent1|Rev:TplTpl_00_hrch" "-s -r "
		0 "|RevRNfosterParent1|Spl_00_loc" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root|Rev:Fk_02_ctr" 
		"-s -r "
		0 "|RevRNfosterParent1|Rev:Fk_02_root_parentConstraint1" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root" 
		"-s -r "
		0 "|RevRNfosterParent1|SplRev_00_mstc" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr" 
		"-s -r "
		0 "|RevRNfosterParent1|Spl_01_loc" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr" 
		"-s -r "
		0 "|RevRNfosterParent1|Rev:Fk_01_root_parentConstraint1" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root" 
		"-s -r "
		0 "|RevRNfosterParent1|SplRev_01_mstc" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr" 
		"-s -r "
		0 "|RevRNfosterParent1|Spl_02_loc" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr" 
		"-s -r "
		0 "|RevRNfosterParent1|FkTpl_02_root_parentConstraint1" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root" 
		"-s -r "
		0 "|RevRNfosterParent1|FkTpl_01_root_parentConstraint1" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root" 
		"-s -r "
		0 "|RevRNfosterParent1|FkTpl_00_root_parentConstraint1" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root" 
		"-s -r "
		5 1 "RevRN" "Rev:MetadataTemplate.message" "RevRN.placeHolderList[87]" 
		""
		5 2 "RevRN" "|Rev:Fk_00_jnt.parent" "RevRN.placeHolderList[88]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.parentInverseMatrix" 
		"RevRN.placeHolderList[89]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.translateY" 
		"RevRN.placeHolderList[90]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.translateZ" 
		"RevRN.placeHolderList[91]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.translateX" 
		"RevRN.placeHolderList[92]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotateX" 
		"RevRN.placeHolderList[93]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotateY" 
		"RevRN.placeHolderList[94]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotateZ" 
		"RevRN.placeHolderList[95]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotateOrder" 
		"RevRN.placeHolderList[96]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotatePivot" 
		"RevRN.placeHolderList[97]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root.rotatePivotTranslate" 
		"RevRN.placeHolderList[98]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.parentInverseMatrix" 
		"RevRN.placeHolderList[99]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.translateY" 
		"RevRN.placeHolderList[100]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.translateZ" 
		"RevRN.placeHolderList[101]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.translateX" 
		"RevRN.placeHolderList[102]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotateX" 
		"RevRN.placeHolderList[103]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotateY" 
		"RevRN.placeHolderList[104]" ""
		5 4 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotateZ" 
		"RevRN.placeHolderList[105]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotateOrder" 
		"RevRN.placeHolderList[106]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotatePivot" 
		"RevRN.placeHolderList[107]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root.rotatePivotTranslate" 
		"RevRN.placeHolderList[108]" ""
		5 3 "RevRN" "|MainRNfosterParent1|SplRev_02_mstc|Rev:input_00_link|Rev:Fk_00_root|Rev:Fk_00_ctr|Rev:Fk_01_root|Rev:Fk_01_ctr|Rev:Fk_02_root|Rev:Fk_02_ctr|Rev:output_00_link.instObjGroups" 
		"RevRN.placeHolderList[109]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotateX" 
		"RevRN.placeHolderList[110]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotateY" 
		"RevRN.placeHolderList[111]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotateZ" 
		"RevRN.placeHolderList[112]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotateOrder" 
		"RevRN.placeHolderList[113]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.parentInverseMatrix" 
		"RevRN.placeHolderList[114]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotatePivot" 
		"RevRN.placeHolderList[115]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root.rotatePivotTranslate" 
		"RevRN.placeHolderList[116]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.translateX" 
		"RevRN.placeHolderList[117]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.translateY" 
		"RevRN.placeHolderList[118]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.translateZ" 
		"RevRN.placeHolderList[119]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotateX" 
		"RevRN.placeHolderList[120]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotateY" 
		"RevRN.placeHolderList[121]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotateZ" 
		"RevRN.placeHolderList[122]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotateOrder" 
		"RevRN.placeHolderList[123]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.parentInverseMatrix" 
		"RevRN.placeHolderList[124]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotatePivot" 
		"RevRN.placeHolderList[125]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root.rotatePivotTranslate" 
		"RevRN.placeHolderList[126]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.translateX" 
		"RevRN.placeHolderList[127]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.translateY" 
		"RevRN.placeHolderList[128]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.translateZ" 
		"RevRN.placeHolderList[129]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotateX" 
		"RevRN.placeHolderList[130]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotateY" 
		"RevRN.placeHolderList[131]" ""
		5 4 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotateZ" 
		"RevRN.placeHolderList[132]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotateOrder" 
		"RevRN.placeHolderList[133]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.parentInverseMatrix" 
		"RevRN.placeHolderList[134]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotatePivot" 
		"RevRN.placeHolderList[135]" ""
		5 3 "RevRN" "|MainRNfosterParent1|Rev:TplTpl_00_hrch|Rev:Tpl_00_tpl|Rev:FkTpl_00_root|Rev:FkTpl_01_root|Rev:FkTpl_02_root.rotatePivotTranslate" 
		"RevRN.placeHolderList[136]" ""
		5 3 "RevRN" "Rev:ControlsSet.message" "RevRN.placeHolderList[137]" ""
		
		5 3 "RevRN" "Rev:SkinJointsSet.message" "RevRN.placeHolderList[138]" 
		""
		5 2 "RevRN" "Rev:MetadataTemplate._preExecution[0]" "RevRN.placeHolderList[139]" 
		""
		5 3 "RevRN" "Rev:LinkSet.message" "RevRN.placeHolderList[140]" "";
lockNode -l 1 ;
createNode objectSet -n "ControlsSet";
	rename -uid "2CA51A01-44EC-08B6-6AF4-289C327D607B";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "B60EF9BD-40AB-4E0B-E32C-F0AEEF306834";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dnsm";
createNode reference -n "sharedReferenceNode";
	rename -uid "53A54C6D-4ACC-071F-89BA-39908D8C6021";
	setAttr ".ed" -type "dataReferenceEdits" 
		"sharedReferenceNode";
createNode objectSet -n "LinkSet";
	rename -uid "98A85AFD-43EE-B612-7902-D79162672573";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr -s 2 ".dnsm";
createNode objectSet -n "Secondaries";
	rename -uid "81B0EAEF-4701-D18E-2E9A-2DAC839FEBCA";
	setAttr ".ihi" 0;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 1;
	setAttr -av -k on ".unw" 1;
	setAttr -av -k on ".etw";
	setAttr -av -k on ".tps";
	setAttr -av -k on ".tms";
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".st";
	setAttr -cb on ".an";
	setAttr -cb on ".pt";
select -ne :renderGlobalsList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultShaderList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 3 ".r";
select -ne :initialShadingGroup;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :initialParticleSE;
	setAttr -av -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".mwc";
	setAttr -cb on ".an";
	setAttr -cb on ".il";
	setAttr -cb on ".vo";
	setAttr -cb on ".eo";
	setAttr -cb on ".fo";
	setAttr -cb on ".epo";
	setAttr -k on ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr -k on ".cch";
	setAttr -k on ".nds";
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
	setAttr -k off ".eeaa";
	setAttr -k off ".engm";
	setAttr -k off ".mes";
	setAttr -k off ".emb";
	setAttr -k off ".mbbf";
	setAttr -k off ".mbs";
	setAttr -k off ".trm";
	setAttr -k off ".clmt";
	setAttr -k off ".twa";
	setAttr -k off ".twz";
	setAttr -k on ".hwcc";
	setAttr -k on ".hwdp";
	setAttr -k on ".hwql";
connectAttr "MainRN.phl[57]" "FkTpl_02_root_parentConstraint1.tg[0].tt";
connectAttr "MainRN.phl[58]" "FkTpl_02_root_parentConstraint1.tg[0].trp";
connectAttr "MainRN.phl[59]" "FkTpl_02_root_parentConstraint1.tg[0].trt";
connectAttr "MainRN.phl[60]" "FkTpl_02_root_parentConstraint1.tg[0].tr";
connectAttr "MainRN.phl[61]" "FkTpl_02_root_parentConstraint1.tg[0].tro";
connectAttr "MainRN.phl[62]" "FkTpl_02_root_parentConstraint1.tg[0].tpm";
connectAttr "MainRN.phl[63]" "FkTpl_01_root_parentConstraint1.tg[0].ts";
connectAttr "MainRN.phl[64]" "FkTpl_01_root_parentConstraint1.tg[0].tt";
connectAttr "MainRN.phl[65]" "FkTpl_01_root_parentConstraint1.tg[0].trp";
connectAttr "MainRN.phl[66]" "FkTpl_01_root_parentConstraint1.tg[0].trt";
connectAttr "MainRN.phl[67]" "FkTpl_01_root_parentConstraint1.tg[0].tr";
connectAttr "MainRN.phl[68]" "FkTpl_01_root_parentConstraint1.tg[0].tro";
connectAttr "MainRN.phl[69]" "FkTpl_01_root_parentConstraint1.tg[0].tpm";
connectAttr "MainRN.phl[70]" "FkTpl_00_root_parentConstraint1.tg[0].ts";
connectAttr "MainRN.phl[71]" "FkTpl_00_root_parentConstraint1.tg[0].tt";
connectAttr "MainRN.phl[72]" "FkTpl_00_root_parentConstraint1.tg[0].trp";
connectAttr "MainRN.phl[73]" "FkTpl_00_root_parentConstraint1.tg[0].trt";
connectAttr "MainRN.phl[74]" "FkTpl_00_root_parentConstraint1.tg[0].tr";
connectAttr "MainRN.phl[75]" "FkTpl_00_root_parentConstraint1.tg[0].tro";
connectAttr "MainRN.phl[76]" "FkTpl_00_root_parentConstraint1.tg[0].tpm";
connectAttr "MainRN.phl[77]" "LinkSet.dsm" -na;
connectAttr "MainRN.phl[78]" "SplRevMstc_00_prc.tg[0].tpm";
connectAttr "MainRN.phl[79]" "SplRevMstc_01_prc.tg[0].tpm";
connectAttr "MainRN.phl[80]" "SplRevMstc_00_prc.cpim";
connectAttr "MainRN.phl[81]" "SplRevMstc_01_prc.cpim";
connectAttr "MainRN.phl[82]" "ControlsSet.dnsm" -na;
connectAttr "MainRN.phl[83]" "SkinJointsSet.dnsm" -na;
connectAttr "RevRN.phl[87]" "MainRN.phl[84]";
connectAttr "MainRN.phl[85]" "LinkSet.dnsm" -na;
connectAttr "MainRN.phl[86]" "RevRN.phl[88]";
connectAttr "RevRN.phl[89]" "Rev:Fk_01_root_parentConstraint1.cpim";
connectAttr "Rev:Fk_01_root_parentConstraint1.cty" "RevRN.phl[90]";
connectAttr "Rev:Fk_01_root_parentConstraint1.ctz" "RevRN.phl[91]";
connectAttr "Rev:Fk_01_root_parentConstraint1.ctx" "RevRN.phl[92]";
connectAttr "Rev:Fk_01_root_parentConstraint1.crx" "RevRN.phl[93]";
connectAttr "Rev:Fk_01_root_parentConstraint1.cry" "RevRN.phl[94]";
connectAttr "Rev:Fk_01_root_parentConstraint1.crz" "RevRN.phl[95]";
connectAttr "RevRN.phl[96]" "Rev:Fk_01_root_parentConstraint1.cro";
connectAttr "RevRN.phl[97]" "Rev:Fk_01_root_parentConstraint1.crp";
connectAttr "RevRN.phl[98]" "Rev:Fk_01_root_parentConstraint1.crt";
connectAttr "RevRN.phl[99]" "Rev:Fk_02_root_parentConstraint1.cpim";
connectAttr "Rev:Fk_02_root_parentConstraint1.cty" "RevRN.phl[100]";
connectAttr "Rev:Fk_02_root_parentConstraint1.ctz" "RevRN.phl[101]";
connectAttr "Rev:Fk_02_root_parentConstraint1.ctx" "RevRN.phl[102]";
connectAttr "Rev:Fk_02_root_parentConstraint1.crx" "RevRN.phl[103]";
connectAttr "Rev:Fk_02_root_parentConstraint1.cry" "RevRN.phl[104]";
connectAttr "Rev:Fk_02_root_parentConstraint1.crz" "RevRN.phl[105]";
connectAttr "RevRN.phl[106]" "Rev:Fk_02_root_parentConstraint1.cro";
connectAttr "RevRN.phl[107]" "Rev:Fk_02_root_parentConstraint1.crp";
connectAttr "RevRN.phl[108]" "Rev:Fk_02_root_parentConstraint1.crt";
connectAttr "RevRN.phl[109]" "LinkSet.dsm" -na;
connectAttr "FkTpl_00_root_parentConstraint1.crx" "RevRN.phl[110]";
connectAttr "FkTpl_00_root_parentConstraint1.cry" "RevRN.phl[111]";
connectAttr "FkTpl_00_root_parentConstraint1.crz" "RevRN.phl[112]";
connectAttr "RevRN.phl[113]" "FkTpl_00_root_parentConstraint1.cro";
connectAttr "RevRN.phl[114]" "FkTpl_00_root_parentConstraint1.cpim";
connectAttr "RevRN.phl[115]" "FkTpl_00_root_parentConstraint1.crp";
connectAttr "RevRN.phl[116]" "FkTpl_00_root_parentConstraint1.crt";
connectAttr "FkTpl_01_root_parentConstraint1.ctx" "RevRN.phl[117]";
connectAttr "FkTpl_01_root_parentConstraint1.cty" "RevRN.phl[118]";
connectAttr "FkTpl_01_root_parentConstraint1.ctz" "RevRN.phl[119]";
connectAttr "FkTpl_01_root_parentConstraint1.crx" "RevRN.phl[120]";
connectAttr "FkTpl_01_root_parentConstraint1.cry" "RevRN.phl[121]";
connectAttr "FkTpl_01_root_parentConstraint1.crz" "RevRN.phl[122]";
connectAttr "RevRN.phl[123]" "FkTpl_01_root_parentConstraint1.cro";
connectAttr "RevRN.phl[124]" "FkTpl_01_root_parentConstraint1.cpim";
connectAttr "RevRN.phl[125]" "FkTpl_01_root_parentConstraint1.crp";
connectAttr "RevRN.phl[126]" "FkTpl_01_root_parentConstraint1.crt";
connectAttr "FkTpl_02_root_parentConstraint1.ctx" "RevRN.phl[127]";
connectAttr "FkTpl_02_root_parentConstraint1.cty" "RevRN.phl[128]";
connectAttr "FkTpl_02_root_parentConstraint1.ctz" "RevRN.phl[129]";
connectAttr "FkTpl_02_root_parentConstraint1.crx" "RevRN.phl[130]";
connectAttr "FkTpl_02_root_parentConstraint1.cry" "RevRN.phl[131]";
connectAttr "FkTpl_02_root_parentConstraint1.crz" "RevRN.phl[132]";
connectAttr "RevRN.phl[133]" "FkTpl_02_root_parentConstraint1.cro";
connectAttr "RevRN.phl[134]" "FkTpl_02_root_parentConstraint1.cpim";
connectAttr "RevRN.phl[135]" "FkTpl_02_root_parentConstraint1.crp";
connectAttr "RevRN.phl[136]" "FkTpl_02_root_parentConstraint1.crt";
connectAttr "RevRN.phl[137]" "ControlsSet.dnsm" -na;
connectAttr "RevRN.phl[138]" "SkinJointsSet.dnsm" -na;
connectAttr "MainRN.phl[87]" "RevRN.phl[139]";
connectAttr "RevRN.phl[140]" "LinkSet.dnsm" -na;
connectAttr "Spl_00_locShape.wp" "SplLinear_00_crvShape.cp[0]";
connectAttr "Spl_01_locShape.wp" "SplLinear_00_crvShape.cp[1]";
connectAttr "Spl_02_locShape.wp" "SplLinear_00_crvShape.cp[2]";
connectAttr "Spl_00_locShape.wp" "SplQuadratic_00_crvShape.cp[0]";
connectAttr "Spl_01_locShape.wp" "SplQuadratic_00_crvShape.cp[1]";
connectAttr "Spl_02_locShape.wp" "SplQuadratic_00_crvShape.cp[2]";
connectAttr "FkTpl_00_root_parentConstraint1.w0" "FkTpl_00_root_parentConstraint1.tg[0].tw"
		;
connectAttr "FkTpl_01_root_parentConstraint1.w0" "FkTpl_01_root_parentConstraint1.tg[0].tw"
		;
connectAttr "FkTpl_02_root_parentConstraint1.w0" "FkTpl_02_root_parentConstraint1.tg[0].tw"
		;
connectAttr "SplRevMstc_01_prc.ct" "SplRev_01_mstc.t";
connectAttr "SplRevMstc_01_prc.cr" "SplRev_01_mstc.r";
connectAttr "SplRev_01_mstc.t" "Rev:Fk_01_root_parentConstraint1.tg[0].tt";
connectAttr "SplRev_01_mstc.rp" "Rev:Fk_01_root_parentConstraint1.tg[0].trp";
connectAttr "SplRev_01_mstc.rpt" "Rev:Fk_01_root_parentConstraint1.tg[0].trt";
connectAttr "SplRev_01_mstc.r" "Rev:Fk_01_root_parentConstraint1.tg[0].tr";
connectAttr "SplRev_01_mstc.ro" "Rev:Fk_01_root_parentConstraint1.tg[0].tro";
connectAttr "SplRev_01_mstc.s" "Rev:Fk_01_root_parentConstraint1.tg[0].ts";
connectAttr "SplRev_01_mstc.pm" "Rev:Fk_01_root_parentConstraint1.tg[0].tpm";
connectAttr "Rev:Fk_01_root_parentConstraint1.w0" "Rev:Fk_01_root_parentConstraint1.tg[0].tw"
		;
connectAttr "SplRevMstc_00_prc.ct" "SplRev_00_mstc.t";
connectAttr "SplRevMstc_00_prc.cr" "SplRev_00_mstc.r";
connectAttr "SplRev_00_mstc.t" "Rev:Fk_02_root_parentConstraint1.tg[0].tt";
connectAttr "SplRev_00_mstc.rp" "Rev:Fk_02_root_parentConstraint1.tg[0].trp";
connectAttr "SplRev_00_mstc.rpt" "Rev:Fk_02_root_parentConstraint1.tg[0].trt";
connectAttr "SplRev_00_mstc.r" "Rev:Fk_02_root_parentConstraint1.tg[0].tr";
connectAttr "SplRev_00_mstc.ro" "Rev:Fk_02_root_parentConstraint1.tg[0].tro";
connectAttr "SplRev_00_mstc.s" "Rev:Fk_02_root_parentConstraint1.tg[0].ts";
connectAttr "SplRev_00_mstc.pm" "Rev:Fk_02_root_parentConstraint1.tg[0].tpm";
connectAttr "Rev:Fk_02_root_parentConstraint1.w0" "Rev:Fk_02_root_parentConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "SplRev_00_tag.msg" "SplRev_00_tag.child[0]";
connectAttr "MainRNfosterParent1.msg" "MainRN.fp";
connectAttr "sharedReferenceNode.sr" "MainRN.sr";
connectAttr "RevRNfosterParent1.msg" "RevRN.fp";
connectAttr "sharedReferenceNode.sr" "RevRN.sr";
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of 3FkAndReverse.ma
