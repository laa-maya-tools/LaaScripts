//Maya ASCII 2020 scene
//Name: RP2BonesAdvanced.ma
//Last modified: Tue, Jul 19, 2022 11:27:18 AM
//Codeset: 1252
requires maya "2020";
requires -nodeType "floatMath" "lookdevKit" "1.0";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "9A4DD6DE-4CBF-8DC8-37C5-CA82F458D098";
createNode transform -s -n "persp";
	rename -uid "B4B63DCA-4936-003A-7F56-73B45A379CB3";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 37.772517160121943 26.95878706823035 64.948239796075057 ;
	setAttr ".r" -type "double3" -21.338352729559197 -352.1999999999091 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "21E0C8FA-4824-2911-1F6B-A6BB58CD338F";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 72.803912305129316;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 1.25 0 0 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "03876BE8-4FC1-1D6C-5DB7-B1BD1CAE953A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "919BFBD2-42C1-0DCA-9CD3-D1A8A4EB54E5";
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
	rename -uid "AB63888F-4174-7F4B-C57B-A597184D9A38";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 24.35047275687586 -1.923078420946152 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "64BB7816-4FCA-76B5-CEF0-2B8204A494B1";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 36.863077359398801;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "3B713192-42A3-798C-D3D7-9591E6ECB62E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 -0.22970053173944716 0.24967063755088992 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "608A4D6C-4E8A-3193-5454-2B87230FF38C";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 975.10000000000036;
	setAttr ".ow" 40.314206304345639;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 24.999999999999702 -1.2325951644078309e-31 -3.8534702486714423e-06 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Sys_00_grp";
	rename -uid "A3AA4FFA-4E7C-8C85-16FA-339C10383FE8";
	setAttr ".v" no;
createNode joint -n "Ik_00_jnt" -p "Sys_00_grp";
	rename -uid "FD3C5F1A-44CF-7A09-A68D-CE8070C6AEC3";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".is" -type "double3" 1.0099999904632568 1 1 ;
createNode joint -n "Ik_01_jnt" -p "Sys_00_grp";
	rename -uid "6006F585-4D1C-08EE-AAAA-79B325BE5BF1";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".is" -type "double3" 1.0099999904632568 1 1 ;
createNode transform -n "Ik_00_crv" -p "Sys_00_grp";
	rename -uid "B1124AF1-407B-48F3-4B6B-63B815E40340";
createNode nurbsCurve -n "Ik_00_crvShape" -p "Ik_00_crv";
	rename -uid "59391DE8-439D-01A4-E518-E0A8912B5577";
	setAttr -k off ".v";
	setAttr -s 3 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		1 2 0 no 3
		3 0 1 2
		3
		0 0 0
		24.999999999999702 0 -3.8534702482777092e-06
		49.999999999999403 0 1.1693265830365727e-08
		;
createNode transform -n "IkPoleIksc_00_root" -p "Sys_00_grp";
	rename -uid "EF5A3390-4914-4AA3-7BF7-F6BC5945C574";
createNode pointConstraint -n "IkPoleIkscRoot_00_pnc" -p "IkPoleIksc_00_root";
	rename -uid "8D7B2255-42E5-A0EB-8D83-B9B8E5208FF9";
createNode ikHandle -n "IkPole_00_iksc" -p "IkPoleIksc_00_root";
	rename -uid "B9D424A3-4567-73B3-0C71-0A81389D3A10";
	setAttr ".roc" yes;
createNode transform -n "OrigSystem_00_tr" -p "Sys_00_grp";
	rename -uid "6C5349E3-44C1-8EA5-81A0-9F882C22F455";
createNode joint -n "IkPole_00_jnt" -p "OrigSystem_00_tr";
	rename -uid "14AEC72D-4DA9-AADB-39C1-8F8A334D8E70";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode joint -n "IkPoleEnd_00_jnt" -p "IkPole_00_jnt";
	rename -uid "9E99DFDD-4974-E74D-74EE-5687BA39D23C";
	setAttr ".t" -type "double3" 3 0 0 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.60344827586206895;
createNode ikEffector -n "effector2" -p "IkPole_00_jnt";
	rename -uid "6C416B41-42F1-E542-0321-6094BE228E8E";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode transform -n "IkPole_00_root" -p "IkPole_00_jnt";
	rename -uid "66735677-4C19-5361-4A8D-CD84EFBE3C90";
createNode transform -n "IkPole_00_loc" -p "IkPole_00_root";
	rename -uid "0D1D4063-4807-0EB7-E97F-F3941403033B";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 25 0 -15 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "IkPole_00_locLocShape" -p "IkPole_00_loc";
	rename -uid "492E44A3-44C9-42A9-AE30-2A823ECE3C5B";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 5;
createNode transform -n "StretchOrig_00_loc" -p "OrigSystem_00_tr";
	rename -uid "2E0CD9EE-4A8D-D341-3F03-16B66B5B2742";
createNode locator -n "StretchOrig_00_locShape" -p "StretchOrig_00_loc";
	rename -uid "816F329D-41E6-52C3-9BB3-EE9E5610B957";
	setAttr -k off ".v";
createNode joint -n "Aux_00_jnt" -p "OrigSystem_00_tr";
	rename -uid "AB536135-45CD-F6F8-240C-1E97CB7E5CC2";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "Aux_01_jnt" -p "Aux_00_jnt";
	rename -uid "ECC89187-4236-0881-2319-9DB4556A1A11";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".pa" -type "double3" 0 -90 0 ;
	setAttr ".radi" 0.55172413793103448;
createNode joint -n "AuxEnd_02_jnt" -p "Aux_01_jnt";
	rename -uid "4BD89F53-41BD-0DA3-B2DB-B98495F6B619";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode transform -n "Ik_02_loc" -p "AuxEnd_02_jnt";
	rename -uid "D0CE658F-4156-BDAC-DDD3-F995DAF81F01";
createNode locator -n "Ik_02_locShape" -p "Ik_02_loc";
	rename -uid "C2D5A569-4840-8310-F166-5CB82D85003E";
	setAttr -k off ".v";
createNode ikEffector -n "effector1" -p "Aux_01_jnt";
	rename -uid "78CD5108-4698-A473-7610-2F9D3C98F8BD";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode orientConstraint -n "AuxJnt_01_orc" -p "Aux_01_jnt";
	rename -uid "38B3E220-486D-1A14-7C00-049424BEF0F5";
	setAttr ".int" 0;
createNode transform -n "ElbowIkLoc_01_root" -p "Aux_01_jnt";
	rename -uid "8F3730FB-4919-BC2D-FE51-C3A950FC3EBC";
createNode transform -n "Ik_01_loc" -p "ElbowIkLoc_01_root";
	rename -uid "67BA0904-46F4-2FD5-255F-A8B48E86589A";
createNode locator -n "Ik_01_locShape" -p "Ik_01_loc";
	rename -uid "3B5AB65D-420A-3865-3E20-0EB8C41816B4";
	setAttr -k off ".v";
createNode transform -n "Fk_01_snapper" -p "Aux_01_jnt";
	rename -uid "A9172A88-4D5A-F71F-5EB7-A2B184963B9B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".r" -type "double3" 0 4.5016297514303023e-06 0 ;
createNode orientConstraint -n "AuxJnt_00_orc" -p "Aux_00_jnt";
	rename -uid "F4B1242D-456D-6AF4-4344-38B1F336A60B";
	setAttr ".int" 0;
createNode transform -n "Ik_00_loc" -p "Aux_00_jnt";
	rename -uid "57BEAA6C-4C20-2252-B1AD-BE80E8AE1664";
createNode locator -n "Ik_00_locShape" -p "Ik_00_loc";
	rename -uid "3CE95B83-406D-90E5-A2F5-07B54B262530";
	setAttr -k off ".v";
createNode transform -n "Fk_00_snapper" -p "Aux_00_jnt";
	rename -uid "3FE6681B-4444-8F33-0BCB-1BA4B403C61A";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
createNode pointConstraint -n "OrigSystemTr_00_pnc" -p "OrigSystem_00_tr";
	rename -uid "C240F8FE-4EDB-95FD-6EEE-47BD70D9C7B2";
createNode pointConstraint -n "outputLink_00_pnc" -p "Sys_00_grp";
	rename -uid "2A2CD2D7-496E-1DB6-D66E-F68210E2B844";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "AuxEnd_02_jntW0" -dv 1 -min 0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 49.999999999999403 0 1.1693265830365727e-08 ;
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
	setAttr ".rst" -type "double3" 49.999999999999403 0 1.1693265830365727e-08 ;
	setAttr -k on ".w0";
createNode orientConstraint -n "outputLink_00_orc" -p "Sys_00_grp";
	rename -uid "551C7C01-4ECD-C14E-DC0C-C2B7AB2F6FA5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "outputLinkFk_00_mstcW0" -dv 1 -min 
		0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "outputLinkIk_00_mstcW1" -dv 1 -min 
		0 -at "double";
	setAttr -k on ".nds";
	setAttr -k off ".v";
	setAttr ".t" -type "double3" 49.999999999999403 0 1.1693265830365727e-08 ;
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
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "_00_jnt";
	rename -uid "B991C990-49D6-BE46-CAB5-668CA9DA56E0";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -l on ".jox";
	setAttr -l on ".joy";
	setAttr -l on ".joz";
	setAttr ".radi" 0.75862068965517238;
createNode joint -n "_01_jnt" -p "_00_jnt";
	rename -uid "5663E296-49F5-7803-678E-FF93203A2509";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -l on ".jox";
	setAttr -l on ".joy";
	setAttr -l on ".joz";
	setAttr ".radi" 0.75862068965517238;
createNode joint -n "End_01_jnt" -p "_01_jnt";
	rename -uid "65DB72EF-4B13-647D-F64F-BEB1F3174ED5";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr -l on ".jox";
	setAttr -l on ".joy";
	setAttr -l on ".joz";
	setAttr ".radi" 0.75862068965517238;
createNode pointConstraint -n "EndJnt_01_pnc" -p "End_01_jnt";
	rename -uid "92BC077E-4AC4-B93F-B917-A3B64CF402FF";
createNode parentConstraint -n "Jnt_01_prc" -p "_01_jnt";
	rename -uid "7425922E-4931-3BC6-C07C-AAA2E4AEBEE4";
	setAttr ".lr" -type "double3" 0 -1.786670341424925e-05 0 ;
createNode parentConstraint -n "Jnt_00_prc" -p "_00_jnt";
	rename -uid "4CD4FA8B-4AF6-9725-B53B-88B28BE71E9E";
	setAttr ".lr" -type "double3" 0 8.9198182166801621e-06 0 ;
createNode transform -n "Controls_00_grp";
	rename -uid "E2D5BA09-4FC1-705E-E1F2-CD8BC0294DB8";
createNode transform -n "Fk_00_root" -p "Controls_00_grp";
	rename -uid "7A0EAFCC-4466-4322-3F51-6CBB738AB723";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_00_ctr" -p "Fk_00_root";
	rename -uid "819F6986-488E-A952-3F60-51A2F2661BA4";
	addAttr -uap -ci true -k true -sn "fkik" -ln "fkik" -nn "Fk Ik" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
	setAttr -k on ".fkik";
createNode transform -n "Fk_01_root" -p "Fk_00_ctr";
	rename -uid "3BCD9315-400B-0151-21C4-CD9004317599";
	setAttr ".t" -type "double3" 25 0 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_01_ctr" -p "Fk_01_root";
	rename -uid "DB31059E-4708-C4FD-6C79-7F9BBCF18EEE";
	addAttr -uap -ci true -k true -sn "fkik" -ln "fkik" -nn "Fk Ik" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on -k off ".sx";
	setAttr ".mntl" -type "double3" 0 -1 -1 ;
	setAttr ".mxtl" -type "double3" 0 1 1 ;
	setAttr ".mtxe" yes;
	setAttr -k on ".fkik";
createNode transform -n "Fk_02_root" -p "Fk_01_ctr";
	rename -uid "6C082067-4E35-4F96-24C1-BF98131FB280";
	setAttr ".t" -type "double3" 25 3.3306690738754696e-16 2.3386531822211509e-08 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Fk_02_ctr" -p "Fk_02_root";
	rename -uid "A40B39F8-4648-4E5F-A805-8F9F7CA5FEA6";
	addAttr -uap -ci true -k true -sn "fkik" -ln "fkik" -nn "Fk Ik" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".mntl" -type "double3" 0 -1 -1 ;
	setAttr ".mxtl" -type "double3" 0 1 1 ;
	setAttr ".mtxe" yes;
	setAttr -k on ".fkik";
createNode transform -n "Ik_00_snapper" -p "Fk_02_ctr";
	rename -uid "96666541-42F2-A029-B33E-BC8666FD4470";
	setAttr ".v" no;
createNode nurbsCurve -n "Fk_02_ctrShape" -p "Fk_02_ctr";
	rename -uid "DAAE27C5-4C1B-AC82-797F-5CAA669AD4E3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-2.4999999368446882e-05 3.75 -3.75
		-2.4999999368446882e-05 3.75 3.75
		-2.4999999368446882e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 3.75 3.75
		2.5 3.75 -3.75
		2.5 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 -3.75
		-2.4999999368446882e-05 3.75 -3.75
		2.5 3.75 -3.75
		2.5 3.75 3.75
		-2.4999999368446882e-05 3.75 3.75
		-2.4999999368446882e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 3.75
		;
createNode transform -n "outputLinkFk_00_mstc" -p "Fk_02_ctr";
	rename -uid "4507D6A1-4D56-5F35-F18A-85BFA961E0D9";
	setAttr ".v" no;
createNode nurbsCurve -n "Fk_01_ctrShape" -p "Fk_01_ctr";
	rename -uid "5731CB49-42C4-12CB-54AA-8A8AD2BE443B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893772e-05 2.5 -2.5
		-4.9999998736893772e-05 2.5 2.5
		-4.9999998736893772e-05 -2.5 2.5
		24 -2.5 2.5
		24 2.5 2.5
		24 2.5 -2.5
		24 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 -2.5
		-4.9999998736893772e-05 2.5 -2.5
		24 2.5 -2.5
		24 2.5 2.5
		-4.9999998736893772e-05 2.5 2.5
		-4.9999998736893772e-05 -2.5 2.5
		24 -2.5 2.5
		24 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 2.5
		;
createNode transform -n "TwistSnapper_00_root" -p "Fk_00_ctr";
	rename -uid "14D9A920-4A26-8171-69DF-6F893CB7F9CC";
	setAttr ".v" no;
createNode transform -n "Twist_00_snapper" -p "TwistSnapper_00_root";
	rename -uid "912940E0-4C32-7EFF-4033-6CABC6A8BF29";
	setAttr ".v" no;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
createNode aimConstraint -n "TwistSnapper_00_snapper_aimc" -p "Twist_00_snapper";
	rename -uid "70B82A8B-472F-6142-B991-4981A4B6ECCD";
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
	rename -uid "E5B39F4B-4860-2B4F-5ED7-C0B4C49CA1BD";
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
	rename -uid "C1C340A8-46DC-F73C-6064-14881746276A";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893772e-05 2.5 -2.5
		-4.9999998736893772e-05 2.5 2.5
		-4.9999998736893772e-05 -2.5 2.5
		24 -2.5 2.5
		24 2.5 2.5
		24 2.5 -2.5
		24 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 -2.5
		-4.9999998736893772e-05 2.5 -2.5
		24 2.5 -2.5
		24 2.5 2.5
		-4.9999998736893772e-05 2.5 2.5
		-4.9999998736893772e-05 -2.5 2.5
		24 -2.5 2.5
		24 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 -2.5
		-4.9999998736893772e-05 -2.5 2.5
		;
createNode pointConstraint -n "FkRoot_00_root_pnc" -p "Fk_00_root";
	rename -uid "9B0A3E12-4304-4DB1-BDBF-F2BC9663D768";
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
	rename -uid "BFEAC33B-4D65-DD47-1874-F49AD95D0ED7";
createNode transform -n "Twist_00_root" -p "IkCtr_00_root";
	rename -uid "51093D35-4961-DC58-C3B4-8F85B286AE0A";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754706e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 -9.8607613152626519e-32 0 ;
createNode transform -n "Twist_00_off" -p "Twist_00_root";
	rename -uid "D8BABF25-4D8D-1DB6-BED8-99894EB006BF";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Twist_00_ctr" -p "Twist_00_off";
	rename -uid "CFDAB1EA-4D83-561F-0220-2D9B0F3735DB";
	addAttr -uap -ci true -k true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
	addAttr -uap -ci true -k true -sn "antiPop" -ln "antiPop" -min 0 -max 10 -at "double";
	addAttr -uap -ci true -k true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 
		-at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".fkIk";
	setAttr -k on ".antiPop";
	setAttr -k on ".autoStretch";
createNode nurbsCurve -n "Twist_00_ctrShape" -p "Twist_00_ctr";
	rename -uid "FA713145-495B-FE29-BECA-4A98409DB6C8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		3.0000013241587693 -2.9999999999999996 -2.9999961465297513
		-4.2293277529450452e-14 -0.99999999999999933 -4.9999961465297504
		-3.0000013241581724 -2.9999999999999996 -2.9999961465297513
		-0.9999986758412327 -4.2186164819646864e-16 -4.9999961465297522
		-3.0000013241581724 2.9999999999999996 -2.9999961465297549
		-5.5504284848016127e-16 0.99999999999999978 -4.9999961465297522
		3.0000013241587693 2.9999999999999996 -2.9999961465297549
		0.99999867584182667 1.1097401244046583e-15 -4.9999961465297522
		3.0000013241587693 -2.9999999999999996 -2.9999961465297513
		-4.2293277529450452e-14 -0.99999999999999933 -4.9999961465297504
		-3.0000013241581724 -2.9999999999999996 -2.9999961465297513
		;
createNode pointConstraint -n "TwistRoot_00_pnc" -p "Twist_00_root";
	rename -uid "5F1ADD45-4329-987E-0C4C-E3AB390F863B";
	setAttr ".r" -type "double3" 0 4.5016297514302998e-06 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
createNode orientConstraint -n "TwistRoot_00_orc" -p "Twist_00_root";
	rename -uid "ECCDBC05-4FF3-A7E0-3D39-218D0600820A";
	setAttr ".r" -type "double3" 0 2.2508148757151524e-06 0 ;
	setAttr ".s" -type "double3" 0.99999999999999978 0.99999999999999978 0.99999999999999978 ;
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 -1.3399495616089709e-08 0 ;
	setAttr ".int" 2;
createNode transform -n "Ik_00_root" -p "IkCtr_00_root";
	rename -uid "18874DCE-488B-16A3-029D-5B8A575721A8";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Ik_00_ctr" -p "Ik_00_root";
	rename -uid "FA224559-4674-2616-F0CE-D2B4ED997A9D";
	addAttr -uap -ci true -k true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
	addAttr -uap -ci true -k true -sn "antiPop" -ln "antiPop" -min 0 -max 10 -at "double";
	addAttr -uap -ci true -k true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 
		-at "double";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 50 3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".fkIk";
	setAttr -k on ".antiPop";
	setAttr -k on ".autoStretch";
createNode transform -n "IkChilds_00_grp" -p "Ik_00_ctr";
	rename -uid "23074755-4414-54BE-74E5-F1BDB7871AC4";
	setAttr -l on ".v" no;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode transform -n "StretchEnd_00_loc" -p "IkChilds_00_grp";
	rename -uid "057AD56B-426E-41CF-37CB-5C8DB5FC1ABA";
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
createNode locator -n "StretchEnd_00_locShape" -p "StretchEnd_00_loc";
	rename -uid "81CD0658-408C-9030-023F-1A9D3BBEA9A2";
	setAttr -k off ".v";
createNode ikHandle -n "Ik_00_Ikh" -p "IkChilds_00_grp";
	rename -uid "A34C5356-43C2-7AAF-FCA2-7A9F8305B552";
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
	rename -uid "A09A4119-444B-40D7-D39E-BD8ED783DD5F";
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
	rename -uid "ADF88F76-4DBE-5C0B-68B0-E6B24D478384";
	setAttr ".v" no;
createNode nurbsCurve -n "Ik_00_ctrShape" -p "Ik_00_ctr";
	rename -uid "61B9F181-48FC-C41C-B785-CBBD02346B5F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-2.4999999368446882e-05 3.75 -3.75
		-2.4999999368446882e-05 3.75 3.75
		-2.4999999368446882e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 3.75 3.75
		2.5 3.75 -3.75
		2.5 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 -3.75
		-2.4999999368446882e-05 3.75 -3.75
		2.5 3.75 -3.75
		2.5 3.75 3.75
		-2.4999999368446882e-05 3.75 3.75
		-2.4999999368446882e-05 -3.75 3.75
		2.5 -3.75 3.75
		2.5 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 -3.75
		-2.4999999368446882e-05 -3.75 3.75
		;
createNode transform -n "outputLinkIk_00_mstc" -p "Ik_00_ctr";
	rename -uid "E6A16ED3-4A75-8241-072C-14A189A447BA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -5.9685589803848416e-13 -3.3306690738754696e-16 1.1693265830365727e-08 ;
createNode transform -n "Config_00_root" -p "Controls_00_grp";
	rename -uid "EC74A45E-4A1D-412C-6030-0EADD623E531";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Config_00_ctr" -p "Config_00_root";
	rename -uid "28DD66C8-4115-0FD7-AF20-D0AE84F65A18";
	addAttr -ci true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
	addAttr -ci true -sn "antiPop" -ln "antiPop" -min 0 -max 10 -at "double";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
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
	setAttr -k on ".antiPop";
	setAttr -k on ".autoStretch" 1;
createNode nurbsCurve -n "Config_00_ctrShape" -p "Config_00_ctr";
	rename -uid "556FB6E5-4A42-CDF0-5E6D-77AE7801C513";
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
	rename -uid "B72FA34E-4A74-A841-9E03-ADBE5F1DAB8A";
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
	rename -uid "1732FFB7-4922-B5EA-2CDC-75909643AD10";
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
	rename -uid "7BE34EAF-4120-0918-9E58-2299BACE2412";
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
	rename -uid "102E539F-47AA-8EA4-7312-06BFA57FA959";
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
	rename -uid "B19E88F4-4E2E-1879-5C85-42AAC09C420C";
	setAttr ".lr" -type "double3" 0 8.8315032682217241e-06 0 ;
createNode transform -n "Pin_01_root" -p "Controls_00_grp";
	rename -uid "496841AB-403B-C08B-468B-A3BF08955419";
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Pin_01_ctr" -p "Pin_01_root";
	rename -uid "A1BB833B-4D4E-5F1E-1EFE-5F8FB42087F2";
	addAttr -uap -ci true -k true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
	addAttr -uap -ci true -k true -sn "antiPop" -ln "antiPop" -min 0 -max 10 -at "double";
	addAttr -uap -ci true -k true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 
		-at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".fkIk";
	setAttr -k on ".antiPop";
	setAttr -k on ".autoStretch";
createNode nurbsCurve -n "Pin_01_ctrShape" -p "Pin_01_ctr";
	rename -uid "DFA29039-4D5B-4DDA-6747-50A2ADEB6206";
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
createNode parentConstraint -n "PinRoot_01_prc" -p "Pin_01_root";
	rename -uid "E5BB552F-47B2-CF4A-F460-A899F4A931DE";
	setAttr ".s" -type "double3" 1.0000000000000004 1 1.0000000000000002 ;
	setAttr ".lr" -type "double3" 0 -8.8583022594539015e-06 0 ;
createNode transform -n "Tpl_00_tpl";
	rename -uid "63515D44-4D96-453B-4901-249B6340C871";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "OrigSystemTpl_00_tr" -p "Tpl_00_tpl";
	rename -uid "0992DB74-4B01-3BD9-7EAD-3C8CD4AB53E4";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -uap -ci true -k true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".mirror";
createNode locator -n "OrigSystemTpl_00_trShape" -p "OrigSystemTpl_00_tr";
	rename -uid "BEB1F45D-42DC-F59C-E281-2496C444CEB8";
	setAttr -k off ".v";
createNode transform -n "IkTpl_01_loc" -p "OrigSystemTpl_00_tr";
	rename -uid "14663C03-43C6-A0C4-7C4A-EFA213CA245F";
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
	rename -uid "A0B686E6-4FA8-3F82-09FE-239E9CBB989A";
	setAttr -k off ".v";
createNode transform -n "IkTpl_00_ctr" -p "IkTpl_01_loc";
	rename -uid "7DDE73DA-46E6-1921-295C-1DA14B0393B2";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 25 3.3306690738754696e-16 0 ;
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
createNode locator -n "IkTpl_00_ctrShape" -p "IkTpl_00_ctr";
	rename -uid "7CC84AEB-4494-EE0E-9087-36B61758D08B";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTplCtr_02_orc" -p "IkTpl_00_ctr";
	rename -uid "99A15F4F-4591-69B8-E628-648E9B4611E2";
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
createNode transform -n "IkTpl_00_root" -p "IkTpl_00_ctr";
	rename -uid "F3FC34A1-4E96-C433-3FBB-5ABF01B2901A";
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
	setAttr ".it" no;
createNode locator -n "IkTpl_00_rootShape" -p "IkTpl_00_root";
	rename -uid "3582908C-487D-5F9A-AC4F-B88F73618677";
	setAttr -k off ".v";
createNode transform -n "IkPoleTpl_00_loc" -p "IkTpl_01_loc";
	rename -uid "3AC307BF-4167-DE9E-D6A4-4CA1727873CC";
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
createNode locator -n "IkPoleTpl_00_locShape" -p "IkPoleTpl_00_loc";
	rename -uid "ACC50032-42DB-8908-A94A-9A88FE5BD0A6";
	setAttr -k off ".v";
createNode transform -n "FKTpl_02_root" -p "IkTpl_01_loc";
	rename -uid "21A802DC-4E5A-758F-8978-DEABAB9861F3";
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
	rename -uid "DF30204E-47A9-A860-18C9-0CBCAE324C70";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 0 1 0 ;
createNode transform -n "FkTpl_02_ctr" -p "FKTpl_02_root";
	rename -uid "F2797959-4D09-D128-BF7C-A6AFA134B505";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" -3.5527136788005009e-15 3.3306690738754696e-16 2.3570478260457819e-07 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -s 2 "._relatedTo";
createNode locator -n "FkTpl_02_ctrShape" -p "FkTpl_02_ctr";
	rename -uid "24FFB1E7-45E3-D684-E922-C1926FAF5F1A";
	setAttr -k off ".v";
createNode transform -n "FKTpl_01_root" -p "OrigSystemTpl_00_tr";
	rename -uid "3900BDFD-481D-E5EA-3959-1A93E5119A4F";
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
	rename -uid "228B4393-4735-E8E6-FB6D-6799F49F1CB3";
	setAttr -k off ".v";
createNode transform -n "FkTpl_01_ctr" -p "FKTpl_01_root";
	rename -uid "F698BB4F-4CA6-4CF3-2C47-5695F71EAC92";
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
	rename -uid "97825CD1-4D8E-A01E-D60F-70BD65C77FD6";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTpl_01_ctr_orientConstraint1" -p "FkTpl_01_ctr";
	rename -uid "704D7283-4E75-530E-8C0B-989BB1A61A44";
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
createNode transform -n "Config_00_tpl" -p "OrigSystemTpl_00_tr";
	rename -uid "494739A6-40E1-921F-0413-6298F7488661";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -ci true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
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
	setAttr -s 10 "._relatedTo";
createNode locator -n "Config_00_tplShape" -p "Config_00_tpl";
	rename -uid "20DE6C19-4337-D478-FD3E-FC9528E8DDA7";
	setAttr -k off ".v";
	setAttr ".lp" -type "double3" 1.25 0 0 ;
	setAttr ".los" -type "double3" 0.25 1 1 ;
createNode transform -n "FKTpl_00_root" -p "Tpl_00_tpl";
	rename -uid "EA67FFEF-4905-98FE-1240-14ABB79F589E";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "FKTpl_00_rootShape" -p "FKTpl_00_root";
	rename -uid "DBFB758A-410A-91F3-CBB2-EF8EEEAE505D";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode transform -n "FkTpl_00_ctr" -p "FKTpl_00_root";
	rename -uid "549C4F3C-44EB-906A-7242-A689E97A9173";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "FkTpl_00_ctrShape" -p "FkTpl_00_ctr";
	rename -uid "BF1E9169-46E0-ABD0-9FFA-14910A9B6F11";
	setAttr -k off ".v";
createNode orientConstraint -n "FkTpl_00_ctr_orientConstraint1" -p "FkTpl_00_ctr";
	rename -uid "15FBD1FB-4CF5-AF6B-10CD-3C9F4CCDB7B2";
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
createNode transform -n "Stretch_00_tpl" -p "Tpl_00_tpl";
	rename -uid "2D9157CD-4655-2CC7-12CC-3A964883F7B9";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -uap -ci true -sn "neutralPoseMid" -ln "neutralPoseMid" -at "doubleLinear";
	addAttr -uap -ci true -sn "neutralPoseEnd" -ln "neutralPoseEnd" -at "doubleLinear";
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
	setAttr -s 5 "._relatedTo";
	setAttr -av ".neutralPoseMid";
	setAttr -av ".neutralPoseEnd";
createNode locator -n "Stretch_00_tplShape" -p "Stretch_00_tpl";
	rename -uid "A6752ED1-48D3-1F46-27A6-AFB9811BD808";
	setAttr -k off ".v";
createNode transform -n "output_00_link";
	rename -uid "C0D1485F-4E62-DB37-F1A7-2DB1A60A2090";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.40392157 0.63137257 ;
createNode transform -n "input_00_link";
	rename -uid "C0F32081-427E-2C68-DDC3-E38EC046CE25";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "02C947C1-4CEA-BD8C-0879-FE85672CABB5";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "F5A58B09-4B8E-FE30-F2DC-029655060A04";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "A2CC60CD-480D-8FDF-8A27-EB99A3C83DDC";
createNode displayLayerManager -n "layerManager";
	rename -uid "97C9C91B-47B3-D569-436E-1DBE913E7166";
createNode displayLayer -n "defaultLayer";
	rename -uid "101C884F-4F37-C4BD-DFA6-14B7ED3CBD29";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "4B89D380-4D3C-48D4-2D65-85870D9B9D42";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "ABA911EC-4406-7127-359D-9BB5219DF2EC";
	setAttr ".g" yes;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "6F1270A8-4999-FD70-D620-5C866C0FD45A";
createNode unitConversion -n "unitConversion1";
	rename -uid "26758F32-488F-A0D5-A395-8BBC8CC4F3FF";
	setAttr ".cf" -1;
createNode reverse -n "Config_00_rev";
	rename -uid "18907390-4909-99D3-D5E7-48B447647BE0";
createNode unitConversion -n "Twist_00_ucnv";
	rename -uid "CBCE16BC-41C5-D7AC-E994-D08820ACDA75";
createNode motionPath -n "Ik_00_mp";
	rename -uid "D4B405AF-4F00-5D31-F8C6-55B3FF64D26B";
	setAttr ".f" yes;
	setAttr ".fa" 0;
	setAttr ".ua" 1;
	setAttr ".wut" 2;
createNode motionPath -n "Ik_01_mp";
	rename -uid "6D535415-4918-9A83-55B1-D88F50EE8195";
	setAttr ".u" 1;
	setAttr ".f" yes;
	setAttr ".fa" 0;
	setAttr ".ua" 1;
	setAttr ".wut" 2;
createNode objectSet -n "SkinJointsSet";
	rename -uid "4C3CBCEC-449E-EE77-97FD-7CACFE7A1926";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "ControlsSet";
	rename -uid "8D38217A-413A-C807-078A-F5ABB626B308";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "LinkSet";
	rename -uid "18CF66D9-4701-068E-B365-D4BFD9074E37";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
createNode unitConversion -n "FrontTwist_00_ucnv";
	rename -uid "F7DF5D06-490E-22BF-4952-F1BB504F9302";
createNode controller -n "Config_00_tag";
	rename -uid "BA6CF277-459D-5666-0FD8-1091D3FA82A9";
createNode controller -n "Fk_00_tag";
	rename -uid "2F79FF8D-476A-7951-7FDA-7CB1D6988C52";
createNode controller -n "Ik_00_tag";
	rename -uid "DA2DC51B-4140-FA9E-834F-2595D06E61B3";
createNode controller -n "Twist_00_tag";
	rename -uid "532FA0C5-431B-FD3D-679C-5AAD07CF97C2";
createNode controller -n "Pin_01_tag";
	rename -uid "86513BA1-4172-04B9-676B-0390FFA85D9C";
createNode controller -n "Fk_01_tag";
	rename -uid "5CC93904-4D07-0297-E38A-E880983EF7FA";
createNode controller -n "Fk_02_tag";
	rename -uid "4579A715-4298-6D08-5843-EFA87DF420F9";
createNode objectSet -n "Fk";
	rename -uid "2A3D3ED7-4585-E4BC-0604-3D95DFAADD39";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "Ik";
	rename -uid "1BDF1A66-49DB-200E-BB0E-30BAE54C7378";
	setAttr ".ihi" 0;
createNode plusMinusAverage -n "StretchFk_00_pma";
	rename -uid "BFDD254E-4A92-9D41-0235-40B98DF5D2FD";
	setAttr -s 2 ".i2[1]" -type "float2" 25 25;
createNode blendColors -n "Stretch_00_blcl";
	rename -uid "E2421297-484E-EA5E-D8C0-C994CA98EA57";
	setAttr ".c2" -type "float3" 25 25 0 ;
createNode blendColors -n "AutoStretch_00_blcl";
	rename -uid "596DA385-4E70-D7D3-642C-2593F5CC52C9";
	setAttr ".c2" -type "float3" 6 6 0 ;
createNode plusMinusAverage -n "AntiPop_00_pma";
	rename -uid "6BEE03BF-43D3-020E-A445-64B258B0A856";
	setAttr -s 2 ".i2";
	setAttr -s 2 ".i2";
createNode clamp -n "Stretch_00_clp";
	rename -uid "855A1B8E-478E-7FFC-FC60-07AEE7D83265";
	setAttr ".mn" -type "float3" 25 25 0 ;
	setAttr ".mx" -type "float3" 999 999 0 ;
createNode ikSCsolver -n "ikSCsolver";
	rename -uid "F463B591-4856-82BE-606F-24BDA4570131";
createNode script -n "MetadataLimbSnapping";
	rename -uid "29CBAE05-4DBC-75F0-969F-C1ABAA1CD72E";
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
createNode multiplyDivide -n "Stretch_00_mdv";
	rename -uid "D1105C4A-4201-2758-5503-07BE76BF5C66";
createNode multiplyDivide -n "StretchFk_00_mdv";
	rename -uid "F15C92BC-422B-8AD7-7FDE-428737C035CF";
createNode distanceBetween -n "Stretch_00_dist";
	rename -uid "E5C5A9E5-4831-9D8B-5002-43BBC07354FF";
createNode multDoubleLinear -n "StretchIkFact_00_mdl";
	rename -uid "25B337DF-47D7-B788-4087-EF9B7F89EC3B";
	setAttr ".i2" 0.5;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "91010E30-44B6-1F9C-5436-7F900CD0E773";
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
	rename -uid "87FC0CF3-47D6-277E-3671-B2A7B7960EBD";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 20 -ast 1 -aet 20 ";
	setAttr ".st" 6;
createNode multDoubleLinear -n "AntiPop_00_mdl";
	rename -uid "A39EDDF9-4D44-1EF3-3520-E993065B351F";
	setAttr ".i2" 0.1;
createNode script -n "MetadataTemplate";
	rename -uid "7AD7E742-4327-4E4C-5637-A1ACAF0EDBEE";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" (
		"import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#Fk_*_ctr\nfor ind in 4,6,8:\n    template = cmds.listConnections(\"{}._inputTemplate[{}]\".format(_METADATA_TEMPLATE_, ind))[0]\n    try:\n        cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".r\", 0,0,0 )\n    except:\n        cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".ry\", 0 )\ndel template\n#OrigSystem_00_tr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, t=cmds.xform(template, t=True, ws=True, q=True))\ndel template, this\n#Ik_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Ik_00_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[2]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n"
		+ "    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[3]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_00_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[4]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_01_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[5]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_01_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[6]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\n"
		+ "del template, this\n#Fk_02_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[7]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_02_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[8]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n########\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[9]\")[0]\n#StretchIkFact_00_fm\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.setAttr(this + '.floatB', abs(cmds.getAttr(template + \".neutralPoseMid\") + cmds.getAttr(template + \".neutralPoseEnd\")) )\n#StretchIk_00_pma\nthis = cmds.listConnections(template + \"._relatedTo[1]\")[0]\ncmds.setAttr(this + '.input2D[1].input2Dx', abs(cmds.getAttr(template + \".neutralPoseMid\")) )\ncmds.setAttr(this + '.input2D[1].input2Dy', abs(cmds.getAttr(template + \".neutralPoseEnd\")) )\n"
		+ "#AutoStretch_00_blcl\nthis = cmds.listConnections(template + \"._relatedTo[2]\")[0]\ncmds.setAttr(this + '.color2R', abs(cmds.getAttr(template + \".neutralPoseMid\")) )\ncmds.setAttr(this + '.color2G', abs(cmds.getAttr(template + \".neutralPoseEnd\")) )\n#Stretch_00_clp\nthis = cmds.listConnections(template + \"._relatedTo[3]\")[0]\ncmds.setAttr(this + '.minR', abs(cmds.getAttr(template + \".neutralPoseMid\")) )\ncmds.setAttr(this + '.minG', abs(cmds.getAttr(template + \".neutralPoseEnd\")) )\n#StretchFk_00_pma\nthis = cmds.listConnections(template + \"._relatedTo[4]\")[0]\ncmds.setAttr(this + '.input2D[1].input2Dx', abs(cmds.getAttr(template + \".neutralPoseMid\")) )\ncmds.setAttr(this + '.input2D[1].input2Dy', abs(cmds.getAttr(template + \".neutralPoseEnd\")) )\n# Mirror\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[10]\")[0]\nif cmds.getAttr( template + \".mirror\" ):\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".i2\", -1,-1,-1 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[1]\")[0] + \".i2\", -1,-1,-1 )\n"
		+ "    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[2]\")[0] + \".ry\", 180 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[2]\")[0] + \".rz\", 180 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[3]\")[0] + \".conversionFactor\", -1 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[4]\")[0] + \".conversionFactor\", -1 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[5]\")[0] + \".s\", -1,-1,-1 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[6]\")[0] + \".s\", -1,-1,-1 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[7]\")[0] + \".maxTransXLimitEnable\", True )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[7]\")[0] + \".minTransXLimitEnable\", False )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[8]\")[0] + \".maxTransXLimitEnable\", True )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[8]\")[0] + \".minTransXLimitEnable\", False )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[9]\")[0] + \".rotate\", 0,0,-90 )\n"
		+ "del template\n#IkPole_00_ctr\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[11]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this");
	setAttr -l on ".stp" 1;
	setAttr -s 12 "._inputTemplate";
createNode plusMinusAverage -n "StretchIk_00_pma";
	rename -uid "1B5BE37E-41DA-D187-4B02-159F8C5F7C98";
	setAttr -s 2 ".i2[1]" -type "float2" 25 25;
createNode floatMath -n "StretchIkFact_00_fm";
	rename -uid "4C078A3F-48A6-2D73-D66F-49B4BD8BC24B";
	setAttr "._fb" 50;
	setAttr "._cnd" 1;
createNode remapValue -n "remapValue1";
	rename -uid "1F1F7E5B-4390-2D99-3B2F-80AF23E89979";
	setAttr -s 4 ".vl[0:3]"  0 1 3 0.093548387 0.31125829 3 0.2516129
		 0.11258278 3 0.42580646 0.046357617 3;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode objectSet -n "Secondaries";
	rename -uid "CB78A6EA-4B9C-D5F7-FD1A-1E81E94BC914";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
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
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 16 ".u";
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
connectAttr "Ik_00_mp.ac" "Ik_00_jnt.t";
connectAttr "Ik_00_mp.rx" "Ik_00_jnt.rx";
connectAttr "Ik_00_mp.ry" "Ik_00_jnt.ry";
connectAttr "Ik_00_mp.rz" "Ik_00_jnt.rz";
connectAttr "Ik_00_mp.ro" "Ik_00_jnt.ro";
connectAttr "Ik_01_mp.ac" "Ik_01_jnt.t";
connectAttr "Ik_01_mp.rx" "Ik_01_jnt.rx";
connectAttr "Ik_01_mp.ry" "Ik_01_jnt.ry";
connectAttr "Ik_01_mp.rz" "Ik_01_jnt.rz";
connectAttr "Ik_01_mp.ro" "Ik_01_jnt.ro";
connectAttr "Ik_00_locShape.wp" "Ik_00_crvShape.cp[0]";
connectAttr "Ik_01_locShape.wp" "Ik_00_crvShape.cp[1]";
connectAttr "Ik_02_locShape.wp" "Ik_00_crvShape.cp[2]";
connectAttr "IkPoleIkscRoot_00_pnc.cty" "IkPoleIksc_00_root.ty";
connectAttr "IkPoleIkscRoot_00_pnc.ctz" "IkPoleIksc_00_root.tz";
connectAttr "IkPoleIkscRoot_00_pnc.ctx" "IkPoleIksc_00_root.tx";
connectAttr "Ik_00_ctr.wm" "IkPoleIkscRoot_00_pnc.tg[0].tpm";
connectAttr "IkPoleIksc_00_root.pim" "IkPoleIkscRoot_00_pnc.cpim";
connectAttr "IkPole_00_jnt.msg" "IkPole_00_iksc.hsj";
connectAttr "effector2.hp" "IkPole_00_iksc.hee";
connectAttr "ikSCsolver.msg" "IkPole_00_iksc.hsv";
connectAttr "OrigSystemTr_00_pnc.ctx" "OrigSystem_00_tr.tx";
connectAttr "OrigSystemTr_00_pnc.cty" "OrigSystem_00_tr.ty";
connectAttr "OrigSystemTr_00_pnc.ctz" "OrigSystem_00_tr.tz";
connectAttr "IkPole_00_jnt.s" "IkPoleEnd_00_jnt.is";
connectAttr "IkPoleEnd_00_jnt.tx" "effector2.tx";
connectAttr "IkPoleEnd_00_jnt.ty" "effector2.ty";
connectAttr "IkPoleEnd_00_jnt.tz" "effector2.tz";
connectAttr "IkPoleEnd_00_jnt.opm" "effector2.opm";
connectAttr "Twist_00_ucnv.o" "IkPole_00_root.rx";
connectAttr "AuxJnt_00_orc.crx" "Aux_00_jnt.rx";
connectAttr "AuxJnt_00_orc.cry" "Aux_00_jnt.ry";
connectAttr "AuxJnt_00_orc.crz" "Aux_00_jnt.rz";
connectAttr "AuxJnt_01_orc.crx" "Aux_01_jnt.rx";
connectAttr "AuxJnt_01_orc.cry" "Aux_01_jnt.ry";
connectAttr "AuxJnt_01_orc.crz" "Aux_01_jnt.rz";
connectAttr "Aux_00_jnt.s" "Aux_01_jnt.is";
connectAttr "Stretch_00_mdv.ox" "Aux_01_jnt.tx";
connectAttr "Stretch_00_mdv.oy" "AuxEnd_02_jnt.tx";
connectAttr "Aux_01_jnt.s" "AuxEnd_02_jnt.is";
connectAttr "AuxEnd_02_jnt.tx" "effector1.tx";
connectAttr "AuxEnd_02_jnt.ty" "effector1.ty";
connectAttr "AuxEnd_02_jnt.tz" "effector1.tz";
connectAttr "AuxEnd_02_jnt.opm" "effector1.opm";
connectAttr "Fk_01_ctr.wm" "AuxJnt_01_orc.tg[0].tpm";
connectAttr "Config_00_rev.ox" "AuxJnt_01_orc.tg[0].tw";
connectAttr "Aux_01_jnt.pim" "AuxJnt_01_orc.cpim";
connectAttr "Pin_01_ctr.t" "Ik_01_loc.t";
connectAttr "Fk_00_ctr.wm" "AuxJnt_00_orc.tg[0].tpm";
connectAttr "Config_00_rev.ox" "AuxJnt_00_orc.tg[0].tw";
connectAttr "Aux_00_jnt.pim" "AuxJnt_00_orc.cpim";
connectAttr "input_00_link.wm" "OrigSystemTr_00_pnc.tg[0].tpm";
connectAttr "OrigSystem_00_tr.pim" "OrigSystemTr_00_pnc.cpim";
connectAttr "output_00_link.pim" "outputLink_00_pnc.cpim";
connectAttr "output_00_link.rp" "outputLink_00_pnc.crp";
connectAttr "output_00_link.rpt" "outputLink_00_pnc.crt";
connectAttr "AuxEnd_02_jnt.t" "outputLink_00_pnc.tg[0].tt";
connectAttr "AuxEnd_02_jnt.rp" "outputLink_00_pnc.tg[0].trp";
connectAttr "AuxEnd_02_jnt.rpt" "outputLink_00_pnc.tg[0].trt";
connectAttr "AuxEnd_02_jnt.pm" "outputLink_00_pnc.tg[0].tpm";
connectAttr "outputLink_00_pnc.w0" "outputLink_00_pnc.tg[0].tw";
connectAttr "output_00_link.ro" "outputLink_00_orc.cro";
connectAttr "output_00_link.pim" "outputLink_00_orc.cpim";
connectAttr "outputLinkFk_00_mstc.r" "outputLink_00_orc.tg[0].tr";
connectAttr "outputLinkFk_00_mstc.ro" "outputLink_00_orc.tg[0].tro";
connectAttr "outputLinkFk_00_mstc.pm" "outputLink_00_orc.tg[0].tpm";
connectAttr "outputLink_00_orc.w0" "outputLink_00_orc.tg[0].tw";
connectAttr "outputLinkIk_00_mstc.r" "outputLink_00_orc.tg[1].tr";
connectAttr "outputLinkIk_00_mstc.ro" "outputLink_00_orc.tg[1].tro";
connectAttr "outputLinkIk_00_mstc.pm" "outputLink_00_orc.tg[1].tpm";
connectAttr "outputLink_00_orc.w1" "outputLink_00_orc.tg[1].tw";
connectAttr "Config_00_rev.ox" "outputLink_00_orc.w0";
connectAttr "Config_00_ctr.fkIk" "outputLink_00_orc.w1";
connectAttr "Jnt_00_prc.ctx" "_00_jnt.tx";
connectAttr "Jnt_00_prc.cty" "_00_jnt.ty";
connectAttr "Jnt_00_prc.ctz" "_00_jnt.tz";
connectAttr "Jnt_00_prc.crx" "_00_jnt.rx";
connectAttr "Jnt_00_prc.cry" "_00_jnt.ry";
connectAttr "Jnt_00_prc.crz" "_00_jnt.rz";
connectAttr "_00_jnt.s" "_01_jnt.is";
connectAttr "Jnt_01_prc.ctx" "_01_jnt.tx";
connectAttr "Jnt_01_prc.cty" "_01_jnt.ty";
connectAttr "Jnt_01_prc.ctz" "_01_jnt.tz";
connectAttr "Jnt_01_prc.crx" "_01_jnt.rx";
connectAttr "Jnt_01_prc.cry" "_01_jnt.ry";
connectAttr "Jnt_01_prc.crz" "_01_jnt.rz";
connectAttr "_00_jnt.msg" "_01_jnt.parent";
connectAttr "_01_jnt.s" "End_01_jnt.is";
connectAttr "EndJnt_01_pnc.ctx" "End_01_jnt.tx";
connectAttr "EndJnt_01_pnc.cty" "End_01_jnt.ty";
connectAttr "EndJnt_01_pnc.ctz" "End_01_jnt.tz";
connectAttr "_01_jnt.msg" "End_01_jnt.parent";
connectAttr "AuxEnd_02_jnt.wm" "EndJnt_01_pnc.tg[0].tpm";
connectAttr "End_01_jnt.pim" "EndJnt_01_pnc.cpim";
connectAttr "Ik_01_jnt.wm" "Jnt_01_prc.tg[0].tpm";
connectAttr "_01_jnt.pim" "Jnt_01_prc.cpim";
connectAttr "Ik_00_jnt.wm" "Jnt_00_prc.tg[0].tpm";
connectAttr "_00_jnt.pim" "Jnt_00_prc.cpim";
connectAttr "Config_00_rev.ox" "Fk_00_root.v";
connectAttr "FkRoot_00_root_pnc.ctx" "Fk_00_root.tx";
connectAttr "FkRoot_00_root_pnc.cty" "Fk_00_root.ty";
connectAttr "FkRoot_00_root_pnc.ctz" "Fk_00_root.tz";
connectAttr "Config_00_ctr.fkIk" "Fk_00_ctr.fkik";
connectAttr "Config_00_ctr.fkIk" "Fk_01_ctr.fkik";
connectAttr "Config_00_ctr.fkIk" "Fk_02_ctr.fkik";
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
connectAttr "IkPole_00_loc.wm" "TwistSnapperRoot_00_aimc.wum";
connectAttr "Fk_00_root.pim" "FkRoot_00_root_pnc.cpim";
connectAttr "Fk_00_root.rp" "FkRoot_00_root_pnc.crp";
connectAttr "Fk_00_root.rpt" "FkRoot_00_root_pnc.crt";
connectAttr "Aux_00_jnt.t" "FkRoot_00_root_pnc.tg[0].tt";
connectAttr "Aux_00_jnt.rp" "FkRoot_00_root_pnc.tg[0].trp";
connectAttr "Aux_00_jnt.rpt" "FkRoot_00_root_pnc.tg[0].trt";
connectAttr "Aux_00_jnt.pm" "FkRoot_00_root_pnc.tg[0].tpm";
connectAttr "FkRoot_00_root_pnc.w0" "FkRoot_00_root_pnc.tg[0].tw";
connectAttr "Config_00_ctr.fkIk" "IkCtr_00_root.v";
connectAttr "TwistRoot_00_pnc.ct" "Twist_00_root.t";
connectAttr "TwistRoot_00_orc.cr" "Twist_00_root.r";
connectAttr "unitConversion1.o" "Twist_00_off.rx";
connectAttr "Config_00_ctr.fkIk" "Twist_00_ctr.fkIk";
connectAttr "Config_00_ctr.antiPop" "Twist_00_ctr.antiPop";
connectAttr "Config_00_ctr.autoStretch" "Twist_00_ctr.autoStretch";
connectAttr "Aux_01_jnt.wm" "TwistRoot_00_pnc.tg[0].tpm";
connectAttr "Twist_00_root.pim" "TwistRoot_00_pnc.cpim";
connectAttr "Aux_00_jnt.wm" "TwistRoot_00_orc.tg[0].tpm";
connectAttr "Aux_01_jnt.wm" "TwistRoot_00_orc.tg[1].tpm";
connectAttr "Twist_00_root.pim" "TwistRoot_00_orc.cpim";
connectAttr "Config_00_ctr.fkIk" "Ik_00_ctr.fkIk";
connectAttr "Config_00_ctr.antiPop" "Ik_00_ctr.antiPop";
connectAttr "Config_00_ctr.autoStretch" "Ik_00_ctr.autoStretch";
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
connectAttr "IkPole_00_loc.t" "IkIkh_00_pvc.tg[0].tt";
connectAttr "IkPole_00_loc.rp" "IkIkh_00_pvc.tg[0].trp";
connectAttr "IkPole_00_loc.rpt" "IkIkh_00_pvc.tg[0].trt";
connectAttr "IkPole_00_loc.pm" "IkIkh_00_pvc.tg[0].tpm";
connectAttr "IkIkh_00_pvc.w0" "IkIkh_00_pvc.tg[0].tw";
connectAttr "ConfigRoot_00_prc.ct" "Config_00_root.t";
connectAttr "ConfigRoot_00_prc.cr" "Config_00_root.r";
connectAttr "Aux_00_jnt.wm" "ConfigRoot_00_prc.tg[0].tpm";
connectAttr "Config_00_root.pim" "ConfigRoot_00_prc.cpim";
connectAttr "PinRoot_01_prc.ct" "Pin_01_root.t";
connectAttr "PinRoot_01_prc.cr" "Pin_01_root.r";
connectAttr "Config_00_ctr.fkIk" "Pin_01_ctr.fkIk";
connectAttr "Config_00_ctr.antiPop" "Pin_01_ctr.antiPop";
connectAttr "Config_00_ctr.autoStretch" "Pin_01_ctr.autoStretch";
connectAttr "Aux_01_jnt.wm" "PinRoot_01_prc.tg[0].tpm";
connectAttr "Pin_01_root.pim" "PinRoot_01_prc.cpim";
connectAttr "MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "input_00_link.msg" "OrigSystemTpl_00_tr._relatedTo[0]";
connectAttr "Config_00_tpl.mirror" "OrigSystemTpl_00_tr.mirror";
connectAttr "Aux_01_jnt.msg" "IkTpl_01_loc._relatedTo[0]";
connectAttr "Ik_00_ctr.msg" "IkTpl_00_ctr._relatedTo[0]";
connectAttr "FkTpl_02_ctr.ro" "FkTplCtr_02_orc.cro";
connectAttr "FkTpl_02_ctr.pim" "FkTplCtr_02_orc.cpim";
connectAttr "IkTpl_00_ctr.r" "FkTplCtr_02_orc.tg[0].tr";
connectAttr "IkTpl_00_ctr.ro" "FkTplCtr_02_orc.tg[0].tro";
connectAttr "IkTpl_00_ctr.pm" "FkTplCtr_02_orc.tg[0].tpm";
connectAttr "FkTplCtr_02_orc.w0" "FkTplCtr_02_orc.tg[0].tw";
connectAttr "Ik_00_root.msg" "IkTpl_00_root._relatedTo[0]";
connectAttr "IkPole_00_loc.msg" "IkPoleTpl_00_loc._relatedTo[0]";
connectAttr "IkTpl_00_ctr.tx" "FKTpl_02_root.tx" -l on;
connectAttr "Fk_02_root.msg" "FKTpl_02_root._relatedTo[0]";
connectAttr "FkTplCtr_02_orc.crx" "FkTpl_02_ctr.rx" -l on;
connectAttr "FkTplCtr_02_orc.cry" "FkTpl_02_ctr.ry" -l on;
connectAttr "FkTplCtr_02_orc.crz" "FkTpl_02_ctr.rz" -l on;
connectAttr "Fk_02_ctr.msg" "FkTpl_02_ctr._relatedTo[0]";
connectAttr "outputLinkIk_00_mstc.msg" "FkTpl_02_ctr._relatedTo[1]";
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
connectAttr "Stretch_00_mdv.msg" "Config_00_tpl._relatedTo[0]";
connectAttr "StretchFk_00_mdv.msg" "Config_00_tpl._relatedTo[1]";
connectAttr "Twist_00_off.msg" "Config_00_tpl._relatedTo[2]";
connectAttr "FrontTwist_00_ucnv.msg" "Config_00_tpl._relatedTo[3]";
connectAttr "Twist_00_ucnv.msg" "Config_00_tpl._relatedTo[4]";
connectAttr "Pin_01_root.msg" "Config_00_tpl._relatedTo[5]";
connectAttr "ElbowIkLoc_01_root.msg" "Config_00_tpl._relatedTo[6]";
connectAttr "Fk_01_ctr.msg" "Config_00_tpl._relatedTo[7]";
connectAttr "Fk_02_ctr.msg" "Config_00_tpl._relatedTo[8]";
connectAttr "IkPole_00_iksc.msg" "Config_00_tpl._relatedTo[9]";
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
connectAttr "IkTpl_01_loc.tx" "Stretch_00_tpl.neutralPoseMid";
connectAttr "IkTpl_00_ctr.tx" "Stretch_00_tpl.neutralPoseEnd";
connectAttr "StretchIkFact_00_fm.msg" "Stretch_00_tpl._relatedTo[0]";
connectAttr "StretchIk_00_pma.msg" "Stretch_00_tpl._relatedTo[1]";
connectAttr "AutoStretch_00_blcl.msg" "Stretch_00_tpl._relatedTo[2]";
connectAttr "Stretch_00_clp.msg" "Stretch_00_tpl._relatedTo[3]";
connectAttr "StretchFk_00_pma.msg" "Stretch_00_tpl._relatedTo[4]";
connectAttr "outputLink_00_pnc.ctx" "output_00_link.tx";
connectAttr "outputLink_00_pnc.cty" "output_00_link.ty";
connectAttr "outputLink_00_pnc.ctz" "output_00_link.tz";
connectAttr "outputLink_00_orc.crx" "output_00_link.rx";
connectAttr "outputLink_00_orc.cry" "output_00_link.ry";
connectAttr "outputLink_00_orc.crz" "output_00_link.rz";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Twist_00_ctr.rx" "unitConversion1.i";
connectAttr "Config_00_ctr.fkIk" "Config_00_rev.ix";
connectAttr "Twist_00_ctr.rx" "Twist_00_ucnv.i";
connectAttr "Ik_00_crvShape.ws" "Ik_00_mp.gp";
connectAttr "Aux_00_jnt.wm" "Ik_00_mp.wum";
connectAttr "Ik_00_crvShape.ws" "Ik_01_mp.gp";
connectAttr "Aux_01_jnt.wm" "Ik_01_mp.wum";
connectAttr "FrontTwist_00_ucnv.o" "Ik_01_mp.ft";
connectAttr "_00_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "_01_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "End_01_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "Ik.msg" "ControlsSet.dnsm" -na;
connectAttr "Fk.msg" "ControlsSet.dnsm" -na;
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "input_00_link.iog" "LinkSet.dsm" -na;
connectAttr "output_00_link.iog" "LinkSet.dsm" -na;
connectAttr "Pin_01_ctr.rx" "FrontTwist_00_ucnv.i";
connectAttr "Config_00_ctr.msg" "Config_00_tag.act";
connectAttr "Config_00_tag.msg" "Config_00_tag.child[0]";
connectAttr "Fk_00_ctr.msg" "Fk_00_tag.act";
connectAttr "Fk_01_tag.pare" "Fk_00_tag.child[0]";
connectAttr "Ik_00_ctr.msg" "Ik_00_tag.act";
connectAttr "Ik_00_tag.msg" "Ik_00_tag.child[0]";
connectAttr "Twist_00_ctr.msg" "Twist_00_tag.act";
connectAttr "Twist_00_tag.msg" "Twist_00_tag.child[0]";
connectAttr "Pin_01_ctr.msg" "Pin_01_tag.act";
connectAttr "Pin_01_tag.msg" "Pin_01_tag.child[0]";
connectAttr "Fk_01_ctr.msg" "Fk_01_tag.act";
connectAttr "Fk_02_tag.pare" "Fk_01_tag.child[0]";
connectAttr "Fk_02_ctr.msg" "Fk_02_tag.act";
connectAttr "Fk_02_tag.msg" "Fk_02_tag.child[0]";
connectAttr "Fk_00_ctr.iog" "Fk.dsm" -na;
connectAttr "Fk_01_ctr.iog" "Fk.dsm" -na;
connectAttr "Fk_02_ctr.iog" "Fk.dsm" -na;
connectAttr "Ik_00_ctr.iog" "Ik.dsm" -na;
connectAttr "StretchFk_00_mdv.ox" "StretchFk_00_pma.i2[0].i2x";
connectAttr "StretchFk_00_mdv.oy" "StretchFk_00_pma.i2[0].i2y";
connectAttr "StretchFk_00_pma.o2x" "Stretch_00_blcl.c2r";
connectAttr "StretchFk_00_pma.o2y" "Stretch_00_blcl.c2g";
connectAttr "Config_00_ctr.fkIk" "Stretch_00_blcl.b";
connectAttr "AutoStretch_00_blcl.opr" "Stretch_00_blcl.c1r";
connectAttr "AutoStretch_00_blcl.opg" "Stretch_00_blcl.c1g";
connectAttr "Config_00_ctr.autoStretch" "AutoStretch_00_blcl.b";
connectAttr "AntiPop_00_pma.o2x" "AutoStretch_00_blcl.c1r";
connectAttr "AntiPop_00_pma.o2y" "AutoStretch_00_blcl.c1g";
connectAttr "Stretch_00_clp.opr" "AntiPop_00_pma.i2[0].i2x";
connectAttr "Stretch_00_clp.opg" "AntiPop_00_pma.i2[0].i2y";
connectAttr "AntiPop_00_mdl.o" "AntiPop_00_pma.i2[1].i2x";
connectAttr "AntiPop_00_mdl.o" "AntiPop_00_pma.i2[1].i2y";
connectAttr "StretchIk_00_pma.o2x" "Stretch_00_clp.ipr";
connectAttr "StretchIk_00_pma.o2y" "Stretch_00_clp.ipg";
connectAttr "Fk_00_ctr.msg" "MetadataLimbSnapping.fkControls[0]";
connectAttr "Fk_01_ctr.msg" "MetadataLimbSnapping.fkControls[1]";
connectAttr "Fk_02_ctr.msg" "MetadataLimbSnapping.fkControls[2]";
connectAttr "Fk_00_snapper.msg" "MetadataLimbSnapping.fkSnappers[0]";
connectAttr "Fk_01_snapper.msg" "MetadataLimbSnapping.fkSnappers[1]";
connectAttr "Fk_02_snapper.msg" "MetadataLimbSnapping.fkSnappers[2]";
connectAttr "Twist_00_snapper.msg" "MetadataLimbSnapping.poleVSnapper";
connectAttr "Twist_00_ctr.msg" "MetadataLimbSnapping.poleVControl";
connectAttr "Ik_00_snapper.msg" "MetadataLimbSnapping.ikSnapper";
connectAttr "Config_00_ctr.msg" "MetadataLimbSnapping.switchControl";
connectAttr "Ik_00_ctr.msg" "MetadataLimbSnapping.ikControl";
connectAttr "Stretch_00_blcl.opr" "Stretch_00_mdv.i1x";
connectAttr "Stretch_00_blcl.opg" "Stretch_00_mdv.i1y";
connectAttr "Fk_01_ctr.tx" "StretchFk_00_mdv.i1x";
connectAttr "Fk_02_ctr.tx" "StretchFk_00_mdv.i1y";
connectAttr "StretchOrig_00_locShape.wp" "Stretch_00_dist.p1";
connectAttr "StretchEnd_00_locShape.wp" "Stretch_00_dist.p2";
connectAttr "StretchIkFact_00_fm.of" "StretchIkFact_00_mdl.i1";
connectAttr "Config_00_ctr.antiPop" "AntiPop_00_mdl.i1";
connectAttr "OrigSystemTpl_00_tr.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "IkTpl_00_root.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "IkTpl_00_ctr.msg" "MetadataTemplate._inputTemplate[2]";
connectAttr "FKTpl_00_root.msg" "MetadataTemplate._inputTemplate[3]";
connectAttr "FkTpl_00_ctr.msg" "MetadataTemplate._inputTemplate[4]";
connectAttr "FKTpl_01_root.msg" "MetadataTemplate._inputTemplate[5]";
connectAttr "FkTpl_01_ctr.msg" "MetadataTemplate._inputTemplate[6]";
connectAttr "FKTpl_02_root.msg" "MetadataTemplate._inputTemplate[7]";
connectAttr "FkTpl_02_ctr.msg" "MetadataTemplate._inputTemplate[8]";
connectAttr "Stretch_00_tpl.msg" "MetadataTemplate._inputTemplate[9]";
connectAttr "Config_00_tpl.msg" "MetadataTemplate._inputTemplate[10]";
connectAttr "IkPoleTpl_00_loc.msg" "MetadataTemplate._inputTemplate[11]";
connectAttr "StretchIkFact_00_mdl.o" "StretchIk_00_pma.i2[0].i2x";
connectAttr "StretchIkFact_00_mdl.o" "StretchIk_00_pma.i2[0].i2y";
connectAttr "Stretch_00_dist.d" "StretchIkFact_00_fm._fa";
connectAttr "Config_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Pin_01_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Twist_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "unitConversion1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Config_00_rev.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Twist_00_ucnv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "FrontTwist_00_ucnv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "StretchFk_00_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Stretch_00_blcl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "AutoStretch_00_blcl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "AntiPop_00_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Stretch_00_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "StretchIkFact_00_mdl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Stretch_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "StretchFk_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "AntiPop_00_mdl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "StretchIk_00_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "StretchIkFact_00_fm.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "remapValue1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
connectAttr "ikSCsolver.msg" ":ikSystem.sol" -na;
// End of RP2BonesAdvanced.ma
