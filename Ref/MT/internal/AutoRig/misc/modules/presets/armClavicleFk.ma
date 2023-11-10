//Maya ASCII 2020 scene
//Name: armClavicleFk.ma
//Last modified: Tue, Jul 19, 2022 11:19:40 AM
//Codeset: 1252
file -rdi 1 -ns "Arm" -rfn "ArmRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
file -rdi 1 -ns "Hand" -rfn "HandRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/hand/5fingers/3Bones.ma";
file -rdi 2 -ns "FingerA" -rfn "Hand:FingerARN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 2 -ns "FingerB" -rfn "Hand:FingerBRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 2 -ns "FingerC" -rfn "Hand:FingerCRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 2 -ns "FingerD" -rfn "Hand:FingerDRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 2 -ns "FingerE" -rfn "Hand:FingerERN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/3Bones.ma";
file -rdi 1 -ns "Clavicle" -rfn "ClavicleRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/1Bone.ma";
file -r -ns "Arm" -dr 1 -rfn "ArmRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
file -r -ns "Hand" -dr 1 -rfn "HandRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/hand/5fingers/3Bones.ma";
file -r -ns "Clavicle" -dr 1 -rfn "ClavicleRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/1Bone.ma";
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "AE6C24D5-4484-712F-E158-E6822512A056";
createNode transform -s -n "persp";
	rename -uid "418A2578-44B5-D298-D7BD-36BE4AFFCB81";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 27.633053749306562 58.939512581256061 75.489867326510705 ;
	setAttr ".r" -type "double3" -38.738352729606511 -0.60000000000022125 -1.2424722979911184e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0B335899-489D-9E3A-AD36-CA9F90F23A6C";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 115.49416925230713;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "D55A2844-41D3-4993-93DA-FB9DAA296BFC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "1AE68668-4A8C-BF9A-051A-DD9E2D7275AD";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "4E139485-4121-5782-6934-A9893945F9B9";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "8473F687-4285-D584-28F0-0DB96F8C9185";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "42BEEB94-4935-1A8E-1933-F2B5CCEAE91F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "6B9D2E62-4346-12DF-AC43-299DDB52630E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "ArmExtra:FkWorld_00_spc";
	rename -uid "A52BC46A-4303-4680-1B99-F7B52D3DDAFC";
	setAttr ".v" no;
createNode transform -n "ArmExtra:FkCog_00_spc";
	rename -uid "BEC4BFBA-4923-F216-E499-6BA8685AE775";
	setAttr ".v" no;
createNode transform -n "ArmExtra:FkChest_00_spc";
	rename -uid "D6ABD168-4ADD-82AE-D56F-6599214E0344";
	setAttr ".v" no;
createNode transform -n "ArmExtra:IkPoleWorld_00_spc";
	rename -uid "A71B49EE-4A89-8E81-85FE-EAB6166079A5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 55 0 0 ;
createNode transform -n "ArmExtra:IkPoleCog_00_spc";
	rename -uid "01B99959-4B97-6DAA-2374-39A652F793B5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 55 0 0 ;
createNode transform -n "ArmExtra:IkWorld_00_spc";
	rename -uid "553A7660-401D-D13B-CF6C-2789AE9680ED";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "ArmExtra:IkCog_00_spc";
	rename -uid "BCFB32B4-496F-03C7-B8F4-B682B3A2C9C5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "ArmExtra:IkPointA_00_root";
	rename -uid "DE1A8A09-4B9C-DC9A-FDE5-76BB84BE88D6";
createNode transform -n "ArmExtra:IkPointA_00_ctr" -p "ArmExtra:IkPointA_00_root";
	rename -uid "80A7027B-4256-27A8-9D55-288385A00B97";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ArmExtra:IkPointA_00_ctrShape" -p "ArmExtra:IkPointA_00_ctr";
	rename -uid "48D4CD91-4A71-251E-A476-C78D8B813E15";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-5 0 -7.5710346436608233e-07
		1.1356551965491235e-06 0 -5
		0 -5 0
		5 0 0
		-3.7855173218304117e-07 0 5
		0 -5 0
		-5 0 -7.5710346436608233e-07
		-3.7855173218304117e-07 0 5
		0 5 0
		5 0 0
		1.1356551965491235e-06 0 -5
		0 5 0
		-5 0 -7.5710346436608233e-07
		;
createNode transform -n "ArmExtra:IkPointB_00_root";
	rename -uid "3BE6FE41-48C9-0080-055C-879FF61CFACF";
createNode transform -n "ArmExtra:IkPointB_00_ctr" -p "ArmExtra:IkPointB_00_root";
	rename -uid "18DD822A-4BD1-FCF2-5CDE-6BA6864897D4";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "ArmExtra:IkPointB_00_ctrShape" -p "ArmExtra:IkPointB_00_ctr";
	rename -uid "3E8E840F-4674-5978-5478-F8A02A1F44B6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 12 0 no 3
		13 0 1 2 3 4 5 6 7 8 9 10 11 12
		13
		-5 0 -7.5710346436608233e-07
		1.1356551965491235e-06 0 -5
		0 -5 0
		5 0 0
		-3.7855173218304117e-07 0 5
		0 -5 0
		-5 0 -7.5710346436608233e-07
		-3.7855173218304117e-07 0 5
		0 5 0
		5 0 0
		1.1356551965491235e-06 0 -5
		0 5 0
		-5 0 -7.5710346436608233e-07
		;
createNode fosterParent -n "ArmRNfosterParent1";
	rename -uid "504273CC-4143-ED92-3F7F-53ACB38ECFB7";
createNode transform -n "ArmExtra:Tpl_00_tpl" -p "ArmRNfosterParent1";
	rename -uid "918B400D-4709-D1B3-A65B-E68CB9905FC4";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "ArmExtra:IkWorldTpl_00_spc" -p "ArmExtra:Tpl_00_tpl";
	rename -uid "C5A7A8D3-4E09-3806-BE00-A0A6F2675086";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
	setAttr -s 4 "._relatedTo";
createNode locator -n "ArmExtra:IkWorldTpl_00_spcShape" -p "ArmExtra:IkWorldTpl_00_spc";
	rename -uid "48FC7F92-4632-B4FF-40E2-C6AB433F4BF6";
	setAttr -k off ".v";
createNode transform -n "Hand:TplTpl_00_hrch" -p "ArmRNfosterParent1";
	rename -uid "CE8B8A91-46E1-A591-D968-09A5CFBD9230";
	setAttr ".t" -type "double3" -50 -3.3306690738754696e-16 0 ;
createNode transform -n "Hand:inputLink_00_hrch" -p "ArmRNfosterParent1";
	rename -uid "407A3626-4A7C-D2F1-AE39-E2BB093AF8F9";
	setAttr ".t" -type "double3" 5.9685589803848416e-13 0 -1.1693265830365727e-08 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode transform -n "ArmExtra:SpaceSwitch_00_root" -p "ArmRNfosterParent1";
	rename -uid "ADDAF18C-4AB2-E57E-758F-EF9E2BB71C51";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "ArmExtra:SpaceSwitch_00_ctr" -p "ArmExtra:SpaceSwitch_00_root";
	rename -uid "20D4EB73-432C-B6E4-7402-24965E0DE517";
	addAttr -ci true -k true -sn "fk" -ln "fk" -min 0 -max 2 -en "world:cog:chest" 
		-at "enum";
	addAttr -ci true -sn "pole" -ln "pole" -min 0 -max 2 -en "world:cog:hand" -at "enum";
	addAttr -ci true -sn "ik" -ln "ik" -min 0 -max 3 -en "world:cog:pointA:pointB" -at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".fk";
	setAttr -k on ".pole";
	setAttr -k on ".ik";
createNode nurbsCurve -n "ArmExtra:SpaceSwitch_00_ctrShape" -p "ArmExtra:SpaceSwitch_00_ctr";
	rename -uid "B2CA4CB5-4EE5-1877-CCFE-16B5ACBDE2C7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-1.1100856969603225e-16 -1.1081941875543884 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		6.7857323231109122e-17 1.1081941875543877 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode parentConstraint -n "Arm:Ik_01_prc" -p "ArmRNfosterParent1";
	rename -uid "EBF64451-4F85-F26A-48D3-98A7F35C9955";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkWorld_00_spcW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "IkCog_00_spcW1" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w2" -ln "IkPointA_00_spcW2" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w3" -ln "IkPointB_00_spcW3" -dv 1 -min 0 -at "double";
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
	setAttr -s 4 ".tg";
	setAttr ".int" 0;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
	setAttr -k on ".w3";
createNode transform -n "ArmExtra:IkPoleHand_00_spc" -p "ArmRNfosterParent1";
	rename -uid "55948337-4DA3-2348-AF0C-75B0D4A0B60B";
	setAttr ".v" no;
createNode orientConstraint -n "Fk_00_root_orientConstraint1" -p "ArmRNfosterParent1";
	rename -uid "EFC6396D-4CBE-3ADC-E813-039344385394";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkCOG_00_spcW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "FkChest_00_spcW1" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w2" -ln "FkWorld_00_spcW2" -dv 1 -min 0 -at "double";
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
	setAttr -s 3 ".tg";
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
createNode orientConstraint -n "Arm:IkPoleIksc_00_root_orientConstraint1" -p "ArmRNfosterParent1";
	rename -uid "75A60376-41F4-DA65-ED2B-B4BF6D5978CE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkPoleCog_00_spcW0" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "IkPoleHand_00_spcW1" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w2" -ln "IkPoleWorld_00_spcW2" -dv 1 -min 0 
		-at "double";
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
	setAttr -s 3 ".tg";
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
createNode fosterParent -n "ClavicleRNfosterParent1";
	rename -uid "589C652D-4A85-CDF7-122B-5CBFB1E85C21";
createNode transform -n "Arm:inputLink_00_hrch" -p "ClavicleRNfosterParent1";
	rename -uid "EB5E2D3A-46DF-8E36-77BC-909EE307BF61";
createNode transform -n "Arm:TplTpl_00_hrch" -p "ClavicleRNfosterParent1";
	rename -uid "746A467E-484E-1690-B3E1-289B7778AC3A";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "0874A7F1-429E-2AAF-D839-7BB7380F93AE";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "B3D06924-44EE-FAF0-5BD7-86968A4EE8A5";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "1772F27D-403B-B30C-D504-44AFFEDD7BFE";
createNode displayLayerManager -n "layerManager";
	rename -uid "831137BA-4218-B645-17FA-6D9E49C40EB1";
createNode displayLayer -n "defaultLayer";
	rename -uid "D2226347-45A0-2AD3-A377-689D66B7FC7E";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "69D57A0B-4C6C-68F6-0B56-F784FC6C982C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "F316C3FB-4E32-220C-D94D-E2A848054B0B";
	setAttr ".g" yes;
createNode reference -n "ArmRN";
	rename -uid "91418DA6-4082-2B2F-C19D-64836082DF01";
	setAttr -s 2 ".fn";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
	setAttr ".fn[1]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/2BonesAdvanced.ma";
	setAttr -s 63 ".phl";
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
	setAttr ".phl[141]" 0;
	setAttr ".phl[142]" 0;
	setAttr ".phl[143]" 0;
	setAttr ".phl[144]" 0;
	setAttr ".phl[145]" 0;
	setAttr ".phl[146]" 0;
	setAttr ".phl[147]" 0;
	setAttr ".phl[148]" 0;
	setAttr ".phl[149]" 0;
	setAttr ".phl[150]" 0;
	setAttr ".phl[151]" 0;
	setAttr ".phl[152]" 0;
	setAttr ".phl[153]" 0;
	setAttr ".phl[154]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"ArmRN"
		"ArmRN" 7
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[1]" "ArmRN.placeHolderList[53]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[2]" "ArmRN.placeHolderList[54]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[3]" "ArmRN.placeHolderList[55]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[4]" "ArmRN.placeHolderList[56]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[5]" "ArmRN.placeHolderList[57]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._extendBehaviour[6]" "ArmRN.placeHolderList[58]" 
		""
		5 3 "ArmRN" "Arm:TemplateSet.message" "ArmRN.placeHolderList[92]" ""
		
		"ArmRN" 96
		0 "|Arm:Tpl_00_tpl" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch" 
		"-s -r "
		0 "|Arm:input_00_link" "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr|Clavicle:output_00_link|Arm:inputLink_00_hrch" 
		"-s -r "
		0 "|ArmRNfosterParent1|Arm:IkPoleIksc_00_root_orientConstraint1" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root" 
		"-s -r "
		0 "|ArmRNfosterParent1|Fk_00_root_orientConstraint1" "|Arm:Controls_00_grp|Arm:Fk_00_root" 
		"-s -r "
		0 "|ArmRNfosterParent1|ArmExtra:IkPoleHand_00_spc" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root|Arm:Ik_00_ctr" 
		"-s -r "
		0 "|ArmRNfosterParent1|Arm:Ik_01_prc" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root" 
		"-s -r "
		0 "|ArmRNfosterParent1|ArmExtra:SpaceSwitch_00_root" "|Arm:Controls_00_grp|Arm:Config_00_root|Arm:Config_00_ctr" 
		"-s -r "
		0 "|ArmRNfosterParent1|Hand:inputLink_00_hrch" "|Arm:output_00_link" "-s -r "
		
		0 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr|Arm:IkTpl_01_loc|Arm:IkTpl_00_ctr" 
		"-s -r "
		0 "|ArmRNfosterParent1|ArmExtra:Tpl_00_tpl" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl" 
		"-s -r "
		1 |Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr "armSpaceSwitch" "armSpaceSwitch" 
		" -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:chest\" -at \"enum\""
		1 |Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr 
		"armSpaceSwitch" "armSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:chest\" -at \"enum\""
		
		1 |Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr|Arm:Fk_02_root|Arm:Fk_02_ctr 
		"armSpaceSwitch" "armSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:chest\" -at \"enum\""
		
		1 |Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Twist_00_root|Arm:Twist_00_off|Arm:Twist_00_ctr 
		"elbowSpaceSwitch" "elbowSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:hand\" -at \"enum\""
		
		1 |Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root|Arm:Ik_00_ctr "handSpaceSwitch" 
		"handSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 3 -en \"world:cog:pointA:pointB\" -at \"enum\""
		
		1 |Arm:Controls_00_grp|Arm:Pin_01_root|Arm:Pin_01_ctr "elbowSpaceSwitch" 
		"elbowSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:hand\" -at \"enum\""
		
		2 "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root|Arm:IkPole_00_iksc" "rotate" " -type \"double3\" 0 0 0"
		
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr" "rotate" " -type \"double3\" 0 0 0"
		
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr" "rotateOrder" " 4"
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr" "armSpaceSwitch" " -k 1"
		
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr" 
		"rotateY" " 0"
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr" 
		"armSpaceSwitch" " -k 1"
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr|Arm:Fk_02_root|Arm:Fk_02_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr|Arm:Fk_02_root|Arm:Fk_02_ctr" 
		"armSpaceSwitch" " -k 1"
		2 "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Twist_00_root|Arm:Twist_00_off|Arm:Twist_00_ctr" 
		"elbowSpaceSwitch" " -k 1"
		2 "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root|Arm:Ik_00_ctr" "rotate" 
		" -type \"double3\" 0 0 0"
		2 "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root|Arm:Ik_00_ctr" "handSpaceSwitch" 
		" -k 1"
		2 "|Arm:Controls_00_grp|Arm:Pin_01_root|Arm:Pin_01_ctr" "elbowSpaceSwitch" 
		" -av -k 1"
		2 "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl" 
		"visibility" " 0"
		2 "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr" 
		"translate" " -type \"double3\" 10 0 0"
		3 "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr|Clavicle:output_00_link|Arm:inputLink_00_hrch|Arm:input_00_link.message" 
		"|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr._relatedTo[0]" 
		""
		3 "Arm:Ik_00_tag.message" "Arm:Ik_00_tag.children[0]" ""
		3 "Arm:Fk_02_tag.message" "Arm:Fk_02_tag.children[0]" ""
		3 "|Arm:Controls_00_grp|Arm:Fk_00_root.message" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:FKTpl_00_root._relatedTo[0]" 
		""
		3 "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.message" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr|Arm:IkTpl_01_loc|Arm:IkTpl_00_ctr|Arm:IkTpl_00_root._relatedTo[0]" 
		""
		5 3 "ArmRN" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root.parentInverseMatrix" 
		"ArmRN.placeHolderList[93]" ""
		5 4 "ArmRN" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root.rotateX" "ArmRN.placeHolderList[94]" 
		""
		5 4 "ArmRN" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root.rotateY" "ArmRN.placeHolderList[95]" 
		""
		5 4 "ArmRN" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root.rotateZ" "ArmRN.placeHolderList[96]" 
		""
		5 3 "ArmRN" "|Arm:Sys_00_grp|Arm:IkPoleIksc_00_root.rotateOrder" "ArmRN.placeHolderList[97]" 
		""
		5 2 "ArmRN" "|Arm:_00_jnt.parent" "ArmRN.placeHolderList[98]" ""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root.parentInverseMatrix" 
		"ArmRN.placeHolderList[99]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root.rotateX" "ArmRN.placeHolderList[100]" 
		""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root.rotateY" "ArmRN.placeHolderList[101]" 
		""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root.rotateZ" "ArmRN.placeHolderList[102]" 
		""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root.rotateOrder" "ArmRN.placeHolderList[103]" 
		""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr.armSpaceSwitch" 
		"ArmRN.placeHolderList[104]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr.armSpaceSwitch" 
		"ArmRN.placeHolderList[105]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Fk_00_root|Arm:Fk_00_ctr|Arm:Fk_01_root|Arm:Fk_01_ctr|Arm:Fk_02_root|Arm:Fk_02_ctr.armSpaceSwitch" 
		"ArmRN.placeHolderList[106]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Twist_00_root|Arm:Twist_00_off|Arm:Twist_00_ctr.elbowSpaceSwitch" 
		"ArmRN.placeHolderList[107]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.translateX" 
		"ArmRN.placeHolderList[108]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.translateY" 
		"ArmRN.placeHolderList[109]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.translateZ" 
		"ArmRN.placeHolderList[110]" ""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotatePivot" 
		"ArmRN.placeHolderList[111]" ""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotatePivotTranslate" 
		"ArmRN.placeHolderList[112]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotateX" 
		"ArmRN.placeHolderList[113]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotateY" 
		"ArmRN.placeHolderList[114]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotateZ" 
		"ArmRN.placeHolderList[115]" ""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.rotateOrder" 
		"ArmRN.placeHolderList[116]" ""
		5 3 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.parentInverseMatrix" 
		"ArmRN.placeHolderList[117]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root|Arm:Ik_00_ctr.handSpaceSwitch" 
		"ArmRN.placeHolderList[118]" ""
		5 4 "ArmRN" "|Arm:Controls_00_grp|Arm:Pin_01_root|Arm:Pin_01_ctr.elbowSpaceSwitch" 
		"ArmRN.placeHolderList[119]" ""
		5 2 "ArmRN" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr._relatedTo[0]" 
		"ArmRN.placeHolderList[120]" ""
		5 0 "ArmRN" "|Arm:Controls_00_grp|Arm:IkCtr_00_root|Arm:Ik_00_root.message" 
		"|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:OrigSystemTpl_00_tr|Arm:IkTpl_01_loc|Arm:IkTpl_00_ctr|Arm:IkTpl_00_root._relatedTo[0]" 
		"ArmRN.placeHolderList[121]" "ArmRN.placeHolderList[122]" "Arm:IkTpl_00_root._relatedTo[0]"
		
		5 4 "ArmRN" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:FKTpl_00_root._relatedTo[0]" 
		"ArmRN.placeHolderList[123]" ""
		5 4 "ArmRN" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:FKTpl_00_root._relatedTo[1]" 
		"ArmRN.placeHolderList[124]" ""
		5 4 "ArmRN" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root|Arm:TplTpl_00_hrch|Arm:Tpl_00_tpl|Arm:FKTpl_00_root._relatedTo[2]" 
		"ArmRN.placeHolderList[125]" ""
		5 3 "ArmRN" "Arm:SkinJointsSet.message" "ArmRN.placeHolderList[126]" 
		""
		5 3 "ArmRN" "Arm:ControlsSet.message" "ArmRN.placeHolderList[127]" ""
		
		5 3 "ArmRN" "Arm:LinkSet.message" "ArmRN.placeHolderList[128]" ""
		5 2 "ArmRN" "Arm:Ik_00_tag.children[0]" "ArmRN.placeHolderList[129]" 
		""
		5 2 "ArmRN" "Arm:Ik_00_tag.children[1]" "ArmRN.placeHolderList[130]" 
		""
		5 2 "ArmRN" "Arm:Ik_00_tag.children[2]" "ArmRN.placeHolderList[131]" 
		""
		5 2 "ArmRN" "Arm:Ik_00_tag.children[3]" "ArmRN.placeHolderList[132]" 
		""
		5 2 "ArmRN" "Arm:Ik_00_tag.children[4]" "ArmRN.placeHolderList[133]" 
		""
		5 2 "ArmRN" "Arm:Fk_02_tag.children[0]" "ArmRN.placeHolderList[134]" 
		""
		5 2 "ArmRN" "Arm:Fk_02_tag.children[1]" "ArmRN.placeHolderList[135]" 
		""
		5 2 "ArmRN" "Arm:Fk_02_tag.children[2]" "ArmRN.placeHolderList[136]" 
		""
		5 2 "ArmRN" "Arm:Fk_02_tag.children[3]" "ArmRN.placeHolderList[137]" 
		""
		5 2 "ArmRN" "Arm:Fk_02_tag.children[4]" "ArmRN.placeHolderList[138]" 
		""
		5 4 "ArmRN" "Arm:Ik.dagSetMembers" "ArmRN.placeHolderList[139]" ""
		5 4 "ArmRN" "Arm:Ik.dagSetMembers" "ArmRN.placeHolderList[140]" ""
		5 3 "ArmRN" "Arm:MetadataTemplate.message" "ArmRN.placeHolderList[141]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[0]" "ArmRN.placeHolderList[142]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[1]" "ArmRN.placeHolderList[143]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[2]" "ArmRN.placeHolderList[144]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[3]" "ArmRN.placeHolderList[145]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[4]" "ArmRN.placeHolderList[146]" 
		""
		5 2 "ArmRN" "Arm:MetadataTemplate._postExecution[5]" "ArmRN.placeHolderList[147]" 
		""
		5 4 "ArmRN" "Arm:MetadataTemplate._preExecution[0]" "ArmRN.placeHolderList[148]" 
		""
		5 1 "ArmRN" "|Arm:_00_jnt|Arm:_01_jnt|Arm:End_01_jnt.message" "ArmRN.placeHolderList[149]" 
		""
		5 1 "ArmRN" "Arm:Ik_00_tag.parent" "ArmRN.placeHolderList[150]" ""
		5 1 "ArmRN" "Arm:Twist_00_tag.parent" "ArmRN.placeHolderList[151]" ""
		
		5 1 "ArmRN" "Arm:Pin_01_tag.parent" "ArmRN.placeHolderList[152]" ""
		5 1 "ArmRN" "Arm:Fk_00_tag.parent" "ArmRN.placeHolderList[153]" ""
		5 1 "ArmRN" "Arm:MetadataTemplate.message" "ArmRN.placeHolderList[154]" 
		"";
lockNode -l 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "2BA48573-4811-25FF-F988-EB8F19C1D46C";
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
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1148\n            -height 702\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1148\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1148\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "5E217564-420C-D482-C8BC-77A4FF170231";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode choice -n "Arm:SpaceWorld_01_chc";
	rename -uid "18322FF4-4B02-57E0-C5F6-3DB9C6E1645A";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
createNode choice -n "Arm:SpaceCOG_00_chc";
	rename -uid "4DF4B126-4D78-8337-C4BB-FD84BA0C2402";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
createNode choice -n "Arm:SpaceChest_00_chc";
	rename -uid "AED907AE-4DA2-38F3-C175-DE9A5F98BC9E";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
createNode script -n "ArmExtra:MetadataTemplate";
	rename -uid "025BAD43-4C7C-B72F-ED13-78B0BBA86813";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" "import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#Arm:IkWorld_00_spc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this";
	setAttr -l on ".stp" 1;
createNode reference -n "sharedReferenceNode";
	rename -uid "461DF2A9-4C5D-B6C4-242B-A8B801952A8B";
	setAttr ".ed" -type "dataReferenceEdits" 
		"sharedReferenceNode";
createNode objectSet -n "ControlsSet";
	rename -uid "F7A71BE3-48A6-9E4F-B4AC-A29A789442BB";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "8D3D206B-4F06-1718-BA38-F8AC96DDB9D5";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode choice -n "Arm:Spaceworld_01_chc";
	rename -uid "2A7344F2-4A3A-A180-8994-1EA1BE9D30FE";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
createNode choice -n "Arm:Spacecog_01_chc";
	rename -uid "575089C0-4A9C-770E-B0B1-DE9FF7C27C00";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
createNode choice -n "Arm:SpacepointA_00_chc";
	rename -uid "BCE17404-46E0-7217-8CFF-7FBFC1EA12C1";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
	setAttr ".i[3]" 0;
createNode choice -n "Arm:SpacepointB_00_chc";
	rename -uid "2E82994E-427F-FA33-EF4B-A48988CD5167";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 1;
createNode controller -n "ArmExtra:IkPointA_00_tag";
	rename -uid "C0E39A6D-4A83-7F26-1207-669E6356B4C6";
createNode controller -n "ArmExtra:IkPointB_00_tag";
	rename -uid "BE99F4E3-40C8-CF4B-B79A-569D657E345A";
createNode nodeGraphEditorInfo -n "Arm:MayaNodeEditorSavedTabsInfo";
	rename -uid "3AE28B98-4BB9-DC9A-722E-198AE5ECB23C";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 102.17822867557646 -513.0163154400658 ;
	setAttr ".tgi[0].vh" -type "double2" 1509.2848344710339 618.66462983351096 ;
createNode reference -n "HandRN";
	rename -uid "A209361E-4CDB-04FF-8311-518D12EF6C10";
	setAttr -s 28 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".phl[21]" 0;
	setAttr ".phl[22]" 0;
	setAttr ".phl[23]" 0;
	setAttr ".phl[24]" 0;
	setAttr ".phl[25]" 0;
	setAttr ".phl[26]" 0;
	setAttr ".phl[27]" 0;
	setAttr ".phl[28]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"HandRN"
		"Hand:FingerARN" 0
		"HandRN" 0
		"Hand:FingerBRN" 0
		"Hand:FingerDRN" 0
		"Hand:FingerERN" 0
		"Hand:FingerCRN" 0
		"Hand:FingerARN" 7
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:FingerA:Tpl_00_tpl" 
		"visibility" " 0"
		2 "|ArmRNfosterParent1|Hand:inputLink_00_hrch|Hand:input_00_link|Hand:output_00_link|Hand:FingerA:input_00_link|Hand:FingerA:Fk_00_root|Hand:FingerA:Fk_00_ctr|Hand:FingerA:Fk_01_root" 
		"translate" " -type \"double3\" 0 0 4.99999999999999289"
		2 "|ArmRNfosterParent1|Hand:inputLink_00_hrch|Hand:input_00_link|Hand:output_00_link|Hand:FingerA:input_00_link|Hand:FingerA:Fk_00_root|Hand:FingerA:Fk_00_ctr|Hand:FingerA:Fk_01_root|Hand:FingerA:Fk_01_ctr|Hand:FingerA:Fk_02_root" 
		"translate" " -type \"double3\" 0 0 5.00000000000000711"
		5 1 "HandRN" "Hand:FingerA:Fk_00_tag.parent" "HandRN.placeHolderList[1]" 
		""
		5 1 "HandRN" "Hand:FingerA:Fk_00_tag.parent" "HandRN.placeHolderList[6]" 
		""
		5 1 "HandRN" "Hand:FingerA:MetadataTemplate.message" "HandRN.placeHolderList[12]" 
		""
		5 1 "HandRN" "Hand:FingerA:MetadataTemplate.message" "HandRN.placeHolderList[24]" 
		""
		"HandRN" 17
		0 "|Hand:Tpl_00_tpl" "|ArmRNfosterParent1|Hand:TplTpl_00_hrch" "-s -r "
		0 "|Hand:input_00_link" "|ArmRNfosterParent1|Hand:inputLink_00_hrch" "-s -r "
		
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl" "visibility" 
		" 0"
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt" 
		"translate" " -type \"double3\" 50 0 0"
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt" 
		"rotate" " -type \"double3\" 0 90 0"
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:MainTpl_00_jntShape" 
		"visibility" " -k 0 1"
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:MainTpl_00_jntShape" 
		"localPosition" " -type \"double3\" 0 0 3"
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:MainTpl_00_jntShape" 
		"localScale" " -type \"double3\" 2 0.5 2"
		2 "|ArmRNfosterParent1|Hand:inputLink_00_hrch|Hand:input_00_link" "translate" 
		" -type \"double3\" 0 0 0"
		2 "|ArmRNfosterParent1|Hand:inputLink_00_hrch|Hand:input_00_link" "rotate" 
		" -type \"double3\" 0 0 0"
		5 1 "HandRN" "Hand:MetadataTemplate.message" "HandRN.placeHolderList[11]" 
		""
		5 2 "HandRN" "|Hand:Main_00_jnt.parent" "HandRN.placeHolderList[17]" 
		""
		5 0 "HandRN" "Hand:Main_00_tag.message" "Hand:Main_00_tag.children[0]" 
		"HandRN.placeHolderList[18]" "HandRN.placeHolderList[19]" ""
		5 3 "HandRN" "Hand:ControlsSet.message" "HandRN.placeHolderList[20]" 
		""
		5 3 "HandRN" "Hand:SkinJointsSet.message" "HandRN.placeHolderList[21]" 
		""
		5 3 "HandRN" "Hand:LinkSet.message" "HandRN.placeHolderList[22]" ""
		5 1 "HandRN" "Hand:MetadataTemplate.message" "HandRN.placeHolderList[23]" 
		""
		"Hand:FingerBRN" 5
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:FingerB:Tpl_00_tpl" 
		"visibility" " 0"
		5 1 "HandRN" "Hand:FingerB:Fk_00_tag.parent" "HandRN.placeHolderList[2]" 
		""
		5 1 "HandRN" "Hand:FingerB:Fk_00_tag.parent" "HandRN.placeHolderList[7]" 
		""
		5 1 "HandRN" "Hand:FingerB:MetadataTemplate.message" "HandRN.placeHolderList[13]" 
		""
		5 1 "HandRN" "Hand:FingerB:MetadataTemplate.message" "HandRN.placeHolderList[25]" 
		""
		"Hand:FingerERN" 5
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:FingerE:Tpl_00_tpl" 
		"visibility" " 0"
		5 1 "HandRN" "Hand:FingerE:Fk_00_tag.parent" "HandRN.placeHolderList[5]" 
		""
		5 1 "HandRN" "Hand:FingerE:Fk_00_tag.parent" "HandRN.placeHolderList[10]" 
		""
		5 1 "HandRN" "Hand:FingerE:MetadataTemplate.message" "HandRN.placeHolderList[16]" 
		""
		5 1 "HandRN" "Hand:FingerE:MetadataTemplate.message" "HandRN.placeHolderList[28]" 
		""
		"Hand:FingerDRN" 5
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:FingerD:Tpl_00_tpl" 
		"visibility" " 0"
		5 1 "HandRN" "Hand:FingerD:Fk_00_tag.parent" "HandRN.placeHolderList[4]" 
		""
		5 1 "HandRN" "Hand:FingerD:Fk_00_tag.parent" "HandRN.placeHolderList[9]" 
		""
		5 1 "HandRN" "Hand:FingerD:MetadataTemplate.message" "HandRN.placeHolderList[15]" 
		""
		5 1 "HandRN" "Hand:FingerD:MetadataTemplate.message" "HandRN.placeHolderList[27]" 
		""
		"Hand:FingerCRN" 5
		2 "|ArmRNfosterParent1|Hand:TplTpl_00_hrch|Hand:Tpl_00_tpl|Hand:MainTpl_00_jnt|Hand:FingerC:Tpl_00_tpl" 
		"visibility" " 0"
		5 1 "HandRN" "Hand:FingerC:Fk_00_tag.parent" "HandRN.placeHolderList[3]" 
		""
		5 1 "HandRN" "Hand:FingerC:Fk_00_tag.parent" "HandRN.placeHolderList[8]" 
		""
		5 1 "HandRN" "Hand:FingerC:MetadataTemplate.message" "HandRN.placeHolderList[14]" 
		""
		5 1 "HandRN" "Hand:FingerC:MetadataTemplate.message" "HandRN.placeHolderList[26]" 
		"";
lockNode -l 1 ;
createNode objectSet -n "LinkSet";
	rename -uid "FA382E80-457D-197D-3A88-D39608DA5589";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode choice -n "ArmExtra:SpaceWorld_00_chc";
	rename -uid "A137CF19-42F7-3E96-506E-AD9FEC58A5A0";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
createNode choice -n "ArmExtra:SpaceHand_00_chc";
	rename -uid "6FA631A9-46C7-1F96-627C-A0BB9C744F54";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
createNode choice -n "ArmExtra:SpaceCog_00_chc";
	rename -uid "1A61E4D6-40D1-FDFE-C1FD-C1ABE1145CF0";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
createNode reference -n "ClavicleRN";
	rename -uid "3E530BF5-4724-6484-7320-0C803D431890";
	setAttr -s 20 ".phl";
	setAttr ".phl[1]" 0;
	setAttr ".phl[2]" 0;
	setAttr ".phl[3]" 0;
	setAttr ".phl[4]" 0;
	setAttr ".phl[5]" 0;
	setAttr ".phl[6]" 0;
	setAttr ".phl[7]" 0;
	setAttr ".phl[8]" 0;
	setAttr ".phl[9]" 0;
	setAttr ".phl[10]" 0;
	setAttr ".phl[11]" 0;
	setAttr ".phl[12]" 0;
	setAttr ".phl[13]" 0;
	setAttr ".phl[14]" 0;
	setAttr ".phl[15]" 0;
	setAttr ".phl[16]" 0;
	setAttr ".phl[17]" 0;
	setAttr ".phl[18]" 0;
	setAttr ".phl[19]" 0;
	setAttr ".phl[20]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"ClavicleRN"
		"ClavicleRN" 0
		"ClavicleRN" 28
		0 "|ClavicleRNfosterParent1|Arm:TplTpl_00_hrch" "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root" 
		"-s -r "
		0 "|ClavicleRNfosterParent1|Arm:inputLink_00_hrch" "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr|Clavicle:output_00_link" 
		"-s -r "
		2 "|Clavicle:Tpl_00_tpl" "visibility" " 0"
		2 "|Clavicle:Tpl_00_tpl|Clavicle:FkTpl_00_root" "translate" " -type \"double3\" -10 0 0"
		
		2 "|Clavicle:input_00_link" "translate" " -type \"double3\" -10 0 0"
		2 "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr" "rotate" 
		" -type \"double3\" 0 0 0"
		2 "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr|Clavicle:output_00_link" 
		"translate" " -type \"double3\" 10 0 0"
		3 "Clavicle:Fk_00_tag.message" "Clavicle:Fk_00_tag.children[0]" ""
		5 1 "ClavicleRN" "|Clavicle:Fk_00_jnt.message" "ClavicleRN.placeHolderList[1]" 
		""
		5 1 "ClavicleRN" "|Clavicle:input_00_link|Clavicle:Fk_00_root|Clavicle:Fk_00_ctr|Clavicle:output_00_link.message" 
		"ClavicleRN.placeHolderList[2]" ""
		5 3 "ClavicleRN" "|Clavicle:input_00_link.instObjGroups" "ClavicleRN.placeHolderList[3]" 
		""
		5 2 "ClavicleRN" "Clavicle:Fk_00_tag.children[0]" "ClavicleRN.placeHolderList[4]" 
		""
		5 2 "ClavicleRN" "Clavicle:Fk_00_tag.children[1]" "ClavicleRN.placeHolderList[5]" 
		""
		5 2 "ClavicleRN" "Clavicle:Fk_00_tag.children[2]" "ClavicleRN.placeHolderList[6]" 
		""
		5 2 "ClavicleRN" "Clavicle:Fk_00_tag.children[3]" "ClavicleRN.placeHolderList[7]" 
		""
		5 4 "ClavicleRN" "Clavicle:Fk_00_tag.children[4]" "ClavicleRN.placeHolderList[8]" 
		""
		5 4 "ClavicleRN" "Clavicle:Fk_00_tag.children[5]" "ClavicleRN.placeHolderList[9]" 
		""
		5 4 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[0]" "ClavicleRN.placeHolderList[10]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[1]" "ClavicleRN.placeHolderList[11]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[2]" "ClavicleRN.placeHolderList[12]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[3]" "ClavicleRN.placeHolderList[13]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[4]" "ClavicleRN.placeHolderList[14]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[5]" "ClavicleRN.placeHolderList[15]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[6]" "ClavicleRN.placeHolderList[16]" 
		""
		5 2 "ClavicleRN" "Clavicle:MetadataTemplate._postExecution[7]" "ClavicleRN.placeHolderList[17]" 
		""
		5 3 "ClavicleRN" "Clavicle:ControlsSet.message" "ClavicleRN.placeHolderList[18]" 
		""
		5 3 "ClavicleRN" "Clavicle:SkinJointsSet.message" "ClavicleRN.placeHolderList[19]" 
		""
		5 3 "ClavicleRN" "Clavicle:LinkSet.message" "ClavicleRN.placeHolderList[20]" 
		"";
lockNode -l 1 ;
createNode objectSet -n "Secondaries";
	rename -uid "495CDD91-4EBC-589D-1DC3-7F9832A3A9BF";
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
	setAttr ".msaa" yes;
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
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 16 ".u";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 9 ".r";
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
select -ne :ikSystem;
	setAttr -s 2 ".sol";
connectAttr "ArmRN.phl[93]" "Arm:IkPoleIksc_00_root_orientConstraint1.cpim";
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.crx" "ArmRN.phl[94]";
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.cry" "ArmRN.phl[95]";
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.crz" "ArmRN.phl[96]";
connectAttr "ArmRN.phl[97]" "Arm:IkPoleIksc_00_root_orientConstraint1.cro";
connectAttr "ClavicleRN.phl[1]" "ArmRN.phl[98]";
connectAttr "ArmRN.phl[99]" "Fk_00_root_orientConstraint1.cpim";
connectAttr "Fk_00_root_orientConstraint1.crx" "ArmRN.phl[100]";
connectAttr "Fk_00_root_orientConstraint1.cry" "ArmRN.phl[101]";
connectAttr "Fk_00_root_orientConstraint1.crz" "ArmRN.phl[102]";
connectAttr "ArmRN.phl[103]" "Fk_00_root_orientConstraint1.cro";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "ArmRN.phl[104]";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "ArmRN.phl[105]";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "ArmRN.phl[106]";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.pole" "ArmRN.phl[107]";
connectAttr "Arm:Ik_01_prc.ctx" "ArmRN.phl[108]";
connectAttr "Arm:Ik_01_prc.cty" "ArmRN.phl[109]";
connectAttr "Arm:Ik_01_prc.ctz" "ArmRN.phl[110]";
connectAttr "ArmRN.phl[111]" "Arm:Ik_01_prc.crp";
connectAttr "ArmRN.phl[112]" "Arm:Ik_01_prc.crt";
connectAttr "Arm:Ik_01_prc.crx" "ArmRN.phl[113]";
connectAttr "Arm:Ik_01_prc.cry" "ArmRN.phl[114]";
connectAttr "Arm:Ik_01_prc.crz" "ArmRN.phl[115]";
connectAttr "ArmRN.phl[116]" "Arm:Ik_01_prc.cro";
connectAttr "ArmRN.phl[117]" "Arm:Ik_01_prc.cpim";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.ik" "ArmRN.phl[118]";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.pole" "ArmRN.phl[119]";
connectAttr "ClavicleRN.phl[2]" "ArmRN.phl[120]";
connectAttr "ArmRN.phl[121]" "ArmRN.phl[122]";
connectAttr "ArmExtra:FkWorld_00_spc.msg" "ArmRN.phl[123]";
connectAttr "ArmExtra:FkCog_00_spc.msg" "ArmRN.phl[124]";
connectAttr "ArmExtra:FkChest_00_spc.msg" "ArmRN.phl[125]";
connectAttr "ArmRN.phl[126]" "SkinJointsSet.dnsm" -na;
connectAttr "ArmRN.phl[127]" "ControlsSet.dnsm" -na;
connectAttr "ArmRN.phl[128]" "LinkSet.dnsm" -na;
connectAttr "HandRN.phl[1]" "ArmRN.phl[129]";
connectAttr "HandRN.phl[2]" "ArmRN.phl[130]";
connectAttr "HandRN.phl[3]" "ArmRN.phl[131]";
connectAttr "HandRN.phl[4]" "ArmRN.phl[132]";
connectAttr "HandRN.phl[5]" "ArmRN.phl[133]";
connectAttr "HandRN.phl[6]" "ArmRN.phl[134]";
connectAttr "HandRN.phl[7]" "ArmRN.phl[135]";
connectAttr "HandRN.phl[8]" "ArmRN.phl[136]";
connectAttr "HandRN.phl[9]" "ArmRN.phl[137]";
connectAttr "HandRN.phl[10]" "ArmRN.phl[138]";
connectAttr "ArmExtra:IkPointA_00_ctr.iog" "ArmRN.phl[139]";
connectAttr "ArmExtra:IkPointB_00_ctr.iog" "ArmRN.phl[140]";
connectAttr "ArmRN.phl[141]" "ArmExtra:MetadataTemplate._postExecution[0]";
connectAttr "HandRN.phl[11]" "ArmRN.phl[142]";
connectAttr "HandRN.phl[12]" "ArmRN.phl[143]";
connectAttr "HandRN.phl[13]" "ArmRN.phl[144]";
connectAttr "HandRN.phl[14]" "ArmRN.phl[145]";
connectAttr "HandRN.phl[15]" "ArmRN.phl[146]";
connectAttr "HandRN.phl[16]" "ArmRN.phl[147]";
connectAttr "ArmExtra:MetadataTemplate.msg" "ArmRN.phl[148]";
connectAttr "ArmRN.phl[149]" "HandRN.phl[17]";
connectAttr "HandRN.phl[18]" "HandRN.phl[19]";
connectAttr "HandRN.phl[20]" "ControlsSet.dnsm" -na;
connectAttr "HandRN.phl[21]" "SkinJointsSet.dnsm" -na;
connectAttr "HandRN.phl[22]" "LinkSet.dnsm" -na;
connectAttr "ClavicleRN.phl[3]" "LinkSet.dsm" -na;
connectAttr "ArmRN.phl[150]" "ClavicleRN.phl[4]";
connectAttr "ArmRN.phl[151]" "ClavicleRN.phl[5]";
connectAttr "ArmRN.phl[152]" "ClavicleRN.phl[6]";
connectAttr "ArmRN.phl[153]" "ClavicleRN.phl[7]";
connectAttr "ArmExtra:IkPointB_00_tag.pare" "ClavicleRN.phl[8]";
connectAttr "ArmExtra:IkPointA_00_tag.pare" "ClavicleRN.phl[9]";
connectAttr "ArmExtra:MetadataTemplate.msg" "ClavicleRN.phl[10]";
connectAttr "ArmRN.phl[154]" "ClavicleRN.phl[11]";
connectAttr "HandRN.phl[23]" "ClavicleRN.phl[12]";
connectAttr "HandRN.phl[24]" "ClavicleRN.phl[13]";
connectAttr "HandRN.phl[25]" "ClavicleRN.phl[14]";
connectAttr "HandRN.phl[26]" "ClavicleRN.phl[15]";
connectAttr "HandRN.phl[27]" "ClavicleRN.phl[16]";
connectAttr "HandRN.phl[28]" "ClavicleRN.phl[17]";
connectAttr "ClavicleRN.phl[18]" "ControlsSet.dnsm" -na;
connectAttr "ClavicleRN.phl[19]" "SkinJointsSet.dnsm" -na;
connectAttr "ClavicleRN.phl[20]" "LinkSet.dnsm" -na;
connectAttr "ArmExtra:MetadataTemplate.msg" "ArmExtra:Tpl_00_tpl.metadataTemplate"
		;
connectAttr "ArmExtra:IkWorld_00_spc.msg" "ArmExtra:IkWorldTpl_00_spc._relatedTo[0]"
		;
connectAttr "ArmExtra:IkCog_00_spc.msg" "ArmExtra:IkWorldTpl_00_spc._relatedTo[1]"
		;
connectAttr "ArmExtra:IkPointA_00_root.msg" "ArmExtra:IkWorldTpl_00_spc._relatedTo[2]"
		;
connectAttr "ArmExtra:IkPointB_00_root.msg" "ArmExtra:IkWorldTpl_00_spc._relatedTo[3]"
		;
connectAttr "ArmExtra:IkWorld_00_spc.t" "Arm:Ik_01_prc.tg[0].tt";
connectAttr "ArmExtra:IkWorld_00_spc.rp" "Arm:Ik_01_prc.tg[0].trp";
connectAttr "ArmExtra:IkWorld_00_spc.rpt" "Arm:Ik_01_prc.tg[0].trt";
connectAttr "ArmExtra:IkWorld_00_spc.r" "Arm:Ik_01_prc.tg[0].tr";
connectAttr "ArmExtra:IkWorld_00_spc.ro" "Arm:Ik_01_prc.tg[0].tro";
connectAttr "ArmExtra:IkWorld_00_spc.s" "Arm:Ik_01_prc.tg[0].ts";
connectAttr "ArmExtra:IkWorld_00_spc.pm" "Arm:Ik_01_prc.tg[0].tpm";
connectAttr "Arm:Ik_01_prc.w0" "Arm:Ik_01_prc.tg[0].tw";
connectAttr "ArmExtra:IkCog_00_spc.t" "Arm:Ik_01_prc.tg[1].tt";
connectAttr "ArmExtra:IkCog_00_spc.rp" "Arm:Ik_01_prc.tg[1].trp";
connectAttr "ArmExtra:IkCog_00_spc.rpt" "Arm:Ik_01_prc.tg[1].trt";
connectAttr "ArmExtra:IkCog_00_spc.r" "Arm:Ik_01_prc.tg[1].tr";
connectAttr "ArmExtra:IkCog_00_spc.ro" "Arm:Ik_01_prc.tg[1].tro";
connectAttr "ArmExtra:IkCog_00_spc.s" "Arm:Ik_01_prc.tg[1].ts";
connectAttr "ArmExtra:IkCog_00_spc.pm" "Arm:Ik_01_prc.tg[1].tpm";
connectAttr "Arm:Ik_01_prc.w1" "Arm:Ik_01_prc.tg[1].tw";
connectAttr "ArmExtra:IkPointA_00_ctr.t" "Arm:Ik_01_prc.tg[2].tt";
connectAttr "ArmExtra:IkPointA_00_ctr.rp" "Arm:Ik_01_prc.tg[2].trp";
connectAttr "ArmExtra:IkPointA_00_ctr.rpt" "Arm:Ik_01_prc.tg[2].trt";
connectAttr "ArmExtra:IkPointA_00_ctr.r" "Arm:Ik_01_prc.tg[2].tr";
connectAttr "ArmExtra:IkPointA_00_ctr.ro" "Arm:Ik_01_prc.tg[2].tro";
connectAttr "ArmExtra:IkPointA_00_ctr.s" "Arm:Ik_01_prc.tg[2].ts";
connectAttr "ArmExtra:IkPointA_00_ctr.pm" "Arm:Ik_01_prc.tg[2].tpm";
connectAttr "Arm:Ik_01_prc.w2" "Arm:Ik_01_prc.tg[2].tw";
connectAttr "ArmExtra:IkPointB_00_ctr.t" "Arm:Ik_01_prc.tg[3].tt";
connectAttr "ArmExtra:IkPointB_00_ctr.rp" "Arm:Ik_01_prc.tg[3].trp";
connectAttr "ArmExtra:IkPointB_00_ctr.rpt" "Arm:Ik_01_prc.tg[3].trt";
connectAttr "ArmExtra:IkPointB_00_ctr.r" "Arm:Ik_01_prc.tg[3].tr";
connectAttr "ArmExtra:IkPointB_00_ctr.ro" "Arm:Ik_01_prc.tg[3].tro";
connectAttr "ArmExtra:IkPointB_00_ctr.s" "Arm:Ik_01_prc.tg[3].ts";
connectAttr "ArmExtra:IkPointB_00_ctr.pm" "Arm:Ik_01_prc.tg[3].tpm";
connectAttr "Arm:Ik_01_prc.w3" "Arm:Ik_01_prc.tg[3].tw";
connectAttr "Arm:Spaceworld_01_chc.o" "Arm:Ik_01_prc.w0";
connectAttr "Arm:Spacecog_01_chc.o" "Arm:Ik_01_prc.w1";
connectAttr "Arm:SpacepointA_00_chc.o" "Arm:Ik_01_prc.w2";
connectAttr "Arm:SpacepointB_00_chc.o" "Arm:Ik_01_prc.w3";
connectAttr "ArmExtra:FkCog_00_spc.r" "Fk_00_root_orientConstraint1.tg[0].tr";
connectAttr "ArmExtra:FkCog_00_spc.ro" "Fk_00_root_orientConstraint1.tg[0].tro";
connectAttr "ArmExtra:FkCog_00_spc.pm" "Fk_00_root_orientConstraint1.tg[0].tpm";
connectAttr "Fk_00_root_orientConstraint1.w0" "Fk_00_root_orientConstraint1.tg[0].tw"
		;
connectAttr "ArmExtra:FkChest_00_spc.r" "Fk_00_root_orientConstraint1.tg[1].tr";
connectAttr "ArmExtra:FkChest_00_spc.ro" "Fk_00_root_orientConstraint1.tg[1].tro"
		;
connectAttr "ArmExtra:FkChest_00_spc.pm" "Fk_00_root_orientConstraint1.tg[1].tpm"
		;
connectAttr "Fk_00_root_orientConstraint1.w1" "Fk_00_root_orientConstraint1.tg[1].tw"
		;
connectAttr "ArmExtra:FkWorld_00_spc.r" "Fk_00_root_orientConstraint1.tg[2].tr";
connectAttr "ArmExtra:FkWorld_00_spc.ro" "Fk_00_root_orientConstraint1.tg[2].tro"
		;
connectAttr "ArmExtra:FkWorld_00_spc.pm" "Fk_00_root_orientConstraint1.tg[2].tpm"
		;
connectAttr "Fk_00_root_orientConstraint1.w2" "Fk_00_root_orientConstraint1.tg[2].tw"
		;
connectAttr "Arm:SpaceCOG_00_chc.o" "Fk_00_root_orientConstraint1.w0";
connectAttr "Arm:SpaceChest_00_chc.o" "Fk_00_root_orientConstraint1.w1";
connectAttr "Arm:SpaceWorld_01_chc.o" "Fk_00_root_orientConstraint1.w2";
connectAttr "ArmExtra:IkPoleCog_00_spc.r" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[0].tr"
		;
connectAttr "ArmExtra:IkPoleCog_00_spc.ro" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[0].tro"
		;
connectAttr "ArmExtra:IkPoleCog_00_spc.pm" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[0].tpm"
		;
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.w0" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[0].tw"
		;
connectAttr "ArmExtra:IkPoleHand_00_spc.r" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[1].tr"
		;
connectAttr "ArmExtra:IkPoleHand_00_spc.ro" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[1].tro"
		;
connectAttr "ArmExtra:IkPoleHand_00_spc.pm" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[1].tpm"
		;
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.w1" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[1].tw"
		;
connectAttr "ArmExtra:IkPoleWorld_00_spc.r" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[2].tr"
		;
connectAttr "ArmExtra:IkPoleWorld_00_spc.ro" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[2].tro"
		;
connectAttr "ArmExtra:IkPoleWorld_00_spc.pm" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[2].tpm"
		;
connectAttr "Arm:IkPoleIksc_00_root_orientConstraint1.w2" "Arm:IkPoleIksc_00_root_orientConstraint1.tg[2].tw"
		;
connectAttr "ArmExtra:SpaceCog_00_chc.o" "Arm:IkPoleIksc_00_root_orientConstraint1.w0"
		;
connectAttr "ArmExtra:SpaceHand_00_chc.o" "Arm:IkPoleIksc_00_root_orientConstraint1.w1"
		;
connectAttr "ArmExtra:SpaceWorld_00_chc.o" "Arm:IkPoleIksc_00_root_orientConstraint1.w2"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "ArmRNfosterParent1.msg" "ArmRN.fp";
connectAttr "sharedReferenceNode.sr" "ArmRN.sr";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "Arm:SpaceWorld_01_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "Arm:SpaceCOG_00_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.fk" "Arm:SpaceChest_00_chc.s";
connectAttr "ArmExtra:IkWorldTpl_00_spc.msg" "ArmExtra:MetadataTemplate._inputTemplate[0]"
		;
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "ArmExtra:SpaceSwitch_00_ctr.ik" "Arm:Spaceworld_01_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.ik" "Arm:Spacecog_01_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.ik" "Arm:SpacepointA_00_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.ik" "Arm:SpacepointB_00_chc.s";
connectAttr "ArmExtra:IkPointA_00_ctr.msg" "ArmExtra:IkPointA_00_tag.act";
connectAttr "ArmExtra:IkPointA_00_tag.msg" "ArmExtra:IkPointA_00_tag.child[0]";
connectAttr "ArmExtra:IkPointB_00_ctr.msg" "ArmExtra:IkPointB_00_tag.act";
connectAttr "ArmExtra:IkPointB_00_tag.msg" "ArmExtra:IkPointB_00_tag.child[0]";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.pole" "ArmExtra:SpaceWorld_00_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.pole" "ArmExtra:SpaceHand_00_chc.s";
connectAttr "ArmExtra:SpaceSwitch_00_ctr.pole" "ArmExtra:SpaceCog_00_chc.s";
connectAttr "ClavicleRNfosterParent1.msg" "ClavicleRN.fp";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of armClavicleFk.ma
