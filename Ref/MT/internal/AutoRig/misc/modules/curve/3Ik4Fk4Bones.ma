//Maya ASCII 2020 scene
//Name: 3Ik4Fk4Bones.ma
//Last modified: Tue, Jul 19, 2022 08:20:14 AM
//Codeset: 1252
file -rdi 1 -ns "Spl" -rfn "SplRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/4Bones.ma";
file -r -ns "Spl" -dr 1 -rfn "SplRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/4Bones.ma";
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "7C0E9710-4297-12D6-65B2-1096E7B4C7C8";
createNode transform -s -n "persp";
	rename -uid "8CD630A7-499E-4718-8761-F0ADAB366494";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 13.024676999692764 24.744509582001911 45.388614602896183 ;
	setAttr ".r" -type "double3" -17.138352729622792 12.600000000005114 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "0E28CED5-40F8-D9B2-F283-9C918C3FEE30";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 56.351849962917342;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "73BE527B-401A-9C4A-0630-58928C2BD3E5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.22072533587080434 1000.1079544638562 -0.20644420349535197 ;
	setAttr ".r" -type "double3" -90 7.8032614421790409e-22 -7.8032614421790409e-22 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "40758B38-4A85-51E7-937E-17B30C11B961";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 997.60886023867886;
	setAttr ".ow" 18.200661952779907;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 0.041151495108749714 2.4990942251773411 -0.036156055746885407 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "11F1322C-4C03-6D1A-7BE2-6B8DD47B04AA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.69767881127061215 12.929386018098985 1000.1176854994051 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "050A230B-4411-4C24-D6E3-8A9316705DA9";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1176854994051;
	setAttr ".ow" 44.051460713039987;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0 12.000573064489991 0 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "03091BE6-4D66-0CED-4A5D-F086AF689B2F";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1066901615557 10.583662933500234 0.48310376713009795 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "162695FD-4776-A12A-918A-39967B503A3C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1066901615557;
	setAttr ".ow" 67.042946599641482;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 10 0 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Sys_00_grp";
	rename -uid "38B0ABEF-4C4A-0846-0CC8-7981ED3C809D";
	setAttr ".v" no;
createNode transform -n "FkAux_00_crv" -p "Sys_00_grp";
	rename -uid "38A601B8-460B-0D6D-3075-2F9F28F84A13";
createNode nurbsCurve -n "FkAux_00_crvShape" -p "FkAux_00_crv";
	rename -uid "7C22463B-440E-C9A1-5A77-DEB3C4FD6EFB";
	setAttr -k off ".v";
	setAttr -s 3 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 1 0 no 3
		4 0 0 1 1
		3
		0 0 0
		0 10 0
		0 20 0
		;
createNode ikHandle -n "FkAux_00_ih" -p "Sys_00_grp";
	rename -uid "4A46A3CF-4F18-93D5-FE34-2FB075EFA15E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 20.124999523162842 0 ;
	setAttr ".roc" yes;
	setAttr ".dwut" 4;
	setAttr ".dpa" 2;
	setAttr ".dwua" 3;
	setAttr ".dwuv" -type "double3" 0 0 1 ;
	setAttr ".dwve" -type "double3" 0 0 1 ;
	setAttr ".dtce" yes;
createNode joint -n "FkAux_00_jnt" -p "Sys_00_grp";
	rename -uid "082BA5F2-40BA-CD30-6AF4-93A6F84BE45B";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "FkAux_01_jnt" -p "FkAux_00_jnt";
	rename -uid "10A9F8F0-4419-C6D0-E3EF-78A909C0716D";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "FkAux_02_jnt" -p "FkAux_01_jnt";
	rename -uid "1DA66A9C-4801-A4C3-52ED-0ABE7D485B3F";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "FkAux_03_jnt" -p "FkAux_02_jnt";
	rename -uid "3643DE8C-426D-E6DB-9041-DA9DDC3B92F2";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "FkAuxEnd_03_jnt" -p "FkAux_03_jnt";
	rename -uid "43437307-4FED-139A-36E7-4B97464E4ED0";
	setAttr ".t" -type "double3" 0 0.1 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode ikEffector -n "effector1" -p "FkAuxEnd_03_jnt";
	rename -uid "4D1028DA-4046-3F95-223C-918D32AC3698";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0.025 0 ;
	setAttr ".hd" yes;
createNode transform -n "Tpl_00_tpl";
	rename -uid "F5A7676C-479F-33B8-6C51-AD9F44CE5A6E";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "SplIkTpl_00_root" -p "Tpl_00_tpl";
	rename -uid "D761E841-4647-B095-EF6A-C28008ADC802";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplIkTpl_00_rootShape" -p "SplIkTpl_00_root";
	rename -uid "E4941882-46A8-91D7-5159-35B74CDCECF1";
	setAttr -k off ".v";
createNode transform -n "SplIkTpl_02_root" -p "SplIkTpl_00_root";
	rename -uid "002C86C2-42B8-7259-5CAC-72B973C6A5C9";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 20 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplIkTpl_02_rootShape" -p "SplIkTpl_02_root";
	rename -uid "FA85B955-424C-3176-4A50-F3ACD56C8F1C";
	setAttr -k off ".v";
createNode transform -n "SplControls_00_grp";
	rename -uid "7DC03E20-4747-055B-F283-499405526C11";
createNode transform -n "SplIk_01_root" -p "SplControls_00_grp";
	rename -uid "8798A921-4F19-B8F7-6FA4-3FBF4E29618E";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplIk_01_ctr" -p "SplIk_01_root";
	rename -uid "FDA4E65B-4427-9AA4-3636-D3A4D873B717";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "SplIk_01_ctrShape" -p "SplIk_01_ctr";
	rename -uid "2DB93E8E-4F55-110B-BE7B-EA9D1664D619";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 20 2 no 3
		21 0 1 2 5 8 9 10 13 16 17 18 21 24 25 26 27 28 29 30 31 32
		21
		1.7595672550912054 0 3.5191345101824107
		2.8706766905320658 0 2.8706766905320658
		3.5191345101824107 0 1.7595672550912054
		4.0000008494410046 0 0
		3.5191345101824107 0 -1.7595672550912054
		2.8706766905320658 0 -2.8706766905320658
		1.7595672550912054 0 -3.5191345101824107
		0 0 -4.0000008494410046
		-1.7595672550912054 0 -3.5191345101824107
		-2.8706766905320658 0 -2.8706766905320658
		-3.5191345101824107 0 -1.7595672550912054
		-4.0000008494410046 0 0
		-3.5191345101824107 0 1.7595672550912054
		-2.8706766905320658 0 2.8706766905320658
		-1.7595672550912054 0 3.5191345101824107
		-1.4353383452660329 0 4.306015035798092
		-2.8706766905320658 0 4.306015035798092
		0 0 7.1766917263301675
		2.8706766905320658 0 4.306015035798092
		1.4353383452660329 0 4.306015035798092
		1.7595672550912054 0 3.5191345101824107
		;
createNode transform -n "SplIk_01_loc" -p "SplIk_01_ctr";
	rename -uid "4A8B6ED6-453D-21F0-8A3C-E3A268977BA8";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplIk_01_locShape" -p "SplIk_01_loc";
	rename -uid "8521DF76-41D7-BD75-906C-E48C753528F3";
	setAttr -k off ".v";
createNode pointConstraint -n "SplIk_01_root_pointConstraint1" -p "SplIk_01_root";
	rename -uid "4C645AAB-4056-4E12-F4B6-D59FFA4EAA05";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Spl_00_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "Spl_02_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".rst" -type "double3" 0 2.0125000476837163 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode orientConstraint -n "SplIk_01_root_orientConstraint1" -p "SplIk_01_root";
	rename -uid "E817E02E-4EDA-1B1A-0CF0-A88E714EE5F1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Spl_00_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "Spl_02_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr ".int" 0;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "input_00_link";
	rename -uid "8E3463B8-40C7-DBA6-35C7-C7813E565D9B";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "SplIk_00_root" -p "input_00_link";
	rename -uid "992EF146-4FA4-C0B5-04CD-1FAD323B500A";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplIk_00_ctr" -p "SplIk_00_root";
	rename -uid "713E51A2-4CAB-B6B8-0572-DB87DB2E6AB2";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "SplIk_00_ctrShape" -p "SplIk_00_ctr";
	rename -uid "51FEB7CD-46D6-2462-502F-FB9E2EFE0732";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 20 2 no 3
		21 0 1 2 5 8 9 10 13 16 17 18 21 24 25 26 27 28 29 30 31 32
		21
		1.7595672550912054 0 3.5191345101824107
		2.8706766905320658 0 2.8706766905320658
		3.5191345101824107 0 1.7595672550912054
		4.0000008494410046 0 0
		3.5191345101824107 0 -1.7595672550912054
		2.8706766905320658 0 -2.8706766905320658
		1.7595672550912054 0 -3.5191345101824107
		0 0 -4.0000008494410046
		-1.7595672550912054 0 -3.5191345101824107
		-2.8706766905320658 0 -2.8706766905320658
		-3.5191345101824107 0 -1.7595672550912054
		-4.0000008494410046 0 0
		-3.5191345101824107 0 1.7595672550912054
		-2.8706766905320658 0 2.8706766905320658
		-1.7595672550912054 0 3.5191345101824107
		-1.4353383452660329 0 4.306015035798092
		-2.8706766905320658 0 4.306015035798092
		0 0 7.1766917263301675
		2.8706766905320658 0 4.306015035798092
		1.4353383452660329 0 4.306015035798092
		1.7595672550912054 0 3.5191345101824107
		;
createNode transform -n "SplIk_00_loc" -p "SplIk_00_ctr";
	rename -uid "A7160B53-4667-9518-388A-9098A6E17C65";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplIk_00_locShape" -p "SplIk_00_loc";
	rename -uid "7D437A8E-486B-9021-20AC-3A96555F9943";
	setAttr -k off ".v";
createNode transform -n "input_01_link";
	rename -uid "77A031AD-4208-0D86-F409-29B43AEFA744";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "SplIk_02_root" -p "input_01_link";
	rename -uid "D0812251-4F73-E481-9EAD-D6BE9832DD82";
	setAttr ".t" -type "double3" 0 20 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplIk_02_ctr" -p "SplIk_02_root";
	rename -uid "F1BB4070-428A-8216-DDBE-2A944A364DE3";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "SplIk_02_ctrShape" -p "SplIk_02_ctr";
	rename -uid "4B460F12-4622-7107-F8DD-719E799CB50E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 20 2 no 3
		21 0 1 2 5 8 9 10 13 16 17 18 21 24 25 26 27 28 29 30 31 32
		21
		1.7595672550912054 0 3.5191345101824107
		2.8706766905320658 0 2.8706766905320658
		3.5191345101824107 0 1.7595672550912054
		4.0000008494410046 0 0
		3.5191345101824107 0 -1.7595672550912054
		2.8706766905320658 0 -2.8706766905320658
		1.7595672550912054 0 -3.5191345101824107
		0 0 -4.0000008494410046
		-1.7595672550912054 0 -3.5191345101824107
		-2.8706766905320658 0 -2.8706766905320658
		-3.5191345101824107 0 -1.7595672550912054
		-4.0000008494410046 0 0
		-3.5191345101824107 0 1.7595672550912054
		-2.8706766905320658 0 2.8706766905320658
		-1.7595672550912054 0 3.5191345101824107
		-1.4353383452660329 0 4.306015035798092
		-2.8706766905320658 0 4.306015035798092
		0 0 7.1766917263301675
		2.8706766905320658 0 4.306015035798092
		1.4353383452660329 0 4.306015035798092
		1.7595672550912054 0 3.5191345101824107
		;
createNode transform -n "SplIk_02_loc" -p "SplIk_02_ctr";
	rename -uid "DA3AD769-40C7-C3FA-ABEA-218DA4B03D35";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplIk_02_locShape" -p "SplIk_02_loc";
	rename -uid "AE4C194E-4837-5447-717C-62AD4F109EC6";
	setAttr -k off ".v";
createNode fosterParent -n "SplRNfosterParent1";
	rename -uid "E21FF9C9-4EF5-FFDF-E4D4-BD85E406D409";
createNode parentConstraint -n "Spl:input_00_link_parentConstraint1" -p "SplRNfosterParent1";
	rename -uid "E61C1545-4B18-EC7E-7E60-CF93536E0C1D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FkAux_00_jntW0" -dv 1 -min 0 -at "double";
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
	setAttr -k on ".w0";
createNode pointConstraint -n "FkTpl_01_root_pointConstraint1" -p "SplRNfosterParent1";
	rename -uid "C23B8CCC-454C-C0BF-EE22-DF98389C6C12";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplIkTpl_00_rootW0" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplIkTpl_02_rootW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr -k on ".w0" 0.6666;
	setAttr -k on ".w1" 0.3333;
createNode pointConstraint -n "FkTpl_02_root_pointConstraint1" -p "SplRNfosterParent1";
	rename -uid "F69E2692-4622-FBE0-B51F-559368968E23";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplIkTpl_00_rootW0" -dv 1 -min 0 
		-at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplIkTpl_02_rootW1" -dv 1 -min 0 -at "double";
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
	setAttr -s 2 ".tg";
	setAttr -k on ".w0" 0.3333;
	setAttr -k on ".w1" 0.6666;
createNode pointConstraint -n "FkTpl_03_root_pointConstraint1" -p "SplRNfosterParent1";
	rename -uid "CC964859-4F4C-D6C1-90E2-2F9C9DB3A52E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplIkTpl_02_rootW0" -dv 1 -min 0 
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
	setAttr ".rst" -type "double3" 0 6.6666666666666696 0 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "F3A1D2EF-4813-333A-42B0-F19399D63EAE";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "13CED9D4-40C7-9087-7AB6-5DA3650009F6";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "DB35464C-4B21-6ED3-6D94-10A3ABF0953C";
createNode displayLayerManager -n "layerManager";
	rename -uid "B3696A5D-4E05-CE4D-DE11-61972967725E";
createNode displayLayer -n "defaultLayer";
	rename -uid "2B6B19EA-43DB-595E-754B-1F88F425A5D4";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "1C65B3D4-40BB-C185-87FF-EDAE4FECAEE2";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "404520E2-4500-95B9-5E7D-6ABE1FDBE8FD";
	setAttr ".g" yes;
createNode ikSplineSolver -n "ikSplineSolver";
	rename -uid "7B5A25A5-43CB-A9B5-43C5-758CB4435EF8";
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
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1259\n            -height 702\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1259\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1259\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "1B0EF228-4785-DEB8-10E7-ECBB0BF1D4EA";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode curveInfo -n "FkAux_00_cvinf";
	rename -uid "ADF2DAA0-43BC-2084-F587-4F99894DE87E";
createNode multiplyDivide -n "FkAux_00_mdv";
	rename -uid "30E30210-4CE6-9732-2D81-E5B3FFDFDA60";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 3 1 1 ;
createNode clamp -n "FkAux_00_clp";
	rename -uid "98B8D367-488F-20E4-BFE8-698CEF5B89CD";
	setAttr ".mn" -type "float3" 6.6666665 0 0 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode controller -n "SplFk_01_tag";
	rename -uid "8BB43959-4C4E-30B4-DF5B-6998ADA1E15F";
createNode controller -n "SplFk_02_tag";
	rename -uid "BC73E2BF-41CC-9880-D745-579949D2701C";
createNode controller -n "SplFk_00_tag";
	rename -uid "56344578-4CC0-30D2-C93E-5A8A1973E433";
createNode controller -n "SplFk_03_tag";
	rename -uid "04D9E06A-40BA-2023-FA7D-C69C2B1C3278";
createNode controller -n "SplFk_04_tag";
	rename -uid "D9FD2F9F-4BF4-3EC3-F45C-4FAF79595F15";
createNode controller -n "SplIk_00_tag";
	rename -uid "F54EFA2E-4915-6403-0661-009F60B1972A";
createNode controller -n "SplIk_01_tag";
	rename -uid "0227B311-46E1-FE29-C8F8-73AB7B44ABE6";
createNode controller -n "SplIk_02_tag";
	rename -uid "9B0892DC-4815-5998-82DF-BB8C279F9A4E";
createNode reference -n "SplRN";
	rename -uid "403B730D-4B0E-4C89-CF73-408958C85516";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/fk/4Bones.ma";
	setAttr -s 38 ".phl";
	setAttr ".phl[37]" 0;
	setAttr ".phl[38]" 0;
	setAttr ".phl[39]" 0;
	setAttr ".phl[40]" 0;
	setAttr ".phl[41]" 0;
	setAttr ".phl[42]" 0;
	setAttr ".phl[43]" 0;
	setAttr ".phl[44]" 0;
	setAttr ".phl[45]" 0;
	setAttr ".phl[46]" 0;
	setAttr ".phl[47]" 0;
	setAttr ".phl[48]" 0;
	setAttr ".phl[49]" 0;
	setAttr ".phl[50]" 0;
	setAttr ".phl[51]" 0;
	setAttr ".phl[52]" 0;
	setAttr ".phl[53]" 0;
	setAttr ".phl[54]" 0;
	setAttr ".phl[55]" 0;
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
	setAttr ".ed" -type "dataReferenceEdits" 
		"SplRN"
		"SplRN" 6
		3 "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root.instObjGroups" 
		"Spl:TemplateSet.dagSetMembers" "-na"
		3 "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.instObjGroups" 
		"Spl:TemplateSet.dagSetMembers" "-na"
		3 "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.instObjGroups" 
		"Spl:TemplateSet.dagSetMembers" "-na"
		3 "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.instObjGroups" 
		"Spl:TemplateSet.dagSetMembers" "-na"
		5 4 "SplRN" "Spl:TemplateSet.dagSetMembers" "SplRN.placeHolderList[35]" 
		""
		5 4 "SplRN" "Spl:TemplateSet.dagSetMembers" "SplRN.placeHolderList[36]" 
		""
		"SplRN" 42
		0 "|Spl:Tpl_00_tpl" "|Tpl_00_tpl|SplIkTpl_00_root" "-s -r "
		0 "|Spl:input_00_link" "|SplControls_00_grp" "-s -r "
		0 "|SplRNfosterParent1|FkTpl_03_root_pointConstraint1" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root" 
		"-s -r "
		0 "|SplRNfosterParent1|FkTpl_02_root_pointConstraint1" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root" 
		"-s -r "
		0 "|SplRNfosterParent1|FkTpl_01_root_pointConstraint1" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root" 
		"-s -r "
		0 "|SplRNfosterParent1|Spl:input_00_link_parentConstraint1" "|SplControls_00_grp|Spl:input_00_link" 
		"-s -r "
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.translateZ" 
		"SplRN.placeHolderList[37]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.translateX" 
		"SplRN.placeHolderList[38]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.parentInverseMatrix" 
		"SplRN.placeHolderList[39]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.rotatePivot" 
		"SplRN.placeHolderList[40]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root.rotatePivotTranslate" 
		"SplRN.placeHolderList[41]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.translateY" 
		"SplRN.placeHolderList[42]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.translateZ" 
		"SplRN.placeHolderList[43]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.translateX" 
		"SplRN.placeHolderList[44]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.parentInverseMatrix" 
		"SplRN.placeHolderList[45]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.rotatePivot" 
		"SplRN.placeHolderList[46]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root.rotatePivotTranslate" 
		"SplRN.placeHolderList[47]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.translateY" 
		"SplRN.placeHolderList[48]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.translateZ" 
		"SplRN.placeHolderList[49]" ""
		5 4 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.translateX" 
		"SplRN.placeHolderList[50]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.parentInverseMatrix" 
		"SplRN.placeHolderList[51]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.rotatePivot" 
		"SplRN.placeHolderList[52]" ""
		5 3 "SplRN" "|Tpl_00_tpl|SplIkTpl_00_root|Spl:Tpl_00_tpl|Spl:FkTpl_00_root|Spl:FkTpl_01_root|Spl:FkTpl_02_root|Spl:FkTpl_03_root.rotatePivotTranslate" 
		"SplRN.placeHolderList[53]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.translateX" "SplRN.placeHolderList[54]" 
		""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.translateY" "SplRN.placeHolderList[55]" 
		""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.translateZ" "SplRN.placeHolderList[56]" 
		""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotateX" "SplRN.placeHolderList[57]" 
		""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotateY" "SplRN.placeHolderList[58]" 
		""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotateZ" "SplRN.placeHolderList[59]" 
		""
		5 3 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotateOrder" "SplRN.placeHolderList[60]" 
		""
		5 3 "SplRN" "|SplControls_00_grp|Spl:input_00_link.parentInverseMatrix" 
		"SplRN.placeHolderList[61]" ""
		5 3 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotatePivot" "SplRN.placeHolderList[62]" 
		""
		5 3 "SplRN" "|SplControls_00_grp|Spl:input_00_link.rotatePivotTranslate" 
		"SplRN.placeHolderList[63]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root.translate" 
		"SplRN.placeHolderList[64]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root.rotate" 
		"SplRN.placeHolderList[65]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root|Spl:Fk_01_ctr|Spl:Fk_02_root.translate" 
		"SplRN.placeHolderList[66]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root|Spl:Fk_01_ctr|Spl:Fk_02_root.rotate" 
		"SplRN.placeHolderList[67]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root|Spl:Fk_01_ctr|Spl:Fk_02_root|Spl:Fk_02_ctr|Spl:Fk_03_root.translate" 
		"SplRN.placeHolderList[68]" ""
		5 4 "SplRN" "|SplControls_00_grp|Spl:input_00_link|Spl:Fk_00_root|Spl:Fk_00_ctr|Spl:Fk_01_root|Spl:Fk_01_ctr|Spl:Fk_02_root|Spl:Fk_02_ctr|Spl:Fk_03_root.rotate" 
		"SplRN.placeHolderList[69]" ""
		5 3 "SplRN" "Spl:ControlsSet.message" "SplRN.placeHolderList[70]" ""
		
		5 3 "SplRN" "Spl:SkinJointsSet.message" "SplRN.placeHolderList[71]" 
		""
		5 3 "SplRN" "Spl:LinkSet.message" "SplRN.placeHolderList[72]" "";
lockNode -l 1 ;
createNode script -n "MetadataTemplate";
	rename -uid "02CF55A7-4C35-BF3B-2FC3-8F9393874072";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" "import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#SplIk_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#SplIk_02_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this";
	setAttr -l on ".stp" 1;
	setAttr -s 2 "._inputTemplate";
createNode reference -n "sharedReferenceNode";
	rename -uid "E7B50725-435C-F509-E7E6-80B07353954F";
	setAttr ".ed" -type "dataReferenceEdits" 
		"sharedReferenceNode";
createNode nodeGraphEditorInfo -n "Spl:MayaNodeEditorSavedTabsInfo1";
	rename -uid "26B6EEB6-4ACA-2D1E-B3F5-9D91FB43E024";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -2432.8374625518195 -1943.6948374813926 ;
	setAttr ".tgi[0].vh" -type "double2" 2437.4773076530992 1973.3093185822172 ;
createNode objectSet -n "ControlsSet";
	rename -uid "93B8EC86-48C5-37E7-10A1-06B002249612";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr -s 2 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "77443915-4054-51CD-3233-289E9BBFFAE9";
	setAttr ".ihi" 0;
createNode objectSet -n "LinkSet";
	rename -uid "F6449B3B-4B42-1778-E158-BAA649DCF455";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
createNode objectSet -n "Secondaries";
	rename -uid "EAEB6B37-45CE-5E12-953D-4086EAFF8819";
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
	setAttr -s 3 ".u";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 2 ".r";
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
connectAttr "FkTpl_01_root_pointConstraint1.ctz" "SplRN.phl[37]";
connectAttr "FkTpl_01_root_pointConstraint1.ctx" "SplRN.phl[38]";
connectAttr "SplRN.phl[39]" "FkTpl_01_root_pointConstraint1.cpim";
connectAttr "SplRN.phl[40]" "FkTpl_01_root_pointConstraint1.crp";
connectAttr "SplRN.phl[41]" "FkTpl_01_root_pointConstraint1.crt";
connectAttr "FkTpl_02_root_pointConstraint1.cty" "SplRN.phl[42]";
connectAttr "FkTpl_02_root_pointConstraint1.ctz" "SplRN.phl[43]";
connectAttr "FkTpl_02_root_pointConstraint1.ctx" "SplRN.phl[44]";
connectAttr "SplRN.phl[45]" "FkTpl_02_root_pointConstraint1.cpim";
connectAttr "SplRN.phl[46]" "FkTpl_02_root_pointConstraint1.crp";
connectAttr "SplRN.phl[47]" "FkTpl_02_root_pointConstraint1.crt";
connectAttr "FkTpl_03_root_pointConstraint1.cty" "SplRN.phl[48]";
connectAttr "FkTpl_03_root_pointConstraint1.ctz" "SplRN.phl[49]";
connectAttr "FkTpl_03_root_pointConstraint1.ctx" "SplRN.phl[50]";
connectAttr "SplRN.phl[51]" "FkTpl_03_root_pointConstraint1.cpim";
connectAttr "SplRN.phl[52]" "FkTpl_03_root_pointConstraint1.crp";
connectAttr "SplRN.phl[53]" "FkTpl_03_root_pointConstraint1.crt";
connectAttr "Spl:input_00_link_parentConstraint1.ctx" "SplRN.phl[54]";
connectAttr "Spl:input_00_link_parentConstraint1.cty" "SplRN.phl[55]";
connectAttr "Spl:input_00_link_parentConstraint1.ctz" "SplRN.phl[56]";
connectAttr "Spl:input_00_link_parentConstraint1.crx" "SplRN.phl[57]";
connectAttr "Spl:input_00_link_parentConstraint1.cry" "SplRN.phl[58]";
connectAttr "Spl:input_00_link_parentConstraint1.crz" "SplRN.phl[59]";
connectAttr "SplRN.phl[60]" "Spl:input_00_link_parentConstraint1.cro";
connectAttr "SplRN.phl[61]" "Spl:input_00_link_parentConstraint1.cpim";
connectAttr "SplRN.phl[62]" "Spl:input_00_link_parentConstraint1.crp";
connectAttr "SplRN.phl[63]" "Spl:input_00_link_parentConstraint1.crt";
connectAttr "FkAux_01_jnt.t" "SplRN.phl[64]";
connectAttr "FkAux_01_jnt.r" "SplRN.phl[65]";
connectAttr "FkAux_02_jnt.t" "SplRN.phl[66]";
connectAttr "FkAux_02_jnt.r" "SplRN.phl[67]";
connectAttr "FkAux_03_jnt.t" "SplRN.phl[68]";
connectAttr "FkAux_03_jnt.r" "SplRN.phl[69]";
connectAttr "SplRN.phl[70]" "ControlsSet.dnsm" -na;
connectAttr "SplRN.phl[71]" "SkinJointsSet.dnsm" -na;
connectAttr "SplRN.phl[72]" "LinkSet.dnsm" -na;
connectAttr "SplIk_00_locShape.wp" "FkAux_00_crvShape.cp[0]";
connectAttr "SplIk_01_locShape.wp" "FkAux_00_crvShape.cp[1]";
connectAttr "SplIk_02_locShape.wp" "FkAux_00_crvShape.cp[2]";
connectAttr "FkAux_00_jnt.msg" "FkAux_00_ih.hsj";
connectAttr "effector1.hp" "FkAux_00_ih.hee";
connectAttr "ikSplineSolver.msg" "FkAux_00_ih.hsv";
connectAttr "FkAux_00_crvShape.ws" "FkAux_00_ih.ic";
connectAttr "SplIk_00_ctr.wm" "FkAux_00_ih.dwum";
connectAttr "SplIk_02_ctr.wm" "FkAux_00_ih.dwue";
connectAttr "FkAux_00_clp.opr" "FkAux_01_jnt.ty";
connectAttr "FkAux_00_jnt.s" "FkAux_01_jnt.is";
connectAttr "FkAux_00_clp.opr" "FkAux_02_jnt.ty";
connectAttr "FkAux_01_jnt.s" "FkAux_02_jnt.is";
connectAttr "FkAux_00_clp.opr" "FkAux_03_jnt.ty";
connectAttr "FkAux_02_jnt.s" "FkAux_03_jnt.is";
connectAttr "FkAux_03_jnt.s" "FkAuxEnd_03_jnt.is";
connectAttr "MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "input_00_link.msg" "SplIkTpl_00_root._relatedTo[0]";
connectAttr "input_01_link.msg" "SplIkTpl_02_root._relatedTo[0]";
connectAttr "SplIk_01_root_pointConstraint1.ctx" "SplIk_01_root.tx";
connectAttr "SplIk_01_root_pointConstraint1.cty" "SplIk_01_root.ty";
connectAttr "SplIk_01_root_pointConstraint1.ctz" "SplIk_01_root.tz";
connectAttr "SplIk_01_root_orientConstraint1.crx" "SplIk_01_root.rx";
connectAttr "SplIk_01_root_orientConstraint1.cry" "SplIk_01_root.ry";
connectAttr "SplIk_01_root_orientConstraint1.crz" "SplIk_01_root.rz";
connectAttr "SplIk_01_root.pim" "SplIk_01_root_pointConstraint1.cpim";
connectAttr "SplIk_01_root.rp" "SplIk_01_root_pointConstraint1.crp";
connectAttr "SplIk_01_root.rpt" "SplIk_01_root_pointConstraint1.crt";
connectAttr "SplIk_00_ctr.t" "SplIk_01_root_pointConstraint1.tg[0].tt";
connectAttr "SplIk_00_ctr.rp" "SplIk_01_root_pointConstraint1.tg[0].trp";
connectAttr "SplIk_00_ctr.rpt" "SplIk_01_root_pointConstraint1.tg[0].trt";
connectAttr "SplIk_00_ctr.pm" "SplIk_01_root_pointConstraint1.tg[0].tpm";
connectAttr "SplIk_01_root_pointConstraint1.w0" "SplIk_01_root_pointConstraint1.tg[0].tw"
		;
connectAttr "SplIk_02_ctr.t" "SplIk_01_root_pointConstraint1.tg[1].tt";
connectAttr "SplIk_02_ctr.rp" "SplIk_01_root_pointConstraint1.tg[1].trp";
connectAttr "SplIk_02_ctr.rpt" "SplIk_01_root_pointConstraint1.tg[1].trt";
connectAttr "SplIk_02_ctr.pm" "SplIk_01_root_pointConstraint1.tg[1].tpm";
connectAttr "SplIk_01_root_pointConstraint1.w1" "SplIk_01_root_pointConstraint1.tg[1].tw"
		;
connectAttr "SplIk_01_root.ro" "SplIk_01_root_orientConstraint1.cro";
connectAttr "SplIk_01_root.pim" "SplIk_01_root_orientConstraint1.cpim";
connectAttr "SplIk_00_ctr.r" "SplIk_01_root_orientConstraint1.tg[0].tr";
connectAttr "SplIk_00_ctr.ro" "SplIk_01_root_orientConstraint1.tg[0].tro";
connectAttr "SplIk_00_ctr.pm" "SplIk_01_root_orientConstraint1.tg[0].tpm";
connectAttr "SplIk_01_root_orientConstraint1.w0" "SplIk_01_root_orientConstraint1.tg[0].tw"
		;
connectAttr "SplIk_02_ctr.r" "SplIk_01_root_orientConstraint1.tg[1].tr";
connectAttr "SplIk_02_ctr.ro" "SplIk_01_root_orientConstraint1.tg[1].tro";
connectAttr "SplIk_02_ctr.pm" "SplIk_01_root_orientConstraint1.tg[1].tpm";
connectAttr "SplIk_01_root_orientConstraint1.w1" "SplIk_01_root_orientConstraint1.tg[1].tw"
		;
connectAttr "FkAux_00_jnt.t" "Spl:input_00_link_parentConstraint1.tg[0].tt";
connectAttr "FkAux_00_jnt.rp" "Spl:input_00_link_parentConstraint1.tg[0].trp";
connectAttr "FkAux_00_jnt.rpt" "Spl:input_00_link_parentConstraint1.tg[0].trt";
connectAttr "FkAux_00_jnt.r" "Spl:input_00_link_parentConstraint1.tg[0].tr";
connectAttr "FkAux_00_jnt.ro" "Spl:input_00_link_parentConstraint1.tg[0].tro";
connectAttr "FkAux_00_jnt.s" "Spl:input_00_link_parentConstraint1.tg[0].ts";
connectAttr "FkAux_00_jnt.pm" "Spl:input_00_link_parentConstraint1.tg[0].tpm";
connectAttr "FkAux_00_jnt.jo" "Spl:input_00_link_parentConstraint1.tg[0].tjo";
connectAttr "FkAux_00_jnt.ssc" "Spl:input_00_link_parentConstraint1.tg[0].tsc";
connectAttr "FkAux_00_jnt.is" "Spl:input_00_link_parentConstraint1.tg[0].tis";
connectAttr "Spl:input_00_link_parentConstraint1.w0" "Spl:input_00_link_parentConstraint1.tg[0].tw"
		;
connectAttr "SplIkTpl_00_root.t" "FkTpl_01_root_pointConstraint1.tg[0].tt";
connectAttr "SplIkTpl_00_root.rp" "FkTpl_01_root_pointConstraint1.tg[0].trp";
connectAttr "SplIkTpl_00_root.rpt" "FkTpl_01_root_pointConstraint1.tg[0].trt";
connectAttr "SplIkTpl_00_root.pm" "FkTpl_01_root_pointConstraint1.tg[0].tpm";
connectAttr "FkTpl_01_root_pointConstraint1.w0" "FkTpl_01_root_pointConstraint1.tg[0].tw"
		;
connectAttr "SplIkTpl_02_root.t" "FkTpl_01_root_pointConstraint1.tg[1].tt";
connectAttr "SplIkTpl_02_root.rp" "FkTpl_01_root_pointConstraint1.tg[1].trp";
connectAttr "SplIkTpl_02_root.rpt" "FkTpl_01_root_pointConstraint1.tg[1].trt";
connectAttr "SplIkTpl_02_root.pm" "FkTpl_01_root_pointConstraint1.tg[1].tpm";
connectAttr "FkTpl_01_root_pointConstraint1.w1" "FkTpl_01_root_pointConstraint1.tg[1].tw"
		;
connectAttr "SplIkTpl_00_root.t" "FkTpl_02_root_pointConstraint1.tg[0].tt";
connectAttr "SplIkTpl_00_root.rp" "FkTpl_02_root_pointConstraint1.tg[0].trp";
connectAttr "SplIkTpl_00_root.rpt" "FkTpl_02_root_pointConstraint1.tg[0].trt";
connectAttr "SplIkTpl_00_root.pm" "FkTpl_02_root_pointConstraint1.tg[0].tpm";
connectAttr "FkTpl_02_root_pointConstraint1.w0" "FkTpl_02_root_pointConstraint1.tg[0].tw"
		;
connectAttr "SplIkTpl_02_root.t" "FkTpl_02_root_pointConstraint1.tg[1].tt";
connectAttr "SplIkTpl_02_root.rp" "FkTpl_02_root_pointConstraint1.tg[1].trp";
connectAttr "SplIkTpl_02_root.rpt" "FkTpl_02_root_pointConstraint1.tg[1].trt";
connectAttr "SplIkTpl_02_root.pm" "FkTpl_02_root_pointConstraint1.tg[1].tpm";
connectAttr "FkTpl_02_root_pointConstraint1.w1" "FkTpl_02_root_pointConstraint1.tg[1].tw"
		;
connectAttr "SplIkTpl_02_root.t" "FkTpl_03_root_pointConstraint1.tg[0].tt";
connectAttr "SplIkTpl_02_root.rp" "FkTpl_03_root_pointConstraint1.tg[0].trp";
connectAttr "SplIkTpl_02_root.rpt" "FkTpl_03_root_pointConstraint1.tg[0].trt";
connectAttr "SplIkTpl_02_root.pm" "FkTpl_03_root_pointConstraint1.tg[0].tpm";
connectAttr "FkTpl_03_root_pointConstraint1.w0" "FkTpl_03_root_pointConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "FkAux_00_crvShape.ws" "FkAux_00_cvinf.ic";
connectAttr "FkAux_00_cvinf.al" "FkAux_00_mdv.i1x";
connectAttr "FkAux_00_mdv.ox" "FkAux_00_clp.ipr";
connectAttr "SplFk_02_tag.pare" "SplFk_01_tag.child[0]";
connectAttr "SplFk_03_tag.pare" "SplFk_02_tag.child[0]";
connectAttr "SplFk_01_tag.pare" "SplFk_00_tag.child[0]";
connectAttr "SplFk_04_tag.pare" "SplFk_03_tag.child[0]";
connectAttr "SplFk_04_tag.msg" "SplFk_04_tag.child[0]";
connectAttr "SplIk_00_ctr.msg" "SplIk_00_tag.act";
connectAttr "SplIk_00_tag.msg" "SplIk_00_tag.child[0]";
connectAttr "SplIk_01_ctr.msg" "SplIk_01_tag.act";
connectAttr "SplIk_01_tag.msg" "SplIk_01_tag.child[0]";
connectAttr "SplIk_02_ctr.msg" "SplIk_02_tag.act";
connectAttr "SplIk_02_tag.msg" "SplIk_02_tag.child[0]";
connectAttr "SplIkTpl_00_root.iog" "SplRN.phl[35]";
connectAttr "SplIkTpl_02_root.iog" "SplRN.phl[36]";
connectAttr "SplRNfosterParent1.msg" "SplRN.fp";
connectAttr "sharedReferenceNode.sr" "SplRN.sr";
connectAttr "SplIkTpl_00_root.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "SplIkTpl_02_root.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "SplIk_00_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "SplIk_02_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "input_00_link.iog" "LinkSet.dsm" -na;
connectAttr "input_01_link.iog" "LinkSet.dsm" -na;
connectAttr "SplIk_01_ctr.iog" "Secondaries.dsm" -na;
connectAttr "FkAux_00_cvinf.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "FkAux_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "FkAux_00_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikSplineSolver.msg" ":ikSystem.sol" -na;
// End of 3Ik4Fk4Bones.ma
