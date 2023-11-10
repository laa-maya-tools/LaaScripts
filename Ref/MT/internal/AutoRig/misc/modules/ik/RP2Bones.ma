//Maya ASCII 2020 scene
//Name: RP2Bones.ma
//Last modified: Tue, Jul 19, 2022 08:23:32 AM
//Codeset: 1252
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "D6DB94D8-413F-D917-EA29-95ABB09A31CE";
createNode transform -s -n "persp";
	rename -uid "432E97F4-4C8F-FEE9-B2D9-E2B19AF8C353";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 37.704719989808211 31.451461774266779 69.941390804666099 ;
	setAttr ".r" -type "double3" -21.938352729579428 6.999999999999913 4.0055501149795378e-16 ;
	setAttr ".rp" -type "double3" 0 -8.8817841970012523e-16 0 ;
	setAttr ".rpt" -type "double3" -1.0989280019688014e-14 -4.2177348945755501e-14 1.3384310878191735e-13 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "255AF00D-4778-12C2-750F-789594FBCE41";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 79.179082933397666;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 50.999994985219132 0 1.0655284654603747e-08 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "FA203144-4822-51FF-37FB-6EB564E21EF7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 51.216634993109849 1001.395643646957 1.4673750576293259 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "E61384F2-4F7C-C062-2191-1F8F886A9F18";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1004.395643646957;
	setAttr ".ow" 22.36713383031892;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 50.999989970438278 -3 2.3386531822211509e-08 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "D35BFF05-4D14-3ABE-7965-6FBBA4EDB118";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 25.548273193782247 -0.095387839877085323 1001.4878495818449 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "CD28237F-46FF-8141-BBED-E1B76A2A7B60";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1004.9878495818449;
	setAttr ".ow" 20.97967652918754;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 24.999998296731384 0 -3.5 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "D3D0231F-460C-5801-8DA0-C08B4573D5A6";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.20656120987 1.0467180734739778 -2.3118456951265411 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "3D3B91F0-4B0E-D170-BD70-D5A220D07AEF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 975.20656291313855;
	setAttr ".ow" 20.613517422217107;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 24.999998296731384 5.8361871335677051e-08 -3.0538764024172593 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Sys_00_grp";
	rename -uid "170F4F0F-431E-C8D4-CBF0-74883FEA8BCE";
	setAttr ".v" no;
createNode ikHandle -n "IkPole_00_iksc" -p "Sys_00_grp";
	rename -uid "2E4EB6D8-4565-2D7D-0B42-459F27C3BB67";
	setAttr ".roc" yes;
createNode pointConstraint -n "IkPoleIksc_00_pnc" -p "IkPole_00_iksc";
	rename -uid "A801C1CD-4695-953D-8373-A4B32A5D856D";
createNode transform -n "OrigSystem_00_tr" -p "Sys_00_grp";
	rename -uid "31DDBD0F-4405-9F48-E0D3-32AD324A3068";
createNode joint -n "IkPole_00_jnt" -p "OrigSystem_00_tr";
	rename -uid "E77BEA3D-4D46-28A9-C633-2C870EFFC9D3";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "IkPoleEnd_00_jnt" -p "IkPole_00_jnt";
	rename -uid "A12CC7C9-442B-4C6E-AB41-C290CB4CE635";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode ikEffector -n "effector2" -p "IkPole_00_jnt";
	rename -uid "95D26294-4523-22C4-92C5-BC9E5896BA3D";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "IkPole_00_root" -p "IkPole_00_jnt";
	rename -uid "5ED6CDE4-4186-6663-7EE8-24B41BFEB871";
createNode transform -n "IkPole_00_ctr" -p "IkPole_00_root";
	rename -uid "C93FEB75-4E7E-0088-2849-0FA11366480F";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 25 0 -15 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "IkPole_00_ctrLocShape" -p "IkPole_00_ctr";
	rename -uid "07869A31-4DC3-D03B-C39E-21813763503A";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
createNode joint -n "Aux_00_jnt" -p "OrigSystem_00_tr";
	rename -uid "7AB13CA2-4AA2-F8A3-657B-05B24F5907E9";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Aux_01_jnt" -p "Aux_00_jnt";
	rename -uid "1BFF01FE-4C5D-196A-5B57-C0ADE739A8E5";
	setAttr ".t" -type "double3" 25 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 -90 0 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "AuxEnd_02_jnt" -p "Aux_01_jnt";
	rename -uid "E06C82D2-4CA6-2D27-D3F4-D7A9ED355554";
	setAttr ".t" -type "double3" 25 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode ikEffector -n "effector1" -p "Aux_01_jnt";
	rename -uid "0DD17917-415B-C889-1EBA-169AA3CDE897";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode orientConstraint -n "AuxJnt_01_orc" -p "Aux_01_jnt";
	rename -uid "9A0D8EAC-4722-3138-04ED-57A10F751348";
	setAttr ".int" 0;
createNode transform -n "Fk_01_snapper" -p "Aux_01_jnt";
	rename -uid "DDD9C256-46C2-24C0-729C-7A8F0E12389A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".r" -type "double3" 0 4.5016297514303023e-06 0 ;
createNode orientConstraint -n "AuxJnt_00_orc" -p "Aux_00_jnt";
	rename -uid "DEAC21D4-4CF8-3778-D262-EC97A516FB6C";
	setAttr ".int" 0;
createNode transform -n "Fk_00_snapper" -p "Aux_00_jnt";
	rename -uid "24C6273C-4E9B-E932-87EF-4193B67CE8AF";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
createNode pointConstraint -n "OrigSystemTr_00_pnc" -p "OrigSystem_00_tr";
	rename -uid "877F59D3-480C-DA01-AF05-8B8A51545BC4";
createNode orientConstraint -n "outputLink_00_orc" -p "Sys_00_grp";
	rename -uid "85BA2DBA-441C-0B06-FD6E-25B856FA09CA";
	setAttr -s 2 ".tg";
createNode pointConstraint -n "outputLink_00_pnc" -p "Sys_00_grp";
	rename -uid "3387347A-435E-4B0A-8D8A-6DAF1A22FAFE";
createNode transform -n "Controls_00_grp";
	rename -uid "30275F62-45CD-2576-B5DC-358545071E55";
createNode transform -n "Fk_00_root" -p "Controls_00_grp";
	rename -uid "6A04E503-4AC8-F3A8-250D-FE9D334AB75A";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_00_ctr" -p "Fk_00_root";
	rename -uid "150D33AA-48C7-80C7-6954-49B44DD88AF1";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
createNode transform -n "Fk_01_root" -p "Fk_00_ctr";
	rename -uid "1449CC46-4A95-0289-FCCD-9AA06DFEE942";
	setAttr ".t" -type "double3" 25 0 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_01_ctr" -p "Fk_01_root";
	rename -uid "A2263475-4500-A855-7CDD-8488E8093FBB";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
	setAttr ".mntl" -type "double3" 0 -1 -1 ;
	setAttr ".mtxe" yes;
createNode transform -n "Fk_02_root" -p "Fk_01_ctr";
	rename -uid "B98D330B-4E93-2338-E714-4CB5A3D9F944";
	setAttr ".t" -type "double3" 25 3.3306690738754696e-16 2.3386531822211509e-08 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_02_ctr" -p "Fk_02_root";
	rename -uid "CAE0DFE0-4F29-71A2-4B93-A4AE5006049D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 -1 -1 ;
	setAttr ".mtxe" yes;
createNode transform -n "Ik_00_snapper" -p "Fk_02_ctr";
	rename -uid "5805713B-452C-D0CC-A156-6498E27AA309";
	setAttr ".v" no;
createNode nurbsCurve -n "Fk_02_ctrShape" -p "Fk_02_ctr";
	rename -uid "1530E135-44F3-DCDD-59F9-7991587C487C";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893772e-05 3.75 -3.75
		-4.9999998736893772e-05 3.75 3.75
		-4.9999998736893772e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 3.75 3.75
		2.5 3.75 -3.75
		2.5 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 -3.75
		-4.9999998736893772e-05 3.75 -3.75
		2.5 3.75 -3.75
		2.5 3.75 3.75
		-4.9999998736893772e-05 3.75 3.75
		-4.9999998736893772e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 3.75
		;
createNode nurbsCurve -n "Fk_01_ctrShape" -p "Fk_01_ctr";
	rename -uid "90ED99BB-4791-A05A-DF5D-039606C15377";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-05 2.5 -2.5
		-4.9999998736893758e-05 2.5 2.5
		-4.9999998736893758e-05 -2.5 2.5
		24 -2.5 2.5
		24 2.5 2.5
		24 2.5 -2.5
		24 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 -2.5
		-4.9999998736893758e-05 2.5 -2.5
		24 2.5 -2.5
		24 2.5 2.5
		-4.9999998736893758e-05 2.5 2.5
		-4.9999998736893758e-05 -2.5 2.5
		24 -2.5 2.5
		24 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 2.5
		;
createNode transform -n "TwistSnapper_00_root" -p "Fk_00_ctr";
	rename -uid "107C3390-4F91-85EC-D91C-8D93FF9B5352";
	setAttr ".v" no;
createNode transform -n "Twist_00_snapper" -p "TwistSnapper_00_root";
	rename -uid "DAEC07F6-4D44-BDA5-1CBF-6FAEEC21D8C5";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
createNode aimConstraint -n "TwistSnapper_00_snapper_aimc" -p "Twist_00_snapper";
	rename -uid "BE888702-452A-42D4-8AFC-3F97E63553AB";
	addAttr -dcb 0 -ci true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -at "double";
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
	setAttr ".u" -type "double3" 0 0 -1 ;
	setAttr ".wut" 1;
	setAttr -k on ".w0";
createNode aimConstraint -n "TwistSnapperRoot_00_aimc" -p "TwistSnapper_00_root";
	rename -uid "CE6F91AC-45EF-7D3C-77E0-479B57D28A5F";
	addAttr -dcb 0 -ci true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -at "double";
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
	setAttr ".u" -type "double3" 0 0 -1 ;
	setAttr ".wut" 1;
	setAttr -k on ".w0";
createNode nurbsCurve -n "Fk_00_ctrShape" -p "Fk_00_ctr";
	rename -uid "A2108118-4569-FD3A-5F57-DC9C318BFF99";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-05 2.5 -2.5
		-4.9999998736893758e-05 2.5 2.5
		-4.9999998736893758e-05 -2.5 2.5
		24 -2.5 2.5
		24 2.5 2.5
		24 2.5 -2.5
		24 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 -2.5
		-4.9999998736893758e-05 2.5 -2.5
		24 2.5 -2.5
		24 2.5 2.5
		-4.9999998736893758e-05 2.5 2.5
		-4.9999998736893758e-05 -2.5 2.5
		24 -2.5 2.5
		24 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 -2.5
		-4.9999998736893758e-05 -2.5 2.5
		;
createNode pointConstraint -n "FkRoot_00_root_pnc" -p "Fk_00_root";
	rename -uid "5A9C2911-4716-B16D-9A3E-569F73468F86";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Aux_00_jntW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode transform -n "IkCtr_00_root" -p "Controls_00_grp";
	rename -uid "CD007EC9-40FD-220B-2822-B19339907EF4";
createNode transform -n "Ik_00_root" -p "IkCtr_00_root";
	rename -uid "BE457E7C-4C1F-0E75-ED3E-2384761365B6";
	setAttr ".t" -type "double3" 50 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Ik_00_ctr" -p "Ik_00_root";
	rename -uid "48A21C7A-49C6-F23F-970F-688BC4F0A354";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "IkChilds_00_grp" -p "Ik_00_ctr";
	rename -uid "596160ED-460B-6101-ED16-07A1667FA4F8";
	setAttr -l on ".v" no;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode ikHandle -n "Ik_00_Ikh" -p "IkChilds_00_grp";
	rename -uid "BC6ACDB4-44D8-0AC8-FC5A-248BA88E3906";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -l on ".off";
	setAttr -l on ".rol";
	setAttr -l on ".twi";
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "IkIkh_00_pvc" -p "Ik_00_Ikh";
	rename -uid "906DCA83-440F-A5C3-563B-DEB8E50CD48A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "limbPVec_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2 0 -1 ;
	setAttr -k on ".w0";
createNode transform -n "Fk_02_snapper" -p "Ik_00_ctr";
	rename -uid "5FF99BAF-4DAE-7485-B5FA-69BB4EFEC3AE";
	setAttr ".v" no;
createNode nurbsCurve -n "Ik_00_ctrShape" -p "Ik_00_ctr";
	rename -uid "4585DBEC-4633-1EF3-3876-A39A6508C8C0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893772e-05 3.75 -3.75
		-4.9999998736893772e-05 3.75 3.75
		-4.9999998736893772e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 3.75 3.75
		2.5 3.75 -3.75
		2.5 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 -3.75
		-4.9999998736893772e-05 3.75 -3.75
		2.5 3.75 -3.75
		2.5 3.75 3.75
		-4.9999998736893772e-05 3.75 3.75
		-4.9999998736893772e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 -3.75
		-4.9999998736893772e-05 -3.75 3.75
		;
createNode transform -n "Config_00_root" -p "Controls_00_grp";
	rename -uid "14C3C5D3-429A-4A35-312D-F596E5A37272";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Config_00_ctr" -p "Config_00_root";
	rename -uid "693310F3-4384-DA03-A55A-A2A6301E3C82";
	addAttr -ci true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
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
	setAttr -k on ".fkIk" 0.5;
createNode nurbsCurve -n "Config_00_ctrShape" -p "Config_00_ctr";
	rename -uid "633D63FB-44C8-206D-7AEE-DA98FFDC7843";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 10 2 no 3
		11 0 1 2 3 4 5 6 7 8 9 10
		11
		1.6054565561205574 2.8379390945597356 0
		0.019643116439580426 2.8379390945597356 0
		0.019643116439580426 0 0
		0.42233082085178741 0 0
		0.42233082085178741 1.2885691114173157 0
		1.4156191501661386 1.2885691114173157 0
		1.4156191501661386 1.5857741194452566 0
		0.42233082085178741 1.5857741194452566 0
		0.42233082085178741 2.5368853751423321 0
		1.6054565561205574 2.5368853751423321 0
		1.6054565561205574 2.8379390945597356 0
		;
createNode nurbsCurve -n "Config_00_ctrShape1" -p "Config_00_ctr";
	rename -uid "0FAF184A-431C-8FF4-401C-3591DCF6FFDA";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		2.518042459101947 2.8379390945597356 0
		2.1402920461444248 2.8379390945597356 0
		2.1402920461444248 0 0
		2.518042459101947 0 0
		2.518042459101947 1.4381534966530989 0
		3.7587006635403468 0 0
		4.267656257866868 0 0
		2.9597657276493394 1.4838652388530824 0
		4.0713786385185529 2.8379390945597356 0
		3.6666489205005477 2.8379390945597356 0
		2.518042459101947 1.441962844550249 0
		2.518042459101947 2.8379390945597356 0
		;
createNode nurbsCurve -n "Config_00_ctrShape2" -p "Config_00_ctr";
	rename -uid "70DF9DB2-4014-76AC-8A00-958ABB821451";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		5.9604058151864745 2.8379390945597356 0
		5.760986037507295 2.8379390945597356 0
		4.7523424856669285 -0.56758781891194632 0
		4.9517619172934211 -0.56758781891194632 0
		5.9604058151864745 2.8379390945597356 0
		;
createNode nurbsCurve -n "Config_00_ctrShape3" -p "Config_00_ctr";
	rename -uid "B0DA78EA-41C1-2410-2430-F4828E56DE8F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		8.2516489832077085 2.8379390945597356 0
		7.8738985702501836 2.8379390945597356 0
		7.8738985702501836 0 0
		8.2516489832077085 0 0
		8.2516489832077085 1.4381534966530989 0
		9.4923073606724486 0 0
		10.001262954998966 0 0
		8.6933720787287641 1.4838652388530824 0
		9.8049853356506418 2.8379390945597356 0
		9.4002552715799741 2.8379390945597356 0
		8.2516489832077085 1.441962844550249 0
		8.2516489832077085 2.8379390945597356 0
		;
createNode nurbsCurve -n "Config_00_ctrShape4" -p "Config_00_ctr";
	rename -uid "A93172F5-4D4E-C70B-5A51-E3B9A6F24EB0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		7.1357945046445099 2.8379390945597356 0
		6.7331068434888905 2.8379390945597356 0
		6.7331068434888905 0 0
		7.1357945046445099 0 0
		7.1357945046445099 2.8379390945597356 0
		;
createNode parentConstraint -n "ConfigRoot_00_prc" -p "Config_00_root";
	rename -uid "FECA59E6-483E-0CFB-1330-43B439D7E5EB";
	setAttr ".lr" -type "double3" 0 8.8315032682217241e-06 0 ;
createNode transform -n "Tpl_00_tpl";
	rename -uid "ED693278-4EBD-7C38-D2A9-9B931546B6F9";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "OrigSystemTpl_00_tr" -p "Tpl_00_tpl";
	rename -uid "7600D105-4AE2-828C-14BE-4F88E0A70B14";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "OrigSystemTpl_00_trShape" -p "OrigSystemTpl_00_tr";
	rename -uid "3F373E4E-45C4-AA15-08E3-47BC5EBFF7F6";
	setAttr -k off ".v";
createNode transform -n "IkTpl_01_loc" -p "OrigSystemTpl_00_tr";
	rename -uid "BE89EF62-4D6B-4ACA-4B99-3ABEBC3A6584";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 25 0 0 ;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "IkTpl_01_locShape" -p "IkTpl_01_loc";
	rename -uid "B7F900C3-4E3E-029D-8001-B289C4A5D77B";
	setAttr -k off ".v";
createNode transform -n "IkTpl_00_root" -p "IkTpl_01_loc";
	rename -uid "1EA91F22-42BD-C5F5-4A62-02A44DE03CFE";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 25 3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
createNode locator -n "IkTpl_00_rootShape" -p "IkTpl_00_root";
	rename -uid "09D206A5-48DE-51A1-DD75-DD8694BFED97";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTplCtr_02_orc" -p "IkTpl_00_root";
	rename -uid "BF2197EA-46CE-F5A7-F793-4FB1E62405DA";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkTpl_00_rootW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" -3.5527136788005009e-15 0 2.3570478260457819e-07 ;
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
createNode transform -n "IkPoleTpl_00_ctr" -p "IkTpl_01_loc";
	rename -uid "119AD97A-42A5-22B5-322B-3EBC4A414557";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 0 -15 ;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "IkPoleTpl_00_ctrShape" -p "IkPoleTpl_00_ctr";
	rename -uid "B0F88A34-4EE6-EDDE-2959-6CA8B103452C";
	setAttr -k off ".v";
createNode transform -n "FKTpl_02_root" -p "IkTpl_01_loc";
	rename -uid "4BFD540C-45FF-ED7D-3073-48B85777B09A";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FKTpl_02_rootShape" -p "FKTpl_02_root";
	rename -uid "E3E3CC47-4E6F-7CA5-E80F-CD8A961FA879";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 1 0 ;
createNode transform -n "FkTpl_02_ctr" -p "FKTpl_02_root";
	rename -uid "4661DB04-4826-F674-DBBE-CC87BABEA51E";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 3.3306690738754696e-16 2.3570478260457819e-07 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FkTpl_02_ctrShape" -p "FkTpl_02_ctr";
	rename -uid "DC65EBF7-4630-985E-AC20-4185E60B5534";
	setAttr -k off ".v";
createNode transform -n "FKTpl_01_root" -p "OrigSystemTpl_00_tr";
	rename -uid "90F2FF9E-4D1D-13BA-893C-69AA42FB7FAB";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FKTpl_01_rootShape" -p "FKTpl_01_root";
	rename -uid "3989875E-4252-88DC-03ED-4493D3349396";
	setAttr -k off ".v";
createNode transform -n "FkTpl_01_ctr" -p "FKTpl_01_root";
	rename -uid "114CE905-4AA6-53EC-455B-6C82940E6445";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FkTpl_01_ctrShape" -p "FkTpl_01_ctr";
	rename -uid "B539A8ED-4B09-C098-1240-08BCE6490049";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTpl_01_ctr_orientConstraint1" -p "FkTpl_01_ctr";
	rename -uid "D69454A6-491F-CD74-D8AD-62BE4EA7C6C3";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "IkTpl_01_locW0" -dv 1 -min 0 -at "double";
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
createNode transform -n "FKTpl_00_root" -p "Tpl_00_tpl";
	rename -uid "ACAC05A7-40C2-C229-A44C-3B8FB9ABAAAE";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "FKTpl_00_rootShape" -p "FKTpl_00_root";
	rename -uid "16BC938C-4CB9-A58C-259C-FFB9B75D5061";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "FkTpl_00_ctr" -p "FKTpl_00_root";
	rename -uid "D4DED73E-4B9A-97E3-43B8-14AAE12E9FAD";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FkTpl_00_ctrShape" -p "FkTpl_00_ctr";
	rename -uid "EDDBF116-4D8F-988D-8C05-D68A1147F141";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTpl_00_ctr_orientConstraint1" -p "FkTpl_00_ctr";
	rename -uid "1580B3CB-4C19-8136-BCE1-45AD242A17D7";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "origSystemTpl_00_trW0" -dv 1 -min 
		0 -at "double";
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
createNode transform -n "input_00_link";
	rename -uid "FFDC3984-438B-AF18-F10E-258002C7CE25";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "output_00_link";
	rename -uid "954841DB-4A3C-8AEF-D86D-ED9F191EF60A";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.40392157 0.63137257 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "135E0CA0-40E1-7147-03D1-55B209F3B4D6";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "D4DB1481-43B2-B640-886C-CABCBEC14957";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "F6148400-4C2D-DA4B-9889-4D86B22AE381";
createNode displayLayerManager -n "layerManager";
	rename -uid "BE200395-4C05-6564-625E-F2A414B83D0C";
createNode displayLayer -n "defaultLayer";
	rename -uid "6955C09E-484F-5C45-4C09-EFA855C4CADD";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "A40C8D80-4222-30E4-D0AE-FE8B1AEC66D9";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "81A2B3B6-4AC8-9A50-96D2-62AAE09F295A";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "F350B137-4764-3F39-5E04-FCBC8685B7DB";
createNode reverse -n "Config_00_rev";
	rename -uid "6A14EA6B-4E0F-6AF7-39E3-E59B67688692";
createNode objectSet -n "ControlsSet";
	rename -uid "A3F97BB9-4355-DD38-5F2F-12A7628F8A3F";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "LinkSet";
	rename -uid "D5C99B7E-4346-8F90-5DFA-FC8A57AD7E48";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
createNode controller -n "Config_00_tag";
	rename -uid "64C73E42-4415-C5F1-563B-088A3C1B7166";
createNode controller -n "Fk_00_tag";
	rename -uid "373A13DD-449F-6C89-4C2F-3A9397568D04";
createNode controller -n "Ik_00_tag";
	rename -uid "E7CA1AA8-416B-76E5-2CE9-4EBFAD4BDFD8";
createNode controller -n "Twist_00_tag";
	rename -uid "A1B9C43E-41FF-7290-7B69-3BAA03E50B52";
createNode controller -n "Pin_01_tag";
	rename -uid "68ECC4BA-4539-AC0F-99A4-F89761A9C7C5";
createNode controller -n "Fk_01_tag";
	rename -uid "68D517D1-4141-A7D9-D0CC-B4820EB553F6";
createNode controller -n "Fk_02_tag";
	rename -uid "BA72AFF1-4423-C475-64F8-B3822485CC9F";
createNode objectSet -n "Fk";
	rename -uid "2FA0CF07-4971-228B-09E1-7CA48980EB70";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "Ik";
	rename -uid "CE0B7178-4C0F-FB92-525C-43ADE07F8E5D";
	setAttr ".ihi" 0;
createNode ikSCsolver -n "ikSCsolver";
	rename -uid "31A9EAC3-4F20-F585-B991-428AE4458530";
createNode script -n "MetadataLimbSnapping";
	rename -uid "5CFB51AB-4D1E-A771-9C5E-66891A39879E";
	addAttr -s false -ci true -sn "switchControl" -ln "switchControl" -at "message";
	addAttr -s false -ci true -sn "poleVControl" -ln "poleVControl" -at "message";
	addAttr -s false -ci true -sn "poleVSnapper" -ln "poleVSnapper" -at "message";
	addAttr -s false -ci true -m -sn "fkControls" -ln "fkControls" -at "message";
	addAttr -s false -ci true -m -sn "fkSnappers" -ln "fkSnappers" -at "message";
	addAttr -s false -ci true -sn "ikControl" -ln "ikControl" -at "message";
	addAttr -s false -ci true -sn "ikSnapper" -ln "ikSnapper" -at "message";
	addAttr -ci true -sn "poleVMultiplier" -ln "poleVMultiplier" -dv 1 -min -1 -max 
		1 -at "long";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr -l on ".stp" 1;
	setAttr -s 3 ".fkControls";
	setAttr -s 3 ".fkSnappers";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "2BA60D26-46B5-B9E7-0864-4B840B0FD84D";
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
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"wireframe\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 1\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1259\n            -height 702\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n"
		+ "            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n"
		+ "            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n"
		+ "            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n"
		+ "                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n"
		+ "                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n"
		+ "                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 1\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 1\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1259\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 1\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1259\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "83672BB7-4CB9-0F7A-F701-DB98B4A0D575";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode script -n "MetadataTemplate";
	rename -uid "7F7BCA3D-4153-1EAA-81D3-9499DA8E2E24";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" (
		"import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#Ik_*_ctr\nfor ind in 3,5,7:\n    template = cmds.listConnections(\"{}._inputTemplate[{}]\".format(_METADATA_TEMPLATE_, ind))[0]\n    try:\n        cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".r\", 0,0,0 )\n    except:\n        cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".ry\", 0 )\ndel template\n#OrigSystem_00_tr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, t=cmds.xform(template, t=True, ws=True, q=True))\ndel template, this\n#Ik_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[2]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\n"
		+ "cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_00_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[3]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_01_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[4]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_01_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[5]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_02_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[6]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\n"
		+ "del template, this\n#Fk_02_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[7]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#IkPole_00_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[7]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this");
	setAttr -l on ".stp" 1;
	setAttr -s 9 "._inputTemplate";
createNode objectSet -n "Secondaries";
	rename -uid "634997F7-433C-B01F-7276-4B9F010EFEF5";
	setAttr ".ihi" 0;
select -ne :time1;
	setAttr -av -k on ".cch";
	setAttr -av -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -k on ".o" 12;
	setAttr -av -k on ".unw" 12;
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
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
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
connectAttr "IkPole_00_jnt.msg" "IkPole_00_iksc.hsj";
connectAttr "effector2.hp" "IkPole_00_iksc.hee";
connectAttr "ikSCsolver.msg" "IkPole_00_iksc.hsv";
connectAttr "IkPoleIksc_00_pnc.ct" "IkPole_00_iksc.t";
connectAttr "Ik_00_ctr.wm" "IkPoleIksc_00_pnc.tg[0].tpm";
connectAttr "IkPole_00_iksc.pim" "IkPoleIksc_00_pnc.cpim";
connectAttr "OrigSystemTr_00_pnc.cty" "OrigSystem_00_tr.ty";
connectAttr "OrigSystemTr_00_pnc.ctz" "OrigSystem_00_tr.tz";
connectAttr "OrigSystemTr_00_pnc.ctx" "OrigSystem_00_tr.tx";
connectAttr "IkPole_00_jnt.s" "IkPoleEnd_00_jnt.is";
connectAttr "IkPoleEnd_00_jnt.tx" "effector2.tx";
connectAttr "IkPoleEnd_00_jnt.ty" "effector2.ty";
connectAttr "IkPoleEnd_00_jnt.tz" "effector2.tz";
connectAttr "IkPoleEnd_00_jnt.opm" "effector2.opm";
connectAttr "AuxJnt_00_orc.crx" "Aux_00_jnt.rx";
connectAttr "AuxJnt_00_orc.cry" "Aux_00_jnt.ry";
connectAttr "AuxJnt_00_orc.crz" "Aux_00_jnt.rz";
connectAttr "AuxJnt_01_orc.crx" "Aux_01_jnt.rx";
connectAttr "AuxJnt_01_orc.cry" "Aux_01_jnt.ry";
connectAttr "AuxJnt_01_orc.crz" "Aux_01_jnt.rz";
connectAttr "Aux_00_jnt.s" "Aux_01_jnt.is";
connectAttr "Aux_01_jnt.s" "AuxEnd_02_jnt.is";
connectAttr "AuxEnd_02_jnt.tx" "effector1.tx";
connectAttr "AuxEnd_02_jnt.ty" "effector1.ty";
connectAttr "AuxEnd_02_jnt.tz" "effector1.tz";
connectAttr "AuxEnd_02_jnt.opm" "effector1.opm";
connectAttr "Fk_01_ctr.wm" "AuxJnt_01_orc.tg[0].tpm";
connectAttr "Config_00_rev.ox" "AuxJnt_01_orc.tg[0].tw";
connectAttr "Aux_01_jnt.pim" "AuxJnt_01_orc.cpim";
connectAttr "Fk_00_ctr.wm" "AuxJnt_00_orc.tg[0].tpm";
connectAttr "Config_00_rev.ox" "AuxJnt_00_orc.tg[0].tw";
connectAttr "Aux_00_jnt.pim" "AuxJnt_00_orc.cpim";
connectAttr "input_00_link.wm" "OrigSystemTr_00_pnc.tg[0].tpm";
connectAttr "OrigSystem_00_tr.pim" "OrigSystemTr_00_pnc.cpim";
connectAttr "Fk_02_ctr.wm" "outputLink_00_orc.tg[0].tpm";
connectAttr "Ik_00_ctr.wm" "outputLink_00_orc.tg[1].tpm";
connectAttr "output_00_link.pim" "outputLink_00_orc.cpim";
connectAttr "AuxEnd_02_jnt.wm" "outputLink_00_pnc.tg[0].tpm";
connectAttr "output_00_link.pim" "outputLink_00_pnc.cpim";
connectAttr "Config_00_rev.ox" "Fk_00_root.v";
connectAttr "FkRoot_00_root_pnc.ctx" "Fk_00_root.tx";
connectAttr "FkRoot_00_root_pnc.cty" "Fk_00_root.ty";
connectAttr "FkRoot_00_root_pnc.ctz" "Fk_00_root.tz";
connectAttr "TwistSnapperRoot_00_aimc.crx" "TwistSnapper_00_root.rx";
connectAttr "TwistSnapperRoot_00_aimc.cry" "TwistSnapper_00_root.ry";
connectAttr "TwistSnapperRoot_00_aimc.crz" "TwistSnapper_00_root.rz";
connectAttr "TwistSnapper_00_snapper_aimc.crx" "Twist_00_snapper.rx";
connectAttr "TwistSnapper_00_snapper_aimc.cry" "Twist_00_snapper.ry";
connectAttr "TwistSnapper_00_snapper_aimc.crz" "Twist_00_snapper.rz";
connectAttr "Twist_00_snapper.pim" "TwistSnapper_00_snapper_aimc.cpim";
connectAttr "Twist_00_snapper.t" "TwistSnapper_00_snapper_aimc.ct";
connectAttr "Twist_00_snapper.rp" "TwistSnapper_00_snapper_aimc.crp";
connectAttr "Twist_00_snapper.rpt" "TwistSnapper_00_snapper_aimc.crt";
connectAttr "Twist_00_snapper.ro" "TwistSnapper_00_snapper_aimc.cro";
connectAttr "Fk_02_ctr.t" "TwistSnapper_00_snapper_aimc.tg[0].tt";
connectAttr "Fk_02_ctr.rp" "TwistSnapper_00_snapper_aimc.tg[0].trp";
connectAttr "Fk_02_ctr.rpt" "TwistSnapper_00_snapper_aimc.tg[0].trt";
connectAttr "Fk_02_ctr.pm" "TwistSnapper_00_snapper_aimc.tg[0].tpm";
connectAttr "TwistSnapper_00_snapper_aimc.w0" "TwistSnapper_00_snapper_aimc.tg[0].tw"
		;
connectAttr "Fk_01_ctr.wm" "TwistSnapper_00_snapper_aimc.wum";
connectAttr "TwistSnapper_00_root.pim" "TwistSnapperRoot_00_aimc.cpim";
connectAttr "TwistSnapper_00_root.t" "TwistSnapperRoot_00_aimc.ct";
connectAttr "TwistSnapper_00_root.rp" "TwistSnapperRoot_00_aimc.crp";
connectAttr "TwistSnapper_00_root.rpt" "TwistSnapperRoot_00_aimc.crt";
connectAttr "TwistSnapper_00_root.ro" "TwistSnapperRoot_00_aimc.cro";
connectAttr "Fk_02_ctr.t" "TwistSnapperRoot_00_aimc.tg[0].tt";
connectAttr "Fk_02_ctr.rp" "TwistSnapperRoot_00_aimc.tg[0].trp";
connectAttr "Fk_02_ctr.rpt" "TwistSnapperRoot_00_aimc.tg[0].trt";
connectAttr "Fk_02_ctr.pm" "TwistSnapperRoot_00_aimc.tg[0].tpm";
connectAttr "TwistSnapperRoot_00_aimc.w0" "TwistSnapperRoot_00_aimc.tg[0].tw";
connectAttr "IkPole_00_ctr.wm" "TwistSnapperRoot_00_aimc.wum";
connectAttr "Fk_00_root.pim" "FkRoot_00_root_pnc.cpim";
connectAttr "Fk_00_root.rp" "FkRoot_00_root_pnc.crp";
connectAttr "Fk_00_root.rpt" "FkRoot_00_root_pnc.crt";
connectAttr "Aux_00_jnt.t" "FkRoot_00_root_pnc.tg[0].tt";
connectAttr "Aux_00_jnt.rp" "FkRoot_00_root_pnc.tg[0].trp";
connectAttr "Aux_00_jnt.rpt" "FkRoot_00_root_pnc.tg[0].trt";
connectAttr "Aux_00_jnt.pm" "FkRoot_00_root_pnc.tg[0].tpm";
connectAttr "FkRoot_00_root_pnc.w0" "FkRoot_00_root_pnc.tg[0].tw";
connectAttr "Config_00_ctr.fkIk" "IkCtr_00_root.v";
connectAttr "Config_00_ctr.fkIk" "Ik_00_Ikh.ikb" -l on;
connectAttr "Aux_00_jnt.msg" "Ik_00_Ikh.hsj";
connectAttr "effector1.hp" "Ik_00_Ikh.hee";
connectAttr "ikRPsolver.msg" "Ik_00_Ikh.hsv";
connectAttr "IkIkh_00_pvc.ctx" "Ik_00_Ikh.pvx" -l on;
connectAttr "IkIkh_00_pvc.cty" "Ik_00_Ikh.pvy" -l on;
connectAttr "IkIkh_00_pvc.ctz" "Ik_00_Ikh.pvz" -l on;
connectAttr "Ik_00_Ikh.pim" "IkIkh_00_pvc.cpim";
connectAttr "Aux_00_jnt.pm" "IkIkh_00_pvc.ps";
connectAttr "Aux_00_jnt.t" "IkIkh_00_pvc.crp";
connectAttr "IkPole_00_ctr.t" "IkIkh_00_pvc.tg[0].tt";
connectAttr "IkPole_00_ctr.rp" "IkIkh_00_pvc.tg[0].trp";
connectAttr "IkPole_00_ctr.rpt" "IkIkh_00_pvc.tg[0].trt";
connectAttr "IkPole_00_ctr.pm" "IkIkh_00_pvc.tg[0].tpm";
connectAttr "IkIkh_00_pvc.w0" "IkIkh_00_pvc.tg[0].tw";
connectAttr "ConfigRoot_00_prc.ct" "Config_00_root.t";
connectAttr "ConfigRoot_00_prc.cr" "Config_00_root.r";
connectAttr "Aux_00_jnt.wm" "ConfigRoot_00_prc.tg[0].tpm";
connectAttr "Config_00_root.pim" "ConfigRoot_00_prc.cpim";
connectAttr "MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "OrigSystem_00_tr.msg" "OrigSystemTpl_00_tr._relatedTo[0]";
connectAttr "Aux_01_jnt.msg" "IkTpl_01_loc._relatedTo[0]";
connectAttr "Ik_00_root.msg" "IkTpl_00_root._relatedTo[0]";
connectAttr "FkTpl_02_ctr.ro" "FkTplCtr_02_orc.cro";
connectAttr "FkTpl_02_ctr.pim" "FkTplCtr_02_orc.cpim";
connectAttr "IkTpl_00_root.r" "FkTplCtr_02_orc.tg[0].tr";
connectAttr "IkTpl_00_root.ro" "FkTplCtr_02_orc.tg[0].tro";
connectAttr "IkTpl_00_root.pm" "FkTplCtr_02_orc.tg[0].tpm";
connectAttr "FkTplCtr_02_orc.w0" "FkTplCtr_02_orc.tg[0].tw";
connectAttr "IkPole_00_ctr.msg" "IkPoleTpl_00_ctr._relatedTo[0]";
connectAttr "IkTpl_00_root.tx" "FKTpl_02_root.tx" -l on;
connectAttr "Fk_02_root.msg" "FKTpl_02_root._relatedTo[0]";
connectAttr "FkTplCtr_02_orc.crx" "FkTpl_02_ctr.rx" -l on;
connectAttr "FkTplCtr_02_orc.cry" "FkTpl_02_ctr.ry" -l on;
connectAttr "FkTplCtr_02_orc.crz" "FkTpl_02_ctr.rz" -l on;
connectAttr "Fk_02_ctr.msg" "FkTpl_02_ctr._relatedTo[0]";
connectAttr "IkTpl_01_loc.tx" "FKTpl_01_root.tx" -l on;
connectAttr "Fk_01_root.msg" "FKTpl_01_root._relatedTo[0]";
connectAttr "FkTpl_01_ctr_orientConstraint1.crx" "FkTpl_01_ctr.rx" -l on;
connectAttr "FkTpl_01_ctr_orientConstraint1.cry" "FkTpl_01_ctr.ry" -l on;
connectAttr "FkTpl_01_ctr_orientConstraint1.crz" "FkTpl_01_ctr.rz" -l on;
connectAttr "Fk_01_ctr.msg" "FkTpl_01_ctr._relatedTo[0]";
connectAttr "FkTpl_01_ctr.ro" "FkTpl_01_ctr_orientConstraint1.cro";
connectAttr "FkTpl_01_ctr.pim" "FkTpl_01_ctr_orientConstraint1.cpim";
connectAttr "IkTpl_01_loc.r" "FkTpl_01_ctr_orientConstraint1.tg[0].tr";
connectAttr "IkTpl_01_loc.ro" "FkTpl_01_ctr_orientConstraint1.tg[0].tro";
connectAttr "IkTpl_01_loc.pm" "FkTpl_01_ctr_orientConstraint1.tg[0].tpm";
connectAttr "FkTpl_01_ctr_orientConstraint1.w0" "FkTpl_01_ctr_orientConstraint1.tg[0].tw"
		;
connectAttr "OrigSystemTpl_00_tr.t" "FKTpl_00_root.t";
connectAttr "Fk_00_root.msg" "FKTpl_00_root._relatedTo[0]";
connectAttr "FkTpl_00_ctr_orientConstraint1.crx" "FkTpl_00_ctr.rx" -l on;
connectAttr "FkTpl_00_ctr_orientConstraint1.cry" "FkTpl_00_ctr.ry" -l on;
connectAttr "FkTpl_00_ctr_orientConstraint1.crz" "FkTpl_00_ctr.rz" -l on;
connectAttr "Fk_00_ctr.msg" "FkTpl_00_ctr._relatedTo[0]";
connectAttr "FkTpl_00_ctr.ro" "FkTpl_00_ctr_orientConstraint1.cro";
connectAttr "FkTpl_00_ctr.pim" "FkTpl_00_ctr_orientConstraint1.cpim";
connectAttr "OrigSystemTpl_00_tr.r" "FkTpl_00_ctr_orientConstraint1.tg[0].tr";
connectAttr "OrigSystemTpl_00_tr.ro" "FkTpl_00_ctr_orientConstraint1.tg[0].tro";
connectAttr "OrigSystemTpl_00_tr.pm" "FkTpl_00_ctr_orientConstraint1.tg[0].tpm";
connectAttr "FkTpl_00_ctr_orientConstraint1.w0" "FkTpl_00_ctr_orientConstraint1.tg[0].tw"
		;
connectAttr "outputLink_00_orc.crx" "output_00_link.rx";
connectAttr "outputLink_00_orc.cry" "output_00_link.ry";
connectAttr "outputLink_00_orc.crz" "output_00_link.rz";
connectAttr "outputLink_00_pnc.cty" "output_00_link.ty";
connectAttr "outputLink_00_pnc.ctz" "output_00_link.tz";
connectAttr "outputLink_00_pnc.ctx" "output_00_link.tx";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Config_00_ctr.fkIk" "Config_00_rev.ix";
connectAttr "Ik.msg" "ControlsSet.dnsm" -na;
connectAttr "Fk.msg" "ControlsSet.dnsm" -na;
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "input_00_link.iog" "LinkSet.dsm" -na;
connectAttr "output_00_link.iog" "LinkSet.dsm" -na;
connectAttr "Config_00_ctr.msg" "Config_00_tag.act";
connectAttr "Config_00_tag.msg" "Config_00_tag.child[0]";
connectAttr "Fk_00_ctr.msg" "Fk_00_tag.act";
connectAttr "Fk_01_tag.pare" "Fk_00_tag.child[0]";
connectAttr "Ik_00_ctr.msg" "Ik_00_tag.act";
connectAttr "Ik_00_tag.msg" "Ik_00_tag.child[0]";
connectAttr "Twist_00_tag.msg" "Twist_00_tag.child[0]";
connectAttr "Pin_01_tag.msg" "Pin_01_tag.child[0]";
connectAttr "Fk_01_ctr.msg" "Fk_01_tag.act";
connectAttr "Fk_02_tag.pare" "Fk_01_tag.child[0]";
connectAttr "Fk_02_ctr.msg" "Fk_02_tag.act";
connectAttr "Fk_02_tag.msg" "Fk_02_tag.child[0]";
connectAttr "Fk_00_ctr.iog" "Fk.dsm" -na;
connectAttr "Fk_01_ctr.iog" "Fk.dsm" -na;
connectAttr "Fk_02_ctr.iog" "Fk.dsm" -na;
connectAttr "Ik_00_ctr.iog" "Ik.dsm" -na;
connectAttr "Fk_00_ctr.msg" "MetadataLimbSnapping.fkControls[0]";
connectAttr "Fk_01_ctr.msg" "MetadataLimbSnapping.fkControls[1]";
connectAttr "Fk_02_ctr.msg" "MetadataLimbSnapping.fkControls[2]";
connectAttr "Fk_00_snapper.msg" "MetadataLimbSnapping.fkSnappers[0]";
connectAttr "Fk_01_snapper.msg" "MetadataLimbSnapping.fkSnappers[1]";
connectAttr "Fk_02_snapper.msg" "MetadataLimbSnapping.fkSnappers[2]";
connectAttr "Twist_00_snapper.msg" "MetadataLimbSnapping.poleVSnapper";
connectAttr "Ik_00_snapper.msg" "MetadataLimbSnapping.ikSnapper";
connectAttr "Ik_00_ctr.msg" "MetadataLimbSnapping.ikControl";
connectAttr "Config_00_ctr.msg" "MetadataLimbSnapping.switchControl";
connectAttr "OrigSystemTpl_00_tr.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "IkTpl_00_root.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "FKTpl_00_root.msg" "MetadataTemplate._inputTemplate[2]";
connectAttr "FkTpl_00_ctr.msg" "MetadataTemplate._inputTemplate[3]";
connectAttr "FKTpl_01_root.msg" "MetadataTemplate._inputTemplate[4]";
connectAttr "FkTpl_01_ctr.msg" "MetadataTemplate._inputTemplate[5]";
connectAttr "FKTpl_02_root.msg" "MetadataTemplate._inputTemplate[6]";
connectAttr "FkTpl_02_ctr.msg" "MetadataTemplate._inputTemplate[7]";
connectAttr "IkPoleTpl_00_ctr.msg" "MetadataTemplate._inputTemplate[8]";
connectAttr "Config_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Config_00_rev.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
connectAttr "ikSCsolver.msg" ":ikSystem.sol" -na;
// End of RP2Bones.ma
