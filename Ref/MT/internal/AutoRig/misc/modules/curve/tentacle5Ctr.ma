//Maya ASCII 2020 scene
//Name: tentacleControlFive.ma
//Last modified: Mon, Apr 11, 2022 01:24:05 PM
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
fileInfo "UUID" "1BD9DEB6-4136-11EB-6791-F6BD8294440C";
createNode transform -s -n "persp";
	rename -uid "410DB090-420F-E299-620C-8DAD4489DF89";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 15.847995545501039 4.1147242978013967 6.2581370743954752 ;
	setAttr ".r" -type "double3" 1790.0616472688243 -2445.7999999979033 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5E4AE4B8-4759-0117-56AC-EBB7DD429FA2";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 22.765366699684076;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" -2.2204460492503131e-16 -2.2204460492503131e-16 8 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "29C8D78F-4D3C-2FEC-37DB-77A0050482B4";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.025794374884024251 1000.1019942204044 1.9928244083428539 ;
	setAttr ".r" -type "double3" -90 -2.0187008844029305e-20 2.0187008844029305e-20 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "6BDF878A-4F7B-CB72-F7F2-819718B40649";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1019942204044;
	setAttr ".ow" 7.4947206600488059;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" -0.00023513083583283668 0 5.0005165679365735 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "338FF0FA-40EC-A10E-3C8D-2B95F64D03D7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.036453282950931198 -0.69800966914420925 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "71BAAAF4-4A32-6DE1-7200-29838F1DCE0E";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 3.1981116946523098;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "5D56E75D-4595-64C5-F142-D9941AA3C4B5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1267121135343 0.00079802294896268167 8.059179133378727 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "EA0D7E38-4B95-E6AA-422F-958EF70F8A95";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1267120762814;
	setAttr ".ow" 1.0526315789473684;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 3.7252902984619141e-08 -2.9802324191807728e-08 8.0583810806274414 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "Spl_00_grp";
	rename -uid "A95342E2-4D79-CEA4-73C5-0383886377C2";
	setAttr ".v" no;
createNode transform -n "Spl_00_crv" -p "Spl_00_grp";
	rename -uid "24DC475A-4416-A403-8410-24B24D8BBF88";
createNode nurbsCurve -n "Spl_00_crvShape" -p "Spl_00_crv";
	rename -uid "F1CCBA48-494F-87CC-30A0-96998D4536EA";
	setAttr -k off ".v";
	setAttr -s 5 ".cp";
	setAttr ".cc" -type "nurbsCurve" 
		2 3 0 no 3
		6 0 0 1 2 3 3
		5
		0 0 0
		0 8.3266726846886741e-17 2
		0 1.6653345369377348e-16 4
		0 2.4980018054066022e-16 6
		0 3.3306690738754696e-16 8
		;
createNode ikHandle -n "Spl_00_iksp" -p "Spl_00_grp";
	rename -uid "1F06E75E-4CF1-85A1-6E92-67913A1DD6EF";
	setAttr ".t" -type "double3" 0 0 8.0198261817999992 ;
	setAttr ".roc" yes;
	setAttr ".dwut" 4;
	setAttr ".dpa" 4;
	setAttr ".dwua" 6;
	setAttr ".dwuv" -type "double3" 1 0 0 ;
	setAttr ".dwve" -type "double3" 1 0 0 ;
	setAttr ".dwue" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 3.3306690738754696e-16 8 1;
createNode joint -n "Spl_00_jnt";
	rename -uid "06E6DB67-421B-BA4A-B3A1-B08AA8A8E8DF";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_01_jnt" -p "Spl_00_jnt";
	rename -uid "94AEFB45-40A7-6AD9-EAC1-ADB92083DAC1";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.99879024000000016 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_02_jnt" -p "Spl_01_jnt";
	rename -uid "DAC7C0AA-411A-EEDB-EFD2-459AF3EB2670";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.0003211900000011 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_03_jnt" -p "Spl_02_jnt";
	rename -uid "CF273E43-4424-C584-988D-52BD23294950";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.9979990000000001 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_04_jnt" -p "Spl_03_jnt";
	rename -uid "15DF506E-4E86-7C3C-2B70-20A7108B2B55";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_05_jnt" -p "Spl_04_jnt";
	rename -uid "D6D3559F-4CFA-3768-1D1E-0990086839F9";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 5.0002000099999995 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_06_jnt" -p "Spl_05_jnt";
	rename -uid "0F6DD5C3-4D0A-28F6-FA70-DF98A72C8E42";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 5.9996788100000007 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_07_jnt" -p "Spl_06_jnt";
	rename -uid "61EA7D72-483D-0082-1899-A1AFBC575A09";
	setAttr ".t" -type "double3" 0 0 1 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 7.00017041 1;
	setAttr ".radi" 0.2;
createNode joint -n "Spl_08_jnt" -p "Spl_07_jnt";
	rename -uid "EB73A32B-4B13-AA9E-212D-88AD24067305";
	setAttr ".t" -type "double3" 0 0 0.99982959000000005 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 8 1;
	setAttr ".radi" 0.2;
createNode joint -n "SplEnd_08_jnt" -p "Spl_08_jnt";
	rename -uid "9BCE655A-4E1D-C633-AFA1-6089528F0CCF";
	setAttr ".t" -type "double3" 0 0 0.019996591800000001 ;
	setAttr ".radi" 0.2;
createNode ikEffector -n "effector1" -p "Spl_08_jnt";
	rename -uid "145B2EA2-4D93-6DEA-0D7C-53A8CFB53F22";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode joint -n "SplTwist_08_jnt" -p "Spl_08_jnt";
	rename -uid "26967A62-44AA-EAE8-E80C-4EB5C27F9EA0";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 8 1;
	setAttr ".radi" 0.59999999999999987;
createNode scaleConstraint -n "SplTwist_08_jnt_scaleConstraint1" -p "SplTwist_08_jnt";
	rename -uid "8868F9F4-4A33-FE3A-1433-68BEB113133E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_04_ctrW0" -dv 1 -min 0 -at "double";
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
createNode orientConstraint -n "SplTwist_08_jnt_orientConstraint1" -p "SplTwist_08_jnt";
	rename -uid "58FB6153-43B0-10ED-5262-C78504493EE6";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_04_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "SplTwist_07_jnt" -p "Spl_07_jnt";
	rename -uid "00E7B28D-49CE-95F0-A6F8-848478F5A181";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 7.00017041 1;
	setAttr ".radi" 0.59999999999999987;
createNode orientConstraint -n "SplTwist_07_jnt_orientConstraint1" -p "SplTwist_07_jnt";
	rename -uid "15F25D78-4B17-D229-CDCE-9CA46E65A5F6";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_03_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_04_ctrW1" -dv 1 -min 0 -at "double";
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
createNode scaleConstraint -n "SplTwist_07_jnt_scaleConstraint1" -p "SplTwist_07_jnt";
	rename -uid "8A556039-47B9-6FF3-77B2-D69E85F5952B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_03_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_04_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "SplTwist_06_jnt" -p "Spl_06_jnt";
	rename -uid "036FDF35-43D7-F6C7-5DAF-229D1DB951AE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 5.9996788100000007 1;
	setAttr ".radi" 0.59999999999999987;
createNode scaleConstraint -n "SplTwist_06_jnt_scaleConstraint1" -p "SplTwist_06_jnt";
	rename -uid "EFDAB1B0-41A6-13F2-4EA8-A096DAA8C17E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_03_ctrW0" -dv 1 -min 0 -at "double";
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
createNode orientConstraint -n "SplTwist_06_jnt_orientConstraint1" -p "SplTwist_06_jnt";
	rename -uid "62E88256-436E-2D04-B50F-C2BF1857E1C9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_03_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "SplTwist_05_jnt" -p "Spl_05_jnt";
	rename -uid "7E2F20AB-4FA2-9B54-B119-B4B288AA7A1E";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 5.0002000099999995 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode orientConstraint -n "SplTwist_05_jnt_orientConstraint1" -p "SplTwist_05_jnt";
	rename -uid "44DFB4A1-4B42-E0DF-7CAE-FB9D45DEDA03";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_02_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_03_ctrW1" -dv 1 -min 0 -at "double";
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
createNode scaleConstraint -n "SplTwist_05_jnt_scaleConstraint1" -p "SplTwist_05_jnt";
	rename -uid "0617442E-46A7-059C-D1A1-94BE4BE6562B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_02_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_03_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "SplTwist_04_jnt" -p "Spl_04_jnt";
	rename -uid "F4351FB1-40B9-D86D-23BE-EF8B37684457";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 4 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode scaleConstraint -n "SplTwist_04_jnt_scaleConstraint1" -p "SplTwist_04_jnt";
	rename -uid "6248A32C-458C-71FF-48E2-EBA12C9700F2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_02_ctrW0" -dv 1 -min 0 -at "double";
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
createNode orientConstraint -n "SplTwist_04_jnt_orientConstraint1" -p "SplTwist_04_jnt";
	rename -uid "E99DC3F8-48A3-9C94-4052-27BD61ACAFF5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_02_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "SplTwist_03_jnt" -p "Spl_03_jnt";
	rename -uid "EA106B42-48C7-6408-BEFE-4E98859B346D";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.9979990000000001 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode orientConstraint -n "SplTwist_03_jnt_orientConstraint1" -p "SplTwist_03_jnt";
	rename -uid "6C982351-4611-008F-050F-9D8D8D5A87F6";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_01_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_02_ctrW1" -dv 1 -min 0 -at "double";
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
createNode scaleConstraint -n "SplTwist_03_jnt_scaleConstraint1" -p "SplTwist_03_jnt";
	rename -uid "06C83D8E-44AB-1E8E-7E89-A583EC89D713";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_01_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_02_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "SplTwist_02_jnt" -p "Spl_02_jnt";
	rename -uid "F64BC6EA-4DAC-6966-8152-F7BB0FC7FD36";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 2.0003211900000011 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode scaleConstraint -n "SplTwist_02_jnt_scaleConstraint1" -p "SplTwist_02_jnt";
	rename -uid "2B692F4A-499A-E077-94E4-549CB9693E5D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_01_ctrW0" -dv 1 -min 0 -at "double";
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
createNode orientConstraint -n "SplTwist_02_jnt_orientConstraint1" -p "SplTwist_02_jnt";
	rename -uid "AC13D2A1-4637-B043-2A47-9C8D54FCE553";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_01_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "SplTwist_01_jnt" -p "Spl_01_jnt";
	rename -uid "48D014FC-4B8F-D978-B2A6-4887ACDFBB69";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0.99879024000000016 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode orientConstraint -n "SplTwist_01_jnt_orientConstraint1" -p "SplTwist_01_jnt";
	rename -uid "11B535F3-4D0B-C5C4-8919-13857FB2790B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_00_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_01_ctrW1" -dv 1 -min 0 -at "double";
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
createNode scaleConstraint -n "SplTwist_01_jnt_scaleConstraint1" -p "SplTwist_01_jnt";
	rename -uid "0F9AF5E8-4BC1-BE15-E033-6287E7205A7A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_00_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "SplLocal_01_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode joint -n "SplTwist_00_jnt" -p "Spl_00_jnt";
	rename -uid "CBF9F66C-4184-2963-4106-2C995440AB01";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.59999999999999987;
	setAttr ".liw" yes;
createNode scaleConstraint -n "SplTwist_00_jnt_scaleConstraint1" -p "SplTwist_00_jnt";
	rename -uid "3E8CF9DF-478B-72CA-6516-248F0FB41D76";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode orientConstraint -n "SplTwist_00_jnt_orientConstraint1" -p "SplTwist_00_jnt";
	rename -uid "18E2095C-4BA1-B99E-23D7-0A9FD36D7FCA";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplLocal_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode transform -n "SplFk_00_root";
	rename -uid "ED62EBE8-4A22-3C7C-4A47-C5AFC0A98683";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplFk_00_ctr" -p "SplFk_00_root";
	rename -uid "E8748713-4B2C-FF12-26FF-45931E0B6D10";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "SplFk_00_ctrShape" -p "SplFk_00_ctr";
	rename -uid "A58B43CA-4D63-EA8F-47B4-369F6CB1DE2E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		-1.5876215189611809 8.2302579895899048e-17 0
		-1.1226179420151394 -1.1226179420151394 0
		-1.5903313337841668e-16 -1.5876215189611818 0
		1.1226179420151394 -1.1226179420151394 0
		1.5876215189611809 -2.1650338598677999e-16 0
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		;
createNode transform -n "SplFk_01_root" -p "SplFk_00_ctr";
	rename -uid "B1B8CD62-4807-F5D2-30F0-B1B227022B2C";
	setAttr ".t" -type "double3" 0 1.6653345369377348e-16 2.0003211498260498 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplFk_01_ctr" -p "SplFk_01_root";
	rename -uid "00156E98-48BC-F228-1433-EF9A183AFFC5";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "SplFk_01_ctrShape" -p "SplFk_01_ctr";
	rename -uid "9081DA35-4602-114C-6A82-6F9B98D49B3C";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		-1.5876215189611809 8.2302579895899048e-17 0
		-1.1226179420151394 -1.1226179420151394 0
		-1.5903313337841668e-16 -1.5876215189611818 0
		1.1226179420151394 -1.1226179420151394 0
		1.5876215189611809 -2.1650338598677999e-16 0
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		;
createNode transform -n "SplFk_02_root" -p "SplFk_01_ctr";
	rename -uid "E3D114A0-4707-9C2E-15B0-EAAFA78FB176";
	setAttr ".t" -type "double3" 0 1.6653345369377348e-16 1.9996788501739502 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplFk_02_ctr" -p "SplFk_02_root";
	rename -uid "0EE8D49C-496E-8A8C-4E0E-969F099B7726";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "SplFk_02_ctrShape" -p "SplFk_02_ctr";
	rename -uid "FCC4D16E-40BE-DDB3-A8A9-EFA42AE75AE8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		-1.5876215189611809 8.2302579895899048e-17 0
		-1.1226179420151394 -1.1226179420151394 0
		-1.5903313337841668e-16 -1.5876215189611818 0
		1.1226179420151394 -1.1226179420151394 0
		1.5876215189611809 -2.1650338598677999e-16 0
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		;
createNode transform -n "SplFk_03_root" -p "SplFk_02_ctr";
	rename -uid "C388BD49-4FE0-CE91-F7A4-6F93E5D032FC";
	setAttr ".t" -type "double3" 0 0 1.9996786117553711 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplFk_03_ctr" -p "SplFk_03_root";
	rename -uid "6EE837C8-4397-24D9-C186-8996C569AEAC";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 6;
createNode nurbsCurve -n "SplFk_03_ctrShape" -p "SplFk_03_ctr";
	rename -uid "1CDCFA28-44C0-07C5-5B28-D8A964632A8F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		-1.5876215189611809 8.2302579895899048e-17 0
		-1.1226179420151394 -1.1226179420151394 0
		-1.5903313337841668e-16 -1.5876215189611818 0
		1.1226179420151394 -1.1226179420151394 0
		1.5876215189611809 -2.1650338598677999e-16 0
		1.1226179420151394 1.1226179420151399 0
		9.7213780572663606e-17 1.5876215189611804 0
		-1.1226179420151394 1.1226179420151394 0
		;
createNode transform -n "SplTwist_00_root" -p "SplFk_03_ctr";
	rename -uid "7AF3B975-4939-2A0B-55CB-B18F1D66972E";
	setAttr ".t" -type "double3" -2.9891294389188952e-16 1.8614986695115368e-16 2.0003213882446289 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplTwist_00_ctr" -p "SplTwist_00_root";
	rename -uid "0DA3E58E-47CE-D7AD-4F24-C7BF74BEC606";
	addAttr -ci true -sn "autoStretch" -ln "autoStretch" -min 0 -max 1 -at "double";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".autoStretch";
createNode nurbsCurve -n "SplTwist_00_ctrShape" -p "SplTwist_00_ctr";
	rename -uid "A0A56C20-430F-556F-0FE4-91863CF053D6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		1.561806440353394 -2.2204460492503131e-16 0
		9.5633062794040079e-17 1.5618064385686317 0
		1.1102230246251565e-16 1.5618064403533931 0
		-1.5618064385686317 8.0964321569747708e-17 0
		-1.5618064403533931 0 0
		-1.5644721911975322e-16 -1.5618064385686323 0
		-1.1102230246251565e-16 -1.561806440353394 0
		1.5618064385686317 -2.1298299258838056e-16 0
		1.561806440353394 -2.2204460492503131e-16 0
		9.5633062794040079e-17 1.5618064385686317 0
		1.1102230246251565e-16 1.5618064403533931 0
		;
createNode transform -n "SplLocal_04_root" -p "SplTwist_00_ctr";
	rename -uid "CEE7F317-41DD-374B-E650-AD8594881AA9";
	setAttr ".t" -type "double3" 2.9891294389188952e-16 -1.8614986695115368e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplLocal_04_ctr" -p "SplLocal_04_root";
	rename -uid "6A9DAE90-409F-9101-45FF-5189725D824C";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
createNode nurbsCurve -n "SplLocal_04_ctrShape" -p "SplLocal_04_ctr";
	rename -uid "D679C62E-493C-C7A4-05FC-D6BA3746DD9A";
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
createNode locator -n "Spl_04_locShape" -p "SplLocal_04_ctr";
	rename -uid "BB3AFEFD-49F9-59E9-03E7-028614483145";
	setAttr -k off ".v" no;
createNode transform -n "SplLocal_03_root" -p "SplFk_03_ctr";
	rename -uid "B61CD148-4ACD-F4C5-02F5-CC8A8816C0D4";
	setAttr ".t" -type "double3" 0 -8.3266726846886741e-17 0.00032138824462890625 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplLocal_03_ctr" -p "SplLocal_03_root";
	rename -uid "F46F420E-4ADC-05AA-1F87-19889106EB62";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
createNode nurbsCurve -n "SplLocal_03_ctrShape" -p "SplLocal_03_ctr";
	rename -uid "BBCD45E6-4E76-84B8-894F-CAA5B3048D38";
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
createNode locator -n "Spl_03_locShape" -p "SplLocal_03_ctr";
	rename -uid "6AF4D31C-4A7B-94ED-FBC0-29A1C84AD00D";
	setAttr -k off ".v" no;
createNode transform -n "SplLocal_02_root" -p "SplFk_02_ctr";
	rename -uid "E71075C5-41DF-A29F-5A9C-D1AC940B8D5C";
	setAttr ".t" -type "double3" 0 -1.6653345369377348e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplLocal_02_ctr" -p "SplLocal_02_root";
	rename -uid "9E7861E7-428D-1009-ECF8-BDA6502D0704";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
createNode nurbsCurve -n "SplLocal_02_ctrShape" -p "SplLocal_02_ctr";
	rename -uid "9AE2163E-48B8-D620-31DA-9EA45FD9184D";
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
createNode locator -n "Spl_02_locShape" -p "SplLocal_02_ctr";
	rename -uid "947978BB-46A7-242F-D1D2-1498A5E45223";
	setAttr -k off ".v" no;
createNode transform -n "SplLocal_01_root" -p "SplFk_01_ctr";
	rename -uid "389EC2BA-4949-D2A9-7849-9E9C07B1D5D4";
	setAttr ".t" -type "double3" 0 -8.3266726846886741e-17 -0.00032114982604980469 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplLocal_01_ctr" -p "SplLocal_01_root";
	rename -uid "DB3A3633-4AD8-B0BA-37F0-969891FCB68F";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
createNode nurbsCurve -n "SplLocal_01_ctrShape" -p "SplLocal_01_ctr";
	rename -uid "BC443977-4CA9-682F-8DAB-A99DC673604C";
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
createNode locator -n "Spl_01_locShape" -p "SplLocal_01_ctr";
	rename -uid "F94AE22B-4860-DA03-F42D-D989613064DD";
	setAttr -k off ".v" no;
createNode transform -n "SplLocal_00_root";
	rename -uid "6EF579F5-43C6-3061-755B-E885048AE40A";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "SplLocal_00_ctr" -p "SplLocal_00_root";
	rename -uid "FF13A244-4B39-3E96-C6A5-F5AB4BC80BFD";
	setAttr -l on -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
createNode nurbsCurve -n "SplLocal_00_ctrShape" -p "SplLocal_00_ctr";
	rename -uid "F0F6C3BD-4560-F582-878C-FE8AA191CB28";
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
createNode locator -n "Spl_00_locShape" -p "SplLocal_00_ctr";
	rename -uid "6E5F900B-4EB8-5799-2927-21AD52D8EDB6";
	setAttr -k off ".v" no;
createNode scaleConstraint -n "SplLocal_00_root_scaleConstraint1" -p "SplLocal_00_root";
	rename -uid "CDF5F352-4035-6CC4-20F2-BE9A5535CA34";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SplFk_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode transform -n "tentacle_00_geo";
	rename -uid "EAF3D078-4212-D68A-313C-4FBACCFCD9AE";
	setAttr ".t" -type "double3" 0 0 4 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" 90.000000000000028 0 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "tentacle_00_geoShape" -p "tentacle_00_geo";
	rename -uid "D821F54B-44B2-28E0-F9F8-F0847AEC25EB";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.5 0.84375 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 1;
	setAttr ".vcs" 2;
createNode mesh -n "tentacle_00_geoShape1Orig" -p "tentacle_00_geo";
	rename -uid "733BE325-4AF4-5CE6-C99A-BD840C3D6D1F";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 453 ".uvst[0].uvsp";
	setAttr ".uvst[0].uvsp[0:249]" -type "float2" 0.53682846 0.11942154 0.5 0.10416669
		 0.46317154 0.11942154 0.44791669 0.15625 0.46317154 0.19307846 0.5 0.20833331 0.53682846
		 0.19307849 0.55208331 0.15625 0.57365692 0.082593054 0.5 0.052083343 0.42634305 0.082593054
		 0.39583334 0.15625 0.42634305 0.22990695 0.5 0.26041666 0.57365698 0.22990695 0.60416669
		 0.15625 0.61048543 0.04576458 0.5 1.4901161e-08 0.38951457 0.04576458 0.34375 0.15625
		 0.38951457 0.26673543 0.5 0.3125 0.61048543 0.26673543 0.65625 0.15625 0.375 0.3125
		 0.40625 0.3125 0.4375 0.3125 0.46875 0.3125 0.5 0.3125 0.53125 0.3125 0.5625 0.3125
		 0.59375 0.3125 0.625 0.3125 0.375 0.35949248 0.40625 0.35949248 0.4375 0.35949248
		 0.46875 0.35949248 0.5 0.35949248 0.53125 0.35949248 0.5625 0.35949248 0.59375 0.35949248
		 0.625 0.35949248 0.375 0.40648496 0.40625 0.40648496 0.4375 0.40648496 0.46875 0.40648496
		 0.5 0.40648496 0.53125 0.40648496 0.5625 0.40648496 0.59375 0.40648496 0.625 0.40648496
		 0.375 0.45347744 0.40625 0.45347744 0.4375 0.45347744 0.46875 0.45347744 0.5 0.45347744
		 0.53125 0.45347744 0.5625 0.45347744 0.59375 0.45347744 0.625 0.45347744 0.375 0.50046992
		 0.40625 0.50046992 0.4375 0.50046992 0.46875 0.50046992 0.5 0.50046992 0.53125 0.50046992
		 0.5625 0.50046992 0.59375 0.50046992 0.625 0.50046992 0.375 0.5474624 0.40625 0.5474624
		 0.4375 0.5474624 0.46875 0.5474624 0.5 0.5474624 0.53125 0.5474624 0.5625 0.5474624
		 0.59375 0.5474624 0.625 0.5474624 0.375 0.59445488 0.40625 0.59445488 0.4375 0.59445488
		 0.46875 0.59445488 0.5 0.59445488 0.53125 0.59445488 0.5625 0.59445488 0.59375 0.59445488
		 0.625 0.59445488 0.375 0.64144737 0.40625 0.64144737 0.4375 0.64144737 0.46875 0.64144737
		 0.5 0.64144737 0.53125 0.64144737 0.5625 0.64144737 0.59375 0.64144737 0.625 0.64144737
		 0.375 0.68843985 0.40625 0.68843985 0.4375 0.68843985 0.46875 0.68843985 0.5 0.68843985
		 0.53125 0.68843985 0.5625 0.68843985 0.59375 0.68843985 0.625 0.68843985 0.61048543
		 0.73326457 0.5 0.6875 0.38951457 0.73326457 0.34375 0.84375 0.38951457 0.95423543
		 0.5 1 0.61048543 0.95423543 0.65625 0.84375 0.57365692 0.77009308 0.5 0.73958337
		 0.42634305 0.77009308 0.39583334 0.84375 0.42634305 0.91740692 0.5 0.94791663 0.57365698
		 0.91740692 0.60416669 0.84375 0.53682846 0.80692154 0.5 0.79166669 0.46317154 0.80692154
		 0.44791669 0.84375 0.46317154 0.88057846 0.5 0.89583331 0.53682846 0.88057852 0.55208331
		 0.84375 0.5 0.15000001 0.5 0.83749998 0.5 0.3125 0.53125 0.3125 0.53125 0.35949248
		 0.5 0.35949248 0.53125 0.3125 0.5625 0.3125 0.5625 0.35949248 0.53125 0.35949248
		 0.5 0.35949248 0.53125 0.35949248 0.53125 0.40648496 0.5 0.40648496 0.53125 0.35949248
		 0.5625 0.35949248 0.5625 0.40648496 0.53125 0.40648496 0.5 0.40648496 0.53125 0.40648496
		 0.53125 0.45347744 0.5 0.45347744 0.53125 0.40648496 0.5625 0.40648496 0.5625 0.45347744
		 0.53125 0.45347744 0.5 0.45347744 0.53125 0.45347744 0.53125 0.50046992 0.5 0.50046992
		 0.53125 0.45347744 0.5625 0.45347744 0.5625 0.50046992 0.53125 0.50046992 0.5 0.50046992
		 0.53125 0.50046992 0.53125 0.5474624 0.5 0.5474624 0.53125 0.50046992 0.5625 0.50046992
		 0.5625 0.5474624 0.53125 0.5474624 0.5 0.5474624 0.53125 0.5474624 0.53125 0.59445488
		 0.5 0.59445488 0.53125 0.5474624 0.5625 0.5474624 0.5625 0.59445488 0.53125 0.59445488
		 0.5 0.59445488 0.53125 0.59445488 0.53125 0.64144737 0.5 0.64144737 0.53125 0.59445488
		 0.5625 0.59445488 0.5625 0.64144737 0.53125 0.64144737 0.5 0.64144737 0.53125 0.64144737
		 0.53125 0.68843985 0.5 0.68843985 0.53125 0.64144737 0.5625 0.64144737 0.5625 0.68843985
		 0.53125 0.68843985 0.5 0.3125 0.53125 0.3125 0.53125 0.35949248 0.5 0.35949248 0.5625
		 0.3125 0.5625 0.35949248 0.53125 0.40648496 0.5 0.40648496 0.5625 0.40648496 0.53125
		 0.45347744 0.5 0.45347744 0.5625 0.45347744 0.53125 0.50046992 0.5 0.50046992 0.5625
		 0.50046992 0.53125 0.5474624 0.5 0.5474624 0.5625 0.5474624 0.53125 0.59445488 0.5
		 0.59445488 0.5625 0.59445488 0.53125 0.64144737 0.5 0.64144737 0.5625 0.64144737
		 0.53125 0.68843985 0.5 0.68843985 0.5625 0.68843985 0.53125 0.3125 0.53125 0.35949248
		 0.5 0.35949248 0.53125 0.35949248 0.53125 0.35949248 0.5625 0.35949248 0.53125 0.40648496
		 0.5 0.40648496 0.53125 0.40648496 0.53125 0.40648496 0.5625 0.40648496 0.53125 0.45347744
		 0.5 0.45347744 0.53125 0.45347744 0.53125 0.45347744 0.5625 0.45347744 0.53125 0.50046992
		 0.5 0.50046992 0.53125 0.50046992 0.53125 0.50046992 0.5625 0.50046992 0.53125 0.5474624
		 0.5 0.5474624 0.53125 0.5474624 0.53125 0.5474624 0.5625 0.5474624 0.53125 0.59445488
		 0.5 0.59445488;
	setAttr ".uvst[0].uvsp[250:452]" 0.53125 0.59445488 0.53125 0.59445488 0.5625
		 0.59445488 0.53125 0.64144737 0.5 0.64144737 0.53125 0.64144737 0.53125 0.64144737
		 0.5625 0.64144737 0.53125 0.68843985 0.5 0.3125 0.53125 0.3125 0.53125 0.3125 0.53125
		 0.35949248 0.53125 0.35949248 0.5 0.35949248 0.5 0.35949248 0.5 0.3125 0.53125 0.3125
		 0.5625 0.3125 0.53125 0.3125 0.5625 0.3125 0.5625 0.35949248 0.5625 0.35949248 0.53125
		 0.35949248 0.53125 0.35949248 0.53125 0.35949248 0.53125 0.3125 0.53125 0.3125 0.53125
		 0.35949248 0.5 0.35949248 0.53125 0.35949248 0.53125 0.35949248 0.5 0.35949248 0.53125
		 0.35949248 0.53125 0.40648496 0.53125 0.35949248 0.53125 0.40648496 0.5 0.40648496
		 0.5 0.40648496 0.5 0.35949248 0.5 0.35949248 0.53125 0.35949248 0.5625 0.35949248
		 0.5625 0.35949248 0.53125 0.35949248 0.5625 0.35949248 0.5625 0.40648496 0.5625 0.35949248
		 0.5625 0.40648496 0.53125 0.40648496 0.53125 0.40648496 0.53125 0.40648496 0.53125
		 0.35949248 0.53125 0.35949248 0.53125 0.40648496 0.5 0.40648496 0.53125 0.40648496
		 0.53125 0.40648496 0.5 0.40648496 0.53125 0.40648496 0.53125 0.45347744 0.53125 0.40648496
		 0.53125 0.45347744 0.5 0.45347744 0.5 0.45347744 0.5 0.40648496 0.5 0.40648496 0.53125
		 0.40648496 0.5625 0.40648496 0.5625 0.40648496 0.53125 0.40648496 0.5625 0.40648496
		 0.5625 0.45347744 0.5625 0.40648496 0.5625 0.45347744 0.53125 0.45347744 0.53125
		 0.45347744 0.53125 0.45347744 0.53125 0.40648496 0.53125 0.40648496 0.53125 0.45347744
		 0.5 0.45347744 0.53125 0.45347744 0.53125 0.45347744 0.5 0.45347744 0.53125 0.45347744
		 0.53125 0.50046992 0.53125 0.45347744 0.53125 0.50046992 0.5 0.50046992 0.5 0.50046992
		 0.5 0.45347744 0.5 0.45347744 0.53125 0.45347744 0.5625 0.45347744 0.5625 0.45347744
		 0.53125 0.45347744 0.5625 0.45347744 0.5625 0.50046992 0.5625 0.45347744 0.5625 0.50046992
		 0.53125 0.50046992 0.53125 0.50046992 0.53125 0.50046992 0.53125 0.45347744 0.53125
		 0.45347744 0.53125 0.50046992 0.5 0.50046992 0.53125 0.50046992 0.53125 0.50046992
		 0.5 0.50046992 0.53125 0.50046992 0.53125 0.5474624 0.53125 0.50046992 0.53125 0.5474624
		 0.5 0.5474624 0.5 0.5474624 0.5 0.50046992 0.5 0.50046992 0.53125 0.50046992 0.5625
		 0.50046992 0.5625 0.50046992 0.53125 0.50046992 0.5625 0.50046992 0.5625 0.5474624
		 0.5625 0.50046992 0.5625 0.5474624 0.53125 0.5474624 0.53125 0.5474624 0.53125 0.5474624
		 0.53125 0.50046992 0.53125 0.50046992 0.53125 0.5474624 0.5 0.5474624 0.53125 0.5474624
		 0.53125 0.5474624 0.5 0.5474624 0.53125 0.5474624 0.53125 0.59445488 0.53125 0.5474624
		 0.53125 0.59445488 0.5 0.59445488 0.5 0.59445488 0.5 0.5474624 0.5 0.5474624 0.53125
		 0.5474624 0.5625 0.5474624 0.5625 0.5474624 0.53125 0.5474624 0.5625 0.5474624 0.5625
		 0.59445488 0.5625 0.5474624 0.5625 0.59445488 0.53125 0.59445488 0.53125 0.59445488
		 0.53125 0.59445488 0.53125 0.5474624 0.53125 0.5474624 0.53125 0.59445488 0.5 0.59445488
		 0.53125 0.59445488 0.53125 0.59445488 0.5 0.59445488 0.53125 0.59445488 0.53125 0.64144737
		 0.53125 0.59445488 0.53125 0.64144737 0.5 0.64144737 0.5 0.64144737 0.5 0.59445488
		 0.5 0.59445488 0.53125 0.59445488 0.5625 0.59445488 0.5625 0.59445488 0.53125 0.59445488
		 0.5625 0.59445488 0.5625 0.64144737 0.5625 0.59445488 0.5625 0.64144737 0.53125 0.64144737
		 0.53125 0.64144737 0.53125 0.64144737 0.53125 0.59445488 0.53125 0.59445488 0.53125
		 0.64144737 0.5 0.64144737 0.53125 0.64144737 0.53125 0.64144737 0.5 0.64144737 0.53125
		 0.64144737 0.53125 0.68843985 0.53125 0.64144737 0.53125 0.68843985 0.5 0.68843985
		 0.5 0.68843985 0.5 0.64144737 0.5 0.64144737 0.5625 0.64144737 0.53125 0.64144737
		 0.5625 0.64144737 0.53125 0.68843985 0.53125 0.64144737 0.53125 0.68843985;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 25 ".pt";
	setAttr ".pt[80]" -type "float3" 5.5879354e-09 -0.08007779 -1.8626451e-09 ;
	setAttr ".pt[81]" -type "float3" 2.220446e-16 -0.08007779 -5.5879354e-09 ;
	setAttr ".pt[82]" -type "float3" -5.5879354e-09 -0.08007779 -1.8626451e-09 ;
	setAttr ".pt[83]" -type "float3" -3.7252903e-09 -0.08007779 1.4658397e-16 ;
	setAttr ".pt[84]" -type "float3" -5.5879354e-09 -0.08007779 1.8626451e-09 ;
	setAttr ".pt[85]" -type "float3" 2.220446e-16 -0.08007779 5.5879354e-09 ;
	setAttr ".pt[86]" -type "float3" 5.5879354e-09 -0.08007779 1.8626451e-09 ;
	setAttr ".pt[87]" -type "float3" 3.7252903e-09 -0.08007779 1.4658397e-16 ;
	setAttr ".pt[88]" -type "float3" 3.7252903e-09 -0.008947162 -3.7252903e-09 ;
	setAttr ".pt[89]" -type "float3" 4.4408921e-16 -0.008947162 -3.7252903e-09 ;
	setAttr ".pt[90]" -type "float3" -3.7252903e-09 -0.008947162 -3.7252903e-09 ;
	setAttr ".pt[91]" -type "float3" 3.7252903e-09 -0.008947162 2.686712e-16 ;
	setAttr ".pt[92]" -type "float3" -3.7252903e-09 -0.008947162 3.7252903e-09 ;
	setAttr ".pt[93]" -type "float3" 4.4408921e-16 -0.008947162 3.7252903e-09 ;
	setAttr ".pt[94]" -type "float3" 3.7252903e-09 -0.008947162 3.7252903e-09 ;
	setAttr ".pt[95]" -type "float3" -3.7252903e-09 -0.008947162 2.686712e-16 ;
	setAttr ".pt[96]" -type "float3" 4.2840838e-08 0.032285757 -4.0978193e-08 ;
	setAttr ".pt[97]" -type "float3" 3.5527137e-15 0.032285757 -4.8428774e-08 ;
	setAttr ".pt[98]" -type "float3" -3.7252903e-08 0.032285757 -4.0978193e-08 ;
	setAttr ".pt[99]" -type "float3" -3.1664968e-08 0.032285757 4.3077142e-16 ;
	setAttr ".pt[100]" -type "float3" -3.7252903e-08 0.032285757 4.0978193e-08 ;
	setAttr ".pt[101]" -type "float3" 3.5527137e-15 0.032285757 4.8428774e-08 ;
	setAttr ".pt[102]" -type "float3" 4.2840838e-08 0.032285757 4.0978193e-08 ;
	setAttr ".pt[103]" -type "float3" 3.3527613e-08 0.032285757 4.3077142e-16 ;
	setAttr ".pt[105]" -type "float3" 2.6645353e-15 0.041688904 -1.3539256e-15 ;
	setAttr -s 234 ".vt";
	setAttr ".vt[0:165]"  0.23477313 -4 -0.23477313 2.3495483e-10 -4 -0.33201936
		 -0.23477313 -4 -0.23477313 -0.33201933 -4 1.174783e-10 -0.23477313 -4 0.23477313
		 2.3495483e-10 -4 0.33201936 0.23477314 -4 0.23477314 0.33201936 -4 1.174783e-10 0.46954626 -4 -0.46954626
		 2.3495483e-10 -4 -0.66403866 -0.46954626 -4 -0.46954626 -0.66403866 -4 1.174783e-10
		 -0.46954626 -4 0.46954626 2.3495483e-10 -4 0.66403866 0.46954629 -4 0.46954629 0.66403872 -4 1.174783e-10
		 0.70431936 -4 -0.70431936 2.3495483e-10 -4 -0.99605799 -0.70431936 -4 -0.70431936
		 -0.99605799 -4 1.174783e-10 -0.70431936 -4 0.70431936 2.3495483e-10 -4 0.99605805
		 0.70431942 -4 0.70431942 0.99605811 -4 1.174783e-10 0.63820922 -3 -0.63820922 5.8076246e-09 -3 -0.90256417
		 -0.63820922 -3 -0.63820922 -0.90256417 -3 2.9038112e-09 -0.63820922 -3 0.63820922
		 5.8076246e-09 -3 0.90256423 0.63820928 -3 0.63820928 0.90256429 -3 2.9038112e-09
		 0.57209915 -2 -0.57209909 1.138029e-08 -2 -0.80907035 -0.57209909 -2 -0.57209909
		 -0.80907035 -2 5.6901444e-09 -0.57209909 -2 0.57209915 1.138029e-08 -2 0.80907041
		 0.57209921 -2 0.57209915 0.80907047 -2 5.6901444e-09 0.50598902 -1 -0.50598902 1.6952956e-08 -1 -0.71557653
		 -0.50598902 -1 -0.50598902 -0.71557653 -1 8.4764764e-09 -0.50598902 -1 0.50598902
		 1.6952956e-08 -1 0.71557659 0.50598907 -1 0.50598907 0.71557665 -1 8.4764764e-09
		 0.43987894 0 -0.43987891 2.2525622e-08 0 -0.62208271 -0.43987888 0 -0.43987891 -0.62208271 0 1.1262812e-08
		 -0.43987888 0 0.43987894 2.2525622e-08 0 0.62208277 0.43987897 0 0.43987897 0.62208283 0 1.1262812e-08
		 0.37376881 1 -0.37376878 2.8098288e-08 1 -0.52858889 -0.37376878 1 -0.37376878 -0.52858889 1 1.4049146e-08
		 -0.37376878 1 0.37376881 2.8098288e-08 1 0.52858895 0.37376887 1 0.37376884 0.52858901 1 1.4049146e-08
		 0.3076587 2 -0.30765867 3.3670954e-08 2 -0.43509507 -0.30765864 2 -0.30765867 -0.43509507 2 1.6835477e-08
		 -0.30765864 2 0.3076587 3.3670954e-08 2 0.43509513 0.30765873 2 0.30765873 0.43509519 2 1.6835477e-08
		 0.2415486 3 -0.24154854 3.924362e-08 3 -0.34160125 -0.24154854 3 -0.24154854 -0.34160125 3 1.962181e-08
		 -0.24154854 3 0.2415486 3.924362e-08 3 0.34160131 0.24154863 3 0.2415486 0.34160137 3 1.962181e-08
		 0.17543852 4 -0.1754384 4.4816286e-08 4 -0.24810743 -0.1754384 4 -0.1754384 -0.24810737 4 2.2408143e-08
		 -0.1754384 4 0.17543846 4.4816286e-08 4 0.24810749 0.17543852 4 0.17543846 0.24810749 4 2.2408143e-08
		 0.11695904 4 -0.11695895 4.4816286e-08 4 -0.16540492 -0.11695892 4 -0.11695895 -0.16540492 4 2.2408143e-08
		 -0.11695892 4 0.11695901 4.4816286e-08 4 0.16540498 0.11695904 4 0.11695901 0.16540504 4 2.2408143e-08
		 0.058479533 4 -0.058479458 4.4816286e-08 4 -0.082702458 -0.058479443 4 -0.058479458
		 -0.082702458 4 2.2408143e-08 -0.058479443 4 0.058479518 4.4816286e-08 4 0.082702518
		 0.058479533 4 0.058479518 0.082702547 4 2.2408143e-08 2.3495483e-10 -4 1.174783e-10
		 4.4816286e-08 4 2.2408143e-08 -0.64906752 -3.89312029 0.7172128 -0.050396059 -3.89121914 0.96501297
		 -0.050396055 -3.11152077 0.89211601 -0.59287393 -3.11324334 0.66757524 0.050396059 -3.89121914 0.96501297
		 0.64906758 -3.89312005 0.71721286 0.59287399 -3.11324334 0.6675753 0.050396062 -3.11152077 0.89211601
		 -0.5879178 -2.89312911 0.64904881 -0.045440003 -2.89140654 0.87358958 -0.045439996 -2.11170816 0.8006925
		 -0.53172421 -2.1132524 0.59941131 0.045440018 -2.89140654 0.87358958 0.58791786 -2.89312911 0.64904886
		 0.53172433 -2.1132524 0.59941131 0.045440026 -2.11170816 0.80069262 -0.52676845 -1.89314699 0.58088559
		 -0.040484145 -1.89160299 0.78216678 -0.040484145 -1.11190462 0.70926982 -0.47057486 -1.11327028 0.53124809
		 0.040484175 -1.89160299 0.7821669 0.52676845 -1.89314699 0.58088565 0.47057492 -1.11327028 0.53124821
		 0.040484183 -1.11190462 0.70926982 -0.46561921 -0.89317465 0.51272327 -0.035528526 -0.89180899 0.690745
		 -0.035528518 -0.11211109 0.61784798 -0.40942562 -0.11329794 0.46308577 0.035528556 -0.89180899 0.69074506
		 0.46561927 -0.89317465 0.51272333 0.40942571 -0.11329794 0.4630858 0.035528563 -0.11211061 0.61784798
		 -0.40447026 0.10678577 0.4445619 -0.030573159 0.1079731 0.59932417 -0.030573154 0.88767147 0.52642721
		 -0.34827664 0.88666248 0.39492434 0.030573204 0.1079731 0.59932417 0.40447029 0.10678577 0.44456187
		 0.34827673 0.88666248 0.39492437 0.03057321 0.88767147 0.52642715 -0.34332159 1.10673332 0.3764016
		 -0.025618091 1.10774231 0.50790435 -0.025618088 1.88744068 0.43500739 -0.28712794 1.88661003 0.32676408
		 0.025618153 1.10774231 0.50790435 0.34332168 1.10673332 0.37640163 0.28712803 1.88661003 0.32676411
		 0.025618156 1.88744068 0.43500739 -0.28217325 2.10666466 0.30824265 -0.020663382 2.10749435 0.41648597
		 -0.020663377 2.88719273 0.34358901 -0.22597969 2.88654137 0.25860512 0.02066345 2.10749435 0.41648597
		 0.28217334 2.10666466 0.30824268 0.22597975 2.88654137 0.25860512 0.020663453 2.88719273 0.34358901
		 -0.22102538 3.10657787 0.24008521 -0.015709084 3.10722923 0.32506907 -0.01570908 3.8869276 0.25217211
		 -0.16483176 3.88645458 0.19044769;
	setAttr ".vt[166:233]" 0.015709165 3.10722923 0.32506907 0.22102547 3.10657787 0.24008524
		 0.16483188 3.88645458 0.19044772 0.015709169 3.8869276 0.25217211 -0.67278683 -3.8877666 0.77447641
		 -0.07411541 -3.88586545 1.022276521 -0.07411541 -3.10616684 0.94937962 -0.61659324 -3.10788965 0.72483885
		 0.074115403 -3.88586545 1.022276521 0.67278689 -3.88776636 0.77447647 0.6165933 -3.10788965 0.72483891
		 0.07411541 -3.10616684 0.94937962 -0.61163712 -2.88777542 0.70631242 -0.069159359 -2.88605285 0.93085319
		 -0.069159351 -2.10635448 0.85795611 -0.55544353 -2.10789871 0.65667492 0.069159374 -2.88605285 0.93085319
		 0.61163718 -2.88777542 0.70631248 0.55544364 -2.10789871 0.65667492 0.069159381 -2.10635448 0.85795623
		 -0.55048776 -1.88779306 0.6381492 -0.064203486 -1.88624907 0.83943039 -0.064203486 -1.10655069 0.76653343
		 -0.49429423 -1.10791636 0.58851171 0.064203516 -1.88624907 0.83943051 0.55048776 -1.88779306 0.63814926
		 0.49429423 -1.10791636 0.58851182 0.064203523 -1.10655069 0.76653343 -0.48933852 -0.88782072 0.56998688
		 -0.059247866 -0.88645506 0.74800861 -0.059247859 -0.10675716 0.67511159 -0.43314493 -0.10794401 0.52034932
		 0.059247896 -0.88645506 0.74800867 0.48933858 -0.88782072 0.56998694 0.43314505 -0.10794401 0.52034938
		 0.059247904 -0.10675669 0.67511159 -0.42818964 0.1121397 0.50182545 -0.054292507 0.11332703 0.65658778
		 -0.054292504 0.8930254 0.58369082 -0.37199602 0.89201641 0.4521879 0.05429256 0.11332703 0.65658778
		 0.42818967 0.1121397 0.50182545 0.3719961 0.89201641 0.45218793 0.05429256 0.8930254 0.58369076
		 -0.36704096 1.11208725 0.43366516 -0.049337454 1.11309624 0.56516796 -0.04933745 1.89279461 0.49227095
		 -0.31084731 1.89196396 0.38402763 0.049337506 1.11309624 0.56516796 0.36704105 1.11208725 0.43366519
		 0.3108474 1.89196396 0.38402766 0.04933751 1.89279461 0.49227095 -0.30589256 2.11201859 0.3655062
		 -0.044382714 2.11284828 0.47374952 -0.044382706 2.89254665 0.40085256 -0.24969903 2.89189529 0.31586868
		 0.044382781 2.11284828 0.47374952 0.30589265 2.11201859 0.36550623 0.24969909 2.89189529 0.31586868
		 0.044382781 2.89254665 0.40085256 -0.24474472 3.1119318 0.29734877 -0.039428428 3.11258316 0.38233262
		 -0.039428424 3.89228153 0.30943567 -0.1885511 3.89180851 0.24771124 0.039428506 3.11258316 0.38233262
		 0.24474481 3.1119318 0.2973488 0.18855122 3.89180851 0.24771127 0.03942851 3.89228153 0.30943567;
	setAttr -s 472 ".ed";
	setAttr ".ed[0:165]"  0 1 1 1 2 1 2 3 1 3 4 1 4 5 1 5 6 1 6 7 1 7 0 1 8 9 1
		 9 10 1 10 11 1 11 12 1 12 13 1 13 14 1 14 15 1 15 8 1 16 17 0 17 18 0 18 19 0 19 20 0
		 20 21 0 21 22 0 22 23 0 23 16 0 24 25 1 25 26 1 26 27 1 27 28 1 28 29 1 29 30 1 30 31 1
		 31 24 1 32 33 1 33 34 1 34 35 1 35 36 1 36 37 1 37 38 1 38 39 1 39 32 1 40 41 1 41 42 1
		 42 43 1 43 44 1 44 45 1 45 46 1 46 47 1 47 40 1 48 49 1 49 50 1 50 51 1 51 52 1 52 53 1
		 53 54 1 54 55 1 55 48 1 56 57 1 57 58 1 58 59 1 59 60 1 60 61 1 61 62 1 62 63 1 63 56 1
		 64 65 1 65 66 1 66 67 1 67 68 1 68 69 1 69 70 1 70 71 1 71 64 1 72 73 1 73 74 1 74 75 1
		 75 76 1 76 77 1 77 78 1 78 79 1 79 72 1 80 81 0 81 82 0 82 83 0 83 84 0 84 85 0 85 86 0
		 86 87 0 87 80 0 88 89 1 89 90 1 90 91 1 91 92 1 92 93 1 93 94 1 94 95 1 95 88 1 96 97 1
		 97 98 1 98 99 1 99 100 1 100 101 1 101 102 1 102 103 1 103 96 1 0 8 1 1 9 1 2 10 1
		 3 11 1 4 12 1 5 13 1 6 14 1 7 15 1 8 16 1 9 17 1 10 18 1 11 19 1 12 20 1 13 21 1
		 14 22 1 15 23 1 16 24 0 17 25 0 18 26 0 19 27 0 20 28 0 21 29 0 22 30 0 23 31 0 24 32 0
		 25 33 0 26 34 0 27 35 0 28 36 0 29 37 0 30 38 0 31 39 0 32 40 0 33 41 0 34 42 0 35 43 0
		 36 44 0 37 45 0 38 46 0 39 47 0 40 48 0 41 49 0 42 50 0 43 51 0 44 52 0 45 53 0 46 54 0
		 47 55 0 48 56 0 49 57 0 50 58 0 51 59 0 52 60 0 53 61 0 54 62 0 55 63 0 56 64 0 57 65 0
		 58 66 0 59 67 0 60 68 0 61 69 0;
	setAttr ".ed[166:331]" 62 70 0 63 71 0 64 72 0 65 73 0 66 74 0 67 75 0 68 76 0
		 69 77 0 70 78 0 71 79 0 72 80 0 73 81 0 74 82 0 75 83 0 76 84 0 77 85 0 78 86 0 79 87 0
		 80 88 1 81 89 1 82 90 1 83 91 1 84 92 1 85 93 1 86 94 1 87 95 1 88 96 1 89 97 1 90 98 1
		 91 99 1 92 100 1 93 101 1 94 102 1 95 103 1 104 0 1 104 1 1 104 2 1 104 3 1 104 4 1
		 104 5 1 104 6 1 104 7 1 96 105 1 97 105 1 98 105 1 99 105 1 100 105 1 101 105 1 102 105 1
		 103 105 1 20 106 1 21 107 1 106 107 0 29 108 1 107 108 0 28 109 1 109 108 0 106 109 0
		 21 110 1 22 111 1 110 111 0 30 112 1 111 112 0 29 113 1 113 112 0 110 113 0 28 114 1
		 29 115 1 114 115 0 37 116 1 115 116 0 36 117 1 117 116 0 114 117 0 29 118 1 30 119 1
		 118 119 0 38 120 1 119 120 0 37 121 1 121 120 0 118 121 0 36 122 1 37 123 1 122 123 0
		 45 124 1 123 124 0 44 125 1 125 124 0 122 125 0 37 126 1 38 127 1 126 127 0 46 128 1
		 127 128 0 45 129 1 129 128 0 126 129 0 44 130 1 45 131 1 130 131 0 53 132 1 131 132 0
		 52 133 1 133 132 0 130 133 0 45 134 1 46 135 1 134 135 0 54 136 1 135 136 0 53 137 1
		 137 136 0 134 137 0 52 138 1 53 139 1 138 139 0 61 140 1 139 140 0 60 141 1 141 140 0
		 138 141 0 53 142 1 54 143 1 142 143 0 62 144 1 143 144 0 61 145 1 145 144 0 142 145 0
		 60 146 1 61 147 1 146 147 0 69 148 1 147 148 0 68 149 1 149 148 0 146 149 0 61 150 1
		 62 151 1 150 151 0 70 152 1 151 152 0 69 153 1 153 152 0 150 153 0 68 154 1 69 155 1
		 154 155 0 77 156 1 155 156 0 76 157 1 157 156 0 154 157 0 69 158 1 70 159 1 158 159 0
		 78 160 1 159 160 0 77 161 1 161 160 0 158 161 0 76 162 1 77 163 1 162 163 0 85 164 1;
	setAttr ".ed[332:471]" 163 164 0 84 165 1 165 164 0 162 165 0 77 166 1 78 167 1
		 166 167 0 86 168 1 167 168 0 85 169 1 169 168 0 166 169 0 106 170 0 107 171 0 170 171 0
		 108 172 0 171 172 0 109 173 0 173 172 0 170 173 0 110 174 0 111 175 0 174 175 0 112 176 0
		 175 176 0 113 177 0 177 176 0 174 177 0 114 178 0 115 179 0 178 179 0 116 180 0 179 180 0
		 117 181 0 181 180 0 178 181 0 118 182 0 119 183 0 182 183 0 120 184 0 183 184 0 121 185 0
		 185 184 0 182 185 0 122 186 0 123 187 0 186 187 0 124 188 0 187 188 0 125 189 0 189 188 0
		 186 189 0 126 190 0 127 191 0 190 191 0 128 192 0 191 192 0 129 193 0 193 192 0 190 193 0
		 130 194 0 131 195 0 194 195 0 132 196 0 195 196 0 133 197 0 197 196 0 194 197 0 134 198 0
		 135 199 0 198 199 0 136 200 0 199 200 0 137 201 0 201 200 0 198 201 0 138 202 0 139 203 0
		 202 203 0 140 204 0 203 204 0 141 205 0 205 204 0 202 205 0 142 206 0 143 207 0 206 207 0
		 144 208 0 207 208 0 145 209 0 209 208 0 206 209 0 146 210 0 147 211 0 210 211 0 148 212 0
		 211 212 0 149 213 0 213 212 0 210 213 0 150 214 0 151 215 0 214 215 0 152 216 0 215 216 0
		 153 217 0 217 216 0 214 217 0 154 218 0 155 219 0 218 219 0 156 220 0 219 220 0 157 221 0
		 221 220 0 218 221 0 158 222 0 159 223 0 222 223 0 160 224 0 223 224 0 161 225 0 225 224 0
		 222 225 0 162 226 0 163 227 0 226 227 0 164 228 0 227 228 0 165 229 0 229 228 0 226 229 0
		 166 230 0 167 231 0 230 231 0 168 232 0 231 232 0 169 233 0 233 232 0 230 233 0;
	setAttr -s 240 -ch 944 ".fc[0:239]" -type "polyFaces" 
		f 4 0 105 -9 -105
		mu 0 4 0 1 9 8
		f 4 1 106 -10 -106
		mu 0 4 1 2 10 9
		f 4 2 107 -11 -107
		mu 0 4 2 3 11 10
		f 4 3 108 -12 -108
		mu 0 4 3 4 12 11
		f 4 4 109 -13 -109
		mu 0 4 4 5 13 12
		f 4 5 110 -14 -110
		mu 0 4 5 6 14 13
		f 4 6 111 -15 -111
		mu 0 4 6 7 15 14
		f 4 7 104 -16 -112
		mu 0 4 7 0 8 15
		f 4 8 113 -17 -113
		mu 0 4 8 9 17 16
		f 4 9 114 -18 -114
		mu 0 4 9 10 18 17
		f 4 10 115 -19 -115
		mu 0 4 10 11 19 18
		f 4 11 116 -20 -116
		mu 0 4 11 12 20 19
		f 4 12 117 -21 -117
		mu 0 4 12 13 21 20
		f 4 13 118 -22 -118
		mu 0 4 13 14 22 21
		f 4 14 119 -23 -119
		mu 0 4 14 15 23 22
		f 4 15 112 -24 -120
		mu 0 4 15 8 16 23
		f 4 16 121 -25 -121
		mu 0 4 24 25 34 33
		f 4 17 122 -26 -122
		mu 0 4 25 26 35 34
		f 4 18 123 -27 -123
		mu 0 4 26 27 36 35
		f 4 19 124 -28 -124
		mu 0 4 27 28 37 36
		f 4 346 348 -351 -352
		mu 0 4 195 196 197 198
		f 4 354 356 -359 -360
		mu 0 4 222 199 200 223
		f 4 22 127 -31 -127
		mu 0 4 30 31 40 39
		f 4 23 120 -32 -128
		mu 0 4 31 32 41 40
		f 4 24 129 -33 -129
		mu 0 4 33 34 43 42
		f 4 25 130 -34 -130
		mu 0 4 34 35 44 43
		f 4 26 131 -35 -131
		mu 0 4 35 36 45 44
		f 4 27 132 -36 -132
		mu 0 4 36 37 46 45
		f 4 362 364 -367 -368
		mu 0 4 224 225 201 202
		f 4 370 372 -375 -376
		mu 0 4 226 227 203 228
		f 4 30 135 -39 -135
		mu 0 4 39 40 49 48
		f 4 31 128 -40 -136
		mu 0 4 40 41 50 49
		f 4 32 137 -41 -137
		mu 0 4 42 43 52 51
		f 4 33 138 -42 -138
		mu 0 4 43 44 53 52
		f 4 34 139 -43 -139
		mu 0 4 44 45 54 53
		f 4 35 140 -44 -140
		mu 0 4 45 46 55 54
		f 4 378 380 -383 -384
		mu 0 4 229 230 204 205
		f 4 386 388 -391 -392
		mu 0 4 231 232 206 233
		f 4 38 143 -47 -143
		mu 0 4 48 49 58 57
		f 4 39 136 -48 -144
		mu 0 4 49 50 59 58
		f 4 40 145 -49 -145
		mu 0 4 51 52 61 60
		f 4 41 146 -50 -146
		mu 0 4 52 53 62 61
		f 4 42 147 -51 -147
		mu 0 4 53 54 63 62
		f 4 43 148 -52 -148
		mu 0 4 54 55 64 63
		f 4 394 396 -399 -400
		mu 0 4 234 235 207 208
		f 4 402 404 -407 -408
		mu 0 4 236 237 209 238
		f 4 46 151 -55 -151
		mu 0 4 57 58 67 66
		f 4 47 144 -56 -152
		mu 0 4 58 59 68 67
		f 4 48 153 -57 -153
		mu 0 4 60 61 70 69
		f 4 49 154 -58 -154
		mu 0 4 61 62 71 70
		f 4 50 155 -59 -155
		mu 0 4 62 63 72 71
		f 4 51 156 -60 -156
		mu 0 4 63 64 73 72
		f 4 410 412 -415 -416
		mu 0 4 239 240 210 211
		f 4 418 420 -423 -424
		mu 0 4 241 242 212 243
		f 4 54 159 -63 -159
		mu 0 4 66 67 76 75
		f 4 55 152 -64 -160
		mu 0 4 67 68 77 76
		f 4 56 161 -65 -161
		mu 0 4 69 70 79 78
		f 4 57 162 -66 -162
		mu 0 4 70 71 80 79
		f 4 58 163 -67 -163
		mu 0 4 71 72 81 80
		f 4 59 164 -68 -164
		mu 0 4 72 73 82 81
		f 4 426 428 -431 -432
		mu 0 4 244 245 213 214
		f 4 434 436 -439 -440
		mu 0 4 246 247 215 248
		f 4 62 167 -71 -167
		mu 0 4 75 76 85 84
		f 4 63 160 -72 -168
		mu 0 4 76 77 86 85
		f 4 64 169 -73 -169
		mu 0 4 78 79 88 87
		f 4 65 170 -74 -170
		mu 0 4 79 80 89 88
		f 4 66 171 -75 -171
		mu 0 4 80 81 90 89
		f 4 67 172 -76 -172
		mu 0 4 81 82 91 90
		f 4 442 444 -447 -448
		mu 0 4 249 250 216 217
		f 4 450 452 -455 -456
		mu 0 4 251 252 218 253
		f 4 70 175 -79 -175
		mu 0 4 84 85 94 93
		f 4 71 168 -80 -176
		mu 0 4 85 86 95 94
		f 4 72 177 -81 -177
		mu 0 4 87 88 97 96
		f 4 73 178 -82 -178
		mu 0 4 88 89 98 97
		f 4 74 179 -83 -179
		mu 0 4 89 90 99 98
		f 4 75 180 -84 -180
		mu 0 4 90 91 100 99
		f 4 458 460 -463 -464
		mu 0 4 254 255 219 220
		f 4 466 468 -471 -472
		mu 0 4 256 257 221 258
		f 4 78 183 -87 -183
		mu 0 4 93 94 103 102
		f 4 79 176 -88 -184
		mu 0 4 94 95 104 103
		f 4 80 185 -89 -185
		mu 0 4 111 110 118 119
		f 4 81 186 -90 -186
		mu 0 4 110 109 117 118
		f 4 82 187 -91 -187
		mu 0 4 109 108 116 117
		f 4 83 188 -92 -188
		mu 0 4 108 107 115 116
		f 4 84 189 -93 -189
		mu 0 4 107 106 114 115
		f 4 85 190 -94 -190
		mu 0 4 106 105 113 114
		f 4 86 191 -95 -191
		mu 0 4 105 112 120 113
		f 4 87 184 -96 -192
		mu 0 4 112 111 119 120
		f 4 88 193 -97 -193
		mu 0 4 119 118 126 127
		f 4 89 194 -98 -194
		mu 0 4 118 117 125 126
		f 4 90 195 -99 -195
		mu 0 4 117 116 124 125
		f 4 91 196 -100 -196
		mu 0 4 116 115 123 124
		f 4 92 197 -101 -197
		mu 0 4 115 114 122 123
		f 4 93 198 -102 -198
		mu 0 4 114 113 121 122
		f 4 94 199 -103 -199
		mu 0 4 113 120 128 121
		f 4 95 192 -104 -200
		mu 0 4 120 119 127 128
		f 3 -1 -201 201
		mu 0 3 1 0 129
		f 3 -2 -202 202
		mu 0 3 2 1 129
		f 3 -3 -203 203
		mu 0 3 3 2 129
		f 3 -4 -204 204
		mu 0 3 4 3 129
		f 3 -5 -205 205
		mu 0 3 5 4 129
		f 3 -6 -206 206
		mu 0 3 6 5 129
		f 3 -7 -207 207
		mu 0 3 7 6 129
		f 3 -8 -208 200
		mu 0 3 0 7 129
		f 3 96 209 -209
		mu 0 3 127 126 130
		f 3 97 210 -210
		mu 0 3 126 125 130
		f 3 98 211 -211
		mu 0 3 125 124 130
		f 3 99 212 -212
		mu 0 3 124 123 130
		f 3 100 213 -213
		mu 0 3 123 122 130
		f 3 101 214 -214
		mu 0 3 122 121 130
		f 3 102 215 -215
		mu 0 3 121 128 130
		f 3 103 208 -216
		mu 0 3 128 127 130
		f 4 20 217 -219 -217
		mu 0 4 28 29 132 131
		f 4 125 219 -221 -218
		mu 0 4 29 38 133 132
		f 4 -29 221 222 -220
		mu 0 4 38 37 134 133
		f 4 -125 216 223 -222
		mu 0 4 37 28 131 134
		f 4 21 225 -227 -225
		mu 0 4 29 30 136 135
		f 4 126 227 -229 -226
		mu 0 4 30 39 137 136
		f 4 -30 229 230 -228
		mu 0 4 39 38 138 137
		f 4 -126 224 231 -230
		mu 0 4 38 29 135 138
		f 4 28 233 -235 -233
		mu 0 4 37 38 140 139
		f 4 133 235 -237 -234
		mu 0 4 38 47 141 140
		f 4 -37 237 238 -236
		mu 0 4 47 46 142 141
		f 4 -133 232 239 -238
		mu 0 4 46 37 139 142
		f 4 29 241 -243 -241
		mu 0 4 38 39 144 143
		f 4 134 243 -245 -242
		mu 0 4 39 48 145 144
		f 4 -38 245 246 -244
		mu 0 4 48 47 146 145
		f 4 -134 240 247 -246
		mu 0 4 47 38 143 146
		f 4 36 249 -251 -249
		mu 0 4 46 47 148 147
		f 4 141 251 -253 -250
		mu 0 4 47 56 149 148
		f 4 -45 253 254 -252
		mu 0 4 56 55 150 149
		f 4 -141 248 255 -254
		mu 0 4 55 46 147 150
		f 4 37 257 -259 -257
		mu 0 4 47 48 152 151
		f 4 142 259 -261 -258
		mu 0 4 48 57 153 152
		f 4 -46 261 262 -260
		mu 0 4 57 56 154 153
		f 4 -142 256 263 -262
		mu 0 4 56 47 151 154
		f 4 44 265 -267 -265
		mu 0 4 55 56 156 155
		f 4 149 267 -269 -266
		mu 0 4 56 65 157 156
		f 4 -53 269 270 -268
		mu 0 4 65 64 158 157
		f 4 -149 264 271 -270
		mu 0 4 64 55 155 158
		f 4 45 273 -275 -273
		mu 0 4 56 57 160 159
		f 4 150 275 -277 -274
		mu 0 4 57 66 161 160
		f 4 -54 277 278 -276
		mu 0 4 66 65 162 161
		f 4 -150 272 279 -278
		mu 0 4 65 56 159 162
		f 4 52 281 -283 -281
		mu 0 4 64 65 164 163
		f 4 157 283 -285 -282
		mu 0 4 65 74 165 164
		f 4 -61 285 286 -284
		mu 0 4 74 73 166 165
		f 4 -157 280 287 -286
		mu 0 4 73 64 163 166
		f 4 53 289 -291 -289
		mu 0 4 65 66 168 167
		f 4 158 291 -293 -290
		mu 0 4 66 75 169 168
		f 4 -62 293 294 -292
		mu 0 4 75 74 170 169
		f 4 -158 288 295 -294
		mu 0 4 74 65 167 170
		f 4 60 297 -299 -297
		mu 0 4 73 74 172 171
		f 4 165 299 -301 -298
		mu 0 4 74 83 173 172
		f 4 -69 301 302 -300
		mu 0 4 83 82 174 173
		f 4 -165 296 303 -302
		mu 0 4 82 73 171 174
		f 4 61 305 -307 -305
		mu 0 4 74 75 176 175
		f 4 166 307 -309 -306
		mu 0 4 75 84 177 176
		f 4 -70 309 310 -308
		mu 0 4 84 83 178 177
		f 4 -166 304 311 -310
		mu 0 4 83 74 175 178
		f 4 68 313 -315 -313
		mu 0 4 82 83 180 179
		f 4 173 315 -317 -314
		mu 0 4 83 92 181 180
		f 4 -77 317 318 -316
		mu 0 4 92 91 182 181
		f 4 -173 312 319 -318
		mu 0 4 91 82 179 182
		f 4 69 321 -323 -321
		mu 0 4 83 84 184 183
		f 4 174 323 -325 -322
		mu 0 4 84 93 185 184
		f 4 -78 325 326 -324
		mu 0 4 93 92 186 185
		f 4 -174 320 327 -326
		mu 0 4 92 83 183 186
		f 4 76 329 -331 -329
		mu 0 4 91 92 188 187
		f 4 181 331 -333 -330
		mu 0 4 92 101 189 188
		f 4 -85 333 334 -332
		mu 0 4 101 100 190 189
		f 4 -181 328 335 -334
		mu 0 4 100 91 187 190
		f 4 77 337 -339 -337
		mu 0 4 92 93 192 191
		f 4 182 339 -341 -338
		mu 0 4 93 102 193 192
		f 4 -86 341 342 -340
		mu 0 4 102 101 194 193
		f 4 -182 336 343 -342
		mu 0 4 101 92 191 194
		f 4 218 345 -347 -345
		mu 0 4 259 260 196 195
		f 4 220 347 -349 -346
		mu 0 4 261 262 197 196
		f 4 -223 349 350 -348
		mu 0 4 263 264 198 197
		f 4 -224 344 351 -350
		mu 0 4 265 266 195 198
		f 4 226 353 -355 -353
		mu 0 4 267 268 199 269
		f 4 228 355 -357 -354
		mu 0 4 270 271 200 199
		f 4 -231 357 358 -356
		mu 0 4 272 273 274 200
		f 4 -232 352 359 -358
		mu 0 4 275 276 277 278
		f 4 234 361 -363 -361
		mu 0 4 279 280 281 282
		f 4 236 363 -365 -362
		mu 0 4 283 284 201 285
		f 4 -239 365 366 -364
		mu 0 4 286 287 202 201
		f 4 -240 360 367 -366
		mu 0 4 288 289 290 202
		f 4 242 369 -371 -369
		mu 0 4 291 292 293 294
		f 4 244 371 -373 -370
		mu 0 4 295 296 203 297
		f 4 -247 373 374 -372
		mu 0 4 298 299 300 203
		f 4 -248 368 375 -374
		mu 0 4 301 302 303 304
		f 4 250 377 -379 -377
		mu 0 4 305 306 307 308
		f 4 252 379 -381 -378
		mu 0 4 309 310 204 311
		f 4 -255 381 382 -380
		mu 0 4 312 313 205 204
		f 4 -256 376 383 -382
		mu 0 4 314 315 316 205
		f 4 258 385 -387 -385
		mu 0 4 317 318 319 320
		f 4 260 387 -389 -386
		mu 0 4 321 322 206 323
		f 4 -263 389 390 -388
		mu 0 4 324 325 326 206
		f 4 -264 384 391 -390
		mu 0 4 327 328 329 330
		f 4 266 393 -395 -393
		mu 0 4 331 332 333 334
		f 4 268 395 -397 -394
		mu 0 4 335 336 207 337
		f 4 -271 397 398 -396
		mu 0 4 338 339 208 207
		f 4 -272 392 399 -398
		mu 0 4 340 341 342 208
		f 4 274 401 -403 -401
		mu 0 4 343 344 345 346
		f 4 276 403 -405 -402
		mu 0 4 347 348 209 349
		f 4 -279 405 406 -404
		mu 0 4 350 351 352 209
		f 4 -280 400 407 -406
		mu 0 4 353 354 355 356
		f 4 282 409 -411 -409
		mu 0 4 357 358 359 360
		f 4 284 411 -413 -410
		mu 0 4 361 362 210 363
		f 4 -287 413 414 -412
		mu 0 4 364 365 211 210
		f 4 -288 408 415 -414
		mu 0 4 366 367 368 211
		f 4 290 417 -419 -417
		mu 0 4 369 370 371 372
		f 4 292 419 -421 -418
		mu 0 4 373 374 212 375
		f 4 -295 421 422 -420
		mu 0 4 376 377 378 212
		f 4 -296 416 423 -422
		mu 0 4 379 380 381 382
		f 4 298 425 -427 -425
		mu 0 4 383 384 385 386
		f 4 300 427 -429 -426
		mu 0 4 387 388 213 389
		f 4 -303 429 430 -428
		mu 0 4 390 391 214 213
		f 4 -304 424 431 -430
		mu 0 4 392 393 394 214
		f 4 306 433 -435 -433
		mu 0 4 395 396 397 398
		f 4 308 435 -437 -434
		mu 0 4 399 400 215 401
		f 4 -311 437 438 -436
		mu 0 4 402 403 404 215
		f 4 -312 432 439 -438
		mu 0 4 405 406 407 408
		f 4 314 441 -443 -441
		mu 0 4 409 410 411 412
		f 4 316 443 -445 -442
		mu 0 4 413 414 216 415
		f 4 -319 445 446 -444
		mu 0 4 416 417 217 216
		f 4 -320 440 447 -446
		mu 0 4 418 419 420 217
		f 4 322 449 -451 -449
		mu 0 4 421 422 423 424
		f 4 324 451 -453 -450
		mu 0 4 425 426 218 427
		f 4 -327 453 454 -452
		mu 0 4 428 429 430 218
		f 4 -328 448 455 -454
		mu 0 4 431 432 433 434
		f 4 330 457 -459 -457
		mu 0 4 435 436 437 438
		f 4 332 459 -461 -458
		mu 0 4 439 440 219 441
		f 4 -335 461 462 -460
		mu 0 4 442 443 220 219
		f 4 -336 456 463 -462
		mu 0 4 444 445 446 220
		f 4 338 465 -467 -465
		mu 0 4 191 192 447 448
		f 4 340 467 -469 -466
		mu 0 4 192 193 221 449
		f 4 -343 469 470 -468
		mu 0 4 193 194 450 221
		f 4 -344 464 471 -470
		mu 0 4 194 191 451 452;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9D8F97A4-4C17-57DF-07B0-6C82E8CF5EBD";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "FD933BF2-43BB-454B-15C9-459B2C58C545";
	setAttr ".bsdt[0].bscd" -type "Int32Array" 0 ;
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "B7D6504F-462F-1DC3-9384-C191A5EDA686";
createNode displayLayerManager -n "layerManager";
	rename -uid "21EE790F-46FA-D2DF-DBC0-BDAD5D6C00C3";
createNode displayLayer -n "defaultLayer";
	rename -uid "29288208-4F89-018C-5D19-83AFF9216B00";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "9F9BAB14-477C-82C0-58EC-C78D98DA2C9D";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "4A61AA96-426A-5EC7-1B29-548D95A5792B";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "3E9E9823-4862-99BB-5E17-8684F28ECC7C";
	setAttr ".b" -type "string" (
		"// Maya Mel UI Configuration File.\n//\n//  This script is machine generated.  Edit at your own risk.\n//\n//\n\nglobal string $gMainPane;\nif (`paneLayout -exists $gMainPane`) {\n\n\tglobal int $gUseScenePanelConfig;\n\tint    $useSceneConfig = $gUseScenePanelConfig;\n\tint    $nodeEditorPanelVisible = stringArrayContains(\"nodeEditorPanel1\", `getPanel -vis`);\n\tint    $nodeEditorWorkspaceControlOpen = (`workspaceControl -exists nodeEditorPanel1Window` && `workspaceControl -q -visible nodeEditorPanel1Window`);\n\tint    $menusOkayInPanels = `optionVar -q allowMenusInPanels`;\n\tint    $nVisPanes = `paneLayout -q -nvp $gMainPane`;\n\tint    $nPanes = 0;\n\tstring $editorName;\n\tstring $panelName;\n\tstring $itemFilterName;\n\tstring $panelConfig;\n\n\t//\n\t//  get current state of the UI\n\t//\n\tsceneUIReplacement -update $gMainPane;\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Top View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Top View\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"top\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n"
		+ "            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n"
		+ "            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n"
		+ "\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Side View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Side View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"side\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n"
		+ "            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n"
		+ "            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n"
		+ "            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Front View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Front View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"front\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n"
		+ "            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n"
		+ "            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n"
		+ "            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1\n            -height 1\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"modelPanel\" (localizedPanelLabel(\"Persp View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tmodelPanel -edit -l (localizedPanelLabel(\"Persp View\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        modelEditor -e \n            -camera \"persp\" \n            -useInteractiveMode 0\n            -displayLights \"default\" \n            -displayAppearance \"smoothShaded\" \n            -activeOnly 0\n            -ignorePanZoom 0\n"
		+ "            -wireframeOnShaded 1\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 1\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 0\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1319\n            -height 708\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -docTag \"isolOutln_fromSeln\" \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 1\n            -showReferenceMembers 1\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n"
		+ "            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -isSet 0\n            -isSetMember 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -selectCommand \"print(\\\"\\\")\" \n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n"
		+ "            -renderFilterIndex 0\n            -selectionOrder \"chronological\" \n            -expandAttribute 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"Outliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"Outliner\")) -mbv $menusOkayInPanels  $panelName;\n\t\t$editorName = $panelName;\n        outlinerEditor -e \n            -showShapes 0\n            -showAssignedMaterials 0\n            -showTimeEditor 1\n            -showReferenceNodes 0\n            -showReferenceMembers 0\n            -showAttributes 0\n            -showConnected 0\n            -showAnimCurvesOnly 0\n            -showMuteInfo 0\n            -organizeByLayer 1\n            -organizeByClip 1\n            -showAnimLayerWeight 1\n            -autoExpandLayers 1\n            -autoExpand 0\n            -autoExpandAnimatedShapes 1\n            -showDagOnly 1\n"
		+ "            -showAssets 1\n            -showContainedOnly 1\n            -showPublishedAsConnected 0\n            -showParentContainers 0\n            -showContainerContents 1\n            -ignoreDagHierarchy 0\n            -expandConnections 0\n            -showUpstreamCurves 1\n            -showUnitlessCurves 1\n            -showCompounds 1\n            -showLeafs 1\n            -showNumericAttrsOnly 0\n            -highlightActive 1\n            -autoSelectNewObjects 0\n            -doNotSelectNewObjects 0\n            -dropIsParent 1\n            -transmitFilters 0\n            -setFilter \"defaultSetFilter\" \n            -showSetMembers 1\n            -allowMultiSelection 1\n            -alwaysToggleSelect 0\n            -directSelect 0\n            -displayMode \"DAG\" \n            -expandObjects 0\n            -setsIgnoreFilters 1\n            -containersIgnoreFilters 0\n            -editAttrName 0\n            -showAttrValues 0\n            -highlightSecondary 0\n            -showUVAttrsOnly 0\n            -showTextureNodesOnly 0\n            -attrAlphaOrder \"default\" \n"
		+ "            -animLayerFilterOptions \"allAffecting\" \n            -sortOrder \"none\" \n            -longNames 0\n            -niceNames 1\n            -showNamespace 1\n            -showPinIcons 0\n            -mapMotionTrails 0\n            -ignoreHiddenAttribute 0\n            -ignoreOutlinerColor 0\n            -renderFilterVisible 0\n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"graphEditor\" (localizedPanelLabel(\"Graph Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Graph Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n"
		+ "                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 1\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 1\n                -showCompounds 0\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 1\n                -doNotSelectNewObjects 0\n                -dropIsParent 1\n                -transmitFilters 1\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n"
		+ "                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 1\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"GraphEd\");\n            animCurveEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -showPlayRangeShades \"on\" \n                -lockPlayRangeShades \"off\" \n"
		+ "                -smoothness \"fine\" \n                -resultSamples 1\n                -resultScreenSamples 0\n                -resultUpdate \"delayed\" \n                -showUpstreamCurves 1\n                -stackedCurvesMin -1\n                -stackedCurvesMax 1\n                -stackedCurvesSpace 0.2\n                -preSelectionHighlight 0\n                -constrainDrag 0\n                -valueLinesToggle 0\n                -outliner \"graphEditor1OutlineEd\" \n                -highlightAffectedCurves 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dopeSheetPanel\" (localizedPanelLabel(\"Dope Sheet\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dope Sheet\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"OutlineEd\");\n            outlinerEditor -e \n                -showShapes 1\n                -showAssignedMaterials 0\n                -showTimeEditor 1\n"
		+ "                -showReferenceNodes 0\n                -showReferenceMembers 0\n                -showAttributes 1\n                -showConnected 1\n                -showAnimCurvesOnly 1\n                -showMuteInfo 0\n                -organizeByLayer 1\n                -organizeByClip 1\n                -showAnimLayerWeight 1\n                -autoExpandLayers 1\n                -autoExpand 0\n                -autoExpandAnimatedShapes 1\n                -showDagOnly 0\n                -showAssets 1\n                -showContainedOnly 0\n                -showPublishedAsConnected 0\n                -showParentContainers 0\n                -showContainerContents 0\n                -ignoreDagHierarchy 0\n                -expandConnections 1\n                -showUpstreamCurves 1\n                -showUnitlessCurves 0\n                -showCompounds 1\n                -showLeafs 1\n                -showNumericAttrsOnly 1\n                -highlightActive 0\n                -autoSelectNewObjects 0\n                -doNotSelectNewObjects 1\n"
		+ "                -dropIsParent 1\n                -transmitFilters 0\n                -setFilter \"0\" \n                -showSetMembers 0\n                -allowMultiSelection 1\n                -alwaysToggleSelect 0\n                -directSelect 0\n                -displayMode \"DAG\" \n                -expandObjects 0\n                -setsIgnoreFilters 1\n                -containersIgnoreFilters 0\n                -editAttrName 0\n                -showAttrValues 0\n                -highlightSecondary 0\n                -showUVAttrsOnly 0\n                -showTextureNodesOnly 0\n                -attrAlphaOrder \"default\" \n                -animLayerFilterOptions \"allAffecting\" \n                -sortOrder \"none\" \n                -longNames 0\n                -niceNames 1\n                -showNamespace 1\n                -showPinIcons 0\n                -mapMotionTrails 1\n                -ignoreHiddenAttribute 0\n                -ignoreOutlinerColor 0\n                -renderFilterVisible 0\n                $editorName;\n\n\t\t\t$editorName = ($panelName+\"DopeSheetEd\");\n"
		+ "            dopeSheetEditor -e \n                -displayValues 0\n                -snapTime \"integer\" \n                -snapValue \"none\" \n                -outliner \"dopeSheetPanel1OutlineEd\" \n                -showSummary 1\n                -showScene 0\n                -hierarchyBelow 0\n                -showTicks 1\n                -selectionWindow 0 0 0 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"timeEditorPanel\" (localizedPanelLabel(\"Time Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Time Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"clipEditorPanel\" (localizedPanelLabel(\"Trax Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Trax Editor\")) -mbv $menusOkayInPanels  $panelName;\n"
		+ "\n\t\t\t$editorName = clipEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 0 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"sequenceEditorPanel\" (localizedPanelLabel(\"Camera Sequencer\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Camera Sequencer\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = sequenceEditorNameFromPanel($panelName);\n            clipEditor -e \n                -displayValues 0\n                -snapTime \"none\" \n                -snapValue \"none\" \n                -initialized 0\n                -manageSequencer 1 \n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperGraphPanel\" (localizedPanelLabel(\"Hypergraph Hierarchy\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypergraph Hierarchy\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"HyperGraphEd\");\n            hyperGraph -e \n                -graphLayoutStyle \"hierarchicalLayout\" \n                -orientation \"horiz\" \n                -mergeConnections 0\n                -zoom 1\n                -animateTransition 0\n                -showRelationships 1\n                -showShapes 0\n                -showDeformers 0\n                -showExpressions 0\n                -showConstraints 0\n                -showConnectionFromSelected 0\n                -showConnectionToSelected 0\n                -showConstraintLabels 0\n                -showUnderworld 0\n                -showInvisible 0\n                -transitionFrames 1\n                -opaqueContainers 0\n                -freeform 0\n                -imagePosition 0 0 \n                -imageScale 1\n                -imageEnabled 0\n                -graphType \"DAG\" \n"
		+ "                -heatMapDisplay 0\n                -updateSelection 1\n                -updateNodeAdded 1\n                -useDrawOverrideColor 0\n                -limitGraphTraversal -1\n                -range 0 0 \n                -iconSize \"smallIcons\" \n                -showCachedConnections 0\n                $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"hyperShadePanel\" (localizedPanelLabel(\"Hypershade\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Hypershade\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"visorPanel\" (localizedPanelLabel(\"Visor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Visor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n"
		+ "\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"nodeEditorPanel\" (localizedPanelLabel(\"Node Editor\")) `;\n\tif ($nodeEditorPanelVisible || $nodeEditorWorkspaceControlOpen) {\n\t\tif (\"\" == $panelName) {\n\t\t\tif ($useSceneConfig) {\n\t\t\t\t$panelName = `scriptedPanel -unParent  -type \"nodeEditorPanel\" -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels `;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n"
		+ "                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\t}\n\t\t} else {\n\t\t\t$label = `panel -q -label $panelName`;\n\t\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Node Editor\")) -mbv $menusOkayInPanels  $panelName;\n\n\t\t\t$editorName = ($panelName+\"NodeEditorEd\");\n            nodeEditor -e \n                -allAttributes 0\n                -allNodes 0\n                -autoSizeNodes 1\n                -consistentNameSize 1\n                -createNodeCommand \"nodeEdCreateNodeCommand\" \n                -connectNodeOnCreation 0\n                -connectOnDrop 0\n"
		+ "                -copyConnectionsOnPaste 0\n                -connectionStyle \"bezier\" \n                -defaultPinnedState 0\n                -additiveGraphingMode 0\n                -settingsChangedCallback \"nodeEdSyncControls\" \n                -traversalDepthLimit -1\n                -keyPressCommand \"nodeEdKeyPressCommand\" \n                -nodeTitleMode \"name\" \n                -gridSnap 0\n                -gridVisibility 1\n                -crosshairOnEdgeDragging 0\n                -popupMenuScript \"nodeEdBuildPanelMenus\" \n                -showNamespace 1\n                -showShapes 1\n                -showSGShapes 0\n                -showTransforms 1\n                -useAssets 1\n                -syncedSelection 1\n                -extendToShapes 1\n                -editorMode \"default\" \n                -hasWatchpoint 0\n                $editorName;\n\t\t\tif (!$useSceneConfig) {\n\t\t\t\tpanel -e -l $label $panelName;\n\t\t\t}\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"createNodePanel\" (localizedPanelLabel(\"Create Node\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Create Node\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"polyTexturePlacementPanel\" (localizedPanelLabel(\"UV Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"UV Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"renderWindowPanel\" (localizedPanelLabel(\"Render View\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Render View\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"shapePanel\" (localizedPanelLabel(\"Shape Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tshapePanel -edit -l (localizedPanelLabel(\"Shape Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"posePanel\" (localizedPanelLabel(\"Pose Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tposePanel -edit -l (localizedPanelLabel(\"Pose Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynRelEdPanel\" (localizedPanelLabel(\"Dynamic Relationships\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Dynamic Relationships\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"relationshipPanel\" (localizedPanelLabel(\"Relationship Editor\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Relationship Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"referenceEditorPanel\" (localizedPanelLabel(\"Reference Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Reference Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"componentEditorPanel\" (localizedPanelLabel(\"Component Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Component Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"dynPaintScriptedPanelType\" (localizedPanelLabel(\"Paint Effects\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Paint Effects\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"scriptEditorPanel\" (localizedPanelLabel(\"Script Editor\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Script Editor\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"profilerPanel\" (localizedPanelLabel(\"Profiler Tool\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Profiler Tool\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n"
		+ "\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n"
		+ "                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n"
		+ "                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n"
		+ "                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n"
		+ "        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 0\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 1\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 1\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 0\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "C3AC798C-4007-2E51-F84E-3BA0E0FF3CE9";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ikSplineSolver -n "ikSplineSolver";
	rename -uid "4B235A2D-44B1-69E8-9B17-A0976EB5B900";
createNode curveInfo -n "Spl_00_cvinf";
	rename -uid "F0A49565-481A-985E-D796-519DF475CCBC";
createNode multiplyDivide -n "Spl_00_mdv";
	rename -uid "C2BDAEC7-4130-D477-2409-9E8AD4E24A61";
	setAttr ".op" 2;
	setAttr ".i2" -type "float3" 8 1 1 ;
createNode clamp -n "Spl_00_clp";
	rename -uid "ABB62E7C-486A-1262-E4DA-DA9F982449A4";
	setAttr ".mn" -type "float3" 1 -999 -999 ;
	setAttr ".mx" -type "float3" 999 999 999 ;
createNode multiplyDivide -n "SplTwist_00_mdv";
	rename -uid "372644A6-4949-EE67-096B-2FA937D69D4A";
	setAttr ".i2" -type "float3" 0.75 0.5 0.25 ;
createNode unitConversion -n "unitConversion1";
	rename -uid "95B24857-476F-E43B-598A-13A5A1EBDE53";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion2";
	rename -uid "1CDA766C-4B77-55AA-E6F1-BB8A13E46F23";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	rename -uid "D22C7C4F-48EA-DE72-5746-819BA2C9ECB5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion4";
	rename -uid "733373C6-445A-0CC1-1A2D-12A69F804395";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "multiplyDivide1";
	rename -uid "3D546E19-4FD3-0005-5C81-70AE779F50A0";
	setAttr ".op" 2;
	setAttr ".i1" -type "float3" 1 1 1 ;
createNode skinCluster -n "skinCluster1";
	rename -uid "E81A60AF-49CE-2944-5804-A7BAF4ADE2DC";
	setAttr ".skm" 1;
	setAttr -s 234 ".wl";
	setAttr ".wl[0:233].w"
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		1 8 1
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 0 1
		1 8 1
		1 0 1
		1 8 1
		1 8 1
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		1 8 1
		1 8 1
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		1 0 1
		1 0 1
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		1 0 1
		1 0 1
		1 8 1
		1 8 1
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		1 8 1
		1 8 1
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 7 0.75 8 0.25
		2 7 0.75 8 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 6 0.75 7 0.25
		2 6 0.75 7 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 5 0.75 6 0.25
		2 5 0.75 6 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 4 0.75 5 0.25
		2 4 0.75 5 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 3 0.75 4 0.25
		2 3 0.75 4 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 2 0.75 3 0.25
		2 2 0.75 3 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		1 0 1
		1 0 1
		2 1 0.75 2 0.25
		2 1 0.75 2 0.25
		1 0 1
		1 0 1;
	setAttr -s 9 ".pm";
	setAttr ".pm[0]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -8 1;
	setAttr ".pm[1]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -7.00017041 1;
	setAttr ".pm[2]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -5.9996788100000007 1;
	setAttr ".pm[3]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -5.0002000099999995 1;
	setAttr ".pm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -4 1;
	setAttr ".pm[5]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -2.9979990000000001 1;
	setAttr ".pm[6]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -2.0003211900000011 1;
	setAttr ".pm[7]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 -0.99879024000000016 1;
	setAttr ".pm[8]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 -4.4408920985006262e-16 1 0 0 -1 -4.4408920985006262e-16 0
		 0 0 4 1;
	setAttr -s 9 ".ma";
	setAttr -s 9 ".dpf[0:8]"  4 4 4 4 4 4 4 4 4;
	setAttr -s 9 ".lw";
	setAttr -s 9 ".lw";
	setAttr ".mi" 5;
	setAttr ".bm" 1;
	setAttr ".ucm" yes;
	setAttr -s 9 ".ifcl";
	setAttr -s 9 ".ifcl";
createNode tweak -n "tweak1";
	rename -uid "DF1C2CDB-406A-598F-CA16-19AE6E0C43D8";
createNode objectSet -n "skinCluster1Set";
	rename -uid "46494C25-4D06-CDE4-6336-6DB6E6B613F8";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "64E07D18-43E7-E0B1-16FE-899A7222507D";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "253B6C57-447F-B20A-5D1B-41A752157EAC";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	rename -uid "D23CC24C-49A8-8918-B072-59887201B92C";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "17CF1B6B-43D6-7112-A3AC-C2A7A82A4E1F";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "5BB8482E-4C16-B11B-9DF7-FE8FFFDC08AB";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose2";
	rename -uid "010FBB59-4ACA-60A8-4387-50A4FDAE499E";
	setAttr -s 18 ".wm";
	setAttr -s 18 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.99879024000000016 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 1.0015309500000009 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.997677809999999 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 1.0020009999999999 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 1.0002000099999995 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.99947880000000122 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 1.0004915999999993 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0.99982959000000005 0
		 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[13]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[14]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[15]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[16]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[17]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 18 ".m";
	setAttr -s 18 ".p";
	setAttr -s 18 ".g[0:17]" yes yes yes yes yes yes yes yes yes no no 
		no no no no no no no;
	setAttr ".bp" yes;
createNode blendColors -n "Spl_00_blcl";
	rename -uid "D835F709-4EB8-AC79-A040-BDA707DC51B5";
	setAttr ".c2" -type "float3" 1 0 0 ;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "80F38D90-41FE-B472-6F52-F5AED4987137";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -1266.5641368278959 -4446.1860894886913 ;
	setAttr ".tgi[0].vh" -type "double2" 184.8585462081308 -3729.4511965336983 ;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 6 ".u";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	addAttr -ci true -h true -sn "dss" -ln "defaultSurfaceShader" -dt "string";
	setAttr ".dss" -type "string" "lambert1";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
connectAttr "Spl_00_locShape.wp" "Spl_00_crvShape.cp[0]";
connectAttr "Spl_01_locShape.wp" "Spl_00_crvShape.cp[1]";
connectAttr "Spl_02_locShape.wp" "Spl_00_crvShape.cp[2]";
connectAttr "Spl_03_locShape.wp" "Spl_00_crvShape.cp[3]";
connectAttr "Spl_04_locShape.wp" "Spl_00_crvShape.cp[4]";
connectAttr "Spl_00_jnt.msg" "Spl_00_iksp.hsj";
connectAttr "effector1.hp" "Spl_00_iksp.hee";
connectAttr "ikSplineSolver.msg" "Spl_00_iksp.hsv";
connectAttr "Spl_00_crvShape.ws" "Spl_00_iksp.ic";
connectAttr "SplTwist_00_ctr.rz" "Spl_00_iksp.twi";
connectAttr "Spl_00_blcl.opr" "Spl_00_jnt.sz";
connectAttr "Spl_00_jnt.s" "Spl_01_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_01_jnt.sz";
connectAttr "Spl_01_jnt.s" "Spl_02_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_02_jnt.sz";
connectAttr "Spl_02_jnt.s" "Spl_03_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_03_jnt.sz";
connectAttr "Spl_03_jnt.s" "Spl_04_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_04_jnt.sz";
connectAttr "Spl_04_jnt.s" "Spl_05_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_05_jnt.sz";
connectAttr "Spl_05_jnt.s" "Spl_06_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_06_jnt.sz";
connectAttr "Spl_06_jnt.s" "Spl_07_jnt.is";
connectAttr "Spl_00_blcl.opr" "Spl_07_jnt.sz";
connectAttr "Spl_07_jnt.s" "Spl_08_jnt.is";
connectAttr "SplEnd_08_jnt.tx" "effector1.tx";
connectAttr "SplEnd_08_jnt.ty" "effector1.ty";
connectAttr "SplEnd_08_jnt.tz" "effector1.tz";
connectAttr "SplEnd_08_jnt.opm" "effector1.opm";
connectAttr "SplTwist_08_jnt_orientConstraint1.crz" "SplTwist_08_jnt.rz";
connectAttr "SplTwist_08_jnt_scaleConstraint1.csx" "SplTwist_08_jnt.sx";
connectAttr "SplTwist_08_jnt_scaleConstraint1.csy" "SplTwist_08_jnt.sy";
connectAttr "SplTwist_08_jnt_scaleConstraint1.csz" "SplTwist_08_jnt.sz";
connectAttr "SplTwist_08_jnt.pim" "SplTwist_08_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_04_ctr.s" "SplTwist_08_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_04_ctr.pm" "SplTwist_08_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_08_jnt_scaleConstraint1.w0" "SplTwist_08_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_08_jnt.ro" "SplTwist_08_jnt_orientConstraint1.cro";
connectAttr "SplTwist_08_jnt.pim" "SplTwist_08_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_08_jnt.jo" "SplTwist_08_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_08_jnt.is" "SplTwist_08_jnt_orientConstraint1.is";
connectAttr "SplLocal_04_ctr.r" "SplTwist_08_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_04_ctr.ro" "SplTwist_08_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_04_ctr.pm" "SplTwist_08_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_08_jnt_orientConstraint1.w0" "SplTwist_08_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_07_jnt_orientConstraint1.crz" "SplTwist_07_jnt.rz";
connectAttr "SplTwist_07_jnt_scaleConstraint1.csx" "SplTwist_07_jnt.sx";
connectAttr "SplTwist_07_jnt_scaleConstraint1.csy" "SplTwist_07_jnt.sy";
connectAttr "SplTwist_07_jnt_scaleConstraint1.csz" "SplTwist_07_jnt.sz";
connectAttr "SplTwist_07_jnt.ro" "SplTwist_07_jnt_orientConstraint1.cro";
connectAttr "SplTwist_07_jnt.pim" "SplTwist_07_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_07_jnt.jo" "SplTwist_07_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_07_jnt.is" "SplTwist_07_jnt_orientConstraint1.is";
connectAttr "SplLocal_03_ctr.r" "SplTwist_07_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_03_ctr.ro" "SplTwist_07_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_07_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_07_jnt_orientConstraint1.w0" "SplTwist_07_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_04_ctr.r" "SplTwist_07_jnt_orientConstraint1.tg[1].tr";
connectAttr "SplLocal_04_ctr.ro" "SplTwist_07_jnt_orientConstraint1.tg[1].tro";
connectAttr "SplLocal_04_ctr.pm" "SplTwist_07_jnt_orientConstraint1.tg[1].tpm";
connectAttr "SplTwist_07_jnt_orientConstraint1.w1" "SplTwist_07_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_07_jnt.pim" "SplTwist_07_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_03_ctr.s" "SplTwist_07_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_07_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_07_jnt_scaleConstraint1.w0" "SplTwist_07_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_04_ctr.s" "SplTwist_07_jnt_scaleConstraint1.tg[1].ts";
connectAttr "SplLocal_04_ctr.pm" "SplTwist_07_jnt_scaleConstraint1.tg[1].tpm";
connectAttr "SplTwist_07_jnt_scaleConstraint1.w1" "SplTwist_07_jnt_scaleConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_06_jnt_orientConstraint1.crz" "SplTwist_06_jnt.rz";
connectAttr "SplTwist_06_jnt_scaleConstraint1.csx" "SplTwist_06_jnt.sx";
connectAttr "SplTwist_06_jnt_scaleConstraint1.csy" "SplTwist_06_jnt.sy";
connectAttr "SplTwist_06_jnt_scaleConstraint1.csz" "SplTwist_06_jnt.sz";
connectAttr "SplTwist_06_jnt.pim" "SplTwist_06_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_03_ctr.s" "SplTwist_06_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_06_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_06_jnt_scaleConstraint1.w0" "SplTwist_06_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_06_jnt.ro" "SplTwist_06_jnt_orientConstraint1.cro";
connectAttr "SplTwist_06_jnt.pim" "SplTwist_06_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_06_jnt.jo" "SplTwist_06_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_06_jnt.is" "SplTwist_06_jnt_orientConstraint1.is";
connectAttr "SplLocal_03_ctr.r" "SplTwist_06_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_03_ctr.ro" "SplTwist_06_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_06_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_06_jnt_orientConstraint1.w0" "SplTwist_06_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_05_jnt_orientConstraint1.crz" "SplTwist_05_jnt.rz";
connectAttr "SplTwist_05_jnt_scaleConstraint1.csx" "SplTwist_05_jnt.sx";
connectAttr "SplTwist_05_jnt_scaleConstraint1.csy" "SplTwist_05_jnt.sy";
connectAttr "SplTwist_05_jnt_scaleConstraint1.csz" "SplTwist_05_jnt.sz";
connectAttr "SplTwist_05_jnt.ro" "SplTwist_05_jnt_orientConstraint1.cro";
connectAttr "SplTwist_05_jnt.pim" "SplTwist_05_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_05_jnt.jo" "SplTwist_05_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_05_jnt.is" "SplTwist_05_jnt_orientConstraint1.is";
connectAttr "SplLocal_02_ctr.r" "SplTwist_05_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_02_ctr.ro" "SplTwist_05_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_05_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_05_jnt_orientConstraint1.w0" "SplTwist_05_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_03_ctr.r" "SplTwist_05_jnt_orientConstraint1.tg[1].tr";
connectAttr "SplLocal_03_ctr.ro" "SplTwist_05_jnt_orientConstraint1.tg[1].tro";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_05_jnt_orientConstraint1.tg[1].tpm";
connectAttr "SplTwist_05_jnt_orientConstraint1.w1" "SplTwist_05_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_05_jnt.pim" "SplTwist_05_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_02_ctr.s" "SplTwist_05_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_05_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_05_jnt_scaleConstraint1.w0" "SplTwist_05_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_03_ctr.s" "SplTwist_05_jnt_scaleConstraint1.tg[1].ts";
connectAttr "SplLocal_03_ctr.pm" "SplTwist_05_jnt_scaleConstraint1.tg[1].tpm";
connectAttr "SplTwist_05_jnt_scaleConstraint1.w1" "SplTwist_05_jnt_scaleConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_04_jnt_orientConstraint1.crz" "SplTwist_04_jnt.rz";
connectAttr "SplTwist_04_jnt_scaleConstraint1.csx" "SplTwist_04_jnt.sx";
connectAttr "SplTwist_04_jnt_scaleConstraint1.csy" "SplTwist_04_jnt.sy";
connectAttr "SplTwist_04_jnt_scaleConstraint1.csz" "SplTwist_04_jnt.sz";
connectAttr "SplTwist_04_jnt.pim" "SplTwist_04_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_02_ctr.s" "SplTwist_04_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_04_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_04_jnt_scaleConstraint1.w0" "SplTwist_04_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_04_jnt.ro" "SplTwist_04_jnt_orientConstraint1.cro";
connectAttr "SplTwist_04_jnt.pim" "SplTwist_04_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_04_jnt.jo" "SplTwist_04_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_04_jnt.is" "SplTwist_04_jnt_orientConstraint1.is";
connectAttr "SplLocal_02_ctr.r" "SplTwist_04_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_02_ctr.ro" "SplTwist_04_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_04_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_04_jnt_orientConstraint1.w0" "SplTwist_04_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_03_jnt_orientConstraint1.crz" "SplTwist_03_jnt.rz";
connectAttr "SplTwist_03_jnt_scaleConstraint1.csx" "SplTwist_03_jnt.sx";
connectAttr "SplTwist_03_jnt_scaleConstraint1.csy" "SplTwist_03_jnt.sy";
connectAttr "SplTwist_03_jnt_scaleConstraint1.csz" "SplTwist_03_jnt.sz";
connectAttr "SplTwist_03_jnt.ro" "SplTwist_03_jnt_orientConstraint1.cro";
connectAttr "SplTwist_03_jnt.pim" "SplTwist_03_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_03_jnt.jo" "SplTwist_03_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_03_jnt.is" "SplTwist_03_jnt_orientConstraint1.is";
connectAttr "SplLocal_01_ctr.r" "SplTwist_03_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_01_ctr.ro" "SplTwist_03_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_03_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_03_jnt_orientConstraint1.w0" "SplTwist_03_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_02_ctr.r" "SplTwist_03_jnt_orientConstraint1.tg[1].tr";
connectAttr "SplLocal_02_ctr.ro" "SplTwist_03_jnt_orientConstraint1.tg[1].tro";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_03_jnt_orientConstraint1.tg[1].tpm";
connectAttr "SplTwist_03_jnt_orientConstraint1.w1" "SplTwist_03_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_03_jnt.pim" "SplTwist_03_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_01_ctr.s" "SplTwist_03_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_03_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_03_jnt_scaleConstraint1.w0" "SplTwist_03_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_02_ctr.s" "SplTwist_03_jnt_scaleConstraint1.tg[1].ts";
connectAttr "SplLocal_02_ctr.pm" "SplTwist_03_jnt_scaleConstraint1.tg[1].tpm";
connectAttr "SplTwist_03_jnt_scaleConstraint1.w1" "SplTwist_03_jnt_scaleConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_02_jnt_orientConstraint1.crz" "SplTwist_02_jnt.rz";
connectAttr "SplTwist_02_jnt_scaleConstraint1.csx" "SplTwist_02_jnt.sx";
connectAttr "SplTwist_02_jnt_scaleConstraint1.csy" "SplTwist_02_jnt.sy";
connectAttr "SplTwist_02_jnt_scaleConstraint1.csz" "SplTwist_02_jnt.sz";
connectAttr "SplTwist_02_jnt.pim" "SplTwist_02_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_01_ctr.s" "SplTwist_02_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_02_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_02_jnt_scaleConstraint1.w0" "SplTwist_02_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_02_jnt.ro" "SplTwist_02_jnt_orientConstraint1.cro";
connectAttr "SplTwist_02_jnt.pim" "SplTwist_02_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_02_jnt.jo" "SplTwist_02_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_02_jnt.is" "SplTwist_02_jnt_orientConstraint1.is";
connectAttr "SplLocal_01_ctr.r" "SplTwist_02_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_01_ctr.ro" "SplTwist_02_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_02_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_02_jnt_orientConstraint1.w0" "SplTwist_02_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_01_jnt_orientConstraint1.crz" "SplTwist_01_jnt.rz";
connectAttr "SplTwist_01_jnt_scaleConstraint1.csx" "SplTwist_01_jnt.sx";
connectAttr "SplTwist_01_jnt_scaleConstraint1.csy" "SplTwist_01_jnt.sy";
connectAttr "SplTwist_01_jnt_scaleConstraint1.csz" "SplTwist_01_jnt.sz";
connectAttr "SplTwist_01_jnt.ro" "SplTwist_01_jnt_orientConstraint1.cro";
connectAttr "SplTwist_01_jnt.pim" "SplTwist_01_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_01_jnt.jo" "SplTwist_01_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_01_jnt.is" "SplTwist_01_jnt_orientConstraint1.is";
connectAttr "SplLocal_00_ctr.r" "SplTwist_01_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_00_ctr.ro" "SplTwist_01_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_00_ctr.pm" "SplTwist_01_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_01_jnt_orientConstraint1.w0" "SplTwist_01_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_01_ctr.r" "SplTwist_01_jnt_orientConstraint1.tg[1].tr";
connectAttr "SplLocal_01_ctr.ro" "SplTwist_01_jnt_orientConstraint1.tg[1].tro";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_01_jnt_orientConstraint1.tg[1].tpm";
connectAttr "SplTwist_01_jnt_orientConstraint1.w1" "SplTwist_01_jnt_orientConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_01_jnt.pim" "SplTwist_01_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_00_ctr.s" "SplTwist_01_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_00_ctr.pm" "SplTwist_01_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_01_jnt_scaleConstraint1.w0" "SplTwist_01_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplLocal_01_ctr.s" "SplTwist_01_jnt_scaleConstraint1.tg[1].ts";
connectAttr "SplLocal_01_ctr.pm" "SplTwist_01_jnt_scaleConstraint1.tg[1].tpm";
connectAttr "SplTwist_01_jnt_scaleConstraint1.w1" "SplTwist_01_jnt_scaleConstraint1.tg[1].tw"
		;
connectAttr "SplTwist_00_jnt_orientConstraint1.crz" "SplTwist_00_jnt.rz";
connectAttr "SplTwist_00_jnt_scaleConstraint1.csx" "SplTwist_00_jnt.sx";
connectAttr "SplTwist_00_jnt_scaleConstraint1.csy" "SplTwist_00_jnt.sy";
connectAttr "SplTwist_00_jnt_scaleConstraint1.csz" "SplTwist_00_jnt.sz";
connectAttr "SplTwist_00_jnt.pim" "SplTwist_00_jnt_scaleConstraint1.cpim";
connectAttr "SplLocal_00_ctr.s" "SplTwist_00_jnt_scaleConstraint1.tg[0].ts";
connectAttr "SplLocal_00_ctr.pm" "SplTwist_00_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "SplTwist_00_jnt_scaleConstraint1.w0" "SplTwist_00_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "SplTwist_00_jnt.ro" "SplTwist_00_jnt_orientConstraint1.cro";
connectAttr "SplTwist_00_jnt.pim" "SplTwist_00_jnt_orientConstraint1.cpim";
connectAttr "SplTwist_00_jnt.jo" "SplTwist_00_jnt_orientConstraint1.cjo";
connectAttr "SplTwist_00_jnt.is" "SplTwist_00_jnt_orientConstraint1.is";
connectAttr "SplLocal_00_ctr.r" "SplTwist_00_jnt_orientConstraint1.tg[0].tr";
connectAttr "SplLocal_00_ctr.ro" "SplTwist_00_jnt_orientConstraint1.tg[0].tro";
connectAttr "SplLocal_00_ctr.pm" "SplTwist_00_jnt_orientConstraint1.tg[0].tpm";
connectAttr "SplTwist_00_jnt_orientConstraint1.w0" "SplTwist_00_jnt_orientConstraint1.tg[0].tw"
		;
connectAttr "unitConversion2.o" "SplLocal_03_root.rz";
connectAttr "unitConversion3.o" "SplLocal_02_root.rz";
connectAttr "unitConversion4.o" "SplLocal_01_root.rz";
connectAttr "SplLocal_00_root_scaleConstraint1.csx" "SplLocal_00_root.sx";
connectAttr "SplLocal_00_root_scaleConstraint1.csy" "SplLocal_00_root.sy";
connectAttr "SplLocal_00_root_scaleConstraint1.csz" "SplLocal_00_root.sz";
connectAttr "SplLocal_00_root.pim" "SplLocal_00_root_scaleConstraint1.cpim";
connectAttr "SplFk_00_ctr.s" "SplLocal_00_root_scaleConstraint1.tg[0].ts";
connectAttr "SplFk_00_ctr.pm" "SplLocal_00_root_scaleConstraint1.tg[0].tpm";
connectAttr "SplLocal_00_root_scaleConstraint1.w0" "SplLocal_00_root_scaleConstraint1.tg[0].tw"
		;
connectAttr "skinCluster1GroupId.id" "tentacle_00_geoShape.iog.og[2].gid";
connectAttr "skinCluster1Set.mwc" "tentacle_00_geoShape.iog.og[2].gco";
connectAttr "groupId2.id" "tentacle_00_geoShape.iog.og[3].gid";
connectAttr "tweakSet1.mwc" "tentacle_00_geoShape.iog.og[3].gco";
connectAttr "skinCluster1.og[0]" "tentacle_00_geoShape.i";
connectAttr "tweak1.vl[0].vt[0]" "tentacle_00_geoShape.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Spl_00_crvShape.ws" "Spl_00_cvinf.ic";
connectAttr "Spl_00_cvinf.al" "Spl_00_mdv.i1x";
connectAttr "Spl_00_mdv.ox" "Spl_00_clp.ipr";
connectAttr "multiplyDivide1.ox" "Spl_00_clp.ipg";
connectAttr "unitConversion1.o" "SplTwist_00_mdv.i1x";
connectAttr "unitConversion1.o" "SplTwist_00_mdv.i1y";
connectAttr "unitConversion1.o" "SplTwist_00_mdv.i1z";
connectAttr "SplTwist_00_ctr.rz" "unitConversion1.i";
connectAttr "SplTwist_00_mdv.ox" "unitConversion2.i";
connectAttr "SplTwist_00_mdv.oy" "unitConversion3.i";
connectAttr "SplTwist_00_mdv.oz" "unitConversion4.i";
connectAttr "Spl_00_mdv.ox" "multiplyDivide1.i2x";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose2.msg" "skinCluster1.bp";
connectAttr "SplTwist_08_jnt.wm" "skinCluster1.ma[0]";
connectAttr "SplTwist_07_jnt.wm" "skinCluster1.ma[1]";
connectAttr "SplTwist_06_jnt.wm" "skinCluster1.ma[2]";
connectAttr "SplTwist_05_jnt.wm" "skinCluster1.ma[3]";
connectAttr "SplTwist_04_jnt.wm" "skinCluster1.ma[4]";
connectAttr "SplTwist_03_jnt.wm" "skinCluster1.ma[5]";
connectAttr "SplTwist_02_jnt.wm" "skinCluster1.ma[6]";
connectAttr "SplTwist_01_jnt.wm" "skinCluster1.ma[7]";
connectAttr "SplTwist_00_jnt.wm" "skinCluster1.ma[8]";
connectAttr "SplTwist_08_jnt.liw" "skinCluster1.lw[0]";
connectAttr "SplTwist_07_jnt.liw" "skinCluster1.lw[1]";
connectAttr "SplTwist_06_jnt.liw" "skinCluster1.lw[2]";
connectAttr "SplTwist_05_jnt.liw" "skinCluster1.lw[3]";
connectAttr "SplTwist_04_jnt.liw" "skinCluster1.lw[4]";
connectAttr "SplTwist_03_jnt.liw" "skinCluster1.lw[5]";
connectAttr "SplTwist_02_jnt.liw" "skinCluster1.lw[6]";
connectAttr "SplTwist_01_jnt.liw" "skinCluster1.lw[7]";
connectAttr "SplTwist_00_jnt.liw" "skinCluster1.lw[8]";
connectAttr "SplTwist_08_jnt.obcc" "skinCluster1.ifcl[0]";
connectAttr "SplTwist_07_jnt.obcc" "skinCluster1.ifcl[1]";
connectAttr "SplTwist_06_jnt.obcc" "skinCluster1.ifcl[2]";
connectAttr "SplTwist_05_jnt.obcc" "skinCluster1.ifcl[3]";
connectAttr "SplTwist_04_jnt.obcc" "skinCluster1.ifcl[4]";
connectAttr "SplTwist_03_jnt.obcc" "skinCluster1.ifcl[5]";
connectAttr "SplTwist_02_jnt.obcc" "skinCluster1.ifcl[6]";
connectAttr "SplTwist_01_jnt.obcc" "skinCluster1.ifcl[7]";
connectAttr "SplTwist_00_jnt.obcc" "skinCluster1.ifcl[8]";
connectAttr "SplTwist_05_jnt.msg" "skinCluster1.ptt";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "tentacle_00_geoShape.iog.og[2]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "tentacle_00_geoShape.iog.og[3]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "tentacle_00_geoShape1Orig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "Spl_00_jnt.msg" "bindPose2.m[0]";
connectAttr "Spl_01_jnt.msg" "bindPose2.m[1]";
connectAttr "Spl_02_jnt.msg" "bindPose2.m[2]";
connectAttr "Spl_03_jnt.msg" "bindPose2.m[3]";
connectAttr "Spl_04_jnt.msg" "bindPose2.m[4]";
connectAttr "Spl_05_jnt.msg" "bindPose2.m[5]";
connectAttr "Spl_06_jnt.msg" "bindPose2.m[6]";
connectAttr "Spl_07_jnt.msg" "bindPose2.m[7]";
connectAttr "Spl_08_jnt.msg" "bindPose2.m[8]";
connectAttr "SplTwist_08_jnt.msg" "bindPose2.m[9]";
connectAttr "SplTwist_07_jnt.msg" "bindPose2.m[10]";
connectAttr "SplTwist_06_jnt.msg" "bindPose2.m[11]";
connectAttr "SplTwist_05_jnt.msg" "bindPose2.m[12]";
connectAttr "SplTwist_04_jnt.msg" "bindPose2.m[13]";
connectAttr "SplTwist_03_jnt.msg" "bindPose2.m[14]";
connectAttr "SplTwist_02_jnt.msg" "bindPose2.m[15]";
connectAttr "SplTwist_01_jnt.msg" "bindPose2.m[16]";
connectAttr "SplTwist_00_jnt.msg" "bindPose2.m[17]";
connectAttr "bindPose2.w" "bindPose2.p[0]";
connectAttr "bindPose2.m[0]" "bindPose2.p[1]";
connectAttr "bindPose2.m[1]" "bindPose2.p[2]";
connectAttr "bindPose2.m[2]" "bindPose2.p[3]";
connectAttr "bindPose2.m[3]" "bindPose2.p[4]";
connectAttr "bindPose2.m[4]" "bindPose2.p[5]";
connectAttr "bindPose2.m[5]" "bindPose2.p[6]";
connectAttr "bindPose2.m[6]" "bindPose2.p[7]";
connectAttr "bindPose2.m[7]" "bindPose2.p[8]";
connectAttr "bindPose2.m[8]" "bindPose2.p[9]";
connectAttr "bindPose2.m[7]" "bindPose2.p[10]";
connectAttr "bindPose2.m[6]" "bindPose2.p[11]";
connectAttr "bindPose2.m[5]" "bindPose2.p[12]";
connectAttr "bindPose2.m[4]" "bindPose2.p[13]";
connectAttr "bindPose2.m[3]" "bindPose2.p[14]";
connectAttr "bindPose2.m[2]" "bindPose2.p[15]";
connectAttr "bindPose2.m[1]" "bindPose2.p[16]";
connectAttr "bindPose2.m[0]" "bindPose2.p[17]";
connectAttr "Spl_00_jnt.bps" "bindPose2.wm[0]";
connectAttr "Spl_01_jnt.bps" "bindPose2.wm[1]";
connectAttr "Spl_02_jnt.bps" "bindPose2.wm[2]";
connectAttr "Spl_03_jnt.bps" "bindPose2.wm[3]";
connectAttr "Spl_04_jnt.bps" "bindPose2.wm[4]";
connectAttr "Spl_05_jnt.bps" "bindPose2.wm[5]";
connectAttr "Spl_06_jnt.bps" "bindPose2.wm[6]";
connectAttr "Spl_07_jnt.bps" "bindPose2.wm[7]";
connectAttr "Spl_08_jnt.bps" "bindPose2.wm[8]";
connectAttr "SplTwist_08_jnt.bps" "bindPose2.wm[9]";
connectAttr "SplTwist_07_jnt.bps" "bindPose2.wm[10]";
connectAttr "SplTwist_06_jnt.bps" "bindPose2.wm[11]";
connectAttr "SplTwist_05_jnt.bps" "bindPose2.wm[12]";
connectAttr "SplTwist_04_jnt.bps" "bindPose2.wm[13]";
connectAttr "SplTwist_03_jnt.bps" "bindPose2.wm[14]";
connectAttr "SplTwist_02_jnt.bps" "bindPose2.wm[15]";
connectAttr "SplTwist_01_jnt.bps" "bindPose2.wm[16]";
connectAttr "SplTwist_00_jnt.bps" "bindPose2.wm[17]";
connectAttr "SplTwist_00_ctr.autoStretch" "Spl_00_blcl.b";
connectAttr "Spl_00_clp.opr" "Spl_00_blcl.c1r";
connectAttr "Spl_00_cvinf.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Spl_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Spl_00_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "SplTwist_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "multiplyDivide1.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Spl_00_blcl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "tentacle_00_geoShape.iog" ":initialShadingGroup.dsm" -na;
connectAttr "ikSplineSolver.msg" ":ikSystem.sol" -na;
// End of tentacleControlFive.ma
