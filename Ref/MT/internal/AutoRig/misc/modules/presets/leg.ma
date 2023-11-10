//Maya ASCII 2020 scene
//Name: leg.ma
//Last modified: Tue, Jul 19, 2022 09:48:26 AM
//Codeset: 1252
file -rdi 1 -ns "Leg" -rfn "LegRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
file -rdi 1 -ns "Foot" -rfn "FootRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/presets/footRoll.ma";
file -r -ns "Leg" -dr 1 -rfn "LegRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
file -r -ns "Foot" -dr 1 -rfn "FootRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/presets/footRoll.ma";
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "4EA0859C-42B4-4C9B-DF71-20801EF79D37";
createNode transform -s -n "persp";
	rename -uid "5D5D6746-43ED-5346-1898-76AB4C529F98";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 77.568641585530699 60.336978828876255 81.373706008443222 ;
	setAttr ".r" -type "double3" -16.538352729608711 40.600000000008976 1.0472391919523514e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "F960D4C5-49AE-683D-0320-B598F4A00815";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 125.35266298840892;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 9.9920072216264089e-16 9.9920072216264089e-16 5 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "55D0253B-462D-9311-CF3C-51ACA27BB9FA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "D9B771C8-4662-A74F-C71A-1FA90B6A3DC1";
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
	rename -uid "3C6417EF-46CD-0590-ECBB-CF99563CEAC8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 2.6272678592047063 10.126036293944207 1000.1687653368517 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "044AA792-49DA-EF01-73E6-CBA2017EE4C3";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 998.56089036398168;
	setAttr ".ow" 10.617098850759954;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 1.6078749728700701 11.60787497287007 1.6078749728700701 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "7D2AEFD0-4F28-12DF-7C0E-1B9AA4B4B2DC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "D41F0D30-490C-0D73-D2DC-96921B8AD35C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "LegExtra:FkWorld_00_spc";
	rename -uid "6CEE0CC2-47E6-ED1A-9A6A-B39976AE2F31";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 60 0 ;
	setAttr ".r" -type "double3" 180 0 -90 ;
createNode transform -n "LegExtra:FkCog_00_spc";
	rename -uid "45B55B6D-4BD1-9C0F-0B49-24AD213BD6AE";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 60 0 ;
	setAttr ".r" -type "double3" 180 0 -90 ;
createNode transform -n "LegExtra:FkHips_00_spc";
	rename -uid "959E6F1F-4A2F-717D-5374-70A9930E3AE6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 60 0 ;
	setAttr ".r" -type "double3" 180 0 -90 ;
createNode transform -n "Leg:IkPoleWorld_00_spc";
	rename -uid "A93E3FB4-4AA1-6978-A8C8-7193A3E4ABB3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 10 0 ;
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "Leg:IkPoleCog_00_spc";
	rename -uid "5C082487-4B64-EB7B-32B9-748AB3CA7127";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 10 0 ;
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "Leg:IkPoleHips_00_spc";
	rename -uid "78DE3CE0-40FB-02E9-32AB-11BF2A7C5C9F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 10 0 ;
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "LegExtra:IkWorld_00_spc";
	rename -uid "C06C5365-4EA4-FD14-7A3F-E49330D514A6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "LegExtra:IkCog_00_spc";
	rename -uid "C78BB10B-40D8-4B99-F5B2-1EB6CCC94760";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "LegExtra:IkHips_00_spc";
	rename -uid "27BE219D-421B-D5EB-F8F9-69ACAF058BB8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "LegExtra:IkPointA_00_root";
	rename -uid "804F6AF8-425E-53F5-ED43-8B9EDAB2B361";
createNode transform -n "LegExtra:IkPointA_00_ctr" -p "LegExtra:IkPointA_00_root";
	rename -uid "B5A34D90-48C4-B171-F1D7-FE8AE4AEA060";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode nurbsCurve -n "LegExtra:IkPointA_00_ctrShape" -p "LegExtra:IkPointA_00_ctr";
	rename -uid "3D8ABD58-46B8-34CB-0AFD-ED8CC2A8362E";
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
createNode transform -n "LegExtra:IkPointB_00_root";
	rename -uid "0EAE2AA3-4FC4-F2D4-CB7E-64BE3A46F53E";
createNode transform -n "LegExtra:IkPointB_00_ctr" -p "LegExtra:IkPointB_00_root";
	rename -uid "964FDA5D-4820-5730-481B-4F97E2045193";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode nurbsCurve -n "LegExtra:IkPointB_00_ctrShape" -p "LegExtra:IkPointB_00_ctr";
	rename -uid "4E731F79-4EBC-273D-8C42-5E8D55F0EBE8";
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
createNode fosterParent -n "LegRNfosterParent1";
	rename -uid "B1367BEE-407B-9BAA-8B5C-46854D154B65";
createNode transform -n "LegExtra:Tpl_00_tpl" -p "LegRNfosterParent1";
	rename -uid "3E8B8AB8-460D-99D4-1C61-FB8EDC6CE5A9";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "LegExtra:IkSpacesTpl_00_spc" -p "LegExtra:Tpl_00_tpl";
	rename -uid "2ED10189-4CC6-31F8-EDD8-AF86F47F9D3A";
	addAttr -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
	setAttr -s 5 "._relatedTo";
	setAttr -s 5 "._relatedTo";
createNode locator -n "LegExtra:IkSpacesTpl_00_spcShape" -p "LegExtra:IkSpacesTpl_00_spc";
	rename -uid "FC5AFB97-44B2-31D9-03FE-D4B352FB561B";
	setAttr -k off ".v";
createNode transform -n "Foot:TplTpl_00_hrch" -p "LegRNfosterParent1";
	rename -uid "8193F9DE-4356-A11D-F489-7691378A0934";
	setAttr ".t" -type "double3" 3.3306690738754696e-16 -10 -4.0788932203406729e-32 ;
createNode transform -n "Foot:BallRoot_00_hrch" -p "LegRNfosterParent1";
	rename -uid "7CEF9C8D-4EEA-7957-4934-2BA768CF8908";
	setAttr ".t" -type "double3" 0 0 5 ;
createNode transform -n "Leg:SpaceSwitch_00_root" -p "LegRNfosterParent1";
	rename -uid "4267B7F4-4782-17AF-5636-F2AB6DD2580D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754701e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Leg:SpaceSwitch_00_ctr" -p "Leg:SpaceSwitch_00_root";
	rename -uid "CDAF78A4-4BDA-FBEF-ADB7-649BF51AB584";
	addAttr -ci true -k true -sn "ik" -ln "ik" -min 0 -max 4 -en "world:cog:hips:pointA:pointB" 
		-at "enum";
	addAttr -ci true -k true -sn "fk" -ln "fk" -min 0 -max 2 -en "world:cog:hips" -at "enum";
	addAttr -ci true -sn "pole" -ln "pole" -min 0 -max 3 -en "world:cog:hips:foot" -at "enum";
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
	setAttr -k on ".ik";
	setAttr -k on ".fk";
	setAttr -k on ".pole";
createNode nurbsCurve -n "Leg:SpaceSwitch_00_ctrShape" -p "Leg:SpaceSwitch_00_ctr";
	rename -uid "86DF1B7D-4B9E-6974-EF9B-D3B6067703F7";
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
createNode transform -n "Foot:ConfigRoot_00_hrch" -p "LegRNfosterParent1";
	rename -uid "95A05E5F-4656-3BA4-9B04-62AA2FD5D7B1";
	setAttr ".t" -type "double3" 52.207796899661986 2.7931512506044798e-14 22.876755514793729 ;
	setAttr ".r" -type "double3" -156.33761277817791 0 -89.999999999999972 ;
createNode parentConstraint -n "Leg:Ik_00_prc" -p "LegRNfosterParent1";
	rename -uid "BA886368-4150-6B20-2F19-81B375DE7DC5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkWorld_00_spcW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "IkCog_00_spcW1" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w2" -ln "IkHips_00_spcW2" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w3" -ln "IkPointA_00_spcW3" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w4" -ln "IkPointB_00_spcW4" -dv 1 -min 0 -at "double";
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
	setAttr -s 5 ".tg";
	setAttr ".int" 0;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
	setAttr -k on ".w3";
	setAttr -k on ".w4";
createNode transform -n "Leg:IkPoleFoot_00_spc" -p "LegRNfosterParent1";
	rename -uid "6099EF0E-4209-9371-5FA2-E989E26904C2";
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "Foot:inputLink_00_hrch" -p "LegRNfosterParent1";
	rename -uid "17C63A98-49DD-48FA-A871-C1A2410EE1D9";
	setAttr ".t" -type "double3" 0 -10 0 ;
createNode pointConstraint -n "IkChilds_00_grp_pointConstraint1" -p "LegRNfosterParent1";
	rename -uid "2DBE2B86-41DF-9658-9D08-4C905C58226F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "output_00_linkW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 -10 0 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "Fk_00_root_orientConstraint1" -p "LegRNfosterParent1";
	rename -uid "1F4DB99A-4A6D-665C-002C-E788F83A2405";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkHips_00_spcW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "FkCOG_00_spcW1" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 180 0 -90 ;
	setAttr ".o" -type "double3" 360 0 0 ;
	setAttr ".rsrr" -type "double3" 540 0 -90 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
createNode transform -n "Foot:inputLink_01_hrch" -p "LegRNfosterParent1";
	rename -uid "6BE5B219-477E-F8B8-0901-CAAD61D4F666";
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".r" -type "double3" 180 0 -90 ;
createNode transform -n "Leg:outputLink_00_hrch" -p "LegRNfosterParent1";
	rename -uid "7B82DCE5-4D42-EA38-1AF4-06B7D8BB5BE0";
	setAttr ".t" -type "double3" 1.6641871818287461e-15 10.000000000002384 -3.5917534273394516e-15 ;
	setAttr ".r" -type "double3" 90 -45 -45.000000000000014 ;
	setAttr ".s" -type "double3" 1 1 0.99999999999999989 ;
createNode orientConstraint -n "Leg:IkPoleIksc_00_root_orientConstraint1" -p "LegRNfosterParent1";
	rename -uid "1818DE6C-45A4-BD1B-1F19-138BC2892099";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkPoleCog_00_spcW0" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "IkPoleWorld_00_spcW1" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w2" -ln "IkPoleFoot_00_spcW2" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w3" -ln "IkPoleHips_00_spcW3" -dv 1 -min 0 
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
	setAttr -s 4 ".tg";
	setAttr ".lr" -type "double3" 0 0 -90 ;
	setAttr ".rsrr" -type "double3" 0 0 -90 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
	setAttr -k on ".w2";
	setAttr -k on ".w3";
createNode fosterParent -n "FootRNfosterParent1";
	rename -uid "09AA36D1-4093-3935-7930-40AB3857068D";
createNode pointConstraint -n "Foot:IkTpl_00_mstc_pointConstraint1" -p "FootRNfosterParent1";
	rename -uid "A16B2AD6-41EA-2DCC-828C-9BBD55E7FB59";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkTpl_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".o" -type "double3" 3.3306690738754696e-16 0 0 ;
	setAttr ".rst" -type "double3" 0 10 -5 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "D1210C3B-4842-6F7A-B58D-63948D4733B6";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "BD9DA572-4C7F-C1B9-9B4A-E5BA31F03CB7";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "7E658FA2-4DCF-B7BA-94E6-7D99A4ED83DA";
createNode displayLayerManager -n "layerManager";
	rename -uid "1197505C-4F8E-6CC4-E78F-9BABD96026A2";
createNode displayLayer -n "defaultLayer";
	rename -uid "0C555B9C-4EBA-B4BE-8AE1-CA9613ACAF6D";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "2AAFBD8A-4F32-171C-458A-E68AF593C440";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "98C8F215-4190-0724-490A-C9ADB7A241AA";
	setAttr ".g" yes;
createNode reference -n "LegRN";
	rename -uid "20A35059-4260-5931-0600-B7A6FD4A1F56";
	setAttr -s 2 ".fn";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/RP2BonesAdvanced.ma";
	setAttr ".fn[1]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/ik/2BonesAdvanced.ma";
	setAttr -s 54 ".phl";
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
	setAttr ".phl[155]" 0;
	setAttr ".phl[156]" 0;
	setAttr ".phl[157]" 0;
	setAttr ".phl[158]" 0;
	setAttr ".phl[159]" 0;
	setAttr ".phl[160]" 0;
	setAttr ".phl[161]" 0;
	setAttr ".phl[162]" 0;
	setAttr ".phl[163]" 0;
	setAttr ".phl[164]" 0;
	setAttr ".phl[165]" 0;
	setAttr ".phl[166]" 0;
	setAttr ".phl[167]" 0;
	setAttr ".phl[168]" 0;
	setAttr ".phl[169]" 0;
	setAttr ".phl[170]" 0;
	setAttr ".phl[171]" 0;
	setAttr ".phl[172]" 0;
	setAttr ".phl[173]" 0;
	setAttr ".phl[174]" 0;
	setAttr ".phl[175]" 0;
	setAttr ".phl[176]" 0;
	setAttr ".phl[177]" 0;
	setAttr ".phl[178]" 0;
	setAttr ".phl[179]" 0;
	setAttr ".phl[180]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"LegRN"
		"LegRN" 6
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_root.translate" 
		"LegRN.placeHolderList[29]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_root.parentMatrix" 
		"LegRN.placeHolderList[30]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_root.rotatePivot" 
		"LegRN.placeHolderList[31]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_root.rotatePivotTranslate" 
		"LegRN.placeHolderList[32]" ""
		5 2 "LegRN" "Leg:MetadataTemplate._extendBehaviour[1]" "LegRN.placeHolderList[85]" 
		""
		5 3 "LegRN" "Leg:TemplateSet.message" "LegRN.placeHolderList[127]" ""
		
		"LegRN" 114
		0 "|Leg:output_00_link" "|LegRNfosterParent1|Leg:outputLink_00_hrch" "-s -r "
		
		0 "|LegRNfosterParent1|Leg:IkPoleIksc_00_root_orientConstraint1" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root" 
		"-s -r "
		0 "|LegRNfosterParent1|Leg:outputLink_00_hrch" "|Leg:Sys_00_grp" "-s -r "
		
		0 "|LegRNfosterParent1|Foot:inputLink_01_hrch" "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|Fk_00_root_orientConstraint1" "|Leg:Controls_00_grp|Leg:Fk_00_root" 
		"-s -r "
		0 "|LegRNfosterParent1|IkChilds_00_grp_pointConstraint1" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp" 
		"-s -r "
		0 "|LegRNfosterParent1|Foot:inputLink_00_hrch" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|Leg:IkPoleFoot_00_spc" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|Leg:Ik_00_prc" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root" 
		"-s -r "
		0 "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch" "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|Leg:SpaceSwitch_00_root" "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|Foot:BallRoot_00_hrch" "|Leg:Controls_00_grp" "-s -r "
		
		0 "|LegRNfosterParent1|Foot:TplTpl_00_hrch" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr" 
		"-s -r "
		0 "|LegRNfosterParent1|LegExtra:Tpl_00_tpl" "|Leg:Tpl_00_tpl" "-s -r "
		1 |Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr "legSpaceSwitch" "legSpaceSwitch" 
		" -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:hips\" -at \"enum\""
		1 |Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr 
		"legSpaceSwitch" "legSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:hips\" -at \"enum\""
		
		1 |Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr 
		"legSpaceSwitch" "legSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 2 -en \"world:cog:hips\" -at \"enum\""
		
		1 |Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Twist_00_root|Leg:Twist_00_off|Leg:Twist_00_ctr 
		"kneeSpaceSwitch" "kneeSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 3 -en \"world:cog:hips:foot\" -at \"enum\""
		
		1 |Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr "handSpaceSwitch" 
		"handSpaceSwitch" " -uap -ci 1 -k 1 -min 0 -max 4 -en \"world:cog:hips:pointA:pointB\" -at \"enum\""
		
		1 |Leg:Controls_00_grp|Leg:Pin_01_root|Leg:Pin_01_ctr "kneeSpaceSwitch" "kneeSpaceSwitch" 
		" -uap -ci 1 -k 1 -min 0 -max 3 -en \"world:cog:hips:foot\" -at \"enum\""
		2 "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root|Leg:IkPole_00_iksc" "rotate" " -type \"double3\" 0 0 -90"
		
		2 "|Leg:Sys_00_grp|Leg:OrigSystem_00_tr|Leg:IkPole_00_jnt|Leg:IkPole_00_root|Leg:IkPole_00_loc" 
		"translate" " -type \"double3\" 25 0 15"
		2 "|Leg:Sys_00_grp|Leg:OrigSystem_00_tr|Leg:IkPole_00_jnt|Leg:IkPole_00_root|Leg:IkPole_00_loc" 
		"rotate" " -type \"double3\" 180 0 0"
		2 "|Leg:Sys_00_grp|Leg:outputLink_00_orc" "nodeState" " -k 1 0"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root" "rotatePivotTranslate" " -type \"double3\" 0 0 0"
		
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr" "rotate" " -type \"double3\" 0 0 0"
		
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr" "rotateOrder" " 2"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr" "legSpaceSwitch" " -av -k 1"
		
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root" "translate" 
		" -type \"double3\" 25 0 0"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root" "rotate" 
		" -type \"double3\" 0 0 0"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr" 
		"legSpaceSwitch" " -k 1"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root" 
		"translate" " -type \"double3\" 25 0 0"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr" 
		"legSpaceSwitch" " -k 1"
		2 "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Twist_00_root|Leg:Twist_00_off|Leg:Twist_00_ctr" 
		"rotateX" " 0"
		2 "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Twist_00_root|Leg:Twist_00_off|Leg:Twist_00_ctr" 
		"kneeSpaceSwitch" " -k 1"
		2 "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr" "translate" 
		" -type \"double3\" 0 10 0"
		2 "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr" "rotate" 
		" -type \"double3\" 0 0 0"
		2 "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr" "handSpaceSwitch" 
		" -k 1"
		2 "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr" "fkIk" " -k 1 1"
		
		2 "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr" "antiPop" " -k 1 0"
		
		2 "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr" "autoStretch" 
		" -k 1 1"
		2 "|Leg:Controls_00_grp|Leg:Pin_01_root|Leg:Pin_01_ctr" "kneeSpaceSwitch" 
		" -k 1"
		2 "|Leg:Tpl_00_tpl" "visibility" " 0"
		2 "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr" "translate" " -type \"double3\" 0 60 0"
		
		2 "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr" "rotate" " -type \"double3\" 180 0 -90"
		
		2 "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr" 
		"rotate" " -type \"double3\" 0 180 90"
		2 "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr|Leg:FkTplCtr_02_orc" 
		"offset" " -type \"double3\" 0 -180 -270"
		2 "|Leg:Tpl_00_tpl|Leg:FKTpl_00_root" "rotate" " -type \"double3\" 180 0 -90"
		
		2 "|LegRNfosterParent1|Leg:outputLink_00_hrch|Leg:output_00_link" "visibility" 
		" 1"
		2 "|LegRNfosterParent1|Leg:outputLink_00_hrch|Leg:output_00_link" "displayLocalAxis" 
		" 0"
		2 "|Leg:input_00_link" "translate" " -type \"double3\" 0 60 0"
		2 "Leg:StretchFk_00_pma" "input2D" " -s 2"
		2 "Leg:StretchFk_00_pma" "input2D[1]" " -type \"float2\" 25 25"
		2 "Leg:AutoStretch_00_blcl" "color2" " -type \"float3\" 25 25 0"
		2 "Leg:Stretch_00_clp" "min" " -type \"float3\" 25 25 0"
		2 "Leg:StretchIk_00_pma" "input2D" " -s 2"
		2 "Leg:StretchIk_00_pma" "input2D[1]" " -type \"float2\" 25 25"
		2 "Leg:StretchIkFact_00_fm" "floatB" " 50"
		3 "Leg:Ik_00_tag.message" "Leg:Ik_00_tag.children[0]" ""
		3 "Leg:Fk_02_tag.message" "Leg:Fk_02_tag.children[0]" ""
		5 3 "LegRN" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root.parentInverseMatrix" 
		"LegRN.placeHolderList[128]" ""
		5 4 "LegRN" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root.rotateX" "LegRN.placeHolderList[129]" 
		""
		5 4 "LegRN" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root.rotateY" "LegRN.placeHolderList[130]" 
		""
		5 4 "LegRN" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root.rotateZ" "LegRN.placeHolderList[131]" 
		""
		5 3 "LegRN" "|Leg:Sys_00_grp|Leg:IkPoleIksc_00_root.rotateOrder" "LegRN.placeHolderList[132]" 
		""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root.parentInverseMatrix" 
		"LegRN.placeHolderList[133]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root.rotateX" "LegRN.placeHolderList[134]" 
		""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root.rotateY" "LegRN.placeHolderList[135]" 
		""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root.rotateZ" "LegRN.placeHolderList[136]" 
		""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root.rotateOrder" "LegRN.placeHolderList[137]" 
		""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr.legSpaceSwitch" 
		"LegRN.placeHolderList[138]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr.legSpaceSwitch" 
		"LegRN.placeHolderList[139]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr.legSpaceSwitch" 
		"LegRN.placeHolderList[140]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Twist_00_root|Leg:Twist_00_off|Leg:Twist_00_ctr.kneeSpaceSwitch" 
		"LegRN.placeHolderList[141]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.translateX" 
		"LegRN.placeHolderList[142]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.translateY" 
		"LegRN.placeHolderList[143]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.translateZ" 
		"LegRN.placeHolderList[144]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotatePivot" 
		"LegRN.placeHolderList[145]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotatePivotTranslate" 
		"LegRN.placeHolderList[146]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotateX" 
		"LegRN.placeHolderList[147]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotateY" 
		"LegRN.placeHolderList[148]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotateZ" 
		"LegRN.placeHolderList[149]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.rotateOrder" 
		"LegRN.placeHolderList[150]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root.parentInverseMatrix" 
		"LegRN.placeHolderList[151]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr.handSpaceSwitch" 
		"LegRN.placeHolderList[152]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.parentInverseMatrix" 
		"LegRN.placeHolderList[153]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.translateX" 
		"LegRN.placeHolderList[154]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.translateY" 
		"LegRN.placeHolderList[155]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.translateZ" 
		"LegRN.placeHolderList[156]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.rotatePivot" 
		"LegRN.placeHolderList[157]" ""
		5 3 "LegRN" "|Leg:Controls_00_grp|Leg:IkCtr_00_root|Leg:Ik_00_root|Leg:Ik_00_ctr|Leg:IkChilds_00_grp.rotatePivotTranslate" 
		"LegRN.placeHolderList[158]" ""
		5 4 "LegRN" "|Leg:Controls_00_grp|Leg:Pin_01_root|Leg:Pin_01_ctr.kneeSpaceSwitch" 
		"LegRN.placeHolderList[159]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr.translate" 
		"LegRN.placeHolderList[160]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr.parentMatrix" 
		"LegRN.placeHolderList[161]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr.rotatePivot" 
		"LegRN.placeHolderList[162]" ""
		5 3 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:IkTpl_01_loc|Leg:IkTpl_00_ctr.rotatePivotTranslate" 
		"LegRN.placeHolderList[163]" ""
		5 4 "LegRN" "|Leg:Tpl_00_tpl|Leg:FKTpl_00_root._relatedTo[1]" "LegRN.placeHolderList[164]" 
		""
		5 4 "LegRN" "|Leg:Tpl_00_tpl|Leg:FKTpl_00_root._relatedTo[2]" "LegRN.placeHolderList[165]" 
		""
		5 4 "LegRN" "|Leg:Tpl_00_tpl|Leg:FKTpl_00_root._relatedTo[3]" "LegRN.placeHolderList[166]" 
		""
		5 3 "LegRN" "|Leg:input_00_link.instObjGroups" "LegRN.placeHolderList[167]" 
		""
		5 3 "LegRN" "Leg:SkinJointsSet.message" "LegRN.placeHolderList[168]" 
		""
		5 3 "LegRN" "Leg:ControlsSet.message" "LegRN.placeHolderList[169]" ""
		
		5 3 "LegRN" "Leg:LinkSet.message" "LegRN.placeHolderList[170]" ""
		5 2 "LegRN" "Leg:Ik_00_tag.children[0]" "LegRN.placeHolderList[171]" 
		""
		5 2 "LegRN" "Leg:Fk_02_tag.children[0]" "LegRN.placeHolderList[172]" 
		""
		5 4 "LegRN" "Leg:Ik.dagSetMembers" "LegRN.placeHolderList[173]" ""
		5 4 "LegRN" "Leg:Ik.dagSetMembers" "LegRN.placeHolderList[174]" ""
		5 3 "LegRN" "Leg:MetadataTemplate.message" "LegRN.placeHolderList[175]" 
		""
		5 4 "LegRN" "Leg:MetadataTemplate._preExecution[0]" "LegRN.placeHolderList[176]" 
		""
		5 2 "LegRN" "Leg:MetadataTemplate._postExecution[0]" "LegRN.placeHolderList[177]" 
		""
		5 1 "LegRN" "|Leg:_00_jnt|Leg:_01_jnt|Leg:End_01_jnt.message" "LegRN.placeHolderList[178]" 
		""
		5 1 "LegRN" "|Leg:Tpl_00_tpl|Leg:OrigSystemTpl_00_tr|Leg:Config_00_tpl.mirror" 
		"LegRN.placeHolderList[179]" ""
		5 1 "LegRN" "|Leg:Controls_00_grp|Leg:Config_00_root|Leg:Config_00_ctr.fkIk" 
		"LegRN.placeHolderList[180]" "";
lockNode -l 1 ;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "B13E1472-4E4E-E8D8-F77A-C6A7811473C3";
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
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1185\n            -height 702\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1185\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1185\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A822E7B8-4CDD-EF05-9C56-C2AD26DEDC6A";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode choice -n "Leg:SpaceWorld_01_chc";
	rename -uid "07A1D46D-4D20-FBC9-3D9E-3D90546FDD05";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
createNode choice -n "Leg:SpaceCog_00_chc";
	rename -uid "E84E3700-435D-9DE0-4E0C-52AC560971DE";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
createNode choice -n "Leg:SpaceHips_00_chc";
	rename -uid "2B5EFA2C-4639-80A5-8899-17A0F8F53E97";
	setAttr -s 3 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
createNode reference -n "sharedReferenceNode";
	rename -uid "55D372E7-4F5D-550E-C008-C8A3CAE320C7";
	setAttr ".ed" -type "dataReferenceEdits" 
		"sharedReferenceNode";
createNode objectSet -n "ControlsSet";
	rename -uid "2884932E-4C24-5B51-96FE-0A87D6189678";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "14DAA43E-468A-3EC3-BCBD-85AEAEF612ED";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dnsm";
createNode script -n "LegExtra:MetadataTemplate";
	rename -uid "9E8B86F5-4715-3D30-509C-039D09A13A67";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" "import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#Leg:IkWorld_00_spc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this";
	setAttr -l on ".stp" 1;
	setAttr -s 2 "._postExecution";
createNode choice -n "Leg:SpaceWorld_00_chc";
	rename -uid "C2BCAFC1-4823-04B3-C0A7-7B98F27CC2D5";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
createNode choice -n "Leg:PoleSpaceCog_00_chc";
	rename -uid "44C72011-42E7-143E-F5C3-7F883A6462C9";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
createNode choice -n "Leg:SpaceHips_01_chc";
	rename -uid "D495449A-4B8A-F2AF-D747-39AF24A73B1A";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
	setAttr ".i[3]" 0;
createNode choice -n "Leg:SpaceFoot_00_chc";
	rename -uid "AC32C594-4E34-A1EC-A7A5-A6905A417EF9";
	setAttr -s 4 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 1;
createNode choice -n "Leg:Spaceworld_01_chc";
	rename -uid "703F2475-41D8-86B6-A42D-97922A4ACA77";
	setAttr -s 5 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
	setAttr ".i[4]" 0;
createNode choice -n "Leg:Spacecog_01_chc";
	rename -uid "6E5BE930-4DF5-7A26-2F5F-8393A7ED2CA9";
	setAttr -s 5 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
	setAttr ".i[4]" 0;
createNode choice -n "Leg:Spacehips_01_chc";
	rename -uid "EEB43AB0-4F47-4E64-A368-4F876131F02C";
	setAttr -s 5 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 1;
	setAttr ".i[3]" 0;
	setAttr ".i[4]" 0;
createNode choice -n "Leg:SpacepointA_00_chc";
	rename -uid "E03B0D58-420B-D680-B74E-E5846C3A97EE";
	setAttr -s 5 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 1;
	setAttr ".i[4]" 0;
createNode choice -n "Leg:SpacepointB_00_chc";
	rename -uid "CF15A0FA-4E98-8399-F1C8-DD83AE8E4CF1";
	setAttr -s 5 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 0;
	setAttr ".i[2]" 0;
	setAttr ".i[3]" 0;
	setAttr ".i[4]" 1;
createNode reference -n "FootRN";
	rename -uid "31B14AB0-4990-ED58-5365-D3B09841DD77";
	setAttr -s 21 ".phl";
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
	setAttr ".phl[29]" 0;
	setAttr ".phl[30]" 0;
	setAttr ".phl[31]" 0;
	setAttr ".phl[32]" 0;
	setAttr ".phl[33]" 0;
	setAttr ".phl[34]" 0;
	setAttr ".phl[35]" 0;
	setAttr ".phl[36]" 0;
	setAttr ".phl[37]" 0;
	setAttr ".phl[38]" 0;
	setAttr ".phl[39]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"FootRN"
		"FootRN" 1
		5 3 "FootRN" "Foot:TemplateSet.message" "FootRN.placeHolderList[19]" 
		""
		"FootRN" 35
		0 "|Foot:Tpl_00_tpl" "|LegRNfosterParent1|Foot:TplTpl_00_hrch" "-s -r "
		0 "|Foot:Ball_00_root" "|LegRNfosterParent1|Foot:BallRoot_00_hrch" "-s -r "
		
		0 "|Foot:Config_00_root" "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch" "-s -r "
		
		0 "|Foot:input_00_link" "|LegRNfosterParent1|Foot:inputLink_00_hrch" "-s -r "
		
		0 "|Foot:input_01_link" "|LegRNfosterParent1|Foot:inputLink_01_hrch" "-s -r "
		
		0 "|FootRNfosterParent1|Foot:IkTpl_00_mstc_pointConstraint1" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc" 
		"-s -r "
		2 "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch|Foot:Config_00_root" "translate" 
		" -type \"double3\" 0 0 0"
		2 "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch|Foot:Config_00_root" "scale" 
		" -type \"double3\" 1 1.00000000000000022 1.00000000000000022"
		2 "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch|Foot:Config_00_root" "rotatePivot" 
		" -type \"double3\" 0 0 0"
		2 "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch|Foot:Config_00_root" "scalePivotTranslate" 
		" -type \"double3\" 0 0 0"
		2 "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl" "visibility" 
		" 0"
		2 "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc|Foot:IkTpl_00_mstcShape" 
		"visibility" " -k 0 0"
		2 "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:output_00_link" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:RollMainCtr_00_root|Foot:RollMain_00_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|LegRNfosterParent1|Foot:inputLink_01_hrch|Foot:input_01_link" "translate" 
		" -type \"double3\" 0 0 0"
		5 1 "FootRN" "Foot:BankHeel_00_tag.parent" "FootRN.placeHolderList[20]" 
		""
		5 1 "FootRN" "Foot:Ball_00_tag.parent" "FootRN.placeHolderList[21]" 
		""
		5 1 "FootRN" "Foot:MetadataTemplate.message" "FootRN.placeHolderList[22]" 
		""
		5 2 "FootRN" "|Foot:_00_jnt.parent" "FootRN.placeHolderList[23]" ""
		5 4 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.translateX" 
		"FootRN.placeHolderList[24]" ""
		5 4 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.translateY" 
		"FootRN.placeHolderList[25]" ""
		5 4 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.translateZ" 
		"FootRN.placeHolderList[26]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.parentInverseMatrix" 
		"FootRN.placeHolderList[27]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.rotatePivot" 
		"FootRN.placeHolderList[28]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:BankInTpl_00_footroll|Foot:BankExtTpl_00_footroll|Foot:BankHeelTpl_00_footroll|Foot:BankToeTpl_00_footroll|Foot:BallMainTpl_00_root|Foot:IkTpl_00_mstc.rotatePivotTranslate" 
		"FootRN.placeHolderList[29]" ""
		5 2 "FootRN" "|LegRNfosterParent1|Foot:TplTpl_00_hrch|Foot:Tpl_00_tpl|Foot:RollMainTpl_00_root|Foot:Config_00_tpl.mirror" 
		"FootRN.placeHolderList[30]" ""
		5 2 "FootRN" "|LegRNfosterParent1|Foot:ConfigRoot_00_hrch|Foot:Config_00_root|Foot:Config_00_ctr.fkik" 
		"FootRN.placeHolderList[31]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:output_00_link.translate" 
		"FootRN.placeHolderList[32]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:output_00_link.parentMatrix" 
		"FootRN.placeHolderList[33]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:output_00_link.rotatePivot" 
		"FootRN.placeHolderList[34]" ""
		5 3 "FootRN" "|LegRNfosterParent1|Foot:inputLink_00_hrch|Foot:input_00_link|Foot:RollMain_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:Ik_00_mstc|Foot:output_00_link.rotatePivotTranslate" 
		"FootRN.placeHolderList[35]" ""
		5 3 "FootRN" "Foot:MetadataTemplate.message" "FootRN.placeHolderList[36]" 
		""
		5 3 "FootRN" "Foot:ControlsSet.message" "FootRN.placeHolderList[37]" 
		""
		5 3 "FootRN" "Foot:SkinJointsSet.message" "FootRN.placeHolderList[38]" 
		""
		5 3 "FootRN" "Foot:LinkSet.message" "FootRN.placeHolderList[39]" "";
lockNode -l 1 ;
createNode objectSet -n "LinkSet";
	rename -uid "7CD938DA-47DA-71FB-29C2-6EA0848EAB48";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dnsm";
createNode objectSet -n "Secondaries";
	rename -uid "DBCDE4CE-4B39-73ED-E18E-5F8B8B1D2480";
	setAttr ".ihi" 0;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "1FD95C21-4206-96F8-7737-E089529B71FE";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -310.18906699229302 -235.92436333909868 ;
	setAttr ".tgi[0].vh" -type "double2" 320.90335228083131 271.63864763422634 ;
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
	setAttr -s 23 ".u";
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
select -ne :ikSystem;
	setAttr -s 2 ".sol";
connectAttr "LegRN.phl[128]" "Leg:IkPoleIksc_00_root_orientConstraint1.cpim";
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.crx" "LegRN.phl[129]";
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.cry" "LegRN.phl[130]";
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.crz" "LegRN.phl[131]";
connectAttr "LegRN.phl[132]" "Leg:IkPoleIksc_00_root_orientConstraint1.cro";
connectAttr "LegRN.phl[133]" "Fk_00_root_orientConstraint1.cpim";
connectAttr "Fk_00_root_orientConstraint1.crx" "LegRN.phl[134]";
connectAttr "Fk_00_root_orientConstraint1.cry" "LegRN.phl[135]";
connectAttr "Fk_00_root_orientConstraint1.crz" "LegRN.phl[136]";
connectAttr "LegRN.phl[137]" "Fk_00_root_orientConstraint1.cro";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "LegRN.phl[138]";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "LegRN.phl[139]";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "LegRN.phl[140]";
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "LegRN.phl[141]";
connectAttr "Leg:Ik_00_prc.ctx" "LegRN.phl[142]";
connectAttr "Leg:Ik_00_prc.cty" "LegRN.phl[143]";
connectAttr "Leg:Ik_00_prc.ctz" "LegRN.phl[144]";
connectAttr "LegRN.phl[145]" "Leg:Ik_00_prc.crp";
connectAttr "LegRN.phl[146]" "Leg:Ik_00_prc.crt";
connectAttr "Leg:Ik_00_prc.crx" "LegRN.phl[147]";
connectAttr "Leg:Ik_00_prc.cry" "LegRN.phl[148]";
connectAttr "Leg:Ik_00_prc.crz" "LegRN.phl[149]";
connectAttr "LegRN.phl[150]" "Leg:Ik_00_prc.cro";
connectAttr "LegRN.phl[151]" "Leg:Ik_00_prc.cpim";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "LegRN.phl[152]";
connectAttr "LegRN.phl[153]" "IkChilds_00_grp_pointConstraint1.cpim";
connectAttr "IkChilds_00_grp_pointConstraint1.ctx" "LegRN.phl[154]";
connectAttr "IkChilds_00_grp_pointConstraint1.cty" "LegRN.phl[155]";
connectAttr "IkChilds_00_grp_pointConstraint1.ctz" "LegRN.phl[156]";
connectAttr "LegRN.phl[157]" "IkChilds_00_grp_pointConstraint1.crp";
connectAttr "LegRN.phl[158]" "IkChilds_00_grp_pointConstraint1.crt";
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "LegRN.phl[159]";
connectAttr "LegRN.phl[160]" "Foot:IkTpl_00_mstc_pointConstraint1.tg[0].tt";
connectAttr "LegRN.phl[161]" "Foot:IkTpl_00_mstc_pointConstraint1.tg[0].tpm";
connectAttr "LegRN.phl[162]" "Foot:IkTpl_00_mstc_pointConstraint1.tg[0].trp";
connectAttr "LegRN.phl[163]" "Foot:IkTpl_00_mstc_pointConstraint1.tg[0].trt";
connectAttr "LegExtra:FkWorld_00_spc.msg" "LegRN.phl[164]";
connectAttr "LegExtra:FkCog_00_spc.msg" "LegRN.phl[165]";
connectAttr "LegExtra:FkHips_00_spc.msg" "LegRN.phl[166]";
connectAttr "LegRN.phl[167]" "LinkSet.dsm" -na;
connectAttr "LegRN.phl[168]" "SkinJointsSet.dnsm" -na;
connectAttr "LegRN.phl[169]" "ControlsSet.dnsm" -na;
connectAttr "LegRN.phl[170]" "LinkSet.dnsm" -na;
connectAttr "FootRN.phl[20]" "LegRN.phl[171]";
connectAttr "FootRN.phl[21]" "LegRN.phl[172]";
connectAttr "LegExtra:IkPointA_00_ctr.iog" "LegRN.phl[173]";
connectAttr "LegExtra:IkPointB_00_ctr.iog" "LegRN.phl[174]";
connectAttr "LegRN.phl[175]" "LegExtra:MetadataTemplate._postExecution[0]";
connectAttr "LegExtra:MetadataTemplate.msg" "LegRN.phl[176]";
connectAttr "FootRN.phl[22]" "LegRN.phl[177]";
connectAttr "LegRN.phl[178]" "FootRN.phl[23]";
connectAttr "Foot:IkTpl_00_mstc_pointConstraint1.ctx" "FootRN.phl[24]";
connectAttr "Foot:IkTpl_00_mstc_pointConstraint1.cty" "FootRN.phl[25]";
connectAttr "Foot:IkTpl_00_mstc_pointConstraint1.ctz" "FootRN.phl[26]";
connectAttr "FootRN.phl[27]" "Foot:IkTpl_00_mstc_pointConstraint1.cpim";
connectAttr "FootRN.phl[28]" "Foot:IkTpl_00_mstc_pointConstraint1.crp";
connectAttr "FootRN.phl[29]" "Foot:IkTpl_00_mstc_pointConstraint1.crt";
connectAttr "LegRN.phl[179]" "FootRN.phl[30]";
connectAttr "LegRN.phl[180]" "FootRN.phl[31]";
connectAttr "FootRN.phl[32]" "IkChilds_00_grp_pointConstraint1.tg[0].tt";
connectAttr "FootRN.phl[33]" "IkChilds_00_grp_pointConstraint1.tg[0].tpm";
connectAttr "FootRN.phl[34]" "IkChilds_00_grp_pointConstraint1.tg[0].trp";
connectAttr "FootRN.phl[35]" "IkChilds_00_grp_pointConstraint1.tg[0].trt";
connectAttr "FootRN.phl[36]" "LegExtra:MetadataTemplate._postExecution[1]";
connectAttr "FootRN.phl[37]" "ControlsSet.dnsm" -na;
connectAttr "FootRN.phl[38]" "SkinJointsSet.dnsm" -na;
connectAttr "FootRN.phl[39]" "LinkSet.dnsm" -na;
connectAttr "LegExtra:MetadataTemplate.msg" "LegExtra:Tpl_00_tpl.metadataTemplate"
		;
connectAttr "LegExtra:IkWorld_00_spc.msg" "LegExtra:IkSpacesTpl_00_spc._relatedTo[0]"
		;
connectAttr "LegExtra:IkCog_00_spc.msg" "LegExtra:IkSpacesTpl_00_spc._relatedTo[1]"
		;
connectAttr "LegExtra:IkHips_00_spc.msg" "LegExtra:IkSpacesTpl_00_spc._relatedTo[2]"
		;
connectAttr "LegExtra:IkPointA_00_root.msg" "LegExtra:IkSpacesTpl_00_spc._relatedTo[3]"
		;
connectAttr "LegExtra:IkPointB_00_root.msg" "LegExtra:IkSpacesTpl_00_spc._relatedTo[4]"
		;
connectAttr "LegExtra:IkWorld_00_spc.t" "Leg:Ik_00_prc.tg[0].tt";
connectAttr "LegExtra:IkWorld_00_spc.rp" "Leg:Ik_00_prc.tg[0].trp";
connectAttr "LegExtra:IkWorld_00_spc.rpt" "Leg:Ik_00_prc.tg[0].trt";
connectAttr "LegExtra:IkWorld_00_spc.r" "Leg:Ik_00_prc.tg[0].tr";
connectAttr "LegExtra:IkWorld_00_spc.ro" "Leg:Ik_00_prc.tg[0].tro";
connectAttr "LegExtra:IkWorld_00_spc.s" "Leg:Ik_00_prc.tg[0].ts";
connectAttr "LegExtra:IkWorld_00_spc.pm" "Leg:Ik_00_prc.tg[0].tpm";
connectAttr "Leg:Ik_00_prc.w0" "Leg:Ik_00_prc.tg[0].tw";
connectAttr "LegExtra:IkCog_00_spc.t" "Leg:Ik_00_prc.tg[1].tt";
connectAttr "LegExtra:IkCog_00_spc.rp" "Leg:Ik_00_prc.tg[1].trp";
connectAttr "LegExtra:IkCog_00_spc.rpt" "Leg:Ik_00_prc.tg[1].trt";
connectAttr "LegExtra:IkCog_00_spc.r" "Leg:Ik_00_prc.tg[1].tr";
connectAttr "LegExtra:IkCog_00_spc.ro" "Leg:Ik_00_prc.tg[1].tro";
connectAttr "LegExtra:IkCog_00_spc.s" "Leg:Ik_00_prc.tg[1].ts";
connectAttr "LegExtra:IkCog_00_spc.pm" "Leg:Ik_00_prc.tg[1].tpm";
connectAttr "Leg:Ik_00_prc.w1" "Leg:Ik_00_prc.tg[1].tw";
connectAttr "LegExtra:IkHips_00_spc.t" "Leg:Ik_00_prc.tg[2].tt";
connectAttr "LegExtra:IkHips_00_spc.rp" "Leg:Ik_00_prc.tg[2].trp";
connectAttr "LegExtra:IkHips_00_spc.rpt" "Leg:Ik_00_prc.tg[2].trt";
connectAttr "LegExtra:IkHips_00_spc.r" "Leg:Ik_00_prc.tg[2].tr";
connectAttr "LegExtra:IkHips_00_spc.ro" "Leg:Ik_00_prc.tg[2].tro";
connectAttr "LegExtra:IkHips_00_spc.s" "Leg:Ik_00_prc.tg[2].ts";
connectAttr "LegExtra:IkHips_00_spc.pm" "Leg:Ik_00_prc.tg[2].tpm";
connectAttr "Leg:Ik_00_prc.w2" "Leg:Ik_00_prc.tg[2].tw";
connectAttr "LegExtra:IkPointA_00_ctr.t" "Leg:Ik_00_prc.tg[3].tt";
connectAttr "LegExtra:IkPointA_00_ctr.rp" "Leg:Ik_00_prc.tg[3].trp";
connectAttr "LegExtra:IkPointA_00_ctr.rpt" "Leg:Ik_00_prc.tg[3].trt";
connectAttr "LegExtra:IkPointA_00_ctr.r" "Leg:Ik_00_prc.tg[3].tr";
connectAttr "LegExtra:IkPointA_00_ctr.ro" "Leg:Ik_00_prc.tg[3].tro";
connectAttr "LegExtra:IkPointA_00_ctr.s" "Leg:Ik_00_prc.tg[3].ts";
connectAttr "LegExtra:IkPointA_00_ctr.pm" "Leg:Ik_00_prc.tg[3].tpm";
connectAttr "Leg:Ik_00_prc.w3" "Leg:Ik_00_prc.tg[3].tw";
connectAttr "LegExtra:IkPointB_00_ctr.t" "Leg:Ik_00_prc.tg[4].tt";
connectAttr "LegExtra:IkPointB_00_ctr.rp" "Leg:Ik_00_prc.tg[4].trp";
connectAttr "LegExtra:IkPointB_00_ctr.rpt" "Leg:Ik_00_prc.tg[4].trt";
connectAttr "LegExtra:IkPointB_00_ctr.r" "Leg:Ik_00_prc.tg[4].tr";
connectAttr "LegExtra:IkPointB_00_ctr.ro" "Leg:Ik_00_prc.tg[4].tro";
connectAttr "LegExtra:IkPointB_00_ctr.s" "Leg:Ik_00_prc.tg[4].ts";
connectAttr "LegExtra:IkPointB_00_ctr.pm" "Leg:Ik_00_prc.tg[4].tpm";
connectAttr "Leg:Ik_00_prc.w4" "Leg:Ik_00_prc.tg[4].tw";
connectAttr "Leg:Spaceworld_01_chc.o" "Leg:Ik_00_prc.w0";
connectAttr "Leg:Spacecog_01_chc.o" "Leg:Ik_00_prc.w1";
connectAttr "Leg:Spacehips_01_chc.o" "Leg:Ik_00_prc.w2";
connectAttr "Leg:SpacepointA_00_chc.o" "Leg:Ik_00_prc.w3";
connectAttr "Leg:SpacepointB_00_chc.o" "Leg:Ik_00_prc.w4";
connectAttr "IkChilds_00_grp_pointConstraint1.w0" "IkChilds_00_grp_pointConstraint1.tg[0].tw"
		;
connectAttr "LegExtra:FkHips_00_spc.r" "Fk_00_root_orientConstraint1.tg[0].tr";
connectAttr "LegExtra:FkHips_00_spc.ro" "Fk_00_root_orientConstraint1.tg[0].tro"
		;
connectAttr "LegExtra:FkHips_00_spc.pm" "Fk_00_root_orientConstraint1.tg[0].tpm"
		;
connectAttr "Fk_00_root_orientConstraint1.w0" "Fk_00_root_orientConstraint1.tg[0].tw"
		;
connectAttr "LegExtra:FkCog_00_spc.r" "Fk_00_root_orientConstraint1.tg[1].tr";
connectAttr "LegExtra:FkCog_00_spc.ro" "Fk_00_root_orientConstraint1.tg[1].tro";
connectAttr "LegExtra:FkCog_00_spc.pm" "Fk_00_root_orientConstraint1.tg[1].tpm";
connectAttr "Fk_00_root_orientConstraint1.w1" "Fk_00_root_orientConstraint1.tg[1].tw"
		;
connectAttr "LegExtra:FkWorld_00_spc.r" "Fk_00_root_orientConstraint1.tg[2].tr";
connectAttr "LegExtra:FkWorld_00_spc.ro" "Fk_00_root_orientConstraint1.tg[2].tro"
		;
connectAttr "LegExtra:FkWorld_00_spc.pm" "Fk_00_root_orientConstraint1.tg[2].tpm"
		;
connectAttr "Fk_00_root_orientConstraint1.w2" "Fk_00_root_orientConstraint1.tg[2].tw"
		;
connectAttr "Leg:SpaceHips_00_chc.o" "Fk_00_root_orientConstraint1.w0";
connectAttr "Leg:SpaceCog_00_chc.o" "Fk_00_root_orientConstraint1.w1";
connectAttr "Leg:SpaceWorld_01_chc.o" "Fk_00_root_orientConstraint1.w2";
connectAttr "Leg:IkPoleCog_00_spc.r" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[0].tr"
		;
connectAttr "Leg:IkPoleCog_00_spc.ro" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[0].tro"
		;
connectAttr "Leg:IkPoleCog_00_spc.pm" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[0].tpm"
		;
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.w0" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[0].tw"
		;
connectAttr "Leg:IkPoleWorld_00_spc.r" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[1].tr"
		;
connectAttr "Leg:IkPoleWorld_00_spc.ro" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[1].tro"
		;
connectAttr "Leg:IkPoleWorld_00_spc.pm" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[1].tpm"
		;
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.w1" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[1].tw"
		;
connectAttr "Leg:IkPoleFoot_00_spc.r" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[2].tr"
		;
connectAttr "Leg:IkPoleFoot_00_spc.ro" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[2].tro"
		;
connectAttr "Leg:IkPoleFoot_00_spc.pm" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[2].tpm"
		;
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.w2" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[2].tw"
		;
connectAttr "Leg:IkPoleHips_00_spc.r" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[3].tr"
		;
connectAttr "Leg:IkPoleHips_00_spc.ro" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[3].tro"
		;
connectAttr "Leg:IkPoleHips_00_spc.pm" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[3].tpm"
		;
connectAttr "Leg:IkPoleIksc_00_root_orientConstraint1.w3" "Leg:IkPoleIksc_00_root_orientConstraint1.tg[3].tw"
		;
connectAttr "Leg:PoleSpaceCog_00_chc.o" "Leg:IkPoleIksc_00_root_orientConstraint1.w0"
		;
connectAttr "Leg:SpaceWorld_00_chc.o" "Leg:IkPoleIksc_00_root_orientConstraint1.w1"
		;
connectAttr "Leg:SpaceFoot_00_chc.o" "Leg:IkPoleIksc_00_root_orientConstraint1.w2"
		;
connectAttr "Leg:SpaceHips_01_chc.o" "Leg:IkPoleIksc_00_root_orientConstraint1.w3"
		;
connectAttr "Foot:IkTpl_00_mstc_pointConstraint1.w0" "Foot:IkTpl_00_mstc_pointConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "LegRNfosterParent1.msg" "LegRN.fp";
connectAttr "sharedReferenceNode.sr" "LegRN.sr";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "Leg:SpaceWorld_01_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "Leg:SpaceCog_00_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.fk" "Leg:SpaceHips_00_chc.s";
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "LegExtra:IkSpacesTpl_00_spc.msg" "LegExtra:MetadataTemplate._inputTemplate[0]"
		;
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "Leg:SpaceWorld_00_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "Leg:PoleSpaceCog_00_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "Leg:SpaceHips_01_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.pole" "Leg:SpaceFoot_00_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "Leg:Spaceworld_01_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "Leg:Spacecog_01_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "Leg:Spacehips_01_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "Leg:SpacepointA_00_chc.s";
connectAttr "Leg:SpaceSwitch_00_ctr.ik" "Leg:SpacepointB_00_chc.s";
connectAttr "FootRNfosterParent1.msg" "FootRN.fp";
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of leg.ma
