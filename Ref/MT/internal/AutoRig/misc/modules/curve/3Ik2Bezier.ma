//Maya ASCII 2020 scene
//Name: 3Ik2Bezier.ma
//Last modified: Mon, Jul 18, 2022 04:26:08 PM
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
fileInfo "UUID" "5483FB28-408D-8661-36C2-EBA795D338E8";
createNode transform -s -n "persp";
	rename -uid "7B11B765-4C7E-7365-3AE3-799A8279BF76";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 33.681294297600608 34.095527233528642 73.002401298734554 ;
	setAttr ".r" -type "double3" -14.138352729595283 26.200000000000863 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "3C53E235-40E2-C578-4578-63990592D4DD";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 82.577850304492358;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "6560E096-4C35-62ED-88EE-DBB4FF2BB301";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.778707310484257 1000.1 -0.20714055405958964 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "8AAF73E2-4AF1-743C-2A7A-439439FDE5CB";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 50.643678160919571;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "E56C4386-49BA-5E8C-2B64-05B50B2F23F7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.053178924322288879 14.664441275602799 1000.1338245232499 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "22D2C3C5-46B0-2CD4-25AE-3A879902AF57";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1338245232499;
	setAttr ".ow" 69.398496240601503;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0 12.75 0 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "3CDAF6EA-4413-E425-F11A-66A9804560F8";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.326853385962 28.914138030501331 1.0457537385992974 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "83453158-47DB-C7A4-D115-718DA165B79A";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.326853385962;
	setAttr ".ow" 35.465331604687215;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 30 0 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Sys_00_grp";
	rename -uid "1118FCD9-4857-DC5D-9607-D0BA85300C21";
	setAttr ".v" no;
createNode transform -n "Spl_00_crv" -p "Sys_00_grp";
	rename -uid "8F073EDC-4B9B-77B8-F626-3BBBD6D1F18E";
createNode nurbsCurve -n "Spl_00_crvShape" -p "Spl_00_crv";
	rename -uid "31AC1735-41D6-198B-013D-4C8752535772";
	setAttr -k off ".v";
	setAttr -s 4 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 2 0 no 3
		5 0 0 1 2 2
		4
		-3.3306690738754696e-16 0 0
		-3.3306690738754696e-16 5 0
		0 25 0
		-3.3306690738754696e-16 30 0
		;
createNode transform -n "PosAux_00_crv" -p "Sys_00_grp";
	rename -uid "B415659E-4F0F-61F7-6A79-45A49B937288";
createNode nurbsCurve -n "PosAux_00_crvShape" -p "PosAux_00_crv";
	rename -uid "9994998D-4C02-AE6E-AD6A-3F90832096F1";
	setAttr -k off ".v";
	setAttr -s 4 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 2 0 no 3
		5 0 0 1 2 2
		4
		0 0 0
		0 10 0
		0 20 0
		0 30 0
		;
createNode ikHandle -n "PosAux_00_ikrp" -p "Sys_00_grp";
	rename -uid "07906AEB-4990-955D-77B6-01A83DF1BAF2";
	setAttr ".t" -type "double3" 0 30 0 ;
	setAttr ".r" -type "double3" 0 0 90 ;
	setAttr ".roc" yes;
createNode transform -n "OrigPos_00_tr" -p "Sys_00_grp";
	rename -uid "3D2B341B-4A3B-717E-2611-A4B398F2AF0B";
createNode transform -n "PosAux_01_loc" -p "OrigPos_00_tr";
	rename -uid "C2D1C068-4E3D-62E7-105C-739060025E67";
createNode locator -n "PosAux_01_locShape" -p "PosAux_01_loc";
	rename -uid "5E8B1C38-4F0F-1F0A-1B79-9E89D6E34C6C";
	setAttr -k off ".v";
createNode pointConstraint -n "PosAux_01_loc_pointConstraint1" -p "PosAux_01_loc";
	rename -uid "F64CAC28-44AE-5FD2-FE03-C9A24C1D3839";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplPos_00_rootW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "OrigPos_00_trW1" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 15 0 ;
	setAttr -k on ".w0" 0.33333;
	setAttr -k on ".w1" 0.66666;
createNode transform -n "PosAux_02_loc" -p "OrigPos_00_tr";
	rename -uid "3E2D933D-4AE6-B337-5786-DD895C47380B";
createNode locator -n "PosAux_02_locShape" -p "PosAux_02_loc";
	rename -uid "803558DA-434A-70BA-F085-D487FC219426";
	setAttr -k off ".v";
createNode pointConstraint -n "PosAux_02_loc_pointConstraint1" -p "PosAux_02_loc";
	rename -uid "EA747497-4909-A6FB-79BF-0F8D2A71F570";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplPos_00_rootW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "OrigPos_00_trW1" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 15 0 ;
	setAttr -k on ".w0" 0.66666;
	setAttr -k on ".w1" 0.33333;
createNode joint -n "PosAux_00_jnt" -p "OrigPos_00_tr";
	rename -uid "C4D3E972-4367-6C57-7373-DC884F0D51D3";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 90 ;
	setAttr ".radi" 0.5;
createNode joint -n "PosAux_01_jnt" -p "PosAux_00_jnt";
	rename -uid "F942BDB3-4DBD-0215-7C7C-ADA199017D08";
	setAttr ".t" -type "double3" 10 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "PosAux_02_jnt" -p "PosAux_01_jnt";
	rename -uid "5A2207A3-4BC9-F264-0106-3F9DE6CE2CFD";
	setAttr ".t" -type "double3" 10 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode joint -n "PosAux_03_jnt" -p "PosAux_02_jnt";
	rename -uid "69FB6090-4F57-A5B5-64E3-89A170A53613";
	setAttr ".t" -type "double3" 10 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.5;
createNode ikEffector -n "effector1" -p "PosAux_02_jnt";
	rename -uid "2D835A87-4A29-7326-335A-CB9FD8B5670A";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode pointConstraint -n "OrigPos_00_tr_pointConstraint1" -p "OrigPos_00_tr";
	rename -uid "36DF8650-409B-10BD-34A7-2EAAD1BDE314";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "group1W0" -dv 1 -min 0 -at "double";
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
createNode transform -n "SplControls_00_grp";
	rename -uid "FEACD865-4E0B-FE75-7F01-D3A90E309DEB";
createNode transform -n "SplPos_01_root" -p "SplControls_00_grp";
	rename -uid "D4D07BE3-4A90-805A-98F3-3F98D99FD420";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplPos_01_ctr" -p "SplPos_01_root";
	rename -uid "269852F9-40C0-9CE1-94CA-61804A716AD4";
	addAttr -ci true -sn "spaceSwith" -ln "spaceSwith" -min 0 -max 1 -en "world:cog" 
		-at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".spaceSwith" 1;
createNode transform -n "PosAux_03_loc" -p "SplPos_01_ctr";
	rename -uid "934AED8B-400C-B28E-4C2A-D99F9C10CF40";
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
createNode locator -n "PosAux_03_locShape" -p "PosAux_03_loc";
	rename -uid "6EBC2D4B-4645-DE34-1D91-F4B1AF11EC5D";
	setAttr -k off ".v";
createNode nurbsCurve -n "SplPos_01_ctrShape" -p "SplPos_01_ctr";
	rename -uid "19D4EC9C-468E-0DFD-2B1A-9EA97B013E4A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-6 0.5 -3
		-6 0.5 3
		-6 -0.5 3
		6 -0.5 3
		6 0.5 3
		6 0.5 -3
		6 -0.5 -3
		-6 -0.5 -3
		-6 0.5 -3
		6 0.5 -3
		6 0.5 3
		-6 0.5 3
		-6 -0.5 3
		6 -0.5 3
		6 -0.5 -3
		-6 -0.5 -3
		-6 -0.5 3
		;
createNode parentConstraint -n "SplPos_01_root_parentConstraint1" -p "SplPos_01_root";
	rename -uid "5414A3E8-459E-A399-F5A7-D184752B3A34";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplPosWorld_00_spcW0" -dv 1 -min 
		0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplPosCOG_00_spcW1" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 30 0 ;
	setAttr ".int" 0;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "Spl_02_root" -p "SplControls_00_grp";
	rename -uid "4C102962-4151-76C7-B79B-FCBAD111E60E";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode parentConstraint -n "Spl_02_root_parentConstraint1" -p "Spl_02_root";
	rename -uid "D6A85691-4AAC-98C2-976F-C5B475C23A56";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "PosAux_03_jntW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 0 90 ;
	setAttr ".rst" -type "double3" 0 12 0 ;
	setAttr ".rsrr" -type "double3" 0 0 90 ;
	setAttr -k on ".w0";
createNode transform -n "Spl_02_aux" -p "Spl_02_root";
	rename -uid "63EBD3E1-4570-C346-7D4A-79B28312CE06";
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "Spl_02_ctr" -p "Spl_02_aux";
	rename -uid "E9B7F243-456E-3016-DE59-E9A20A0905E5";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Spl_03_loc" -p "Spl_02_ctr";
	rename -uid "5E3498D4-493F-1D6B-6B87-33B435E22F45";
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
createNode locator -n "Spl_03_locShape" -p "Spl_03_loc";
	rename -uid "16391BC0-4B3D-BADA-3442-C8BA4554E53D";
	setAttr -k off ".v";
createNode transform -n "SplBezier_01_root" -p "Spl_02_ctr";
	rename -uid "AFB953F0-42C8-09E6-41CE-37AA78EBCB44";
	setAttr ".t" -type "double3" 3.3306690738754696e-16 -5 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplBezier_01_off" -p "SplBezier_01_root";
	rename -uid "49583DE7-4548-FA28-3465-398F99E7C292";
createNode transform -n "SplBezier_01_ctr" -p "SplBezier_01_off";
	rename -uid "7560E40B-4314-94D9-259E-9F9E5B2F5A92";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Spl_02_loc" -p "SplBezier_01_ctr";
	rename -uid "BB1466E3-4CAB-DD09-C38F-8C84B101FE83";
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
	rename -uid "F67B3270-407B-49E9-E4E0-80B428CD034F";
	setAttr -k off ".v";
createNode nurbsCurve -n "SplBezier_01_ctrShape" -p "SplBezier_01_ctr";
	rename -uid "7D53C7F6-431F-1D47-C6F8-60991FBB3B78";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		0 2.5 0
		0 1.767766922712326 1.7677667737007141
		0 0 2.4999998509883881
		0 -1.767766922712326 1.7677667737007141
		0 -2.5 0
		0 -1.767766922712326 -1.7677667737007141
		0 0 -2.4999997019767761
		0 1.767766922712326 -1.7677667737007141
		0 2.5 0
		-1.7677667737007141 1.767766922712326 0
		-2.4999997019767761 0 0
		-1.7677667737007141 -1.767766922712326 0
		0 -2.5 0
		1.767766922712326 -1.767766922712326 0
		2.5 0 0
		1.767766922712326 0 1.767766922712326
		0 0 2.4999998509883881
		-1.7677667737007141 0 1.7677667737007141
		-2.4999997019767761 0 0
		-1.7677667737007141 0 -1.7677667737007141
		0 0 -2.4999997019767761
		1.7677667737007141 0 -1.7677667737007141
		2.5 0 0
		1.767766922712326 1.767766922712326 0
		0 2.5 0
		;
createNode nurbsCurve -n "Spl_02_ctrShape" -p "Spl_02_ctr";
	rename -uid "5B4E3F47-46EC-B216-1218-D68AB369EDCE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 20 0 no 3
		25 0 0 0 1 2 3 4 5 6 7 8 9 10 10.494106049999999 11 12 13 14 15 16 17 18 19
		 19 19
		23
		-1.4999999999999998 0 4.7623100280761719
		-2.6028518013817576 0 4.437503921729026
		-4.6218223791474289 0.74223843123286493 2.8866529405375956
		-5.366043346951435 1.6781042793090855 -0.76404728023843649
		-3.601310539963166 0.77450966737342597 -4.0903813053187781
		-1.2431743008821102e-15 0 -5.4578166651989735
		3.6013105399631677 0.77450966737342597 -4.0903813053187807
		5.3714453646248295 1.6781042793090855 -0.71895190675891651
		4.6034130444704218 0.74223843123286493 2.6209458253739757
		2.6989046328726292 0 4.351834883243014
		1.5000000000000002 0 4.7623100000000003
		1.5 0 4.7623100000000003
		1.5 0 4.7623100000000003
		2.6155099868774414 0 4.7623100280761719
		2.6155099868774414 0 4.7623100280761719
		2.6155099868774414 0 4.7623100280761719
		0 0 7
		0 0 7
		0 0 7
		-2.6155104637145996 0 4.7623100280761719
		-2.6155104637145996 0 4.7623100280761719
		-2.6155104637145996 0 4.7623100280761719
		-1.5 0 4.7623100280761719
		;
createNode transform -n "Spl_00_root" -p "SplControls_00_grp";
	rename -uid "D07EE359-4F9E-BF70-08E0-3FBED3C62EAB";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode parentConstraint -n "Spl_00_root_parentConstraint1" -p "Spl_00_root";
	rename -uid "CDC41712-4F96-4761-C9A0-F1BC04DD54DB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "PosAux_00_jntW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 0 90 ;
	setAttr ".rst" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".rsrr" -type "double3" 0 0 90 ;
	setAttr -k on ".w0";
createNode transform -n "Spl_00_aux" -p "Spl_00_root";
	rename -uid "992D8D86-4424-F6CE-8572-B79C06B7CE53";
	setAttr ".r" -type "double3" 0 0 -90 ;
createNode transform -n "Spl_00_ctr" -p "Spl_00_aux";
	rename -uid "D135D73D-4E92-111C-3915-9BB9A2E30B43";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Spl_00_loc" -p "Spl_00_ctr";
	rename -uid "3057AB24-4091-F0F9-6267-2B9400D41645";
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
createNode locator -n "Spl_00_locShape" -p "Spl_00_loc";
	rename -uid "591F9962-401E-3813-C022-998E70D0844D";
	setAttr -k off ".v";
createNode transform -n "SplBezier_00_root" -p "Spl_00_ctr";
	rename -uid "AE76D390-42F7-1F16-FD6C-31A92853AB13";
	setAttr ".t" -type "double3" 0 5 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplBezier_00_off" -p "SplBezier_00_root";
	rename -uid "2190BC1D-409F-FA34-C56A-B3970BB8BDC4";
createNode transform -n "SplBezier_00_ctr" -p "SplBezier_00_off";
	rename -uid "B2477D17-4F54-2F0B-8510-0C85C8526F6A";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Spl_01_loc" -p "SplBezier_00_ctr";
	rename -uid "14D29B0B-4E62-2973-E109-C0A2DBC75B80";
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
createNode locator -n "Spl_01_locShape" -p "Spl_01_loc";
	rename -uid "2C7D9916-4925-2420-4A67-928CFAF769D5";
	setAttr -k off ".v";
createNode nurbsCurve -n "SplBezier_00_ctrShape" -p "SplBezier_00_ctr";
	rename -uid "FDE07D0E-4CC7-36DE-C0B6-FFB67EA89622";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		0 2.5 0
		0 1.767766922712326 1.7677667737007141
		0 0 2.4999998509883881
		0 -1.767766922712326 1.7677667737007141
		0 -2.5 0
		0 -1.767766922712326 -1.7677667737007141
		0 0 -2.4999997019767761
		0 1.767766922712326 -1.7677667737007141
		0 2.5 0
		-1.7677667737007141 1.767766922712326 0
		-2.4999997019767761 0 0
		-1.7677667737007141 -1.767766922712326 0
		0 -2.5 0
		1.767766922712326 -1.767766922712326 0
		2.5 0 0
		1.767766922712326 0 1.767766922712326
		0 0 2.4999998509883881
		-1.7677667737007141 0 1.7677667737007141
		-2.4999997019767761 0 0
		-1.7677667737007141 0 -1.7677667737007141
		0 0 -2.4999997019767761
		1.7677667737007141 0 -1.7677667737007141
		2.5 0 0
		1.767766922712326 1.767766922712326 0
		0 2.5 0
		;
createNode nurbsCurve -n "Spl_00_ctrShape" -p "Spl_00_ctr";
	rename -uid "4061AE83-4163-DA33-EDD2-E4BBDA0F81C3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 20 0 no 3
		25 0 0 0 1 2 3 4 5 6 7 8 9 10 10.494106049999999 11 12 13 14 15 16 17 18 19
		 19 19
		23
		-1.4999999999999998 0 4.7623100280761719
		-2.6028518013817576 0 4.437503921729026
		-4.6218223791474289 0.74223843123286493 2.8866529405375956
		-5.366043346951435 1.6781042793090855 -0.76404728023843649
		-3.601310539963166 0.77450966737342597 -4.0903813053187781
		-1.2431743008821102e-15 0 -5.4578166651989735
		3.6013105399631677 0.77450966737342597 -4.0903813053187807
		5.3714453646248295 1.6781042793090855 -0.71895190675891651
		4.6034130444704218 0.74223843123286493 2.6209458253739757
		2.6989046328726292 0 4.351834883243014
		1.5000000000000002 0 4.7623100000000003
		1.5 0 4.7623100000000003
		1.5 0 4.7623100000000003
		2.6155099868774414 0 4.7623100280761719
		2.6155099868774414 0 4.7623100280761719
		2.6155099868774414 0 4.7623100280761719
		0 0 7
		0 0 7
		0 0 7
		-2.6155104637145996 0 4.7623100280761719
		-2.6155104637145996 0 4.7623100280761719
		-2.6155104637145996 0 4.7623100280761719
		-1.5 0 4.7623100280761719
		;
createNode transform -n "Spl_01_root" -p "SplControls_00_grp";
	rename -uid "4E6C94D4-4CCA-34F2-5DB6-14B4A5D4B118";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Spl_01_ctr" -p "Spl_01_root";
	rename -uid "D043CC7D-4D42-E7E3-2248-B584082B1D17";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -4.4408920985006262e-16 0 ;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Spl_01_ctrShape" -p "Spl_01_ctr";
	rename -uid "A9C8655E-4C0C-FF94-9660-4C92EB12A8D0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		0 3.75 0
		0 2.6516503840684891 2.6516501605510712
		0 0 3.7499997764825821
		0 -2.6516503840684891 2.6516501605510712
		0 -3.75 0
		0 -2.6516503840684891 -2.6516501605510712
		0 0 -3.7499995529651642
		0 2.6516503840684891 -2.6516501605510712
		0 3.75 0
		-2.6516501605510712 2.6516503840684891 0
		-3.7499995529651642 0 0
		-2.6516501605510712 -2.6516503840684891 0
		0 -3.75 0
		2.6516503840684891 -2.6516503840684891 0
		3.75 0 0
		2.6516503840684891 0 2.6516503840684891
		0 0 3.7499997764825821
		-2.6516501605510712 0 2.6516501605510712
		-3.7499995529651642 0 0
		-2.6516501605510712 0 -2.6516501605510712
		0 0 -3.7499995529651642
		2.6516501605510712 0 -2.6516501605510712
		3.75 0 0
		2.6516503840684891 2.6516503840684891 0
		0 3.75 0
		;
createNode pointConstraint -n "Spl_01_root_pointConstraint1" -p "Spl_01_root";
	rename -uid "1D8E51AD-4615-E3F0-C211-47BD5409897C";
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
createNode orientConstraint -n "Spl_01_root_orientConstraint1" -p "Spl_01_root";
	rename -uid "E1440AD6-468F-2C6D-0917-9A9E58B9F8F7";
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
createNode transform -n "Tpl_00_tpl";
	rename -uid "1FD89C7F-45C7-ED5D-AE8F-93B5AA2D6736";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "OrigPosTpl_00_tr" -p "Tpl_00_tpl";
	rename -uid "6A596BB9-4C6A-D684-A85D-AAAD97ECEE8C";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "OrigPosTpl_00_trShape" -p "OrigPosTpl_00_tr";
	rename -uid "BD80CB2A-4BCA-972F-7ED4-6FBA3A6D630D";
	setAttr -k off ".v";
createNode transform -n "SplBezierTpl_00_root" -p "OrigPosTpl_00_tr";
	rename -uid "F69F2167-46FB-3D4B-B72D-52B2283701AE";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 5 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplBezierTpl_00_rootShape" -p "SplBezierTpl_00_root";
	rename -uid "60BC18E6-4571-1E6E-252B-24A2D9AB4DE5";
	setAttr -k off ".v";
createNode transform -n "PosAuxTpl_01_jnt" -p "OrigPosTpl_00_tr";
	rename -uid "8B7DB18F-439C-67DE-FA99-10A10E56FF42";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
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
	setAttr -s 4 "._relatedTo";
createNode locator -n "PosAuxTpl_01_jntShape" -p "PosAuxTpl_01_jnt";
	rename -uid "89B744CB-4F12-D33C-A7EF-D89398E75487";
	setAttr -k off ".v";
createNode transform -n "SplPosTpl_00_root" -p "OrigPosTpl_00_tr";
	rename -uid "402D2A67-46D7-7ADE-4314-0284CB278D82";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 30 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -s 2 "._relatedTo";
createNode locator -n "SplPosTpl_00_rootShape" -p "SplPosTpl_00_root";
	rename -uid "AECD071A-4D4C-4183-2971-0DBF52DBCC72";
	setAttr -k off ".v";
createNode transform -n "SplTplTop_03_off" -p "SplPosTpl_00_root";
	rename -uid "00886AC8-4074-252D-76E3-7EA593487F18";
	setAttr -l on ".v";
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode aimConstraint -n "SplTplTop_03_off_aimConstraint1" -p "SplTplTop_03_off";
	rename -uid "7E29B431-44EA-9B49-47E3-CA81543B0B28";
	addAttr -dcb 0 -ci true -sn "w0" -ln "OrigPosTpl_00_trW0" -dv 1 -at "double";
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
	setAttr ".a" -type "double3" 0 -1 0 ;
	setAttr ".u" -type "double3" 0 0 1 ;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".wut" 2;
	setAttr -k on ".w0";
createNode transform -n "SplTpl_03_loc" -p "SplTplTop_03_off";
	rename -uid "9B7C614C-40BC-DB25-BD63-25BD30C4B9C1";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplTpl_03_locShape" -p "SplTpl_03_loc";
	rename -uid "FA1C8CC1-49F1-E36C-6B08-5392CC126D95";
	setAttr -k off ".v";
createNode transform -n "SplBezierTpl_01_root" -p "SplTplTop_03_off";
	rename -uid "ECCAAD57-4EFF-6AB9-1E35-58BB8BD520C8";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 -5 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "SplBezierTpl_01_rootShape" -p "SplBezierTpl_01_root";
	rename -uid "02340980-44A2-3ECA-1280-6E9180058F96";
	setAttr -k off ".v";
createNode transform -n "referenceTpl_00_crv" -p "OrigPosTpl_00_tr";
	rename -uid "5191C06B-4B70-30CD-15BA-1DA3A1E21DFA";
	setAttr ".tmp" yes;
	setAttr ".it" no;
createNode nurbsCurve -n "referenceTpl_00_crvShape" -p "referenceTpl_00_crv";
	rename -uid "798A8B84-47AE-68BB-BF4B-2D94F32FDACB";
	setAttr -k off ".v";
	setAttr -s 4 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 2 0 no 3
		5 0 0 1 2 2
		4
		0 0 0
		0 5 0
		0 25 0
		0 30 0
		;
createNode transform -n "SplPosWorld_00_spc";
	rename -uid "FACB2097-4CAC-70B7-ED92-86B398B69856";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 30 0 ;
createNode transform -n "SplPosCog_00_spc";
	rename -uid "975C5554-42B5-5523-3775-40861308FF4C";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 30 0 ;
createNode transform -n "input_00_link";
	rename -uid "4F2E7FB0-4725-7FB1-B1FD-AEA07AB7A2CC";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "SplPos_00_root" -p "input_00_link";
	rename -uid "D8897447-4900-5557-463C-BAAF8ABBF28D";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplPos_00_ctr" -p "SplPos_00_root";
	rename -uid "EC464EFC-4A4D-3129-CF42-91A48C8BB6B8";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "SplPos_00_ctrShape" -p "SplPos_00_ctr";
	rename -uid "1EE86EAE-4CB6-5694-DD95-A8A4BA03EC80";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-6 0.5 -3
		-6 0.5 3
		-6 -0.5 3
		6 -0.5 3
		6 0.5 3
		6 0.5 -3
		6 -0.5 -3
		-6 -0.5 -3
		-6 0.5 -3
		6 0.5 -3
		6 0.5 3
		-6 0.5 3
		-6 -0.5 3
		6 -0.5 3
		6 -0.5 -3
		-6 -0.5 -3
		-6 -0.5 3
		;
createNode transform -n "PosAux_00_loc" -p "SplPos_00_ctr";
	rename -uid "DD7AC9AE-4EE5-A732-343D-D28FD313F53D";
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
createNode locator -n "PosAux_00_locShape" -p "PosAux_00_loc";
	rename -uid "2348C421-430F-8BC3-A960-FE9EE8FEE147";
	setAttr -k off ".v";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "ED3A97F7-4C22-7A31-B8B0-4F8F036BD918";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "81CD24B9-4DA8-3F0D-D41E-0A9210569711";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "06B87998-4F5B-09ED-C742-3097C989C37E";
createNode displayLayerManager -n "layerManager";
	rename -uid "34815E8F-46FD-15CC-2DA6-E3AA9FCEFDD8";
createNode displayLayer -n "defaultLayer";
	rename -uid "258D412C-4C95-B5D8-73F4-4297AF17D388";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "2B3239AD-489E-7ECC-C04F-80BA66DE0B6D";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "479262BC-4DBE-46A9-D76A-AEA536A960D7";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "23D18254-423C-9F20-2ABA-E0BEB75FB545";
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
	rename -uid "03C2204D-4683-8BD6-80DA-F7BE9002AB5A";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ikSplineSolver -n "ikSplineSolver";
	rename -uid "432A59BD-4814-B7CF-BCEB-CF960AF7E6BC";
createNode objectSet -n "ControlsSet";
	rename -uid "1DE316CC-49F4-79F3-B6EB-ED8AC0F72192";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "DBE47DED-42BC-2D03-BD1A-4BA7D052DD76";
	setAttr ".ihi" 0;
createNode controller -n "SplBezier_00_tag";
	rename -uid "DEC9D33D-466C-E075-5508-E9B299FD5B76";
createNode controller -n "Spl_00_tag";
	rename -uid "DB55A30D-4199-51B0-948C-1CB12776D210";
createNode controller -n "SplBezier_01_tag";
	rename -uid "417D5711-425A-D6E3-C172-2D956681A3BA";
createNode controller -n "Spl_02_tag";
	rename -uid "DEF9C21F-4C7C-E4E1-382B-C990EE371394";
createNode controller -n "Spl_01_tag";
	rename -uid "996B9AE3-4FE0-BF91-E4E8-71AF4A8C0FAD";
createNode controller -n "SplPos_00_tag";
	rename -uid "580B28E3-4615-FEAC-551A-D1B1056797B3";
	setAttr -s 3 ".child";
createNode script -n "MetadataTemplate";
	rename -uid "0B8FBAA3-4230-1E9C-8B2D-208D27AD3135";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" (
		"import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#OrigPos_00_tr\n#SplPos_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#SplPos_00_spaces\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Spl_03_loc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[2]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.setAttr(this + \".localPosition\", *cmds.getAttr(template + \".t\")[0])\ndel template, this\n#SplBezier_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[3]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\n"
		+ "del template, this\n#PosAux_*_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[4]\")[0]\ncrv = cmds.listConnections(template + \"._relatedTo[0]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\")[1:]:\n    cmds.setAttr( this + \".tx\", cmds.arclen( crv ) /3.0 )\ndel template, this, crv\n#SplBezier_01_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[5]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this");
	setAttr -l on ".stp" 1;
	setAttr -s 6 "._inputTemplate";
createNode choice -n "SpaceWorld_00_chc";
	rename -uid "5DCAE1D3-4E8A-4F3F-7723-C18EE7056907";
	setAttr -s 2 ".i";
	setAttr ".i[0]" 1;
	setAttr ".i[1]" 0;
createNode choice -n "SpaceCOG_00_chc";
	rename -uid "7FFFC70D-4B84-6DE4-C5DD-82A01589FB8F";
	setAttr -s 2 ".i";
	setAttr ".i[0]" 0;
	setAttr ".i[1]" 1;
createNode controller -n "SplPos_01_tag";
	rename -uid "1E954DEC-4455-9DBF-A6F6-EB849418DF00";
	setAttr -s 3 ".child";
createNode objectSet -n "LinkSet";
	rename -uid "07C24CA5-4580-A7F1-2CA6-9B9CEFD92911";
	setAttr ".ihi" 0;
createNode objectSet -n "Secondaries";
	rename -uid "9C7E761B-4A5A-58C2-7078-05A11749202D";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
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
connectAttr "Spl_00_locShape.wp" "Spl_00_crvShape.cp[0]";
connectAttr "Spl_01_locShape.wp" "Spl_00_crvShape.cp[1]";
connectAttr "Spl_02_locShape.wp" "Spl_00_crvShape.cp[2]";
connectAttr "Spl_03_locShape.wp" "Spl_00_crvShape.cp[3]";
connectAttr "PosAux_00_locShape.wp" "PosAux_00_crvShape.cp[0]";
connectAttr "PosAux_01_locShape.wp" "PosAux_00_crvShape.cp[1]";
connectAttr "PosAux_02_locShape.wp" "PosAux_00_crvShape.cp[2]";
connectAttr "PosAux_03_locShape.wp" "PosAux_00_crvShape.cp[3]";
connectAttr "PosAux_00_jnt.msg" "PosAux_00_ikrp.hsj";
connectAttr "effector1.hp" "PosAux_00_ikrp.hee";
connectAttr "ikSplineSolver.msg" "PosAux_00_ikrp.hsv";
connectAttr "PosAux_00_crvShape.ws" "PosAux_00_ikrp.ic";
connectAttr "OrigPos_00_tr_pointConstraint1.ctx" "OrigPos_00_tr.tx";
connectAttr "OrigPos_00_tr_pointConstraint1.cty" "OrigPos_00_tr.ty";
connectAttr "OrigPos_00_tr_pointConstraint1.ctz" "OrigPos_00_tr.tz";
connectAttr "PosAux_01_loc_pointConstraint1.ctx" "PosAux_01_loc.tx";
connectAttr "PosAux_01_loc_pointConstraint1.cty" "PosAux_01_loc.ty";
connectAttr "PosAux_01_loc_pointConstraint1.ctz" "PosAux_01_loc.tz";
connectAttr "PosAux_01_loc.pim" "PosAux_01_loc_pointConstraint1.cpim";
connectAttr "PosAux_01_loc.rp" "PosAux_01_loc_pointConstraint1.crp";
connectAttr "PosAux_01_loc.rpt" "PosAux_01_loc_pointConstraint1.crt";
connectAttr "SplPos_01_root.t" "PosAux_01_loc_pointConstraint1.tg[0].tt";
connectAttr "SplPos_01_root.rp" "PosAux_01_loc_pointConstraint1.tg[0].trp";
connectAttr "SplPos_01_root.rpt" "PosAux_01_loc_pointConstraint1.tg[0].trt";
connectAttr "SplPos_01_root.pm" "PosAux_01_loc_pointConstraint1.tg[0].tpm";
connectAttr "PosAux_01_loc_pointConstraint1.w0" "PosAux_01_loc_pointConstraint1.tg[0].tw"
		;
connectAttr "OrigPos_00_tr.t" "PosAux_01_loc_pointConstraint1.tg[1].tt";
connectAttr "OrigPos_00_tr.rp" "PosAux_01_loc_pointConstraint1.tg[1].trp";
connectAttr "OrigPos_00_tr.rpt" "PosAux_01_loc_pointConstraint1.tg[1].trt";
connectAttr "OrigPos_00_tr.pm" "PosAux_01_loc_pointConstraint1.tg[1].tpm";
connectAttr "PosAux_01_loc_pointConstraint1.w1" "PosAux_01_loc_pointConstraint1.tg[1].tw"
		;
connectAttr "PosAux_02_loc_pointConstraint1.ctx" "PosAux_02_loc.tx";
connectAttr "PosAux_02_loc_pointConstraint1.cty" "PosAux_02_loc.ty";
connectAttr "PosAux_02_loc_pointConstraint1.ctz" "PosAux_02_loc.tz";
connectAttr "PosAux_02_loc.pim" "PosAux_02_loc_pointConstraint1.cpim";
connectAttr "PosAux_02_loc.rp" "PosAux_02_loc_pointConstraint1.crp";
connectAttr "PosAux_02_loc.rpt" "PosAux_02_loc_pointConstraint1.crt";
connectAttr "SplPos_01_root.t" "PosAux_02_loc_pointConstraint1.tg[0].tt";
connectAttr "SplPos_01_root.rp" "PosAux_02_loc_pointConstraint1.tg[0].trp";
connectAttr "SplPos_01_root.rpt" "PosAux_02_loc_pointConstraint1.tg[0].trt";
connectAttr "SplPos_01_root.pm" "PosAux_02_loc_pointConstraint1.tg[0].tpm";
connectAttr "PosAux_02_loc_pointConstraint1.w0" "PosAux_02_loc_pointConstraint1.tg[0].tw"
		;
connectAttr "OrigPos_00_tr.t" "PosAux_02_loc_pointConstraint1.tg[1].tt";
connectAttr "OrigPos_00_tr.rp" "PosAux_02_loc_pointConstraint1.tg[1].trp";
connectAttr "OrigPos_00_tr.rpt" "PosAux_02_loc_pointConstraint1.tg[1].trt";
connectAttr "OrigPos_00_tr.pm" "PosAux_02_loc_pointConstraint1.tg[1].tpm";
connectAttr "PosAux_02_loc_pointConstraint1.w1" "PosAux_02_loc_pointConstraint1.tg[1].tw"
		;
connectAttr "PosAux_00_jnt.s" "PosAux_01_jnt.is";
connectAttr "PosAux_01_jnt.s" "PosAux_02_jnt.is";
connectAttr "PosAux_02_jnt.s" "PosAux_03_jnt.is";
connectAttr "PosAux_03_jnt.tx" "effector1.tx";
connectAttr "PosAux_03_jnt.ty" "effector1.ty";
connectAttr "PosAux_03_jnt.tz" "effector1.tz";
connectAttr "PosAux_03_jnt.opm" "effector1.opm";
connectAttr "OrigPos_00_tr.pim" "OrigPos_00_tr_pointConstraint1.cpim";
connectAttr "OrigPos_00_tr.rp" "OrigPos_00_tr_pointConstraint1.crp";
connectAttr "OrigPos_00_tr.rpt" "OrigPos_00_tr_pointConstraint1.crt";
connectAttr "input_00_link.t" "OrigPos_00_tr_pointConstraint1.tg[0].tt";
connectAttr "input_00_link.rp" "OrigPos_00_tr_pointConstraint1.tg[0].trp";
connectAttr "input_00_link.rpt" "OrigPos_00_tr_pointConstraint1.tg[0].trt";
connectAttr "input_00_link.pm" "OrigPos_00_tr_pointConstraint1.tg[0].tpm";
connectAttr "OrigPos_00_tr_pointConstraint1.w0" "OrigPos_00_tr_pointConstraint1.tg[0].tw"
		;
connectAttr "SplPos_01_root_parentConstraint1.ctx" "SplPos_01_root.tx";
connectAttr "SplPos_01_root_parentConstraint1.cty" "SplPos_01_root.ty";
connectAttr "SplPos_01_root_parentConstraint1.ctz" "SplPos_01_root.tz";
connectAttr "SplPos_01_root_parentConstraint1.crx" "SplPos_01_root.rx";
connectAttr "SplPos_01_root_parentConstraint1.cry" "SplPos_01_root.ry";
connectAttr "SplPos_01_root_parentConstraint1.crz" "SplPos_01_root.rz";
connectAttr "SplPos_01_root.ro" "SplPos_01_root_parentConstraint1.cro";
connectAttr "SplPos_01_root.pim" "SplPos_01_root_parentConstraint1.cpim";
connectAttr "SplPos_01_root.rp" "SplPos_01_root_parentConstraint1.crp";
connectAttr "SplPos_01_root.rpt" "SplPos_01_root_parentConstraint1.crt";
connectAttr "SplPosWorld_00_spc.t" "SplPos_01_root_parentConstraint1.tg[0].tt";
connectAttr "SplPosWorld_00_spc.rp" "SplPos_01_root_parentConstraint1.tg[0].trp"
		;
connectAttr "SplPosWorld_00_spc.rpt" "SplPos_01_root_parentConstraint1.tg[0].trt"
		;
connectAttr "SplPosWorld_00_spc.r" "SplPos_01_root_parentConstraint1.tg[0].tr";
connectAttr "SplPosWorld_00_spc.ro" "SplPos_01_root_parentConstraint1.tg[0].tro"
		;
connectAttr "SplPosWorld_00_spc.s" "SplPos_01_root_parentConstraint1.tg[0].ts";
connectAttr "SplPosWorld_00_spc.pm" "SplPos_01_root_parentConstraint1.tg[0].tpm"
		;
connectAttr "SplPos_01_root_parentConstraint1.w0" "SplPos_01_root_parentConstraint1.tg[0].tw"
		;
connectAttr "SplPosCog_00_spc.t" "SplPos_01_root_parentConstraint1.tg[1].tt";
connectAttr "SplPosCog_00_spc.rp" "SplPos_01_root_parentConstraint1.tg[1].trp";
connectAttr "SplPosCog_00_spc.rpt" "SplPos_01_root_parentConstraint1.tg[1].trt";
connectAttr "SplPosCog_00_spc.r" "SplPos_01_root_parentConstraint1.tg[1].tr";
connectAttr "SplPosCog_00_spc.ro" "SplPos_01_root_parentConstraint1.tg[1].tro";
connectAttr "SplPosCog_00_spc.s" "SplPos_01_root_parentConstraint1.tg[1].ts";
connectAttr "SplPosCog_00_spc.pm" "SplPos_01_root_parentConstraint1.tg[1].tpm";
connectAttr "SplPos_01_root_parentConstraint1.w1" "SplPos_01_root_parentConstraint1.tg[1].tw"
		;
connectAttr "SpaceWorld_00_chc.o" "SplPos_01_root_parentConstraint1.w0";
connectAttr "SpaceCOG_00_chc.o" "SplPos_01_root_parentConstraint1.w1";
connectAttr "Spl_02_root_parentConstraint1.ctx" "Spl_02_root.tx";
connectAttr "Spl_02_root_parentConstraint1.cty" "Spl_02_root.ty";
connectAttr "Spl_02_root_parentConstraint1.ctz" "Spl_02_root.tz";
connectAttr "Spl_02_root_parentConstraint1.crx" "Spl_02_root.rx";
connectAttr "Spl_02_root_parentConstraint1.cry" "Spl_02_root.ry";
connectAttr "Spl_02_root_parentConstraint1.crz" "Spl_02_root.rz";
connectAttr "Spl_02_root.ro" "Spl_02_root_parentConstraint1.cro";
connectAttr "Spl_02_root.pim" "Spl_02_root_parentConstraint1.cpim";
connectAttr "Spl_02_root.rp" "Spl_02_root_parentConstraint1.crp";
connectAttr "Spl_02_root.rpt" "Spl_02_root_parentConstraint1.crt";
connectAttr "PosAux_03_jnt.t" "Spl_02_root_parentConstraint1.tg[0].tt";
connectAttr "PosAux_03_jnt.rp" "Spl_02_root_parentConstraint1.tg[0].trp";
connectAttr "PosAux_03_jnt.rpt" "Spl_02_root_parentConstraint1.tg[0].trt";
connectAttr "PosAux_03_jnt.r" "Spl_02_root_parentConstraint1.tg[0].tr";
connectAttr "PosAux_03_jnt.ro" "Spl_02_root_parentConstraint1.tg[0].tro";
connectAttr "PosAux_03_jnt.s" "Spl_02_root_parentConstraint1.tg[0].ts";
connectAttr "PosAux_03_jnt.pm" "Spl_02_root_parentConstraint1.tg[0].tpm";
connectAttr "PosAux_03_jnt.jo" "Spl_02_root_parentConstraint1.tg[0].tjo";
connectAttr "PosAux_03_jnt.ssc" "Spl_02_root_parentConstraint1.tg[0].tsc";
connectAttr "PosAux_03_jnt.is" "Spl_02_root_parentConstraint1.tg[0].tis";
connectAttr "Spl_02_root_parentConstraint1.w0" "Spl_02_root_parentConstraint1.tg[0].tw"
		;
connectAttr "Spl_01_ctr.t" "SplBezier_01_off.t";
connectAttr "Spl_00_root_parentConstraint1.ctx" "Spl_00_root.tx";
connectAttr "Spl_00_root_parentConstraint1.cty" "Spl_00_root.ty";
connectAttr "Spl_00_root_parentConstraint1.ctz" "Spl_00_root.tz";
connectAttr "Spl_00_root_parentConstraint1.crx" "Spl_00_root.rx";
connectAttr "Spl_00_root_parentConstraint1.cry" "Spl_00_root.ry";
connectAttr "Spl_00_root_parentConstraint1.crz" "Spl_00_root.rz";
connectAttr "Spl_00_root.ro" "Spl_00_root_parentConstraint1.cro";
connectAttr "Spl_00_root.pim" "Spl_00_root_parentConstraint1.cpim";
connectAttr "Spl_00_root.rp" "Spl_00_root_parentConstraint1.crp";
connectAttr "Spl_00_root.rpt" "Spl_00_root_parentConstraint1.crt";
connectAttr "PosAux_00_jnt.t" "Spl_00_root_parentConstraint1.tg[0].tt";
connectAttr "PosAux_00_jnt.rp" "Spl_00_root_parentConstraint1.tg[0].trp";
connectAttr "PosAux_00_jnt.rpt" "Spl_00_root_parentConstraint1.tg[0].trt";
connectAttr "PosAux_00_jnt.r" "Spl_00_root_parentConstraint1.tg[0].tr";
connectAttr "PosAux_00_jnt.ro" "Spl_00_root_parentConstraint1.tg[0].tro";
connectAttr "PosAux_00_jnt.s" "Spl_00_root_parentConstraint1.tg[0].ts";
connectAttr "PosAux_00_jnt.pm" "Spl_00_root_parentConstraint1.tg[0].tpm";
connectAttr "PosAux_00_jnt.jo" "Spl_00_root_parentConstraint1.tg[0].tjo";
connectAttr "PosAux_00_jnt.ssc" "Spl_00_root_parentConstraint1.tg[0].tsc";
connectAttr "PosAux_00_jnt.is" "Spl_00_root_parentConstraint1.tg[0].tis";
connectAttr "Spl_00_root_parentConstraint1.w0" "Spl_00_root_parentConstraint1.tg[0].tw"
		;
connectAttr "Spl_01_ctr.t" "SplBezier_00_off.t";
connectAttr "Spl_01_root_pointConstraint1.ctx" "Spl_01_root.tx";
connectAttr "Spl_01_root_pointConstraint1.cty" "Spl_01_root.ty";
connectAttr "Spl_01_root_pointConstraint1.ctz" "Spl_01_root.tz";
connectAttr "Spl_01_root_orientConstraint1.crx" "Spl_01_root.rx";
connectAttr "Spl_01_root_orientConstraint1.cry" "Spl_01_root.ry";
connectAttr "Spl_01_root_orientConstraint1.crz" "Spl_01_root.rz";
connectAttr "Spl_01_root.pim" "Spl_01_root_pointConstraint1.cpim";
connectAttr "Spl_01_root.rp" "Spl_01_root_pointConstraint1.crp";
connectAttr "Spl_01_root.rpt" "Spl_01_root_pointConstraint1.crt";
connectAttr "Spl_00_ctr.t" "Spl_01_root_pointConstraint1.tg[0].tt";
connectAttr "Spl_00_ctr.rp" "Spl_01_root_pointConstraint1.tg[0].trp";
connectAttr "Spl_00_ctr.rpt" "Spl_01_root_pointConstraint1.tg[0].trt";
connectAttr "Spl_00_ctr.pm" "Spl_01_root_pointConstraint1.tg[0].tpm";
connectAttr "Spl_01_root_pointConstraint1.w0" "Spl_01_root_pointConstraint1.tg[0].tw"
		;
connectAttr "Spl_02_ctr.t" "Spl_01_root_pointConstraint1.tg[1].tt";
connectAttr "Spl_02_ctr.rp" "Spl_01_root_pointConstraint1.tg[1].trp";
connectAttr "Spl_02_ctr.rpt" "Spl_01_root_pointConstraint1.tg[1].trt";
connectAttr "Spl_02_ctr.pm" "Spl_01_root_pointConstraint1.tg[1].tpm";
connectAttr "Spl_01_root_pointConstraint1.w1" "Spl_01_root_pointConstraint1.tg[1].tw"
		;
connectAttr "Spl_01_root.ro" "Spl_01_root_orientConstraint1.cro";
connectAttr "Spl_01_root.pim" "Spl_01_root_orientConstraint1.cpim";
connectAttr "Spl_00_ctr.r" "Spl_01_root_orientConstraint1.tg[0].tr";
connectAttr "Spl_00_ctr.ro" "Spl_01_root_orientConstraint1.tg[0].tro";
connectAttr "Spl_00_ctr.pm" "Spl_01_root_orientConstraint1.tg[0].tpm";
connectAttr "Spl_01_root_orientConstraint1.w0" "Spl_01_root_orientConstraint1.tg[0].tw"
		;
connectAttr "Spl_02_ctr.r" "Spl_01_root_orientConstraint1.tg[1].tr";
connectAttr "Spl_02_ctr.ro" "Spl_01_root_orientConstraint1.tg[1].tro";
connectAttr "Spl_02_ctr.pm" "Spl_01_root_orientConstraint1.tg[1].tpm";
connectAttr "Spl_01_root_orientConstraint1.w1" "Spl_01_root_orientConstraint1.tg[1].tw"
		;
connectAttr "MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "input_00_link.msg" "OrigPosTpl_00_tr._relatedTo[0]";
connectAttr "SplBezier_00_root.msg" "SplBezierTpl_00_root._relatedTo[0]";
connectAttr "PosAux_00_crvShape.msg" "PosAuxTpl_01_jnt._relatedTo[0]";
connectAttr "PosAux_01_jnt.msg" "PosAuxTpl_01_jnt._relatedTo[1]";
connectAttr "PosAux_02_jnt.msg" "PosAuxTpl_01_jnt._relatedTo[2]";
connectAttr "PosAux_03_jnt.msg" "PosAuxTpl_01_jnt._relatedTo[3]";
connectAttr "SplPosWorld_00_spc.msg" "SplPosTpl_00_root._relatedTo[0]";
connectAttr "SplPosCog_00_spc.msg" "SplPosTpl_00_root._relatedTo[1]";
connectAttr "SplTplTop_03_off_aimConstraint1.crx" "SplTplTop_03_off.rx" -l on;
connectAttr "SplTplTop_03_off_aimConstraint1.cry" "SplTplTop_03_off.ry" -l on;
connectAttr "SplTplTop_03_off_aimConstraint1.crz" "SplTplTop_03_off.rz" -l on;
connectAttr "SplTplTop_03_off.pim" "SplTplTop_03_off_aimConstraint1.cpim";
connectAttr "SplTplTop_03_off.t" "SplTplTop_03_off_aimConstraint1.ct";
connectAttr "SplTplTop_03_off.rp" "SplTplTop_03_off_aimConstraint1.crp";
connectAttr "SplTplTop_03_off.rpt" "SplTplTop_03_off_aimConstraint1.crt";
connectAttr "SplTplTop_03_off.ro" "SplTplTop_03_off_aimConstraint1.cro";
connectAttr "OrigPosTpl_00_tr.t" "SplTplTop_03_off_aimConstraint1.tg[0].tt";
connectAttr "OrigPosTpl_00_tr.rp" "SplTplTop_03_off_aimConstraint1.tg[0].trp";
connectAttr "OrigPosTpl_00_tr.rpt" "SplTplTop_03_off_aimConstraint1.tg[0].trt";
connectAttr "OrigPosTpl_00_tr.pm" "SplTplTop_03_off_aimConstraint1.tg[0].tpm";
connectAttr "SplTplTop_03_off_aimConstraint1.w0" "SplTplTop_03_off_aimConstraint1.tg[0].tw"
		;
connectAttr "SplPosTpl_00_root.wm" "SplTplTop_03_off_aimConstraint1.wum";
connectAttr "Spl_03_loc.msg" "SplTpl_03_loc._relatedTo[0]";
connectAttr "SplBezier_01_root.msg" "SplBezierTpl_01_root._relatedTo[0]";
connectAttr "OrigPosTpl_00_trShape.wp" "referenceTpl_00_crvShape.cp[0]";
connectAttr "SplBezierTpl_00_rootShape.wp" "referenceTpl_00_crvShape.cp[1]";
connectAttr "SplBezierTpl_01_rootShape.wp" "referenceTpl_00_crvShape.cp[2]";
connectAttr "SplTpl_03_locShape.wp" "referenceTpl_00_crvShape.cp[3]";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Spl_01_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "SplPos_01_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "SplPos_00_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "SplBezier_00_ctr.msg" "SplBezier_00_tag.act";
connectAttr "SplBezier_00_tag.msg" "SplBezier_00_tag.child[0]";
connectAttr "Spl_00_ctr.msg" "Spl_00_tag.act";
connectAttr "SplBezier_00_tag.pare" "Spl_00_tag.child[0]";
connectAttr "SplBezier_01_ctr.msg" "SplBezier_01_tag.act";
connectAttr "SplBezier_01_tag.msg" "SplBezier_01_tag.child[0]";
connectAttr "Spl_02_ctr.msg" "Spl_02_tag.act";
connectAttr "SplBezier_01_tag.pare" "Spl_02_tag.child[0]";
connectAttr "Spl_01_ctr.msg" "Spl_01_tag.act";
connectAttr "Spl_02_tag.pare" "Spl_01_tag.child[0]";
connectAttr "SplPos_01_ctr.msg" "SplPos_00_tag.act";
connectAttr "Spl_00_tag.pare" "SplPos_00_tag.child[0]";
connectAttr "Spl_01_tag.pare" "SplPos_00_tag.child[1]";
connectAttr "Spl_02_tag.pare" "SplPos_00_tag.child[2]";
connectAttr "OrigPosTpl_00_tr.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "SplPosTpl_00_root.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "SplTpl_03_loc.msg" "MetadataTemplate._inputTemplate[2]";
connectAttr "SplBezierTpl_00_root.msg" "MetadataTemplate._inputTemplate[3]";
connectAttr "PosAuxTpl_01_jnt.msg" "MetadataTemplate._inputTemplate[4]";
connectAttr "SplBezierTpl_01_root.msg" "MetadataTemplate._inputTemplate[5]";
connectAttr "SplPos_01_ctr.spaceSwith" "SpaceWorld_00_chc.s";
connectAttr "SplPos_01_ctr.spaceSwith" "SpaceCOG_00_chc.s";
connectAttr "SplPos_00_ctr.msg" "SplPos_01_tag.act";
connectAttr "Spl_00_tag.pare" "SplPos_01_tag.child[0]";
connectAttr "Spl_01_tag.pare" "SplPos_01_tag.child[1]";
connectAttr "Spl_02_tag.pare" "SplPos_01_tag.child[2]";
connectAttr "input_00_link.iog" "LinkSet.dsm" -na;
connectAttr "SplBezier_01_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Spl_02_ctr.iog" "Secondaries.dsm" -na;
connectAttr "SplBezier_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Spl_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikSplineSolver.msg" ":ikSystem.sol" -na;
// End of 3Ik2Bezier.ma
