//Maya ASCII 2020 scene
//Name: cape.ma
//Last modified: Mon, Apr 11, 2022 10:09:15 AM
//Codeset: 1252
requires maya "2020";
requires "stereoCamera" "10.0";
requires "stereoCamera" "10.0";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "7800D535-4054-0A50-BEA5-B398D2367876";
createNode transform -s -n "persp";
	rename -uid "D89C12B0-4D97-9D42-2CFC-018EB127EEFD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 5.106584615006458 4.5908507262599603 -17.035509096043945 ;
	setAttr ".r" -type "double3" -9.3383527292365862 523.79999999955987 0 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "6F1E85F9-4D2C-5DB4-018B-C2A3C385FA37";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 19.559239820414238;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 0.5 -2.5 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "A6D5B46F-41BE-E6F1-22AA-BEA49CBF9DCA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "CBCD2C11-4FA5-8FFF-7F8B-FE99B458A295";
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
	rename -uid "151F1CFD-4706-3944-C904-CE96B6F9E164";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "04CDE77E-4CF1-1480-A55E-18BFF8A3A3EE";
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
	rename -uid "72A8BD65-4052-BB6E-BD6B-26B67F34F83E";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 1.5951554187279742 1.2679690561850692 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "6B747066-4FD4-4ED2-B5AA-22B26D685F37";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 14.563440860215053;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode transform -n "rig";
	rename -uid "48FA721D-4E57-C681-221D-14A5DCF2F204";
createNode transform -n "export" -p "rig";
	rename -uid "4F174500-4B71-C211-83D2-729C7C2B7C5C";
	setAttr ".v" no;
createNode joint -n "cn_:Hold_00_jnt" -p "export";
	rename -uid "E005AF54-42CA-047F-6DDA-7DBA04AB43F9";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".radi" 0.5;
	setAttr ".liw" yes;
createNode joint -n "cn_:Fk_00_jnt" -p "cn_:Hold_00_jnt";
	rename -uid "C9A3E8DE-49DA-D561-79AD-0494B6472E42";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 90 0 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 0.5 5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "cn_:Fk_01_jnt" -p "cn_:Fk_00_jnt";
	rename -uid "35C7F741-4BD5-FCEC-4F95-D68E8AEC86AF";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 0.5 2.5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "cn_:Fk_02_jnt" -p "cn_:Fk_01_jnt";
	rename -uid "D5E35F99-42F1-A0BE-2E49-3DAF7C60E4C7";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 0.5 0 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "cn_:Fk_03_jnt" -p "cn_:Fk_02_jnt";
	rename -uid "90FD4BA3-4367-2588-BC58-719A8A986836";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 0 0.5 -2.5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode parentConstraint -n "cn_:Fk_03_jnt_parentConstraint1" -p "cn_:Fk_03_jnt";
	rename -uid "CFCA4D81-4B0C-75BC-4E41-FCA7AC34AB1E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cn_:Fk_03_jnt_scaleConstraint1" -p "cn_:Fk_03_jnt";
	rename -uid "42EBEA6E-49DC-5F39-77EF-42A3982D2797";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "cn_:Fk_02_jnt_parentConstraint1" -p "cn_:Fk_02_jnt";
	rename -uid "909D6B5E-4FB3-A802-D1D1-3FA68779A3FE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cn_:Fk_02_jnt_scaleConstraint1" -p "cn_:Fk_02_jnt";
	rename -uid "AE5E7482-4296-4E30-960E-03AA806ACF0A";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "cn_:Fk_01_jnt_parentConstraint1" -p "cn_:Fk_01_jnt";
	rename -uid "E7BE4BD4-4C4A-9DAE-5D6A-B085B58B0CF1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cn_:Fk_01_jnt_scaleConstraint1" -p "cn_:Fk_01_jnt";
	rename -uid "1A0D9ED8-446E-518B-AD87-9BAAC9FE5F7E";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "cn_:Fk_00_jnt_parentConstraint1" -p "cn_:Fk_00_jnt";
	rename -uid "FA922B06-4693-29B7-50A3-45BDAA1DCF16";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 0.50000000000000033 5 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "cn_:Fk_00_jnt_scaleConstraint1" -p "cn_:Fk_00_jnt";
	rename -uid "5E4A7FED-477E-6EAB-0C4D-C39A5FD48297";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "lf_:Fk_00_jnt" -p "cn_:Hold_00_jnt";
	rename -uid "74CB937C-4D1C-0B95-3129-3FA30DDA3C03";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 90 0 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 5 0.5 5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "lf_:Fk_01_jnt" -p "lf_:Fk_00_jnt";
	rename -uid "554EC148-4489-82FD-51DD-33AEB250102F";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 5 0.5 2.5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "lf_:Fk_02_jnt" -p "lf_:Fk_01_jnt";
	rename -uid "AC3EAF83-4A6A-8791-E454-9CA68622CBAE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 5 0.5 0 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "lf_:Fk_03_jnt" -p "lf_:Fk_02_jnt";
	rename -uid "DEED1D42-466F-48C1-9E49-DA81D55CCDD3";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 -1 0 0 1 0 0 1 0 0 0 5 0.5 -2.5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode parentConstraint -n "lf_:Fk_03_jnt_parentConstraint1" -p "lf_:Fk_03_jnt";
	rename -uid "359A1140-4292-6923-F598-C2A646F291D1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "lf_:Fk_03_jnt_scaleConstraint1" -p "lf_:Fk_03_jnt";
	rename -uid "8318E5EA-44F6-2E76-423B-5684DAEA4F51";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "lf_:Fk_02_jnt_parentConstraint1" -p "lf_:Fk_02_jnt";
	rename -uid "722BDB4C-48FE-58C9-E66A-B7BD1D8C3267";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "lf_:Fk_02_jnt_scaleConstraint1" -p "lf_:Fk_02_jnt";
	rename -uid "FCA9E511-44D1-2C80-C315-2798093ACD6F";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "lf_:Fk_01_jnt_parentConstraint1" -p "lf_:Fk_01_jnt";
	rename -uid "52E333F4-4424-EAAF-611C-ED8D9E577DE1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "lf_:Fk_01_jnt_scaleConstraint1" -p "lf_:Fk_01_jnt";
	rename -uid "BC031D38-43BA-DC7C-DE43-79B58CF042C1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "lf_:Fk_00_jnt_parentConstraint1" -p "lf_:Fk_00_jnt";
	rename -uid "D3DD76C7-4F3E-6FEE-4CF2-95BB89A1BC8D";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 5 0.50000000000000033 5 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "lf_:Fk_00_jnt_scaleConstraint1" -p "lf_:Fk_00_jnt";
	rename -uid "7CCC914D-4A7C-2F54-4A9D-38AA6C49E6B5";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode joint -n "rt_:Fk_00_jnt" -p "cn_:Hold_00_jnt";
	rename -uid "1CC54250-4FFE-D224-5F3D-E99D5D485DC8";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".v" no;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" -180 -90 0 ;
	setAttr ".bps" -type "matrix" 0 0 1 0 1.2246467991473532e-16 -1 0 0 1 1.2246467991473532e-16 0 0
		 -5 0.5 5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "rt_:Fk_01_jnt" -p "rt_:Fk_00_jnt";
	rename -uid "B325D25D-497E-6FF6-9981-6BB600035DEE";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 1 0 1.2246467991473532e-16 -1 0 0 1 1.2246467991473532e-16 0 0
		 -5 0.5 2.5 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "rt_:Fk_02_jnt" -p "rt_:Fk_01_jnt";
	rename -uid "781E6759-473E-BB97-1989-AE8416BABB30";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 1 0 1.2246467991473532e-16 -1 0 0 1 1.2246467991473532e-16 0 0
		 -5 0.5 0 1;
	setAttr ".radi" 0.57758620689655171;
	setAttr ".liw" yes;
createNode joint -n "rt_:Fk_03_jnt" -p "rt_:Fk_02_jnt";
	rename -uid "247D7723-4F95-DA38-0BC8-51A48948481B";
	addAttr -ci true -sn "liw" -ln "lockInfluenceWeights" -min 0 -max 1 -at "bool";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".bps" -type "matrix" 0 0 1 0 1.2246467991473532e-16 -1 0 0 1 1.2246467991473532e-16 0 0
		 -5 0.5 -2.5 1;
	setAttr ".radi" 0.57758620689655171;
createNode parentConstraint -n "rt_:Fk_03_jnt_parentConstraint1" -p "rt_:Fk_03_jnt";
	rename -uid "6611D595-4ACB-D518-A6D0-FDA03C4E67CC";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "rt_:Fk_03_jnt_scaleConstraint1" -p "rt_:Fk_03_jnt";
	rename -uid "A1CF35C0-4605-B98A-C8C4-D3A3DE662B3B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_03_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "rt_:Fk_02_jnt_parentConstraint1" -p "rt_:Fk_02_jnt";
	rename -uid "27102740-45C0-7C31-3978-3D91005707BB";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -2.5 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "rt_:Fk_02_jnt_scaleConstraint1" -p "rt_:Fk_02_jnt";
	rename -uid "A4F297F7-4619-C455-255C-4CB35EB5BDA1";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_02_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "rt_:Fk_01_jnt_parentConstraint1" -p "rt_:Fk_01_jnt";
	rename -uid "C64DF3A6-43C3-BDE4-DD20-CBB4BF0D0FE4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -2.5 3.8857805861880479e-16 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "rt_:Fk_01_jnt_scaleConstraint1" -p "rt_:Fk_01_jnt";
	rename -uid "568333AB-45F7-C1A5-D31D-3B8896CFBE53";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_01_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "rt_:Fk_00_jnt_parentConstraint1" -p "rt_:Fk_00_jnt";
	rename -uid "A6E01E07-4E24-D551-DA2A-4E958DE18017";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" -1.4033418597069752e-14 0 0 ;
	setAttr ".rst" -type "double3" -5 0.49999999999999967 5 ;
	setAttr ".rsrr" -type "double3" -1.4033418597069752e-14 0 0 ;
	setAttr -k on ".w0";
createNode scaleConstraint -n "rt_:Fk_00_jnt_scaleConstraint1" -p "rt_:Fk_00_jnt";
	rename -uid "F5E7F931-4BB8-27D3-560A-F3B7D7D9D4C4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Fk_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode transform -n "controls" -p "rig";
	rename -uid "5F01D1E7-449C-45F5-8E00-A88DF11D2BA8";
createNode transform -n "lf_:Fk_00_root" -p "controls";
	rename -uid "0AA10790-4F3A-F862-9B75-EA94387861DD";
	setAttr ".t" -type "double3" 5 0.50000000000000033 5 ;
	setAttr ".r" -type "double3" 0 90 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_00_off" -p "lf_:Fk_00_root";
	rename -uid "1EFC78D5-42F7-6C99-0A59-CA957FEAFA8D";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_00_ctr" -p "lf_:Fk_00_off";
	rename -uid "B4C54D04-4561-726B-C086-DD95E1C31578";
createNode nurbsCurve -n "lf_:Fk_00_ctrShape" -p "lf_:Fk_00_ctr";
	rename -uid "1550D681-4283-16CD-8560-509DCBF8F7E6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "lf_:Fk_01_root" -p "lf_:Fk_00_ctr";
	rename -uid "3F7C50F1-4E04-8177-39CF-B98E9DFB0EF9";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_01_off" -p "lf_:Fk_01_root";
	rename -uid "FEAC6446-4328-D5B0-AA27-B3A6F3FEC015";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_01_ctr" -p "lf_:Fk_01_off";
	rename -uid "4FDE95BF-4D47-6553-76E7-768BAB449A94";
createNode nurbsCurve -n "lf_:Fk_01_ctrShape" -p "lf_:Fk_01_ctr";
	rename -uid "6F12EA29-4015-4F6E-203C-9BA8DA9178D9";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "lf_:Fk_02_root" -p "lf_:Fk_01_ctr";
	rename -uid "E0A89F7E-40E1-5985-F71B-EF92D3D03BB9";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_02_off" -p "lf_:Fk_02_root";
	rename -uid "E4A60C0D-4B9C-0F68-3A92-29B8EDD1AF31";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_02_ctr" -p "lf_:Fk_02_off";
	rename -uid "3B9F08BB-492E-08E5-D379-D784C05B1DE6";
createNode nurbsCurve -n "lf_:Fk_02_ctrShape" -p "lf_:Fk_02_ctr";
	rename -uid "80B0B3E0-46DA-10F0-C8EE-BA9E3DB1E1AF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "lf_:Fk_03_root" -p "lf_:Fk_02_ctr";
	rename -uid "F1933A7B-4F22-588E-A279-EBB83C23A898";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_03_off" -p "lf_:Fk_03_root";
	rename -uid "3DF49AC1-4D03-6D7E-7AC8-D2BD1EAB26E5";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "lf_:Fk_03_ctr" -p "lf_:Fk_03_off";
	rename -uid "40BC4D95-48EA-F88E-ACF0-828C8ADD1B5C";
createNode nurbsCurve -n "lf_:Fk_03_ctrShape" -p "lf_:Fk_03_ctr";
	rename -uid "7D40E9D5-4A44-0806-6134-E19CA3978BDE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "rt_:Fk_00_root" -p "controls";
	rename -uid "DB668E9F-43D5-F547-8E93-51B778C0FD9B";
	setAttr ".t" -type "double3" -5 0.50000000000000033 5 ;
	setAttr ".r" -type "double3" 180 -90 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_00_off" -p "rt_:Fk_00_root";
	rename -uid "BA112588-4648-B066-3783-1E9F5D94BF7F";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_00_ctr" -p "rt_:Fk_00_off";
	rename -uid "1B67C6CC-41CD-2A7A-BA74-65B54667D0E7";
createNode nurbsCurve -n "rt_:Fk_00_ctrShape" -p "rt_:Fk_00_ctr";
	rename -uid "D577D0C3-4381-9BA1-5604-A5B4DBA99A96";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		-1.3297057932470169 1.0532262044701118e-17 0
		-0.94024398338800319 -0.14366143025336295 0
		0.64910425081237344 -0.89886861862891299 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		;
createNode transform -n "rt_:Fk_01_root" -p "rt_:Fk_00_ctr";
	rename -uid "D2AA8FBF-4364-65A4-0240-1395B363A159";
	setAttr ".t" -type "double3" -2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_01_off" -p "rt_:Fk_01_root";
	rename -uid "F7125C2C-42EC-303D-3934-27ABEF3EB07B";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_01_ctr" -p "rt_:Fk_01_off";
	rename -uid "A5F251C1-48A7-2F6B-EB7F-498F6CD5D1C1";
createNode nurbsCurve -n "rt_:Fk_01_ctrShape" -p "rt_:Fk_01_ctr";
	rename -uid "C087CE3A-4187-0595-1E52-00B47B3E7E29";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		-1.3297057932470169 1.0532262044701118e-17 0
		-0.94024398338800319 -0.14366143025336295 0
		0.64910425081237344 -0.89886861862891299 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		;
createNode transform -n "rt_:Fk_02_root" -p "rt_:Fk_01_ctr";
	rename -uid "D3538E7B-4D23-1F05-F037-13BEEB7D2D91";
	setAttr ".t" -type "double3" -2.5 3.8857805861880479e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_02_off" -p "rt_:Fk_02_root";
	rename -uid "80BF1BFE-427A-81C1-47C5-0492CB310D02";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_02_ctr" -p "rt_:Fk_02_off";
	rename -uid "AD1D0473-46A8-2EC6-F1CD-EA96870A339F";
createNode nurbsCurve -n "rt_:Fk_02_ctrShape" -p "rt_:Fk_02_ctr";
	rename -uid "643D667F-4E3F-C6C3-2A43-70B30A405F24";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		-1.3297057932470169 1.0532262044701118e-17 0
		-0.94024398338800319 -0.14366143025336295 0
		0.64910425081237344 -0.89886861862891299 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		;
createNode transform -n "rt_:Fk_03_root" -p "rt_:Fk_02_ctr";
	rename -uid "69471B74-4BE4-EFFD-FF2B-BC8437E3D460";
	setAttr ".t" -type "double3" -2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_03_off" -p "rt_:Fk_03_root";
	rename -uid "32E4990E-4CFD-E200-4E4B-A286AB5A0144";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "rt_:Fk_03_ctr" -p "rt_:Fk_03_off";
	rename -uid "FA8EA7CB-4972-D88D-D1B1-F291B13E7A51";
createNode nurbsCurve -n "rt_:Fk_03_ctrShape" -p "rt_:Fk_03_ctr";
	rename -uid "0E5EB89F-4644-E2F7-4BBB-6EA84FDDF822";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		-1.3297057932470169 1.0532262044701118e-17 0
		-0.94024398338800319 -0.14366143025336295 0
		0.64910425081237344 -0.89886861862891299 0
		0.78361162489122449 -0.78361162489122438 0
		1.1081941875543881 -1.511240500779959e-16 0
		0.78361162489122449 0.7836116248912246 0
		0.64910425081237366 0.89886861862891232 0
		-0.94024398338800319 0.14366143025336289 0
		;
createNode transform -n "cn_:Fk_00_root" -p "controls";
	rename -uid "7C8BAA7A-4A7E-0F39-7991-288EE6FE44E1";
	setAttr ".t" -type "double3" 0 0.50000000000000033 5 ;
	setAttr ".r" -type "double3" 0 90 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_00_off" -p "cn_:Fk_00_root";
	rename -uid "278D5783-4A08-46A4-22A4-C2B7F579D876";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_00_ctr" -p "cn_:Fk_00_off";
	rename -uid "B22140F7-4F23-35AE-8C3C-3290DCDEC571";
createNode nurbsCurve -n "cn_:Fk_00_ctrShape" -p "cn_:Fk_00_ctr";
	rename -uid "5994A6A7-4132-8835-647D-AD9C01171333";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "cn_:Fk_01_root" -p "cn_:Fk_00_ctr";
	rename -uid "A66F968B-4BA7-C439-CCD9-86AF8E5656EE";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_01_off" -p "cn_:Fk_01_root";
	rename -uid "AE9ACB49-4D61-741A-10F0-068171E87815";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_01_ctr" -p "cn_:Fk_01_off";
	rename -uid "65AD9F72-45B5-AB45-E90D-3EABC7CE04BD";
createNode nurbsCurve -n "cn_:Fk_01_ctrShape" -p "cn_:Fk_01_ctr";
	rename -uid "01EC6DF0-435C-9477-47F9-829406C15971";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "cn_:Fk_02_root" -p "cn_:Fk_01_ctr";
	rename -uid "7B6E2CC2-4457-14DD-B5BE-E0B1494E0B1D";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_02_off" -p "cn_:Fk_02_root";
	rename -uid "778C0D0C-4E85-1443-EA65-DD8F896BC335";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_02_ctr" -p "cn_:Fk_02_off";
	rename -uid "4D9B18EA-41DC-196C-8EDC-DF82C3C396D1";
createNode nurbsCurve -n "cn_:Fk_02_ctrShape" -p "cn_:Fk_02_ctr";
	rename -uid "24010796-465D-F503-0268-668A0028B5E2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "cn_:Fk_03_root" -p "cn_:Fk_02_ctr";
	rename -uid "8A48F5EE-4933-D72B-6350-65A4EA900A90";
	setAttr ".t" -type "double3" 2.5 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_03_off" -p "cn_:Fk_03_root";
	rename -uid "7EF5F640-442E-889D-8D84-DFB6BF66AC21";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "cn_:Fk_03_ctr" -p "cn_:Fk_03_off";
	rename -uid "1A43FA24-448C-6DE0-ECE0-D886F11E5C38";
createNode nurbsCurve -n "cn_:Fk_03_ctrShape" -p "cn_:Fk_03_ctr";
	rename -uid "A901C85D-4AAB-14D9-B01F-A7BA4F040C28";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 8 2 no 3
		13 -2 -1 0 1 2 3 4 5 6 7 8 9 10
		11
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		-1.1081941875543881 5.7448982375248304e-17 0
		-0.78361162489122449 -0.78361162489122449 0
		-0.64910425081237377 -0.89886861862891299 0
		0.94024398338800319 -0.14366143025336289 0
		1.3297057932470169 -2.7705940660208365e-17 0
		0.94024398338800319 0.143661430253363 0
		-0.64910425081237355 0.89886861862891232 0
		-0.78361162489122449 0.78361162489122438 0
		;
createNode transform -n "Config_00_root" -p "controls";
	rename -uid "DEEDAF00-410E-4F3D-3C02-4EAC4E9478A0";
	setAttr ".t" -type "double3" 0 0 7 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Config_00_ctr" -p "Config_00_root";
	rename -uid "DD97CE86-400C-EE6C-62D0-A3A742B6D1FE";
	addAttr -ci true -k true -sn "_03_amplitude" -ln "_03_amplitude" -at "double";
	addAttr -ci true -k true -sn "_02_amplitude" -ln "_02_amplitude" -at "double";
	addAttr -ci true -k true -sn "_01_amplitude" -ln "_01_amplitude" -at "double";
	addAttr -ci true -sn "_00_amplitude" -ln "_00_amplitude" -at "double";
	addAttr -ci true -sn "frecuency" -ln "frecuency" -at "double";
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
	setAttr -k on "._03_amplitude" 1;
	setAttr -k on "._02_amplitude" 1;
	setAttr -k on "._01_amplitude" 1;
	setAttr -k on "._00_amplitude" 1;
	setAttr -k on ".frecuency";
createNode nurbsCurve -n "Config_00_ctrShape" -p "Config_00_ctr";
	rename -uid "BA169B4B-47A8-D950-929E-EFBF2015D307";
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
createNode transform -n "setup" -p "rig";
	rename -uid "E158B456-4EB4-B6F2-32F1-6C9498DB2453";
createNode transform -n "geo" -p "rig";
	rename -uid "A33E539F-413E-4138-1B70-E6955BF63BEF";
	setAttr ".ovdt" 2;
	setAttr ".ove" yes;
createNode transform -n "cape_geo" -p "geo";
	rename -uid "07AF931E-4910-AB89-AB91-5CABB1773098";
	setAttr ".t" -type "double3" 0 0.5 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode mesh -n "cape_geoShape" -p "cape_geo";
	rename -uid "6843B11A-4776-E32B-2713-B1B8E3FCF11A";
	setAttr -k off ".v";
	setAttr -s 4 ".iog[0].og";
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".pv" -type "double2" 0.25 0.75 ;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr ".dr" 3;
	setAttr ".dsm" 2;
	setAttr ".vcs" 2;
createNode mesh -n "cape_geoShape1Orig" -p "cape_geo";
	rename -uid "8BC852D6-44FB-1465-F046-D5935EF45D11";
	setAttr -k off ".v";
	setAttr ".io" yes;
	setAttr ".vir" yes;
	setAttr ".vif" yes;
	setAttr ".uvst[0].uvsn" -type "string" "map1";
	setAttr -s 81 ".uvst[0].uvsp[0:80]" -type "float2" 0 0 0.125 0 0.25
		 0 0.375 0 0.5 0 0.625 0 0.75 0 0.875 0 1 0 0 0.125 0.125 0.125 0.25 0.125 0.375 0.125
		 0.5 0.125 0.625 0.125 0.75 0.125 0.875 0.125 1 0.125 0 0.25 0.125 0.25 0.25 0.25
		 0.375 0.25 0.5 0.25 0.625 0.25 0.75 0.25 0.875 0.25 1 0.25 0 0.375 0.125 0.375 0.25
		 0.375 0.375 0.375 0.5 0.375 0.625 0.375 0.75 0.375 0.875 0.375 1 0.375 0 0.5 0.125
		 0.5 0.25 0.5 0.375 0.5 0.5 0.5 0.625 0.5 0.75 0.5 0.875 0.5 1 0.5 0 0.625 0.125 0.625
		 0.25 0.625 0.375 0.625 0.5 0.625 0.625 0.625 0.75 0.625 0.875 0.625 1 0.625 0 0.75
		 0.125 0.75 0.25 0.75 0.375 0.75 0.5 0.75 0.625 0.75 0.75 0.75 0.875 0.75 1 0.75 0
		 0.875 0.125 0.875 0.25 0.875 0.375 0.875 0.5 0.875 0.625 0.875 0.75 0.875 0.875 0.875
		 1 0.875 0 1 0.125 1 0.25 1 0.375 1 0.5 1 0.625 1 0.75 1 0.875 1 1 1;
	setAttr ".cuvs" -type "string" "map1";
	setAttr ".dcc" -type "string" "Ambient+Diffuse";
	setAttr ".covm[0]"  0 1 1;
	setAttr ".cdvm[0]"  0 1 1;
	setAttr -s 81 ".vt[0:80]"  -5 0 5 -3.75 0 5 -2.5 0 5 -1.25 0 5 0 0 5
		 1.25 0 5 2.5 0 5 3.75 0 5 5 0 5 -5 0 3.75 -3.75 0 3.75 -2.5 0 3.75 -1.25 0 3.75 0 0 3.75
		 1.25 0 3.75 2.5 0 3.75 3.75 0 3.75 5 0 3.75 -5 0 2.5 -3.75 0 2.5 -2.5 0 2.5 -1.25 0 2.5
		 0 0 2.5 1.25 0 2.5 2.5 0 2.5 3.75 0 2.5 5 0 2.5 -5 0 1.25 -3.75 0 1.25 -2.5 0 1.25
		 -1.25 0 1.25 0 0 1.25 1.25 0 1.25 2.5 0 1.25 3.75 0 1.25 5 0 1.25 -5 0 0 -3.75 0 0
		 -2.5 0 0 -1.25 0 0 0 0 0 1.25 0 0 2.5 0 0 3.75 0 0 5 0 0 -5 0 -1.25 -3.75 0 -1.25
		 -2.5 0 -1.25 -1.25 0 -1.25 0 0 -1.25 1.25 0 -1.25 2.5 0 -1.25 3.75 0 -1.25 5 0 -1.25
		 -5 0 -2.5 -3.75 0 -2.5 -2.5 0 -2.5 -1.25 0 -2.5 0 0 -2.5 1.25 0 -2.5 2.5 0 -2.5 3.75 0 -2.5
		 5 0 -2.5 -5 0 -3.75 -3.75 0 -3.75 -2.5 0 -3.75 -1.25 0 -3.75 0 0 -3.75 1.25 0 -3.75
		 2.5 0 -3.75 3.75 0 -3.75 5 0 -3.75 -5 0 -5 -3.75 0 -5 -2.5 0 -5 -1.25 0 -5 0 0 -5
		 1.25 0 -5 2.5 0 -5 3.75 0 -5 5 0 -5;
	setAttr -s 144 ".ed[0:143]"  0 1 0 0 9 0 1 2 0 1 10 1 2 3 0 2 11 1 3 4 0
		 3 12 1 4 5 0 4 13 1 5 6 0 5 14 1 6 7 0 6 15 1 7 8 0 7 16 1 8 17 0 9 10 1 9 18 0 10 11 1
		 10 19 1 11 12 1 11 20 1 12 13 1 12 21 1 13 14 1 13 22 1 14 15 1 14 23 1 15 16 1 15 24 1
		 16 17 1 16 25 1 17 26 0 18 19 1 18 27 0 19 20 1 19 28 1 20 21 1 20 29 1 21 22 1 21 30 1
		 22 23 1 22 31 1 23 24 1 23 32 1 24 25 1 24 33 1 25 26 1 25 34 1 26 35 0 27 28 1 27 36 0
		 28 29 1 28 37 1 29 30 1 29 38 1 30 31 1 30 39 1 31 32 1 31 40 1 32 33 1 32 41 1 33 34 1
		 33 42 1 34 35 1 34 43 1 35 44 0 36 37 1 36 45 0 37 38 1 37 46 1 38 39 1 38 47 1 39 40 1
		 39 48 1 40 41 1 40 49 1 41 42 1 41 50 1 42 43 1 42 51 1 43 44 1 43 52 1 44 53 0 45 46 1
		 45 54 0 46 47 1 46 55 1 47 48 1 47 56 1 48 49 1 48 57 1 49 50 1 49 58 1 50 51 1 50 59 1
		 51 52 1 51 60 1 52 53 1 52 61 1 53 62 0 54 55 1 54 63 0 55 56 1 55 64 1 56 57 1 56 65 1
		 57 58 1 57 66 1 58 59 1 58 67 1 59 60 1 59 68 1 60 61 1 60 69 1 61 62 1 61 70 1 62 71 0
		 63 64 1 63 72 0 64 65 1 64 73 1 65 66 1 65 74 1 66 67 1 66 75 1 67 68 1 67 76 1 68 69 1
		 68 77 1 69 70 1 69 78 1 70 71 1 70 79 1 71 80 0 72 73 0 73 74 0 74 75 0 75 76 0 76 77 0
		 77 78 0 78 79 0 79 80 0;
	setAttr -s 64 -ch 256 ".fc[0:63]" -type "polyFaces" 
		f 4 0 3 -18 -2
		mu 0 4 0 1 10 9
		f 4 2 5 -20 -4
		mu 0 4 1 2 11 10
		f 4 4 7 -22 -6
		mu 0 4 2 3 12 11
		f 4 6 9 -24 -8
		mu 0 4 3 4 13 12
		f 4 8 11 -26 -10
		mu 0 4 4 5 14 13
		f 4 10 13 -28 -12
		mu 0 4 5 6 15 14
		f 4 12 15 -30 -14
		mu 0 4 6 7 16 15
		f 4 14 16 -32 -16
		mu 0 4 7 8 17 16
		f 4 17 20 -35 -19
		mu 0 4 9 10 19 18
		f 4 19 22 -37 -21
		mu 0 4 10 11 20 19
		f 4 21 24 -39 -23
		mu 0 4 11 12 21 20
		f 4 23 26 -41 -25
		mu 0 4 12 13 22 21
		f 4 25 28 -43 -27
		mu 0 4 13 14 23 22
		f 4 27 30 -45 -29
		mu 0 4 14 15 24 23
		f 4 29 32 -47 -31
		mu 0 4 15 16 25 24
		f 4 31 33 -49 -33
		mu 0 4 16 17 26 25
		f 4 34 37 -52 -36
		mu 0 4 18 19 28 27
		f 4 36 39 -54 -38
		mu 0 4 19 20 29 28
		f 4 38 41 -56 -40
		mu 0 4 20 21 30 29
		f 4 40 43 -58 -42
		mu 0 4 21 22 31 30
		f 4 42 45 -60 -44
		mu 0 4 22 23 32 31
		f 4 44 47 -62 -46
		mu 0 4 23 24 33 32
		f 4 46 49 -64 -48
		mu 0 4 24 25 34 33
		f 4 48 50 -66 -50
		mu 0 4 25 26 35 34
		f 4 51 54 -69 -53
		mu 0 4 27 28 37 36
		f 4 53 56 -71 -55
		mu 0 4 28 29 38 37
		f 4 55 58 -73 -57
		mu 0 4 29 30 39 38
		f 4 57 60 -75 -59
		mu 0 4 30 31 40 39
		f 4 59 62 -77 -61
		mu 0 4 31 32 41 40
		f 4 61 64 -79 -63
		mu 0 4 32 33 42 41
		f 4 63 66 -81 -65
		mu 0 4 33 34 43 42
		f 4 65 67 -83 -67
		mu 0 4 34 35 44 43
		f 4 68 71 -86 -70
		mu 0 4 36 37 46 45
		f 4 70 73 -88 -72
		mu 0 4 37 38 47 46
		f 4 72 75 -90 -74
		mu 0 4 38 39 48 47
		f 4 74 77 -92 -76
		mu 0 4 39 40 49 48
		f 4 76 79 -94 -78
		mu 0 4 40 41 50 49
		f 4 78 81 -96 -80
		mu 0 4 41 42 51 50
		f 4 80 83 -98 -82
		mu 0 4 42 43 52 51
		f 4 82 84 -100 -84
		mu 0 4 43 44 53 52
		f 4 85 88 -103 -87
		mu 0 4 45 46 55 54
		f 4 87 90 -105 -89
		mu 0 4 46 47 56 55
		f 4 89 92 -107 -91
		mu 0 4 47 48 57 56
		f 4 91 94 -109 -93
		mu 0 4 48 49 58 57
		f 4 93 96 -111 -95
		mu 0 4 49 50 59 58
		f 4 95 98 -113 -97
		mu 0 4 50 51 60 59
		f 4 97 100 -115 -99
		mu 0 4 51 52 61 60
		f 4 99 101 -117 -101
		mu 0 4 52 53 62 61
		f 4 102 105 -120 -104
		mu 0 4 54 55 64 63
		f 4 104 107 -122 -106
		mu 0 4 55 56 65 64
		f 4 106 109 -124 -108
		mu 0 4 56 57 66 65
		f 4 108 111 -126 -110
		mu 0 4 57 58 67 66
		f 4 110 113 -128 -112
		mu 0 4 58 59 68 67
		f 4 112 115 -130 -114
		mu 0 4 59 60 69 68
		f 4 114 117 -132 -116
		mu 0 4 60 61 70 69
		f 4 116 118 -134 -118
		mu 0 4 61 62 71 70
		f 4 119 122 -137 -121
		mu 0 4 63 64 73 72
		f 4 121 124 -138 -123
		mu 0 4 64 65 74 73
		f 4 123 126 -139 -125
		mu 0 4 65 66 75 74
		f 4 125 128 -140 -127
		mu 0 4 66 67 76 75
		f 4 127 130 -141 -129
		mu 0 4 67 68 77 76
		f 4 129 132 -142 -131
		mu 0 4 68 69 78 77
		f 4 131 134 -143 -133
		mu 0 4 69 70 79 78
		f 4 133 135 -144 -135
		mu 0 4 70 71 80 79;
	setAttr ".cd" -type "dataPolyComponent" Index_Data Edge 0 ;
	setAttr ".cvd" -type "dataPolyComponent" Index_Data Vertex 0 ;
	setAttr ".pd[0]" -type "dataPolyComponent" Index_Data UV 0 ;
	setAttr ".hfd" -type "dataPolyComponent" Index_Data Face 0 ;
createNode transform -n "templates" -p "rig";
	rename -uid "7836D098-41D8-50EC-0A4A-BFA769B74D39";
	setAttr ".v" no;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "F34C0B6C-4D63-B57A-6D3A-20A1D8F42442";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "615996E5-4C9C-F324-6716-35A765B82B8A";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "4444C016-4BD1-1E96-10DD-D29594C113CD";
createNode displayLayerManager -n "layerManager";
	rename -uid "2C93FDBB-49E3-C97A-B860-E08EA6055971";
createNode displayLayer -n "defaultLayer";
	rename -uid "3D00A9EB-4BFA-8B36-966D-4FB7814C294B";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "0F7D6D16-4C09-BD4B-8C90-B189F77D6C40";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "B6F0B6C4-4869-377F-8B98-2B87AB1F88AF";
	setAttr ".g" yes;
createNode skinCluster -n "skinCluster1";
	rename -uid "14089917-4319-8FC0-C8A0-32A7C35BA5EC";
	setAttr -s 81 ".wl";
	setAttr ".wl[0:80].w"
		3 0 0.016665011644363403 4 0.66670000553131104 9 0.31663498282432556
		3 0 0.066660001873970032 4 0.66670000553131104 9 0.26663999259471893
		3 0 0.16664999723434448 4 0.66670000553131104 9 0.16664999723434448
		3 0 0.26664000749588013 4 0.66670000553131104 9 0.066659986972808838
		4 0 0.29997000098228455 4 0.66670000553131104 5 0.016664996743202209 
		9 0.016664996743202209
		3 0 0.26664000749588013 4 0.66670000553131104 5 0.066659986972808838
		3 0 0.16664999723434448 4 0.66670000553131104 5 0.16664999723434448
		3 0 0.066660001873970032 4 0.66670000553131104 5 0.26663999259471893
		3 0 0.016665011644363403 4 0.66670000553131104 5 0.31663498282432556
		3 0 0.033330023288726807 4 0.33340001106262207 9 0.63326996564865112
		3 0 0.13332000374794006 4 0.33340001106262207 9 0.53327998518943787
		3 0 0.33329999446868896 4 0.33340001106262207 9 0.33329999446868896
		3 0 0.53328001499176025 4 0.33340001106262207 9 0.13331997394561768
		4 0 0.59994000196456909 4 0.33340001106262207 5 0.033329993486404419 
		9 0.033329993486404419
		3 0 0.53328001499176025 4 0.33340001106262207 5 0.13331997394561768
		3 0 0.33329999446868896 4 0.33340001106262207 5 0.33329999446868896
		3 0 0.13332000374794006 4 0.33340001106262207 5 0.53327998518943787
		3 0 0.033330023288726807 4 0.33340001106262207 5 0.63326996564865112
		5 0 0.028334997594356537 1 0.016665011644363403 4 0.10000000149011612 
		9 0.53836500644683838 10 0.31663498282432556
		5 0 0.11334000527858734 1 0.066660001873970032 4 0.10000000149011612 
		9 0.45335999876260757 10 0.26663999259471893
		5 0 0.28334999084472656 1 0.16664999723434448 4 0.10000000149011612 
		9 0.28335001319646835 10 0.16664999723434448
		5 0 0.45336002111434937 1 0.26664000749588013 4 0.10000000149011612 
		9 0.11333998292684555 10 0.066659986972808838
		7 0 0.51002997159957886 1 0.29997000098228455 4 0.10000000149011612 
		5 0.028335016220808029 6 0.016664996743202209 9 0.028335016220808029 
		10 0.016664996743202209
		5 0 0.45336002111434937 1 0.26664000749588013 4 0.10000000149011612 
		5 0.11333998292684555 6 0.066659986972808838
		5 0 0.28334999084472656 1 0.16664999723434448 4 0.10000000149011612 
		5 0.28335001319646835 6 0.16664999723434448
		5 0 0.11334000527858734 1 0.066660001873970032 4 0.10000000149011612 
		5 0.45335999876260757 6 0.26663999259471893
		5 0 0.028334997594356537 1 0.016665011644363403 4 0.10000000149011612 
		5 0.53836500644683838 6 0.31663498282432556
		4 0 0.016670018434524536 1 0.033330023288726807 9 0.31672999262809753 
		10 0.63326996564865112
		4 0 0.066680006682872772 1 0.13332000374794006 9 0.2667200043797493 
		10 0.53327998518943787
		4 0 0.16670000553131104 1 0.33329999446868896 9 0.16670000553131104 
		10 0.33329999446868896
		4 0 0.26672002673149109 1 0.53328001499176025 9 0.066679984331130981 
		10 0.13331997394561768
		6 0 0.30006000399589539 1 0.59994000196456909 5 0.016670003533363342 
		6 0.033329993486404419 9 0.016670003533363342 10 0.033329993486404419
		4 0 0.26672002673149109 1 0.53328001499176025 5 0.066679984331130981 
		6 0.13331997394561768
		4 0 0.16670000553131104 1 0.33329999446868896 5 0.16670000553131104 
		6 0.33329999446868896
		4 0 0.066680006682872772 1 0.13332000374794006 5 0.2667200043797493 
		6 0.53327998518943787
		4 0 0.016670018434524536 1 0.033330023288726807 5 0.31672999262809753 
		6 0.63326996564865112
		6 0 0.0050000026920928864 1 0.028334997553161712 2 0.016665011675674357 
		9 0.094999998807907104 10 0.53836500644683838 11 0.31663498282432556
		6 0 0.020000001415610313 1 0.11334000527858734 2 0.066660001873970032 
		9 0.080000000074505806 10 0.45335999876260757 11 0.26663999259471893
		6 0 0.05000000074505806 1 0.28334999084472656 2 0.16664999723434448 
		9 0.05000000074505806 10 0.28335001319646835 11 0.16664999723434448
		6 0 0.080000005662441254 1 0.45336002111434937 2 0.26664000749588013 
		9 0.019999995827674866 10 0.11333998292684555 11 0.066659986972808838
		9 0 0.08999999612569809 1 0.51002997159957886 2 0.29997000098228455 
		5 0.0050000026822090149 6 0.028335016220808029 7 0.016664996743202209 
		9 0.0050000026822090149 10 0.028335016220808029 11 0.016664996743202209
		6 0 0.080000005662441254 1 0.45336002111434937 2 0.26664000749588013 
		5 0.019999995827674866 6 0.11333998292684555 7 0.066659986972808838
		6 0 0.05000000074505806 1 0.28334999084472656 2 0.16664999723434448 
		5 0.05000000074505806 6 0.28335001319646835 7 0.16664999723434448
		6 0 0.020000001415610313 1 0.11334000527858734 2 0.066660001873970032 
		5 0.080000000074505806 6 0.45335999876260757 7 0.26663999259471893
		6 0 0.0050000026920928864 1 0.028334997553161712 2 0.016665011675674357 
		5 0.094999998807907104 6 0.53836500644683838 7 0.31663498282432556
		4 1 0.016670018434524536 2 0.033330023288726807 10 0.31672999262809753 
		11 0.63326996564865112
		4 1 0.066680006682872772 2 0.13332000374794006 10 0.2667200043797493 
		11 0.53327998518943787
		4 1 0.16670000553131104 2 0.33329999446868896 10 0.16670000553131104 
		11 0.33329999446868896
		4 1 0.26672002673149109 2 0.53328001499176025 10 0.066679984331130981 
		11 0.13331997394561768
		6 1 0.30006000399589539 2 0.59994000196456909 6 0.016670003533363342 
		7 0.033329993486404419 10 0.016670003533363342 11 0.033329993486404419
		4 1 0.26672002673149109 2 0.53328001499176025 6 0.066679984331130981 
		7 0.13331997394561768
		4 1 0.16670000553131104 2 0.33329999446868896 6 0.16670000553131104 
		7 0.33329999446868896
		4 1 0.066680006682872772 2 0.13332000374794006 6 0.2667200043797493 
		7 0.53327998518943787
		4 1 0.016670018434524536 2 0.033330023288726807 6 0.31672999262809753 
		7 0.63326996564865112
		6 1 0.0050000026822090149 2 0.028334997594356537 3 0.016665011644363403 
		10 0.094999998807907104 11 0.53836500644683838 12 0.31663498282432556
		6 1 0.020000001415610313 2 0.11334000527858734 3 0.066660001873970032 
		10 0.080000000074505806 11 0.45335999876260757 12 0.26663999259471893
		6 1 0.05000000074505806 2 0.28334999084472656 3 0.16664999723434448 
		10 0.05000000074505806 11 0.28335001319646835 12 0.16664999723434448
		6 1 0.080000005662441254 2 0.45336002111434937 3 0.26664000749588013 
		10 0.019999995827674866 11 0.11333998292684555 12 0.066659986972808838
		9 1 0.08999999612569809 2 0.51002997159957886 3 0.29997000098228455 
		6 0.0050000026822090149 7 0.028335016220808029 8 0.016664996743202209 
		10 0.0050000026822090149 11 0.028335016220808029 12 0.016664996743202209
		6 1 0.080000005662441254 2 0.45336002111434937 3 0.26664000749588013 
		6 0.019999995827674866 7 0.11333998292684555 8 0.066659986972808838
		6 1 0.05000000074505806 2 0.28334999084472656 3 0.16664999723434448 
		6 0.05000000074505806 7 0.28335001319646835 8 0.16664999723434448
		6 1 0.020000001415610313 2 0.11334000527858734 3 0.066660001873970032 
		6 0.080000000074505806 7 0.45335999876260757 8 0.26663999259471893
		6 1 0.0050000026822090149 2 0.028334997594356537 3 0.016665011644363403 
		6 0.094999998807907104 7 0.53836500644683838 8 0.31663498282432556
		4 2 0.016670018434524536 3 0.033330023288726807 11 0.31672999262809753 
		12 0.63326996564865112
		4 2 0.066680006682872772 3 0.13332000374794006 11 0.2667200043797493 
		12 0.53327998518943787
		4 2 0.16670000553131104 3 0.33329999446868896 11 0.16670000553131104 
		12 0.33329999446868896
		4 2 0.26672002673149109 3 0.53328001499176025 11 0.066679984331130981 
		12 0.13331997394561762
		6 2 0.30006000399589539 3 0.59994000196456909 7 0.016670003533363342 
		8 0.033329993486404419 11 0.016670003533363342 12 0.033329993486404419
		4 2 0.26672002673149109 3 0.53328001499176025 7 0.066679984331130981 
		8 0.13331997394561762
		4 2 0.16670000553131104 3 0.33329999446868896 7 0.16670000553131104 
		8 0.33329999446868896
		4 2 0.066680006682872772 3 0.13332000374794006 7 0.2667200043797493 
		8 0.53327998518943787
		4 2 0.016670018434524536 3 0.033330023288726807 7 0.31672999262809753 
		8 0.63326996564865112
		2 3 0.050000011920928955 12 0.94999998807907104
		2 3 0.20000000298023224 12 0.79999999701976776
		2 3 0.5 12 0.5
		2 3 0.80000001192092896 12 0.19999998807907104
		3 3 0.89999997615814209 8 0.050000011920928955 12 0.050000011920928955
		2 3 0.80000001192092896 8 0.19999998807907104
		2 3 0.5 8 0.5
		2 3 0.20000000298023224 8 0.79999999701976776
		2 3 0.050000011920928955 8 0.94999998807907104;
	setAttr -s 13 ".pm";
	setAttr ".pm[0]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 5 -0.5 0 1;
	setAttr ".pm[1]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 2.5 -0.5 0 1;
	setAttr ".pm[2]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 0 -0.5 0 1;
	setAttr ".pm[3]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 -2.5 -0.5 0 1;
	setAttr ".pm[4]" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0 0 1;
	setAttr ".pm[5]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 5 -0.5 -5 1;
	setAttr ".pm[6]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 2.5 -0.5 -5 1;
	setAttr ".pm[7]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 0 -0.5 -5 1;
	setAttr ".pm[8]" -type "matrix" 0 0 1 0 0 1 0 0 -1 0 0 0 -2.5 -0.5 -5 1;
	setAttr ".pm[9]" -type "matrix" 0 1.2246467991473532e-16 1 0 0 -1 1.2246467991473532e-16 0
		 1 0 0 0 -5 0.50000000000000067 5 1;
	setAttr ".pm[10]" -type "matrix" 0 1.2246467991473532e-16 1 0 0 -1 1.2246467991473532e-16 0
		 1 0 0 0 -2.5 0.50000000000000067 5 1;
	setAttr ".pm[11]" -type "matrix" 0 1.2246467991473532e-16 1 0 0 -1 1.2246467991473532e-16 0
		 1 0 0 0 0 0.50000000000000067 5 1;
	setAttr ".pm[12]" -type "matrix" 0 1.2246467991473532e-16 1 0 0 -1 1.2246467991473532e-16 0
		 1 0 0 0 2.5 0.50000000000000067 5 1;
	setAttr ".gm" -type "matrix" 1 0 0 0 0 1 0 0 0 0 1 0 0 0.5 0 1;
	setAttr -s 13 ".ma";
	setAttr -s 13 ".dpf[0:12]"  4 4 4 4 4 4 4 4 4 4 4 4 4;
	setAttr ".smt[0]"  0;
	setAttr -s 13 ".lw";
	setAttr -s 13 ".lw";
	setAttr ".mi" 5;
	setAttr ".bm" 1;
	setAttr ".ucm" yes;
	setAttr -s 13 ".ifcl";
	setAttr -s 13 ".ifcl";
createNode tweak -n "tweak1";
	rename -uid "DEAC6803-472D-BAC7-F036-6AA6C62B5442";
createNode objectSet -n "skinCluster1Set";
	rename -uid "7EB3BCBC-4899-4893-812C-8CA975DFF5B6";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "skinCluster1GroupId";
	rename -uid "45AC0D83-4B93-0840-897E-99892803B1C8";
	setAttr ".ihi" 0;
createNode groupParts -n "skinCluster1GroupParts";
	rename -uid "FA3CEC38-4BA2-164E-4205-AAA5DAC23BB4";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode objectSet -n "tweakSet1";
	rename -uid "9DAD6718-458C-FFE5-E9DB-6AA365C556AD";
	setAttr ".ihi" 0;
	setAttr ".vo" yes;
createNode groupId -n "groupId2";
	rename -uid "806E2E19-482B-1B50-50BB-72953AECF3C6";
	setAttr ".ihi" 0;
createNode groupParts -n "groupParts2";
	rename -uid "2A7C49AE-4E09-D6C9-713A-B8899E46CC18";
	setAttr ".ihi" 0;
	setAttr ".ic" -type "componentList" 1 "vtx[*]";
createNode dagPose -n "bindPose1";
	rename -uid "98CFD528-467A-8A55-D9A4-9AB61BEAE142";
	setAttr -s 13 ".wm";
	setAttr -s 13 ".xm";
	setAttr ".xm[0]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0.5 5 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0.70710678118654757 0 0.70710678118654757 1 1 1 yes;
	setAttr ".xm[1]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[2]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[3]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[4]" -type "matrix" "xform" 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[5]" -type "matrix" "xform" 1 1 1 0 0 0 0 5 0.5 5 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0.70710678118654757 0 0.70710678118654757 1 1 1 yes;
	setAttr ".xm[6]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[7]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[8]" -type "matrix" "xform" 1 1 1 0 0 0 0 2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[9]" -type "matrix" "xform" 1 1 1 0 0 0 0 -5 0.5 5 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 -0.70710678118654757 -4.3297802811774664e-17 -0.70710678118654757 4.3297802811774664e-17 1
		 1 1 yes;
	setAttr ".xm[10]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[11]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr ".xm[12]" -type "matrix" "xform" 1 1 1 0 0 0 0 -2.5 0 0 0 0 0 0 0 0 0
		 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 1 1 1 yes;
	setAttr -s 13 ".m";
	setAttr -s 13 ".p";
	setAttr ".bp" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "D55F3A8B-41C5-7DCE-A086-4892EBBD3CFE";
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
		+ "            -wireframeOnShaded 0\n            -headsUpDisplay 1\n            -holdOuts 1\n            -selectionHiliteDisplay 1\n            -useDefaultMaterial 0\n            -bufferMode \"double\" \n            -twoSidedLighting 0\n            -backfaceCulling 0\n            -xray 0\n            -jointXray 0\n            -activeComponentsXray 0\n            -displayTextures 0\n            -smoothWireframe 0\n            -lineWidth 1\n            -textureAnisotropic 0\n            -textureHilight 1\n            -textureSampling 2\n            -textureDisplay \"modulate\" \n            -textureMaxSize 32768\n            -fogging 0\n            -fogSource \"fragment\" \n            -fogMode \"linear\" \n            -fogStart 0\n            -fogEnd 100\n            -fogDensity 0.1\n            -fogColor 0.5 0.5 0.5 1 \n            -depthOfFieldPreview 1\n            -maxConstantTransparency 1\n            -rendererName \"vp2Renderer\" \n            -objectFilterShowInHUD 1\n            -isFiltered 0\n            -colorResolution 256 256 \n            -bumpResolution 512 512 \n"
		+ "            -textureCompression 0\n            -transparencyAlgorithm \"frontAndBackCull\" \n            -transpInShadows 0\n            -cullingOverride \"none\" \n            -lowQualityLighting 0\n            -maximumNumHardwareLights 1\n            -occlusionCulling 0\n            -shadingModel 0\n            -useBaseRenderer 0\n            -useReducedRenderer 0\n            -smallObjectCulling 0\n            -smallObjectThreshold -1 \n            -interactiveDisableShadows 0\n            -interactiveBackFaceCull 0\n            -sortTransparent 1\n            -controllers 1\n            -nurbsCurves 1\n            -nurbsSurfaces 1\n            -polymeshes 1\n            -subdivSurfaces 1\n            -planes 1\n            -lights 1\n            -cameras 1\n            -controlVertices 1\n            -hulls 1\n            -grid 1\n            -imagePlane 1\n            -joints 1\n            -ikHandles 1\n            -deformers 1\n            -dynamics 1\n            -particleInstancers 1\n            -fluids 1\n            -hairSystems 1\n            -follicles 1\n"
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1319\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "A42895DB-4998-14FB-B02B-08A7E09D1CE2";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 26 -ast 1 -aet 26 ";
	setAttr ".st" 6;
createNode animCurveTA -n "lf_:Fk_00_off_rotateX";
	rename -uid "BC67DEB2-415F-7025-32FD-0DB7ED5936AA";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 4 ".ktv[0:3]"  0 0 2 1.2 8 -1.2 10 0;
	setAttr -s 4 ".kit[0:3]"  1 18 18 1;
	setAttr -s 4 ".kot[0:3]"  1 18 18 1;
	setAttr -s 4 ".kix[0:3]"  0.95047776422584851 1 1 0.95047780594358711;
	setAttr -s 4 ".kiy[0:3]"  0.31079256701573843 0 0 0.3107924394329194;
	setAttr -s 4 ".kox[0:3]"  0.9504777643358916 1 1 0.95047775791377043;
	setAttr -s 4 ".koy[0:3]"  0.31079256667920047 0 0 0.31079258631957724;
	setAttr ".pre" 4;
	setAttr ".pst" 4;
createNode animCurveTA -n "lf_:Fk_00_off_rotateZ";
	rename -uid "771015BF-47E4-900A-8817-B7A7D88E4931";
	setAttr ".tan" 18;
	setAttr ".wgt" no;
	setAttr -s 3 ".ktv[0:2]"  0 0 5 1 10 0;
	setAttr ".pre" 4;
	setAttr ".pst" 4;
createNode unitConversion -n "lf_:Fk_Pos_off_rotateX";
	rename -uid "9BCC01E2-4B4B-9D2B-4EE7-E8B1BCAFEF1C";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion2";
	rename -uid "24FCB97D-4C96-E2F4-C349-94921BAABD5F";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "pos_Fk_00_mdv";
	rename -uid "F044D17B-4234-A6EE-1F9A-B4A82933BCB2";
createNode unitConversion -n "lf_:Fk_Pos_off_rotateZ";
	rename -uid "D7F22B97-4C46-ED73-35BA-2C93434BAD54";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion4";
	rename -uid "3DE9EE04-43CC-6360-D6E7-DAAF45593F50";
	setAttr ".cf" 0.017453292519943295;
createNode unitToTimeConversion -n "unitToTimeConversion1";
	rename -uid "5FBF3897-4FFC-8DB1-0077-519BA52CB1EB";
	setAttr ".cf" 250;
createNode unitConversion -n "lf_:Fk_Neg_off_rotateX";
	rename -uid "46FD13E0-485B-5040-777B-3BB4AB9EE1F9";
	setAttr ".cf" -57.296;
createNode unitConversion -n "lf_:Fk_Neg_off_rotateZ";
	rename -uid "35CE7EDB-44F7-86E7-F642-EE9E89001A42";
	setAttr ".cf" -57.296;
createNode multiplyDivide -n "neg_Fk_00_mdv";
	rename -uid "CF3CEB5F-4DC4-A2AB-DE8F-3AB3CF18F38E";
createNode unitConversion -n "unitConversion5";
	rename -uid "48D55510-4EC3-0B63-9BB0-569686BF026E";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion6";
	rename -uid "43646AD5-40F6-E906-3039-FCA0F7F84D06";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "pos_Fk_01_mdv";
	rename -uid "9B0C6E51-4DBA-506C-8684-E8B134994D0D";
createNode unitConversion -n "unitConversion7";
	rename -uid "555FA3C7-4E4D-CC14-B6CC-94A8270A0AA5";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion8";
	rename -uid "07FE8667-45F0-CD1F-73B1-A3B3FF18D7B4";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "neg_Fk_01_mdv";
	rename -uid "28AEEC75-459A-E5BC-DD07-3D9184644229";
createNode unitConversion -n "unitConversion9";
	rename -uid "9A8A1036-4941-09BD-C50F-15B9507AC605";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion10";
	rename -uid "AB2CAECA-4728-B115-CC65-44B7D372BEFA";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "neg_Fk_02_mdv";
	rename -uid "C1ED299E-4DF9-60A2-5227-F08EFA6A7245";
createNode multiplyDivide -n "pos_Fk_02_mdv";
	rename -uid "60EB5E75-487E-ECB6-81F7-22835AC8333E";
createNode unitConversion -n "unitConversion11";
	rename -uid "21246C42-4365-5B85-BBED-6FB8EB790181";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion12";
	rename -uid "65AAC1E9-42B1-B05E-AD58-FA95F1F51E7C";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion13";
	rename -uid "214B550D-42CF-B58F-4500-838FF8D19C7B";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion14";
	rename -uid "762577FB-4A92-64D5-1531-A1A8621A17E9";
	setAttr ".cf" 0.017453292519943295;
createNode multiplyDivide -n "pos_Fk_03_mdv";
	rename -uid "F33805B1-4EAA-173C-63B3-C0A9E13D87A3";
createNode multiplyDivide -n "neg_Fk_03_mdv";
	rename -uid "CCD6BA6B-4343-1E7C-C02E-8691586C74CE";
createNode unitConversion -n "unitConversion15";
	rename -uid "5EF8ED35-43D0-1D1E-F0E2-3E998AD8D9F2";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion16";
	rename -uid "1E600636-4CD2-6640-F07C-6D8B84792820";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion17";
	rename -uid "D9FC135D-4807-78AD-3F87-7196771C32E8";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion18";
	rename -uid "BA962434-459B-B134-3561-FBBCAA691F37";
	setAttr ".cf" 0.017453292519943295;
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "A7211622-489C-3741-6A03-58A6DAC4950D";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 11413.477847230677 -3333.3332008785719 ;
	setAttr ".tgi[0].vh" -type "double2" 12987.711659343646 -2555.9522793879623 ;
	setAttr -s 17 ".tgi[0].ni";
	setAttr ".tgi[0].ni[0].x" 12862.857421875;
	setAttr ".tgi[0].ni[0].y" -2581.428466796875;
	setAttr ".tgi[0].ni[0].nvs" 18304;
	setAttr ".tgi[0].ni[1].x" 11941.4287109375;
	setAttr ".tgi[0].ni[1].y" -2884.28564453125;
	setAttr ".tgi[0].ni[1].nvs" 18304;
	setAttr ".tgi[0].ni[2].x" 12862.857421875;
	setAttr ".tgi[0].ni[2].y" -3218.571533203125;
	setAttr ".tgi[0].ni[2].nvs" 18304;
	setAttr ".tgi[0].ni[3].x" 11634.2861328125;
	setAttr ".tgi[0].ni[3].y" -2708.571533203125;
	setAttr ".tgi[0].ni[3].nvs" 18304;
	setAttr ".tgi[0].ni[4].x" 11941.4287109375;
	setAttr ".tgi[0].ni[4].y" -2761.428466796875;
	setAttr ".tgi[0].ni[4].nvs" 18304;
	setAttr ".tgi[0].ni[5].x" 11941.4287109375;
	setAttr ".tgi[0].ni[5].y" -2458.571533203125;
	setAttr ".tgi[0].ni[5].nvs" 18304;
	setAttr ".tgi[0].ni[6].x" 12862.857421875;
	setAttr ".tgi[0].ni[6].y" -3341.428466796875;
	setAttr ".tgi[0].ni[6].nvs" 18304;
	setAttr ".tgi[0].ni[7].x" 12555.7138671875;
	setAttr ".tgi[0].ni[7].y" -2544.28564453125;
	setAttr ".tgi[0].ni[7].nvs" 18304;
	setAttr ".tgi[0].ni[8].x" 12555.7138671875;
	setAttr ".tgi[0].ni[8].y" -2702.857177734375;
	setAttr ".tgi[0].ni[8].nvs" 18304;
	setAttr ".tgi[0].ni[9].x" 12555.7138671875;
	setAttr ".tgi[0].ni[9].y" -3221.428466796875;
	setAttr ".tgi[0].ni[9].nvs" 18304;
	setAttr ".tgi[0].ni[10].x" 12555.7138671875;
	setAttr ".tgi[0].ni[10].y" -3062.857177734375;
	setAttr ".tgi[0].ni[10].nvs" 18304;
	setAttr ".tgi[0].ni[11].x" 11020;
	setAttr ".tgi[0].ni[11].y" -2612.857177734375;
	setAttr ".tgi[0].ni[11].nvs" 18304;
	setAttr ".tgi[0].ni[12].x" 11634.2861328125;
	setAttr ".tgi[0].ni[12].y" -2585.71435546875;
	setAttr ".tgi[0].ni[12].nvs" 18304;
	setAttr ".tgi[0].ni[13].x" 12248.5712890625;
	setAttr ".tgi[0].ni[13].y" -2487.142822265625;
	setAttr ".tgi[0].ni[13].nvs" 18304;
	setAttr ".tgi[0].ni[14].x" 11327.142578125;
	setAttr ".tgi[0].ni[14].y" -2660;
	setAttr ".tgi[0].ni[14].nvs" 18304;
	setAttr ".tgi[0].ni[15].x" 12248.5712890625;
	setAttr ".tgi[0].ni[15].y" -3028.571533203125;
	setAttr ".tgi[0].ni[15].nvs" 18304;
	setAttr ".tgi[0].ni[16].x" 11941.4287109375;
	setAttr ".tgi[0].ni[16].y" -2581.428466796875;
	setAttr ".tgi[0].ni[16].nvs" 18304;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".msaa" yes;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 5 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderUtilityList1;
	setAttr -s 8 ".u";
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
connectAttr "cn_:Fk_00_jnt_scaleConstraint1.csx" "cn_:Fk_00_jnt.sx";
connectAttr "cn_:Fk_00_jnt_scaleConstraint1.csy" "cn_:Fk_00_jnt.sy";
connectAttr "cn_:Fk_00_jnt_scaleConstraint1.csz" "cn_:Fk_00_jnt.sz";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.ctx" "cn_:Fk_00_jnt.tx";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.cty" "cn_:Fk_00_jnt.ty";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.ctz" "cn_:Fk_00_jnt.tz";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.crx" "cn_:Fk_00_jnt.rx";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.cry" "cn_:Fk_00_jnt.ry";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.crz" "cn_:Fk_00_jnt.rz";
connectAttr "cn_:Hold_00_jnt.s" "cn_:Fk_00_jnt.is";
connectAttr "cn_:Fk_00_jnt.s" "cn_:Fk_01_jnt.is";
connectAttr "cn_:Fk_01_jnt_scaleConstraint1.csx" "cn_:Fk_01_jnt.sx";
connectAttr "cn_:Fk_01_jnt_scaleConstraint1.csy" "cn_:Fk_01_jnt.sy";
connectAttr "cn_:Fk_01_jnt_scaleConstraint1.csz" "cn_:Fk_01_jnt.sz";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.ctx" "cn_:Fk_01_jnt.tx";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.cty" "cn_:Fk_01_jnt.ty";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.ctz" "cn_:Fk_01_jnt.tz";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.crx" "cn_:Fk_01_jnt.rx";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.cry" "cn_:Fk_01_jnt.ry";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.crz" "cn_:Fk_01_jnt.rz";
connectAttr "cn_:Fk_01_jnt.s" "cn_:Fk_02_jnt.is";
connectAttr "cn_:Fk_02_jnt_scaleConstraint1.csx" "cn_:Fk_02_jnt.sx";
connectAttr "cn_:Fk_02_jnt_scaleConstraint1.csy" "cn_:Fk_02_jnt.sy";
connectAttr "cn_:Fk_02_jnt_scaleConstraint1.csz" "cn_:Fk_02_jnt.sz";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.ctx" "cn_:Fk_02_jnt.tx";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.cty" "cn_:Fk_02_jnt.ty";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.ctz" "cn_:Fk_02_jnt.tz";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.crx" "cn_:Fk_02_jnt.rx";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.cry" "cn_:Fk_02_jnt.ry";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.crz" "cn_:Fk_02_jnt.rz";
connectAttr "cn_:Fk_02_jnt.s" "cn_:Fk_03_jnt.is";
connectAttr "cn_:Fk_03_jnt_scaleConstraint1.csx" "cn_:Fk_03_jnt.sx";
connectAttr "cn_:Fk_03_jnt_scaleConstraint1.csy" "cn_:Fk_03_jnt.sy";
connectAttr "cn_:Fk_03_jnt_scaleConstraint1.csz" "cn_:Fk_03_jnt.sz";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.ctx" "cn_:Fk_03_jnt.tx";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.cty" "cn_:Fk_03_jnt.ty";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.ctz" "cn_:Fk_03_jnt.tz";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.crx" "cn_:Fk_03_jnt.rx";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.cry" "cn_:Fk_03_jnt.ry";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.crz" "cn_:Fk_03_jnt.rz";
connectAttr "cn_:Fk_03_jnt.ro" "cn_:Fk_03_jnt_parentConstraint1.cro";
connectAttr "cn_:Fk_03_jnt.pim" "cn_:Fk_03_jnt_parentConstraint1.cpim";
connectAttr "cn_:Fk_03_jnt.rp" "cn_:Fk_03_jnt_parentConstraint1.crp";
connectAttr "cn_:Fk_03_jnt.rpt" "cn_:Fk_03_jnt_parentConstraint1.crt";
connectAttr "cn_:Fk_03_jnt.jo" "cn_:Fk_03_jnt_parentConstraint1.cjo";
connectAttr "cn_:Fk_03_ctr.t" "cn_:Fk_03_jnt_parentConstraint1.tg[0].tt";
connectAttr "cn_:Fk_03_ctr.rp" "cn_:Fk_03_jnt_parentConstraint1.tg[0].trp";
connectAttr "cn_:Fk_03_ctr.rpt" "cn_:Fk_03_jnt_parentConstraint1.tg[0].trt";
connectAttr "cn_:Fk_03_ctr.r" "cn_:Fk_03_jnt_parentConstraint1.tg[0].tr";
connectAttr "cn_:Fk_03_ctr.ro" "cn_:Fk_03_jnt_parentConstraint1.tg[0].tro";
connectAttr "cn_:Fk_03_ctr.s" "cn_:Fk_03_jnt_parentConstraint1.tg[0].ts";
connectAttr "cn_:Fk_03_ctr.pm" "cn_:Fk_03_jnt_parentConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_03_jnt_parentConstraint1.w0" "cn_:Fk_03_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_03_jnt.ssc" "cn_:Fk_03_jnt_scaleConstraint1.tsc";
connectAttr "cn_:Fk_03_jnt.pim" "cn_:Fk_03_jnt_scaleConstraint1.cpim";
connectAttr "cn_:Fk_03_ctr.s" "cn_:Fk_03_jnt_scaleConstraint1.tg[0].ts";
connectAttr "cn_:Fk_03_ctr.pm" "cn_:Fk_03_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_03_jnt_scaleConstraint1.w0" "cn_:Fk_03_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_02_jnt.ro" "cn_:Fk_02_jnt_parentConstraint1.cro";
connectAttr "cn_:Fk_02_jnt.pim" "cn_:Fk_02_jnt_parentConstraint1.cpim";
connectAttr "cn_:Fk_02_jnt.rp" "cn_:Fk_02_jnt_parentConstraint1.crp";
connectAttr "cn_:Fk_02_jnt.rpt" "cn_:Fk_02_jnt_parentConstraint1.crt";
connectAttr "cn_:Fk_02_jnt.jo" "cn_:Fk_02_jnt_parentConstraint1.cjo";
connectAttr "cn_:Fk_02_ctr.t" "cn_:Fk_02_jnt_parentConstraint1.tg[0].tt";
connectAttr "cn_:Fk_02_ctr.rp" "cn_:Fk_02_jnt_parentConstraint1.tg[0].trp";
connectAttr "cn_:Fk_02_ctr.rpt" "cn_:Fk_02_jnt_parentConstraint1.tg[0].trt";
connectAttr "cn_:Fk_02_ctr.r" "cn_:Fk_02_jnt_parentConstraint1.tg[0].tr";
connectAttr "cn_:Fk_02_ctr.ro" "cn_:Fk_02_jnt_parentConstraint1.tg[0].tro";
connectAttr "cn_:Fk_02_ctr.s" "cn_:Fk_02_jnt_parentConstraint1.tg[0].ts";
connectAttr "cn_:Fk_02_ctr.pm" "cn_:Fk_02_jnt_parentConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_02_jnt_parentConstraint1.w0" "cn_:Fk_02_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_02_jnt.ssc" "cn_:Fk_02_jnt_scaleConstraint1.tsc";
connectAttr "cn_:Fk_02_jnt.pim" "cn_:Fk_02_jnt_scaleConstraint1.cpim";
connectAttr "cn_:Fk_02_ctr.s" "cn_:Fk_02_jnt_scaleConstraint1.tg[0].ts";
connectAttr "cn_:Fk_02_ctr.pm" "cn_:Fk_02_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_02_jnt_scaleConstraint1.w0" "cn_:Fk_02_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_01_jnt.ro" "cn_:Fk_01_jnt_parentConstraint1.cro";
connectAttr "cn_:Fk_01_jnt.pim" "cn_:Fk_01_jnt_parentConstraint1.cpim";
connectAttr "cn_:Fk_01_jnt.rp" "cn_:Fk_01_jnt_parentConstraint1.crp";
connectAttr "cn_:Fk_01_jnt.rpt" "cn_:Fk_01_jnt_parentConstraint1.crt";
connectAttr "cn_:Fk_01_jnt.jo" "cn_:Fk_01_jnt_parentConstraint1.cjo";
connectAttr "cn_:Fk_01_ctr.t" "cn_:Fk_01_jnt_parentConstraint1.tg[0].tt";
connectAttr "cn_:Fk_01_ctr.rp" "cn_:Fk_01_jnt_parentConstraint1.tg[0].trp";
connectAttr "cn_:Fk_01_ctr.rpt" "cn_:Fk_01_jnt_parentConstraint1.tg[0].trt";
connectAttr "cn_:Fk_01_ctr.r" "cn_:Fk_01_jnt_parentConstraint1.tg[0].tr";
connectAttr "cn_:Fk_01_ctr.ro" "cn_:Fk_01_jnt_parentConstraint1.tg[0].tro";
connectAttr "cn_:Fk_01_ctr.s" "cn_:Fk_01_jnt_parentConstraint1.tg[0].ts";
connectAttr "cn_:Fk_01_ctr.pm" "cn_:Fk_01_jnt_parentConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_01_jnt_parentConstraint1.w0" "cn_:Fk_01_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_01_jnt.ssc" "cn_:Fk_01_jnt_scaleConstraint1.tsc";
connectAttr "cn_:Fk_01_jnt.pim" "cn_:Fk_01_jnt_scaleConstraint1.cpim";
connectAttr "cn_:Fk_01_ctr.s" "cn_:Fk_01_jnt_scaleConstraint1.tg[0].ts";
connectAttr "cn_:Fk_01_ctr.pm" "cn_:Fk_01_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_01_jnt_scaleConstraint1.w0" "cn_:Fk_01_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_00_jnt.ro" "cn_:Fk_00_jnt_parentConstraint1.cro";
connectAttr "cn_:Fk_00_jnt.pim" "cn_:Fk_00_jnt_parentConstraint1.cpim";
connectAttr "cn_:Fk_00_jnt.rp" "cn_:Fk_00_jnt_parentConstraint1.crp";
connectAttr "cn_:Fk_00_jnt.rpt" "cn_:Fk_00_jnt_parentConstraint1.crt";
connectAttr "cn_:Fk_00_jnt.jo" "cn_:Fk_00_jnt_parentConstraint1.cjo";
connectAttr "cn_:Fk_00_ctr.t" "cn_:Fk_00_jnt_parentConstraint1.tg[0].tt";
connectAttr "cn_:Fk_00_ctr.rp" "cn_:Fk_00_jnt_parentConstraint1.tg[0].trp";
connectAttr "cn_:Fk_00_ctr.rpt" "cn_:Fk_00_jnt_parentConstraint1.tg[0].trt";
connectAttr "cn_:Fk_00_ctr.r" "cn_:Fk_00_jnt_parentConstraint1.tg[0].tr";
connectAttr "cn_:Fk_00_ctr.ro" "cn_:Fk_00_jnt_parentConstraint1.tg[0].tro";
connectAttr "cn_:Fk_00_ctr.s" "cn_:Fk_00_jnt_parentConstraint1.tg[0].ts";
connectAttr "cn_:Fk_00_ctr.pm" "cn_:Fk_00_jnt_parentConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_00_jnt_parentConstraint1.w0" "cn_:Fk_00_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "cn_:Fk_00_jnt.pim" "cn_:Fk_00_jnt_scaleConstraint1.cpim";
connectAttr "cn_:Fk_00_ctr.s" "cn_:Fk_00_jnt_scaleConstraint1.tg[0].ts";
connectAttr "cn_:Fk_00_ctr.pm" "cn_:Fk_00_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "cn_:Fk_00_jnt_scaleConstraint1.w0" "cn_:Fk_00_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_00_jnt_scaleConstraint1.csx" "lf_:Fk_00_jnt.sx";
connectAttr "lf_:Fk_00_jnt_scaleConstraint1.csy" "lf_:Fk_00_jnt.sy";
connectAttr "lf_:Fk_00_jnt_scaleConstraint1.csz" "lf_:Fk_00_jnt.sz";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.ctx" "lf_:Fk_00_jnt.tx";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.cty" "lf_:Fk_00_jnt.ty";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.ctz" "lf_:Fk_00_jnt.tz";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.crx" "lf_:Fk_00_jnt.rx";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.cry" "lf_:Fk_00_jnt.ry";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.crz" "lf_:Fk_00_jnt.rz";
connectAttr "cn_:Hold_00_jnt.s" "lf_:Fk_00_jnt.is";
connectAttr "lf_:Fk_00_jnt.s" "lf_:Fk_01_jnt.is";
connectAttr "lf_:Fk_01_jnt_scaleConstraint1.csx" "lf_:Fk_01_jnt.sx";
connectAttr "lf_:Fk_01_jnt_scaleConstraint1.csy" "lf_:Fk_01_jnt.sy";
connectAttr "lf_:Fk_01_jnt_scaleConstraint1.csz" "lf_:Fk_01_jnt.sz";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.ctx" "lf_:Fk_01_jnt.tx";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.cty" "lf_:Fk_01_jnt.ty";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.ctz" "lf_:Fk_01_jnt.tz";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.crx" "lf_:Fk_01_jnt.rx";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.cry" "lf_:Fk_01_jnt.ry";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.crz" "lf_:Fk_01_jnt.rz";
connectAttr "lf_:Fk_01_jnt.s" "lf_:Fk_02_jnt.is";
connectAttr "lf_:Fk_02_jnt_scaleConstraint1.csx" "lf_:Fk_02_jnt.sx";
connectAttr "lf_:Fk_02_jnt_scaleConstraint1.csy" "lf_:Fk_02_jnt.sy";
connectAttr "lf_:Fk_02_jnt_scaleConstraint1.csz" "lf_:Fk_02_jnt.sz";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.ctx" "lf_:Fk_02_jnt.tx";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.cty" "lf_:Fk_02_jnt.ty";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.ctz" "lf_:Fk_02_jnt.tz";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.crx" "lf_:Fk_02_jnt.rx";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.cry" "lf_:Fk_02_jnt.ry";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.crz" "lf_:Fk_02_jnt.rz";
connectAttr "lf_:Fk_02_jnt.s" "lf_:Fk_03_jnt.is";
connectAttr "lf_:Fk_03_jnt_scaleConstraint1.csx" "lf_:Fk_03_jnt.sx";
connectAttr "lf_:Fk_03_jnt_scaleConstraint1.csy" "lf_:Fk_03_jnt.sy";
connectAttr "lf_:Fk_03_jnt_scaleConstraint1.csz" "lf_:Fk_03_jnt.sz";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.ctx" "lf_:Fk_03_jnt.tx";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.cty" "lf_:Fk_03_jnt.ty";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.ctz" "lf_:Fk_03_jnt.tz";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.crx" "lf_:Fk_03_jnt.rx";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.cry" "lf_:Fk_03_jnt.ry";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.crz" "lf_:Fk_03_jnt.rz";
connectAttr "lf_:Fk_03_jnt.ro" "lf_:Fk_03_jnt_parentConstraint1.cro";
connectAttr "lf_:Fk_03_jnt.pim" "lf_:Fk_03_jnt_parentConstraint1.cpim";
connectAttr "lf_:Fk_03_jnt.rp" "lf_:Fk_03_jnt_parentConstraint1.crp";
connectAttr "lf_:Fk_03_jnt.rpt" "lf_:Fk_03_jnt_parentConstraint1.crt";
connectAttr "lf_:Fk_03_jnt.jo" "lf_:Fk_03_jnt_parentConstraint1.cjo";
connectAttr "lf_:Fk_03_ctr.t" "lf_:Fk_03_jnt_parentConstraint1.tg[0].tt";
connectAttr "lf_:Fk_03_ctr.rp" "lf_:Fk_03_jnt_parentConstraint1.tg[0].trp";
connectAttr "lf_:Fk_03_ctr.rpt" "lf_:Fk_03_jnt_parentConstraint1.tg[0].trt";
connectAttr "lf_:Fk_03_ctr.r" "lf_:Fk_03_jnt_parentConstraint1.tg[0].tr";
connectAttr "lf_:Fk_03_ctr.ro" "lf_:Fk_03_jnt_parentConstraint1.tg[0].tro";
connectAttr "lf_:Fk_03_ctr.s" "lf_:Fk_03_jnt_parentConstraint1.tg[0].ts";
connectAttr "lf_:Fk_03_ctr.pm" "lf_:Fk_03_jnt_parentConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_03_jnt_parentConstraint1.w0" "lf_:Fk_03_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_03_jnt.ssc" "lf_:Fk_03_jnt_scaleConstraint1.tsc";
connectAttr "lf_:Fk_03_jnt.pim" "lf_:Fk_03_jnt_scaleConstraint1.cpim";
connectAttr "lf_:Fk_03_ctr.s" "lf_:Fk_03_jnt_scaleConstraint1.tg[0].ts";
connectAttr "lf_:Fk_03_ctr.pm" "lf_:Fk_03_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_03_jnt_scaleConstraint1.w0" "lf_:Fk_03_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_02_jnt.ro" "lf_:Fk_02_jnt_parentConstraint1.cro";
connectAttr "lf_:Fk_02_jnt.pim" "lf_:Fk_02_jnt_parentConstraint1.cpim";
connectAttr "lf_:Fk_02_jnt.rp" "lf_:Fk_02_jnt_parentConstraint1.crp";
connectAttr "lf_:Fk_02_jnt.rpt" "lf_:Fk_02_jnt_parentConstraint1.crt";
connectAttr "lf_:Fk_02_jnt.jo" "lf_:Fk_02_jnt_parentConstraint1.cjo";
connectAttr "lf_:Fk_02_ctr.t" "lf_:Fk_02_jnt_parentConstraint1.tg[0].tt";
connectAttr "lf_:Fk_02_ctr.rp" "lf_:Fk_02_jnt_parentConstraint1.tg[0].trp";
connectAttr "lf_:Fk_02_ctr.rpt" "lf_:Fk_02_jnt_parentConstraint1.tg[0].trt";
connectAttr "lf_:Fk_02_ctr.r" "lf_:Fk_02_jnt_parentConstraint1.tg[0].tr";
connectAttr "lf_:Fk_02_ctr.ro" "lf_:Fk_02_jnt_parentConstraint1.tg[0].tro";
connectAttr "lf_:Fk_02_ctr.s" "lf_:Fk_02_jnt_parentConstraint1.tg[0].ts";
connectAttr "lf_:Fk_02_ctr.pm" "lf_:Fk_02_jnt_parentConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_02_jnt_parentConstraint1.w0" "lf_:Fk_02_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_02_jnt.ssc" "lf_:Fk_02_jnt_scaleConstraint1.tsc";
connectAttr "lf_:Fk_02_jnt.pim" "lf_:Fk_02_jnt_scaleConstraint1.cpim";
connectAttr "lf_:Fk_02_ctr.s" "lf_:Fk_02_jnt_scaleConstraint1.tg[0].ts";
connectAttr "lf_:Fk_02_ctr.pm" "lf_:Fk_02_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_02_jnt_scaleConstraint1.w0" "lf_:Fk_02_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_01_jnt.ro" "lf_:Fk_01_jnt_parentConstraint1.cro";
connectAttr "lf_:Fk_01_jnt.pim" "lf_:Fk_01_jnt_parentConstraint1.cpim";
connectAttr "lf_:Fk_01_jnt.rp" "lf_:Fk_01_jnt_parentConstraint1.crp";
connectAttr "lf_:Fk_01_jnt.rpt" "lf_:Fk_01_jnt_parentConstraint1.crt";
connectAttr "lf_:Fk_01_jnt.jo" "lf_:Fk_01_jnt_parentConstraint1.cjo";
connectAttr "lf_:Fk_01_ctr.t" "lf_:Fk_01_jnt_parentConstraint1.tg[0].tt";
connectAttr "lf_:Fk_01_ctr.rp" "lf_:Fk_01_jnt_parentConstraint1.tg[0].trp";
connectAttr "lf_:Fk_01_ctr.rpt" "lf_:Fk_01_jnt_parentConstraint1.tg[0].trt";
connectAttr "lf_:Fk_01_ctr.r" "lf_:Fk_01_jnt_parentConstraint1.tg[0].tr";
connectAttr "lf_:Fk_01_ctr.ro" "lf_:Fk_01_jnt_parentConstraint1.tg[0].tro";
connectAttr "lf_:Fk_01_ctr.s" "lf_:Fk_01_jnt_parentConstraint1.tg[0].ts";
connectAttr "lf_:Fk_01_ctr.pm" "lf_:Fk_01_jnt_parentConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_01_jnt_parentConstraint1.w0" "lf_:Fk_01_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_01_jnt.ssc" "lf_:Fk_01_jnt_scaleConstraint1.tsc";
connectAttr "lf_:Fk_01_jnt.pim" "lf_:Fk_01_jnt_scaleConstraint1.cpim";
connectAttr "lf_:Fk_01_ctr.s" "lf_:Fk_01_jnt_scaleConstraint1.tg[0].ts";
connectAttr "lf_:Fk_01_ctr.pm" "lf_:Fk_01_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_01_jnt_scaleConstraint1.w0" "lf_:Fk_01_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_00_jnt.ro" "lf_:Fk_00_jnt_parentConstraint1.cro";
connectAttr "lf_:Fk_00_jnt.pim" "lf_:Fk_00_jnt_parentConstraint1.cpim";
connectAttr "lf_:Fk_00_jnt.rp" "lf_:Fk_00_jnt_parentConstraint1.crp";
connectAttr "lf_:Fk_00_jnt.rpt" "lf_:Fk_00_jnt_parentConstraint1.crt";
connectAttr "lf_:Fk_00_jnt.jo" "lf_:Fk_00_jnt_parentConstraint1.cjo";
connectAttr "lf_:Fk_00_ctr.t" "lf_:Fk_00_jnt_parentConstraint1.tg[0].tt";
connectAttr "lf_:Fk_00_ctr.rp" "lf_:Fk_00_jnt_parentConstraint1.tg[0].trp";
connectAttr "lf_:Fk_00_ctr.rpt" "lf_:Fk_00_jnt_parentConstraint1.tg[0].trt";
connectAttr "lf_:Fk_00_ctr.r" "lf_:Fk_00_jnt_parentConstraint1.tg[0].tr";
connectAttr "lf_:Fk_00_ctr.ro" "lf_:Fk_00_jnt_parentConstraint1.tg[0].tro";
connectAttr "lf_:Fk_00_ctr.s" "lf_:Fk_00_jnt_parentConstraint1.tg[0].ts";
connectAttr "lf_:Fk_00_ctr.pm" "lf_:Fk_00_jnt_parentConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_00_jnt_parentConstraint1.w0" "lf_:Fk_00_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "lf_:Fk_00_jnt.pim" "lf_:Fk_00_jnt_scaleConstraint1.cpim";
connectAttr "lf_:Fk_00_ctr.s" "lf_:Fk_00_jnt_scaleConstraint1.tg[0].ts";
connectAttr "lf_:Fk_00_ctr.pm" "lf_:Fk_00_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "lf_:Fk_00_jnt_scaleConstraint1.w0" "lf_:Fk_00_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_00_jnt_scaleConstraint1.csx" "rt_:Fk_00_jnt.sx";
connectAttr "rt_:Fk_00_jnt_scaleConstraint1.csy" "rt_:Fk_00_jnt.sy";
connectAttr "rt_:Fk_00_jnt_scaleConstraint1.csz" "rt_:Fk_00_jnt.sz";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.ctx" "rt_:Fk_00_jnt.tx";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.cty" "rt_:Fk_00_jnt.ty";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.ctz" "rt_:Fk_00_jnt.tz";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.crx" "rt_:Fk_00_jnt.rx";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.cry" "rt_:Fk_00_jnt.ry";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.crz" "rt_:Fk_00_jnt.rz";
connectAttr "cn_:Hold_00_jnt.s" "rt_:Fk_00_jnt.is";
connectAttr "rt_:Fk_00_jnt.s" "rt_:Fk_01_jnt.is";
connectAttr "rt_:Fk_01_jnt_scaleConstraint1.csx" "rt_:Fk_01_jnt.sx";
connectAttr "rt_:Fk_01_jnt_scaleConstraint1.csy" "rt_:Fk_01_jnt.sy";
connectAttr "rt_:Fk_01_jnt_scaleConstraint1.csz" "rt_:Fk_01_jnt.sz";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.ctx" "rt_:Fk_01_jnt.tx";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.cty" "rt_:Fk_01_jnt.ty";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.ctz" "rt_:Fk_01_jnt.tz";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.crx" "rt_:Fk_01_jnt.rx";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.cry" "rt_:Fk_01_jnt.ry";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.crz" "rt_:Fk_01_jnt.rz";
connectAttr "rt_:Fk_01_jnt.s" "rt_:Fk_02_jnt.is";
connectAttr "rt_:Fk_02_jnt_scaleConstraint1.csx" "rt_:Fk_02_jnt.sx";
connectAttr "rt_:Fk_02_jnt_scaleConstraint1.csy" "rt_:Fk_02_jnt.sy";
connectAttr "rt_:Fk_02_jnt_scaleConstraint1.csz" "rt_:Fk_02_jnt.sz";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.ctx" "rt_:Fk_02_jnt.tx";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.cty" "rt_:Fk_02_jnt.ty";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.ctz" "rt_:Fk_02_jnt.tz";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.crx" "rt_:Fk_02_jnt.rx";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.cry" "rt_:Fk_02_jnt.ry";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.crz" "rt_:Fk_02_jnt.rz";
connectAttr "rt_:Fk_02_jnt.s" "rt_:Fk_03_jnt.is";
connectAttr "rt_:Fk_03_jnt_scaleConstraint1.csx" "rt_:Fk_03_jnt.sx";
connectAttr "rt_:Fk_03_jnt_scaleConstraint1.csy" "rt_:Fk_03_jnt.sy";
connectAttr "rt_:Fk_03_jnt_scaleConstraint1.csz" "rt_:Fk_03_jnt.sz";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.ctx" "rt_:Fk_03_jnt.tx";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.cty" "rt_:Fk_03_jnt.ty";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.ctz" "rt_:Fk_03_jnt.tz";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.crx" "rt_:Fk_03_jnt.rx";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.cry" "rt_:Fk_03_jnt.ry";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.crz" "rt_:Fk_03_jnt.rz";
connectAttr "rt_:Fk_03_jnt.ro" "rt_:Fk_03_jnt_parentConstraint1.cro";
connectAttr "rt_:Fk_03_jnt.pim" "rt_:Fk_03_jnt_parentConstraint1.cpim";
connectAttr "rt_:Fk_03_jnt.rp" "rt_:Fk_03_jnt_parentConstraint1.crp";
connectAttr "rt_:Fk_03_jnt.rpt" "rt_:Fk_03_jnt_parentConstraint1.crt";
connectAttr "rt_:Fk_03_jnt.jo" "rt_:Fk_03_jnt_parentConstraint1.cjo";
connectAttr "rt_:Fk_03_ctr.t" "rt_:Fk_03_jnt_parentConstraint1.tg[0].tt";
connectAttr "rt_:Fk_03_ctr.rp" "rt_:Fk_03_jnt_parentConstraint1.tg[0].trp";
connectAttr "rt_:Fk_03_ctr.rpt" "rt_:Fk_03_jnt_parentConstraint1.tg[0].trt";
connectAttr "rt_:Fk_03_ctr.r" "rt_:Fk_03_jnt_parentConstraint1.tg[0].tr";
connectAttr "rt_:Fk_03_ctr.ro" "rt_:Fk_03_jnt_parentConstraint1.tg[0].tro";
connectAttr "rt_:Fk_03_ctr.s" "rt_:Fk_03_jnt_parentConstraint1.tg[0].ts";
connectAttr "rt_:Fk_03_ctr.pm" "rt_:Fk_03_jnt_parentConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_03_jnt_parentConstraint1.w0" "rt_:Fk_03_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_03_jnt.ssc" "rt_:Fk_03_jnt_scaleConstraint1.tsc";
connectAttr "rt_:Fk_03_jnt.pim" "rt_:Fk_03_jnt_scaleConstraint1.cpim";
connectAttr "rt_:Fk_03_ctr.s" "rt_:Fk_03_jnt_scaleConstraint1.tg[0].ts";
connectAttr "rt_:Fk_03_ctr.pm" "rt_:Fk_03_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_03_jnt_scaleConstraint1.w0" "rt_:Fk_03_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_02_jnt.ro" "rt_:Fk_02_jnt_parentConstraint1.cro";
connectAttr "rt_:Fk_02_jnt.pim" "rt_:Fk_02_jnt_parentConstraint1.cpim";
connectAttr "rt_:Fk_02_jnt.rp" "rt_:Fk_02_jnt_parentConstraint1.crp";
connectAttr "rt_:Fk_02_jnt.rpt" "rt_:Fk_02_jnt_parentConstraint1.crt";
connectAttr "rt_:Fk_02_jnt.jo" "rt_:Fk_02_jnt_parentConstraint1.cjo";
connectAttr "rt_:Fk_02_ctr.t" "rt_:Fk_02_jnt_parentConstraint1.tg[0].tt";
connectAttr "rt_:Fk_02_ctr.rp" "rt_:Fk_02_jnt_parentConstraint1.tg[0].trp";
connectAttr "rt_:Fk_02_ctr.rpt" "rt_:Fk_02_jnt_parentConstraint1.tg[0].trt";
connectAttr "rt_:Fk_02_ctr.r" "rt_:Fk_02_jnt_parentConstraint1.tg[0].tr";
connectAttr "rt_:Fk_02_ctr.ro" "rt_:Fk_02_jnt_parentConstraint1.tg[0].tro";
connectAttr "rt_:Fk_02_ctr.s" "rt_:Fk_02_jnt_parentConstraint1.tg[0].ts";
connectAttr "rt_:Fk_02_ctr.pm" "rt_:Fk_02_jnt_parentConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_02_jnt_parentConstraint1.w0" "rt_:Fk_02_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_02_jnt.ssc" "rt_:Fk_02_jnt_scaleConstraint1.tsc";
connectAttr "rt_:Fk_02_jnt.pim" "rt_:Fk_02_jnt_scaleConstraint1.cpim";
connectAttr "rt_:Fk_02_ctr.s" "rt_:Fk_02_jnt_scaleConstraint1.tg[0].ts";
connectAttr "rt_:Fk_02_ctr.pm" "rt_:Fk_02_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_02_jnt_scaleConstraint1.w0" "rt_:Fk_02_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_01_jnt.ro" "rt_:Fk_01_jnt_parentConstraint1.cro";
connectAttr "rt_:Fk_01_jnt.pim" "rt_:Fk_01_jnt_parentConstraint1.cpim";
connectAttr "rt_:Fk_01_jnt.rp" "rt_:Fk_01_jnt_parentConstraint1.crp";
connectAttr "rt_:Fk_01_jnt.rpt" "rt_:Fk_01_jnt_parentConstraint1.crt";
connectAttr "rt_:Fk_01_jnt.jo" "rt_:Fk_01_jnt_parentConstraint1.cjo";
connectAttr "rt_:Fk_01_ctr.t" "rt_:Fk_01_jnt_parentConstraint1.tg[0].tt";
connectAttr "rt_:Fk_01_ctr.rp" "rt_:Fk_01_jnt_parentConstraint1.tg[0].trp";
connectAttr "rt_:Fk_01_ctr.rpt" "rt_:Fk_01_jnt_parentConstraint1.tg[0].trt";
connectAttr "rt_:Fk_01_ctr.r" "rt_:Fk_01_jnt_parentConstraint1.tg[0].tr";
connectAttr "rt_:Fk_01_ctr.ro" "rt_:Fk_01_jnt_parentConstraint1.tg[0].tro";
connectAttr "rt_:Fk_01_ctr.s" "rt_:Fk_01_jnt_parentConstraint1.tg[0].ts";
connectAttr "rt_:Fk_01_ctr.pm" "rt_:Fk_01_jnt_parentConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_01_jnt_parentConstraint1.w0" "rt_:Fk_01_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_01_jnt.ssc" "rt_:Fk_01_jnt_scaleConstraint1.tsc";
connectAttr "rt_:Fk_01_jnt.pim" "rt_:Fk_01_jnt_scaleConstraint1.cpim";
connectAttr "rt_:Fk_01_ctr.s" "rt_:Fk_01_jnt_scaleConstraint1.tg[0].ts";
connectAttr "rt_:Fk_01_ctr.pm" "rt_:Fk_01_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_01_jnt_scaleConstraint1.w0" "rt_:Fk_01_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_00_jnt.ro" "rt_:Fk_00_jnt_parentConstraint1.cro";
connectAttr "rt_:Fk_00_jnt.pim" "rt_:Fk_00_jnt_parentConstraint1.cpim";
connectAttr "rt_:Fk_00_jnt.rp" "rt_:Fk_00_jnt_parentConstraint1.crp";
connectAttr "rt_:Fk_00_jnt.rpt" "rt_:Fk_00_jnt_parentConstraint1.crt";
connectAttr "rt_:Fk_00_jnt.jo" "rt_:Fk_00_jnt_parentConstraint1.cjo";
connectAttr "rt_:Fk_00_ctr.t" "rt_:Fk_00_jnt_parentConstraint1.tg[0].tt";
connectAttr "rt_:Fk_00_ctr.rp" "rt_:Fk_00_jnt_parentConstraint1.tg[0].trp";
connectAttr "rt_:Fk_00_ctr.rpt" "rt_:Fk_00_jnt_parentConstraint1.tg[0].trt";
connectAttr "rt_:Fk_00_ctr.r" "rt_:Fk_00_jnt_parentConstraint1.tg[0].tr";
connectAttr "rt_:Fk_00_ctr.ro" "rt_:Fk_00_jnt_parentConstraint1.tg[0].tro";
connectAttr "rt_:Fk_00_ctr.s" "rt_:Fk_00_jnt_parentConstraint1.tg[0].ts";
connectAttr "rt_:Fk_00_ctr.pm" "rt_:Fk_00_jnt_parentConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_00_jnt_parentConstraint1.w0" "rt_:Fk_00_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "rt_:Fk_00_jnt.pim" "rt_:Fk_00_jnt_scaleConstraint1.cpim";
connectAttr "rt_:Fk_00_ctr.s" "rt_:Fk_00_jnt_scaleConstraint1.tg[0].ts";
connectAttr "rt_:Fk_00_ctr.pm" "rt_:Fk_00_jnt_scaleConstraint1.tg[0].tpm";
connectAttr "rt_:Fk_00_jnt_scaleConstraint1.w0" "rt_:Fk_00_jnt_scaleConstraint1.tg[0].tw"
		;
connectAttr "unitConversion2.o" "lf_:Fk_00_off.rx";
connectAttr "unitConversion4.o" "lf_:Fk_00_off.rz";
connectAttr "unitConversion7.o" "lf_:Fk_01_off.rz";
connectAttr "unitConversion8.o" "lf_:Fk_01_off.rx";
connectAttr "unitConversion11.o" "lf_:Fk_02_off.rz";
connectAttr "unitConversion13.o" "lf_:Fk_02_off.rx";
connectAttr "unitConversion17.o" "lf_:Fk_03_off.rz";
connectAttr "unitConversion18.o" "lf_:Fk_03_off.rx";
connectAttr "unitConversion5.o" "rt_:Fk_00_off.rx";
connectAttr "unitConversion4.o" "rt_:Fk_00_off.rz";
connectAttr "unitConversion7.o" "rt_:Fk_01_off.rz";
connectAttr "unitConversion9.o" "rt_:Fk_01_off.rx";
connectAttr "unitConversion11.o" "rt_:Fk_02_off.rz";
connectAttr "unitConversion12.o" "rt_:Fk_02_off.rx";
connectAttr "unitConversion16.o" "rt_:Fk_03_off.rx";
connectAttr "unitConversion17.o" "rt_:Fk_03_off.rz";
connectAttr "unitConversion5.o" "cn_:Fk_00_off.rx";
connectAttr "unitConversion6.o" "cn_:Fk_00_off.rz";
connectAttr "unitConversion10.o" "cn_:Fk_01_off.rz";
connectAttr "unitConversion9.o" "cn_:Fk_01_off.rx";
connectAttr "unitConversion12.o" "cn_:Fk_02_off.rx";
connectAttr "unitConversion14.o" "cn_:Fk_02_off.rz";
connectAttr "unitConversion15.o" "cn_:Fk_03_off.rz";
connectAttr "unitConversion16.o" "cn_:Fk_03_off.rx";
connectAttr "skinCluster1GroupId.id" "cape_geoShape.iog.og[0].gid";
connectAttr "skinCluster1Set.mwc" "cape_geoShape.iog.og[0].gco";
connectAttr "groupId2.id" "cape_geoShape.iog.og[1].gid";
connectAttr "tweakSet1.mwc" "cape_geoShape.iog.og[1].gco";
connectAttr "skinCluster1.og[0]" "cape_geoShape.i";
connectAttr "tweak1.vl[0].vt[0]" "cape_geoShape.twl";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "skinCluster1GroupParts.og" "skinCluster1.ip[0].ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1.ip[0].gi";
connectAttr "bindPose1.msg" "skinCluster1.bp";
connectAttr "cn_:Fk_00_jnt.wm" "skinCluster1.ma[0]";
connectAttr "cn_:Fk_01_jnt.wm" "skinCluster1.ma[1]";
connectAttr "cn_:Fk_02_jnt.wm" "skinCluster1.ma[2]";
connectAttr "cn_:Fk_03_jnt.wm" "skinCluster1.ma[3]";
connectAttr "cn_:Hold_00_jnt.wm" "skinCluster1.ma[4]";
connectAttr "lf_:Fk_00_jnt.wm" "skinCluster1.ma[5]";
connectAttr "lf_:Fk_01_jnt.wm" "skinCluster1.ma[6]";
connectAttr "lf_:Fk_02_jnt.wm" "skinCluster1.ma[7]";
connectAttr "lf_:Fk_03_jnt.wm" "skinCluster1.ma[8]";
connectAttr "rt_:Fk_00_jnt.wm" "skinCluster1.ma[9]";
connectAttr "rt_:Fk_01_jnt.wm" "skinCluster1.ma[10]";
connectAttr "rt_:Fk_02_jnt.wm" "skinCluster1.ma[11]";
connectAttr "rt_:Fk_03_jnt.wm" "skinCluster1.ma[12]";
connectAttr "cn_:Fk_00_jnt.liw" "skinCluster1.lw[0]";
connectAttr "cn_:Fk_01_jnt.liw" "skinCluster1.lw[1]";
connectAttr "cn_:Fk_02_jnt.liw" "skinCluster1.lw[2]";
connectAttr "cn_:Fk_03_jnt.liw" "skinCluster1.lw[3]";
connectAttr "cn_:Hold_00_jnt.liw" "skinCluster1.lw[4]";
connectAttr "lf_:Fk_00_jnt.liw" "skinCluster1.lw[5]";
connectAttr "lf_:Fk_01_jnt.liw" "skinCluster1.lw[6]";
connectAttr "lf_:Fk_02_jnt.liw" "skinCluster1.lw[7]";
connectAttr "lf_:Fk_03_jnt.liw" "skinCluster1.lw[8]";
connectAttr "rt_:Fk_00_jnt.liw" "skinCluster1.lw[9]";
connectAttr "rt_:Fk_01_jnt.liw" "skinCluster1.lw[10]";
connectAttr "rt_:Fk_02_jnt.liw" "skinCluster1.lw[11]";
connectAttr "rt_:Fk_03_jnt.liw" "skinCluster1.lw[12]";
connectAttr "cn_:Fk_00_jnt.obcc" "skinCluster1.ifcl[0]";
connectAttr "cn_:Fk_01_jnt.obcc" "skinCluster1.ifcl[1]";
connectAttr "cn_:Fk_02_jnt.obcc" "skinCluster1.ifcl[2]";
connectAttr "cn_:Fk_03_jnt.obcc" "skinCluster1.ifcl[3]";
connectAttr "cn_:Hold_00_jnt.obcc" "skinCluster1.ifcl[4]";
connectAttr "lf_:Fk_00_jnt.obcc" "skinCluster1.ifcl[5]";
connectAttr "lf_:Fk_01_jnt.obcc" "skinCluster1.ifcl[6]";
connectAttr "lf_:Fk_02_jnt.obcc" "skinCluster1.ifcl[7]";
connectAttr "lf_:Fk_03_jnt.obcc" "skinCluster1.ifcl[8]";
connectAttr "rt_:Fk_00_jnt.obcc" "skinCluster1.ifcl[9]";
connectAttr "rt_:Fk_01_jnt.obcc" "skinCluster1.ifcl[10]";
connectAttr "rt_:Fk_02_jnt.obcc" "skinCluster1.ifcl[11]";
connectAttr "rt_:Fk_03_jnt.obcc" "skinCluster1.ifcl[12]";
connectAttr "lf_:Fk_03_jnt.msg" "skinCluster1.ptt";
connectAttr "groupParts2.og" "tweak1.ip[0].ig";
connectAttr "groupId2.id" "tweak1.ip[0].gi";
connectAttr "skinCluster1GroupId.msg" "skinCluster1Set.gn" -na;
connectAttr "cape_geoShape.iog.og[0]" "skinCluster1Set.dsm" -na;
connectAttr "skinCluster1.msg" "skinCluster1Set.ub[0]";
connectAttr "tweak1.og[0]" "skinCluster1GroupParts.ig";
connectAttr "skinCluster1GroupId.id" "skinCluster1GroupParts.gi";
connectAttr "groupId2.msg" "tweakSet1.gn" -na;
connectAttr "cape_geoShape.iog.og[1]" "tweakSet1.dsm" -na;
connectAttr "tweak1.msg" "tweakSet1.ub[0]";
connectAttr "cape_geoShape1Orig.w" "groupParts2.ig";
connectAttr "groupId2.id" "groupParts2.gi";
connectAttr "cn_:Fk_00_jnt.msg" "bindPose1.m[0]";
connectAttr "cn_:Fk_01_jnt.msg" "bindPose1.m[1]";
connectAttr "cn_:Fk_02_jnt.msg" "bindPose1.m[2]";
connectAttr "cn_:Fk_03_jnt.msg" "bindPose1.m[3]";
connectAttr "cn_:Hold_00_jnt.msg" "bindPose1.m[4]";
connectAttr "lf_:Fk_00_jnt.msg" "bindPose1.m[5]";
connectAttr "lf_:Fk_01_jnt.msg" "bindPose1.m[6]";
connectAttr "lf_:Fk_02_jnt.msg" "bindPose1.m[7]";
connectAttr "lf_:Fk_03_jnt.msg" "bindPose1.m[8]";
connectAttr "rt_:Fk_00_jnt.msg" "bindPose1.m[9]";
connectAttr "rt_:Fk_01_jnt.msg" "bindPose1.m[10]";
connectAttr "rt_:Fk_02_jnt.msg" "bindPose1.m[11]";
connectAttr "rt_:Fk_03_jnt.msg" "bindPose1.m[12]";
connectAttr "bindPose1.w" "bindPose1.p[0]";
connectAttr "bindPose1.m[0]" "bindPose1.p[1]";
connectAttr "bindPose1.m[1]" "bindPose1.p[2]";
connectAttr "bindPose1.m[2]" "bindPose1.p[3]";
connectAttr "bindPose1.w" "bindPose1.p[4]";
connectAttr "bindPose1.w" "bindPose1.p[5]";
connectAttr "bindPose1.m[5]" "bindPose1.p[6]";
connectAttr "bindPose1.m[6]" "bindPose1.p[7]";
connectAttr "bindPose1.m[7]" "bindPose1.p[8]";
connectAttr "bindPose1.w" "bindPose1.p[9]";
connectAttr "bindPose1.m[9]" "bindPose1.p[10]";
connectAttr "bindPose1.m[10]" "bindPose1.p[11]";
connectAttr "bindPose1.m[11]" "bindPose1.p[12]";
connectAttr "cn_:Fk_00_jnt.bps" "bindPose1.wm[0]";
connectAttr "cn_:Fk_01_jnt.bps" "bindPose1.wm[1]";
connectAttr "cn_:Fk_02_jnt.bps" "bindPose1.wm[2]";
connectAttr "cn_:Fk_03_jnt.bps" "bindPose1.wm[3]";
connectAttr "cn_:Hold_00_jnt.bps" "bindPose1.wm[4]";
connectAttr "lf_:Fk_00_jnt.bps" "bindPose1.wm[5]";
connectAttr "lf_:Fk_01_jnt.bps" "bindPose1.wm[6]";
connectAttr "lf_:Fk_02_jnt.bps" "bindPose1.wm[7]";
connectAttr "lf_:Fk_03_jnt.bps" "bindPose1.wm[8]";
connectAttr "rt_:Fk_00_jnt.bps" "bindPose1.wm[9]";
connectAttr "rt_:Fk_01_jnt.bps" "bindPose1.wm[10]";
connectAttr "rt_:Fk_02_jnt.bps" "bindPose1.wm[11]";
connectAttr "rt_:Fk_03_jnt.bps" "bindPose1.wm[12]";
connectAttr "unitToTimeConversion1.o" "lf_:Fk_00_off_rotateX.i";
connectAttr "unitToTimeConversion1.o" "lf_:Fk_00_off_rotateZ.i";
connectAttr "lf_:Fk_00_off_rotateX.o" "lf_:Fk_Pos_off_rotateX.i";
connectAttr "pos_Fk_00_mdv.oy" "unitConversion2.i";
connectAttr "Config_00_ctr._00_amplitude" "pos_Fk_00_mdv.i1x";
connectAttr "Config_00_ctr._00_amplitude" "pos_Fk_00_mdv.i1y";
connectAttr "lf_:Fk_Pos_off_rotateZ.o" "pos_Fk_00_mdv.i2x";
connectAttr "lf_:Fk_Pos_off_rotateX.o" "pos_Fk_00_mdv.i2y";
connectAttr "lf_:Fk_00_off_rotateZ.o" "lf_:Fk_Pos_off_rotateZ.i";
connectAttr "pos_Fk_00_mdv.ox" "unitConversion4.i";
connectAttr "Config_00_ctr.frecuency" "unitToTimeConversion1.i";
connectAttr "lf_:Fk_00_off_rotateX.o" "lf_:Fk_Neg_off_rotateX.i";
connectAttr "lf_:Fk_00_off_rotateZ.o" "lf_:Fk_Neg_off_rotateZ.i";
connectAttr "Config_00_ctr._00_amplitude" "neg_Fk_00_mdv.i1x";
connectAttr "Config_00_ctr._00_amplitude" "neg_Fk_00_mdv.i1y";
connectAttr "lf_:Fk_Neg_off_rotateZ.o" "neg_Fk_00_mdv.i2x";
connectAttr "lf_:Fk_Neg_off_rotateX.o" "neg_Fk_00_mdv.i2y";
connectAttr "neg_Fk_00_mdv.oy" "unitConversion5.i";
connectAttr "neg_Fk_00_mdv.ox" "unitConversion6.i";
connectAttr "Config_00_ctr._01_amplitude" "pos_Fk_01_mdv.i1x";
connectAttr "Config_00_ctr._01_amplitude" "pos_Fk_01_mdv.i1y";
connectAttr "lf_:Fk_Pos_off_rotateZ.o" "pos_Fk_01_mdv.i2x";
connectAttr "lf_:Fk_Pos_off_rotateX.o" "pos_Fk_01_mdv.i2y";
connectAttr "pos_Fk_01_mdv.ox" "unitConversion7.i";
connectAttr "pos_Fk_01_mdv.oy" "unitConversion8.i";
connectAttr "Config_00_ctr._01_amplitude" "neg_Fk_01_mdv.i1x";
connectAttr "Config_00_ctr._01_amplitude" "neg_Fk_01_mdv.i1y";
connectAttr "lf_:Fk_Neg_off_rotateZ.o" "neg_Fk_01_mdv.i2x";
connectAttr "lf_:Fk_Neg_off_rotateX.o" "neg_Fk_01_mdv.i2y";
connectAttr "neg_Fk_01_mdv.oy" "unitConversion9.i";
connectAttr "neg_Fk_01_mdv.ox" "unitConversion10.i";
connectAttr "lf_:Fk_Neg_off_rotateZ.o" "neg_Fk_02_mdv.i1x";
connectAttr "lf_:Fk_Neg_off_rotateX.o" "neg_Fk_02_mdv.i1y";
connectAttr "Config_00_ctr._02_amplitude" "neg_Fk_02_mdv.i2x";
connectAttr "Config_00_ctr._02_amplitude" "neg_Fk_02_mdv.i2y";
connectAttr "lf_:Fk_Pos_off_rotateZ.o" "pos_Fk_02_mdv.i1x";
connectAttr "lf_:Fk_Pos_off_rotateX.o" "pos_Fk_02_mdv.i1y";
connectAttr "Config_00_ctr._02_amplitude" "pos_Fk_02_mdv.i2x";
connectAttr "Config_00_ctr._02_amplitude" "pos_Fk_02_mdv.i2y";
connectAttr "pos_Fk_02_mdv.ox" "unitConversion11.i";
connectAttr "neg_Fk_02_mdv.oy" "unitConversion12.i";
connectAttr "pos_Fk_02_mdv.oy" "unitConversion13.i";
connectAttr "neg_Fk_02_mdv.ox" "unitConversion14.i";
connectAttr "lf_:Fk_Pos_off_rotateZ.o" "pos_Fk_03_mdv.i1x";
connectAttr "lf_:Fk_Pos_off_rotateX.o" "pos_Fk_03_mdv.i1y";
connectAttr "Config_00_ctr._03_amplitude" "pos_Fk_03_mdv.i2x";
connectAttr "Config_00_ctr._03_amplitude" "pos_Fk_03_mdv.i2y";
connectAttr "lf_:Fk_Neg_off_rotateZ.o" "neg_Fk_03_mdv.i1x";
connectAttr "lf_:Fk_Neg_off_rotateX.o" "neg_Fk_03_mdv.i1y";
connectAttr "Config_00_ctr._03_amplitude" "neg_Fk_03_mdv.i2x";
connectAttr "Config_00_ctr._03_amplitude" "neg_Fk_03_mdv.i2y";
connectAttr "neg_Fk_03_mdv.ox" "unitConversion15.i";
connectAttr "neg_Fk_03_mdv.oy" "unitConversion16.i";
connectAttr "pos_Fk_03_mdv.ox" "unitConversion17.i";
connectAttr "pos_Fk_03_mdv.oy" "unitConversion18.i";
connectAttr "cn_:Fk_00_off.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[0].dn";
connectAttr "lf_:Fk_Pos_off_rotateZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[1].dn"
		;
connectAttr "lf_:Fk_00_off.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[2].dn";
connectAttr "lf_:Fk_00_off_rotateX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[3].dn"
		;
connectAttr "lf_:Fk_Neg_off_rotateX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[4].dn"
		;
connectAttr "lf_:Fk_Neg_off_rotateZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[5].dn"
		;
connectAttr "rt_:Fk_00_off.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[6].dn";
connectAttr "unitConversion6.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[7].dn";
connectAttr "unitConversion5.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[8].dn";
connectAttr "unitConversion2.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[9].dn";
connectAttr "unitConversion4.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[10].dn"
		;
connectAttr "Config_00_ctr.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[11].dn";
connectAttr "lf_:Fk_00_off_rotateZ.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[12].dn"
		;
connectAttr "neg_Fk_00_mdv.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[13].dn";
connectAttr "unitToTimeConversion1.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[14].dn"
		;
connectAttr "pos_Fk_00_mdv.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[15].dn";
connectAttr "lf_:Fk_Pos_off_rotateX.msg" "MayaNodeEditorSavedTabsInfo.tgi[0].ni[16].dn"
		;
connectAttr "pos_Fk_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "neg_Fk_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "pos_Fk_01_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "neg_Fk_01_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "neg_Fk_02_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "pos_Fk_02_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "pos_Fk_03_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "neg_Fk_03_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "cape_geoShape.iog" ":initialShadingGroup.dsm" -na;
// End of cape.ma
