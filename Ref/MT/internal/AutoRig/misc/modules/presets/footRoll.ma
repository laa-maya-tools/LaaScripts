//Maya ASCII 2020 scene
//Name: footRoll.ma
//Last modified: Tue, Jul 19, 2022 09:49:45 AM
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
fileInfo "UUID" "54FF5AA5-4074-2FED-F4B2-F89FFA4E4A70";
createNode transform -s -n "persp";
	rename -uid "14455B1C-4DE0-BEB3-7FCF-2EB1B89E0522";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 21.614424476251795 28.867323292854316 59.808680678291502 ;
	setAttr ".r" -type "double3" -24.338352730137494 379.79999999995721 -8.4510035341613977e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "1A7DE48D-4EBC-1A0F-6D0B-04924C90B8D6";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 68.386872412836297;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 -3.8857805861880479e-16 1.7388965517241384 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "AB3C35A6-43F0-3004-D893-A0BE1F66A2CD";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.52876331405431087 1000.1425379944556 1.4956969391280799 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "4EB80C24-479A-4365-6715-D485D5B8ABC9";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 990.14253791967974;
	setAttr ".ow" 39.745140730865565;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".tp" -type "double3" 1.331988169689484 10.000000074775798 0.18068391617573365 ;
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "DA4B3181-4D4C-77EA-CA7B-67B5554B1DF7";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -0.35113001506421015 3.2037466814019631 1000.1026650370112 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "8FEEE171-40E9-BB0F-F68D-E88BB1E210DF";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1002.1026650370112;
	setAttr ".ow" 11.81018253012782;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0 3.227352912004934 -2 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "19510CBE-4B82-03BE-DA86-588BDC9403B5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.2057110651836 2.9073901574595711 17.124926007861152 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "F3A34269-4AF8-D148-1047-C9ACC2AF7942";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.2057110651836;
	setAttr ".ow" 36.733676292572575;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 0 0 5.4999975000000632 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "_00_jnt";
	rename -uid "936A9C7D-41E7-075A-852A-FE897B3B0EC7";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode joint -n "_01_jnt" -p "_00_jnt";
	rename -uid "789973EF-4FAC-2109-E881-52B92DF246E5";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".t" -type "double3" 0 -10 5 ;
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".radi" 0.55172413793103448;
createNode orientConstraint -n "_01_jnt_orientConstraint1" -p "_01_jnt";
	rename -uid "7CDEADA5-4A09-5E12-36A6-9AAF266BE11B";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Ball_00_ctrW0" -dv 1 -min 0 -at "double";
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
createNode parentConstraint -n "Jnt_00_prcn" -p "_00_jnt";
	rename -uid "59E76E56-4E68-590E-3C3D-39980D1FB501";
	setAttr -s 2 ".tg";
createNode transform -n "Ball_00_root";
	rename -uid "5DEB89E6-4EC6-4A46-2B8E-3A84E477C655";
createNode transform -n "Ball_00_ctr" -p "Ball_00_root";
	rename -uid "8A1E16D0-434C-511B-663A-3CA5C1A18CA0";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Ball_00_ctrShape" -p "Ball_00_ctr";
	rename -uid "0A42F038-4BC5-D660-F268-3EADD20BE74D";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-5 5 -4.9999998736893751e-05
		-5 5 10
		-5 -5 10
		5 -5 10
		5 5 10
		5 5 -4.9999998736893751e-05
		5 -5 -4.9999998736893751e-05
		-5 -5 -4.9999998736893751e-05
		-5 5 -4.9999998736893751e-05
		5 5 -4.9999998736893751e-05
		5 5 10
		-5 5 10
		-5 -5 10
		5 -5 10
		5 -5 -4.9999998736893751e-05
		-5 -5 -4.9999998736893751e-05
		-5 -5 10
		;
createNode parentConstraint -n "BallRoot_00_prc" -p "Ball_00_root";
	rename -uid "3BD57664-407E-D818-62FF-17B712B79797";
	setAttr -s 2 ".tg";
	setAttr ".int" 0;
createNode transform -n "Config_00_root";
	rename -uid "044FBCEB-4C80-95A6-3E80-73A4D29B07AA";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 3.0000000000000004 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Config_00_ctr" -p "Config_00_root";
	rename -uid "92AC3BCC-4851-E40B-377B-2FAD746B5463";
	addAttr -ci true -sn "fkik" -ln "fkik" -nn "Fk Ik" -dv 1 -min 0 -max 1 -at "double";
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
	setAttr -k on ".fkik" 0.5;
createNode nurbsCurve -n "Config_00_ctrShape1" -p "Config_00_ctr";
	rename -uid "FF97B814-4075-EEFC-66E3-988F09112415";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-1.4993768790974873 1.707238888564159 -2
		-1.7266228395229661 1.707238888564159 -2
		-1.7266228395229661 8.8981298187784514e-16 -2
		-1.4993768790974873 8.8981298187784514e-16 -2
		-1.4993768790974873 0.86516006700686132 -2
		-0.75302543762583363 8.8981298187784514e-16 -2
		-0.44684945772118778 8.8981298187784514e-16 -2
		-1.2336463200825232 0.89265919977452157 -2
		-0.56492555926565247 1.707238888564159 -2
		-0.80840164910934043 1.707238888564159 -2
		-1.4993768790974873 0.86745168308930665 -2
		-1.4993768790974873 1.707238888564159 -2
		;
createNode nurbsCurve -n "Config_00_ctrShape2" -p "Config_00_ctr";
	rename -uid "78C78C3E-4047-160B-9E93-75AA6D620D0F";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		0.57146974384156635 1.707238888564159 -2
		0.45150339211281915 1.707238888564159 -2
		-0.15527337053947907 -0.34144777771283158 -2
		-0.035307226988070955 -0.34144777771283158 -2
		0.57146974384156635 1.707238888564159 -2
		;
createNode nurbsCurve -n "Config_00_ctrShape3" -p "Config_00_ctr";
	rename -uid "80590B43-4D46-4F8D-D84B-C59B4D73D7B7";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 10 2 no 3
		11 0 1 2 3 4 5 6 7 8 9 10
		11
		-2.0483675694586436 1.707238888564159 -2
		-3.0023564621100101 1.707238888564159 -2
		-3.0023564621100101 8.8981298187784514e-16 -2
		-2.7601088006866012 8.8981298187784514e-16 -2
		-2.7601088006866012 0.77517354119098458 -2
		-2.162569386745989 0.77517354119098458 -2
		-2.162569386745989 0.95396523850189452 -2
		-2.7601088006866012 0.95396523850189452 -2
		-2.7601088006866012 1.5261318949991669 -2
		-2.0483675694586436 1.5261318949991669 -2
		-2.0483675694586436 1.707238888564159 -2
		;
createNode nurbsCurve -n "Config_00_ctrShape4" -p "Config_00_ctr";
	rename -uid "5451659D-4ABE-58AF-7BFA-8681F95F2354";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		1.2785565462567301 1.707238888564159 -2
		1.0363089108554928 1.707238888564159 -2
		1.0363089108554928 8.8981298187784514e-16 -2
		1.2785565462567301 8.8981298187784514e-16 -2
		1.2785565462567301 1.707238888564159 -2
		;
createNode nurbsCurve -n "Config_00_ctrShape5" -p "Config_00_ctr";
	rename -uid "5C2E1335-42D8-A79F-3644-9CA220EFCD34";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		1.949828936645047 1.707238888564159 -2
		1.7225829762195641 1.707238888564159 -2
		1.7225829762195641 8.8981298187784514e-16 -2
		1.949828936645047 8.8981298187784514e-16 -2
		1.949828936645047 0.86516006700686132 -2
		2.6961804822053632 8.8981298187784514e-16 -2
		3.0023564621100101 8.8981298187784514e-16 -2
		2.2155593915713472 0.89265919977452157 -2
		2.8842803605655432 1.707238888564159 -2
		2.6408040625445306 1.707238888564159 -2
		1.949828936645047 0.86745168308930665 -2
		1.949828936645047 1.707238888564159 -2
		;
createNode transform -n "Tpl_00_tpl";
	rename -uid "FD82A170-474C-D36C-5FF2-D48D2B6CD10C";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "RollMainTpl_00_root" -p "Tpl_00_tpl";
	rename -uid "7868E8B6-4214-6EB9-723E-C7BD5B37B443";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -uap -ci true -k true -sn "mirror" -ln "mirror" -min 0 -max 1 -at "bool";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".mirror";
createNode locator -n "RollMainTpl_00_rootShape" -p "RollMainTpl_00_root";
	rename -uid "53E243EA-4173-4CAE-B908-C78F97CE5912";
	setAttr -k off ".v";
createNode transform -n "BankInTpl_00_footroll" -p "RollMainTpl_00_root";
	rename -uid "7216FAE5-4D9C-39B1-D49C-758695F206BF";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -6 0 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "BankInTpl_00_footrollShape" -p "BankInTpl_00_footroll";
	rename -uid "4F0D96B5-4A29-2B90-4C06-F3B1CE5F91B8";
	setAttr -k off ".v";
createNode transform -n "BankExtTpl_00_footroll" -p "BankInTpl_00_footroll";
	rename -uid "D084BAF1-4F65-9C72-DCDA-C68AED6DBB8B";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 12 0 0 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "BankExtTpl_00_footrollShape" -p "BankExtTpl_00_footroll";
	rename -uid "D584D70E-4F58-5F44-2745-EAA40BB6F4BD";
	setAttr -k off ".v";
createNode transform -n "BankHeelTpl_00_footroll" -p "BankExtTpl_00_footroll";
	rename -uid "1EEF0C40-4439-23EE-DC01-22BF9E8F6409";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" -6 0 -10 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "BankHeelTpl_00_footrollShape" -p "BankHeelTpl_00_footroll";
	rename -uid "D215D769-4E90-1B06-B824-53940221B0D5";
	setAttr -k off ".v";
createNode transform -n "BankToeTpl_00_footroll" -p "BankHeelTpl_00_footroll";
	rename -uid "C8031FEB-42DB-4705-E0E3-BDAFDFB9769C";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 3.3306690738754681e-16 25 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "BankToeTpl_00_footrollShape" -p "BankToeTpl_00_footroll";
	rename -uid "4BE50879-4F46-1977-E5D0-F3B7ABFE480A";
	setAttr -k off ".v";
createNode transform -n "BallMainTpl_00_root" -p "BankToeTpl_00_footroll";
	rename -uid "0862FF00-44CD-137C-F968-0FB9900606B3";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 4.9303806576313238e-32 -10 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "BallMainTpl_00_rootShape" -p "BallMainTpl_00_root";
	rename -uid "8F3054B8-4CF8-4670-8001-DEB1C6C58243";
	setAttr -k off ".v";
createNode transform -n "BallFkTpl_00_mstc" -p "BallMainTpl_00_root";
	rename -uid "788ED998-4CA5-A784-066D-4C9665BD7764";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754686e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "BallFkTpl_00_mstcShape" -p "BallFkTpl_00_mstc";
	rename -uid "6FD3CCA5-44B5-F33D-CC68-46AF8D78B78E";
	setAttr -k off ".v";
createNode transform -n "Tpl_01_jnt" -p "BallMainTpl_00_root";
	rename -uid "76568B9B-427F-4B48-0D20-FEB86F6DBB5F";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754686e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Tpl_01_jntShape" -p "Tpl_01_jnt";
	rename -uid "C2068258-4DCE-603D-3BB6-99B5EC3C1893";
	setAttr -k off ".v";
createNode transform -n "BankBallTpl_00_footroll" -p "BallMainTpl_00_root";
	rename -uid "A7452672-4F0D-0B28-EA89-6A8BA09A205B";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 0 -3.3306690738754686e-16 0 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "BankBallTpl_00_footrollShape" -p "BankBallTpl_00_footroll";
	rename -uid "71A8BEA9-4E43-738D-56A2-3E808C48B3F5";
	setAttr -k off ".v";
createNode transform -n "IkTpl_00_mstc" -p "BallMainTpl_00_root";
	rename -uid "FF1C8F28-4AB9-1E1D-B817-EF91147CDB1D";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr ".t" -type "double3" 0 10 -5 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "IkTpl_00_mstcShape" -p "IkTpl_00_mstc";
	rename -uid "99D845BE-40F3-F0A9-7D92-E6BD5D54D364";
	setAttr -k off ".v";
createNode transform -n "FkTpl_00_mstc" -p "IkTpl_00_mstc";
	rename -uid "A84FB658-4624-2460-A66A-9AA41C669C47";
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
createNode locator -n "FkTpl_00_mstcShape" -p "FkTpl_00_mstc";
	rename -uid "31A30C9B-442B-DD09-9B16-6D8A462739F3";
	setAttr -k off ".v";
createNode transform -n "Tpl_00_jnt" -p "IkTpl_00_mstc";
	rename -uid "1E14E947-4DD6-9773-6D44-789049386FB4";
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
createNode locator -n "Tpl_00_jntShape" -p "Tpl_00_jnt";
	rename -uid "2783980F-4D68-5F21-0446-6F8CF430CCCB";
	setAttr -k off ".v";
createNode transform -n "Config_00_tpl" -p "RollMainTpl_00_root";
	rename -uid "A90ACBAE-477F-F516-0A65-7C8C1E621BB2";
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
createNode locator -n "Config_00_tplShape" -p "Config_00_tpl";
	rename -uid "B3BA1CF2-429D-8736-FA6B-5A9C79B64EF8";
	setAttr -k off ".v";
createNode transform -n "input_00_link";
	rename -uid "AABA67BA-454E-B4CC-160C-5280A786B2B0";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "RollMain_00_root" -p "input_00_link";
	rename -uid "98C8CA4D-4912-FEB7-58A2-86A1C6EED818";
createNode transform -n "BankIn_00_footroll" -p "RollMain_00_root";
	rename -uid "BCE6DFAF-40A0-D870-6B9C-41BA9FAF8B35";
	setAttr ".t" -type "double3" -6 0 0 ;
createNode transform -n "BankExt_00_footroll" -p "BankIn_00_footroll";
	rename -uid "897C1A44-4B40-DBA1-54AA-008CF27F09DD";
	setAttr ".t" -type "double3" 12 0 0 ;
createNode transform -n "BankHeel_00_footroll" -p "BankExt_00_footroll";
	rename -uid "79BFE0BF-42CA-493D-1FD3-308453202678";
	setAttr ".t" -type "double3" -6 0 -10 ;
createNode transform -n "BankHeel_00_root" -p "BankHeel_00_footroll";
	rename -uid "467D56E9-4C52-A01B-37A5-3C96F2C47B24";
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "BankHeel_00_ctr" -p "BankHeel_00_root";
	rename -uid "4F179051-4600-2C73-76A2-8C830FEF5157";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "BallMain_00_root" -p "BankHeel_00_ctr";
	rename -uid "336336DB-45D5-4BDF-D252-A6ADC77FA777";
	setAttr ".t" -type "double3" 3.6977854932234928e-32 -9.8607613152626476e-32 15 ;
createNode transform -n "BallMain_00_ctr" -p "BallMain_00_root";
	rename -uid "7E28B271-41D2-CFD7-E715-F4BD4CF4A855";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "BallMain_00_ctrShape" -p "BallMain_00_ctr";
	rename -uid "2768C2E8-41D9-DDB5-571B-74A0E418D74B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 24 0 no 3
		25 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24
		25
		-3.0000007152557373 0.24999999999999967 5.1961519718170166
		-6 0.24999999999999967 -7.152557373046875e-07
		-6 -0.25000000000000033 -7.152557373046875e-07
		-2.9999990463256836 -0.25000000000000033 -5.196152925491333
		-2.9999990463256836 0.24999999999999967 -5.196152925491333
		3.0000014305114746 0.24999999999999967 -5.1961514949798584
		3.0000014305114746 -0.25000000000000033 -5.1961514949798584
		6 -0.25000000000000033 2.384185791015625e-07
		6 0.24999999999999967 2.384185791015625e-07
		2.9999997615814209 0.24999999999999967 5.196152925491333
		2.9999997615814209 -0.25000000000000033 5.196152925491333
		-3.0000007152557373 -0.25000000000000033 5.1961519718170166
		-3.0000007152557373 0.24999999999999967 5.1961519718170166
		2.9999997615814209 0.24999999999999967 5.196152925491333
		2.9999997615814209 -0.25000000000000033 5.196152925491333
		6 -0.25000000000000033 2.384185791015625e-07
		6 0.24999999999999967 2.384185791015625e-07
		3.0000014305114746 0.24999999999999967 -5.1961514949798584
		3.0000014305114746 -0.25000000000000033 -5.1961514949798584
		-2.9999990463256836 -0.25000000000000033 -5.196152925491333
		-2.9999990463256836 0.24999999999999967 -5.196152925491333
		-6 0.24999999999999967 -7.152557373046875e-07
		-6 -0.25000000000000033 -7.152557373046875e-07
		-3.0000007152557373 -0.25000000000000033 5.1961519718170166
		-3.0000007152557373 0.24999999999999967 5.1961519718170166
		;
createNode transform -n "BankToe_00_footroll" -p "BallMain_00_ctr";
	rename -uid "19A55340-417D-BEA8-0730-B5BA680E5FC4";
	setAttr ".t" -type "double3" -3.6977854932234934e-32 -4.9303806576313238e-32 10 ;
createNode transform -n "BankToe_00_root" -p "BankToe_00_footroll";
	rename -uid "EFACE8FB-48E5-C60D-E3DD-B4B9F14B7428";
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "BankToe_00_ctr" -p "BankToe_00_root";
	rename -uid "4BB5D832-4445-418C-96E3-DDBF402C167F";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "BankBall_00_footroll" -p "BankToe_00_ctr";
	rename -uid "9B5568B4-49CF-5578-7860-FEBBE8096487";
	setAttr ".t" -type "double3" 5.4738221262688167e-48 -6.6613381477509373e-16 -10 ;
createNode transform -n "BallIk_00_mstc" -p "BankBall_00_footroll";
	rename -uid "2BF5EB46-4222-DD8F-39E8-05BD35970938";
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-16 ;
createNode transform -n "BallRoll_00_root" -p "BankBall_00_footroll";
	rename -uid "201EBC66-42C5-B27E-77EA-5B9858A54357";
	setAttr ".t" -type "double3" 0 0 4.4408920985006262e-16 ;
createNode transform -n "BallRoll_00_ctr" -p "BallRoll_00_root";
	rename -uid "DBE5893F-42ED-39AA-47E0-09BCADB01824";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode transform -n "Ik_00_mstc" -p "BallRoll_00_ctr";
	rename -uid "C780EE93-479F-6238-DCE9-968146D04F48";
	setAttr ".t" -type "double3" 0 10 -5 ;
createNode transform -n "output_00_link" -p "Ik_00_mstc";
	rename -uid "598B0727-4444-D60D-A1C8-2393D169EFEA";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.40392157 0.63137257 ;
createNode transform -n "RollMainCtr_00_root" -p "Ik_00_mstc";
	rename -uid "02834F10-4AB3-461F-0698-C097EE92AC94";
createNode transform -n "RollMain_00_ctr" -p "RollMainCtr_00_root";
	rename -uid "8079240D-4547-5778-6454-FCB70B7FB4D8";
	addAttr -ci true -sn "ballBreak" -ln "ballBreak" -dv 20 -min 0 -at "double";
	addAttr -ci true -sn "ballFlat" -ln "ballFlat" -dv 60 -at "double";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -k on ".ballBreak";
	setAttr -k on ".ballFlat";
createNode nurbsCurve -n "RollMain_00_ctrShape" -p "RollMain_00_ctr";
	rename -uid "3A7EBD1D-441E-5667-9272-63ABC2C8B904";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 15 0 no 3
		16 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
		16
		5.0181188166138355 4.4865478265876391e-07 5.0181188166138346
		5.0181188166138373 4.3458185954997219 2.5090588101005373
		5.0181188166138373 4.3458179972933397 -2.5090600065132955
		5.0181188166138355 -1.1964127590857743e-06 -5.0181188166138346
		-5.0181188166138355 -1.196412756421239e-06 -5.0181188166138346
		-5.0181188166138364 -4.3458182963965308 -2.5090594083069173
		-5.0181188166138364 -4.3458182963965308 2.5090594083069173
		-5.0181188166138355 4.4865478576738838e-07 5.0181188166138346
		5.0181188166138355 4.4865478265876391e-07 5.0181188166138346
		5.0181188166138337 -4.3458182963965335 2.5090594083069173
		5.0181188166138337 -4.3458182963965335 -2.5090594083069173
		5.0181188166138355 -1.1964127590857743e-06 -5.0181188166138346
		-5.0181188166138355 -1.196412756421239e-06 -5.0181188166138346
		-5.0181188166138337 4.3458179972933433 -2.5090600065132955
		-5.0181188166138337 4.3458185954997255 2.5090588101005373
		-5.0181188166138355 4.4865478576738838e-07 5.0181188166138346
		;
createNode nurbsCurve -n "BallRoll_00_ctrShape" -p "BallRoll_00_ctr";
	rename -uid "80D966FF-43C7-4714-FCA4-5FB9725E8435";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 20 0 no 3
		25 0 0 0 1 2 3 4 5 6 7 8 9 10 10.494106049999999 11 12 13 14 15 16 17 18 19
		 19 19
		23
		5.3924508873606559e-16 1.4571263884158692 -4.6261917411515405
		8.6279214197770523e-16 2.5284560299527605 -4.3106693753668477
		1.2941882129665575e-15 4.4897195674844905 -2.8041454492370641
		1.7255842839554105e-15 5.2126689081508992 0.74220896935520031
		1.0784901774721312e-15 3.4983764137736886 3.9734683591086273
		3.8315668059572215e-31 1.2076413861438485e-15 5.3018191239982162
		-1.2941882129665575e-15 -3.4983764137736904 3.9734683591086299
		-1.7255842839554105e-15 -5.2179165231526277 0.69840253022688203
		-1.2941882129665575e-15 -4.4718364159171262 -2.5460328831738868
		-6.4709410648327877e-16 -2.6217634402510348 -4.2274489642680608
		-4.3139607098885261e-16 -1.4571263884158696 -4.6261917138778532
		-3.2354705324163939e-16 -1.4571263884158692 -4.6261917138778532
		-3.2354705324163939e-16 -1.4571263884158692 -4.6261917138778532
		-8.6279214197770523e-16 -2.5407524140295767 -4.6261917411515405
		-8.6279214197770523e-16 -2.5407524140295767 -4.6261917411515405
		-8.6279214197770523e-16 -2.5407524140295767 -4.6261917411515405
		0 0 -6.7999231459407241
		0 0 -6.7999231459407241
		0 0 -6.7999231459407241
		8.6279214197770523e-16 2.5407528772375803 -4.6261917411515405
		8.6279214197770523e-16 2.5407528772375803 -4.6261917411515405
		8.6279214197770523e-16 2.5407528772375803 -4.6261917411515405
		3.2354705324163939e-16 1.4571263884158692 -4.6261917411515405
		;
createNode nurbsCurve -n "BankToe_00_ctrShape" -p "BankToe_00_ctr";
	rename -uid "DBE186B1-4C77-8442-BAD9-AE83F1A1A383";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 20 0 no 3
		25 0 0 0 1 2 3 4 5 6 7 8 9 10 10.494106049999999 11 12 13 14 15 16 17 18 19
		 19 19
		23
		5.5511151231257827e-16 1.5 4.7623100280761719
		8.8817841970012523e-16 2.6028518013817581 4.437503921729026
		1.3322676295501878e-15 4.6218223791474298 2.8866529405375956
		1.7763568394002505e-15 5.3660433469514359 -0.76404728023843649
		1.1102230246251565e-15 3.6013105399631664 -4.0903813053187781
		3.9443045261050599e-31 1.2431743008821104e-15 -5.4578166651989735
		-1.3322676295501878e-15 -3.6013105399631682 -4.0903813053187807
		-1.7763568394002505e-15 -5.3714453646248304 -0.71895190675891651
		-1.3322676295501878e-15 -4.6034130444704227 2.6209458253739757
		-6.6613381477509392e-16 -2.6989046328726296 4.351834883243014
		-4.4408920985006262e-16 -1.5000000000000004 4.7623100000000003
		-3.3306690738754696e-16 -1.5 4.7623100000000003
		-3.3306690738754696e-16 -1.5 4.7623100000000003
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		0 0 7
		0 0 7
		0 0 7
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		3.3306690738754696e-16 1.5 4.7623100280761719
		;
createNode nurbsCurve -n "BankHeel_00_ctrShape" -p "BankHeel_00_ctr";
	rename -uid "9C66A413-4B58-C37D-C5EC-4A8D36869879";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		3 20 0 no 3
		25 0 0 0 1 2 3 4 5 6 7 8 9 10 10.494106049999999 11 12 13 14 15 16 17 18 19
		 19 19
		23
		5.5511151231257827e-16 1.5 4.7623100280761719
		8.8817841970012523e-16 2.6028518013817581 4.437503921729026
		1.3322676295501878e-15 4.6218223791474298 2.8866529405375956
		1.7763568394002505e-15 5.3660433469514359 -0.76404728023843649
		1.1102230246251565e-15 3.6013105399631664 -4.0903813053187781
		3.9443045261050599e-31 1.2431743008821104e-15 -5.4578166651989735
		-1.3322676295501878e-15 -3.6013105399631682 -4.0903813053187807
		-1.7763568394002505e-15 -5.3714453646248304 -0.71895190675891651
		-1.3322676295501878e-15 -4.6034130444704227 2.6209458253739757
		-6.6613381477509392e-16 -2.6989046328726296 4.351834883243014
		-4.4408920985006262e-16 -1.5000000000000004 4.7623100000000003
		-3.3306690738754696e-16 -1.5 4.7623100000000003
		-3.3306690738754696e-16 -1.5 4.7623100000000003
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		-8.8817841970012523e-16 -2.6155099868774419 4.7623100280761719
		0 0 7
		0 0 7
		0 0 7
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		8.8817841970012523e-16 2.6155104637146001 4.7623100280761719
		3.3306690738754696e-16 1.5 4.7623100280761719
		;
createNode transform -n "input_01_link";
	rename -uid "36EE96CE-4F54-94B9-6438-9282B07A81E3";
	setAttr ".t" -type "double3" 0 10 0 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode transform -n "Fk_00_mstc" -p "input_01_link";
	rename -uid "D58E5FEF-4F4F-5B2C-2DD9-7F9729906C81";
createNode transform -n "BallFk_00_mstc" -p "Fk_00_mstc";
	rename -uid "A9428046-41F4-28DB-1CEA-7F8F456C3394";
	setAttr ".t" -type "double3" 0 -10 5 ;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "A6B6B208-4CCD-8116-0569-6A976CFA457A";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "DE99C331-478B-0238-C798-018FD207037F";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "E6E3F505-4933-7F58-0376-B285269D04F0";
createNode displayLayerManager -n "layerManager";
	rename -uid "865B0E29-4C58-CA5B-F82A-CE893352E2B4";
	setAttr ".cdl" 1;
	setAttr -s 2 ".dli[1]"  1;
createNode displayLayer -n "defaultLayer";
	rename -uid "3F894549-4527-FE7E-EA61-E4BE09A790F4";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "2BB7CAEC-43F7-F496-457D-F38BBB4200B4";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "F8D91FAB-4CFA-4821-DEAB-0880FE482C08";
	setAttr ".g" yes;
createNode clamp -n "BankFootRoll_00_clp";
	rename -uid "6DA6A5B4-4F3F-92E1-30EA-61BAA897957D";
	setAttr ".mn" -type "float3" 0 -999 -999 ;
	setAttr ".mx" -type "float3" 999 0 0 ;
createNode unitConversion -n "unitConversion1";
	rename -uid "CB7D2B6C-4A9F-0314-4598-DE9E5166CCB7";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion2";
	rename -uid "5FEB3A31-4054-BB25-352A-A398BCEA816B";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion3";
	rename -uid "03B7BA9E-4CB0-6C21-22A2-84AA4571C7F7";
	setAttr ".cf" 0.017453292519943295;
createNode unitConversion -n "unitConversion4";
	rename -uid "746F631E-42CA-F135-58D0-78B42FA58746";
	setAttr ".cf" 57.295779513082323;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "594EF02C-47EC-00F6-0D00-419D883A52DC";
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
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1185\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"wireframe\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1185\\n    -height 702\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "721A155F-4671-60CE-2580-CDB593ED7F0A";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode clamp -n "BankFootRoll_01_clp";
	rename -uid "3FEA5E84-44A1-9668-DAD8-3192E7F9017B";
	setAttr ".mn" -type "float3" -999 0 0 ;
	setAttr ".mx" -type "float3" 0 999 0 ;
createNode unitConversion -n "unitConversion12";
	rename -uid "8BE59E14-4E33-C9FD-8524-FFB214D1AC78";
	setAttr ".cf" 0.017453292519943295;
createNode plusMinusAverage -n "BankFootRoll_01_pma";
	rename -uid "40C882B9-4EC2-0A2B-8E2F-53B09D6E6B9D";
	setAttr ".op" 2;
	setAttr -s 2 ".i1";
	setAttr -s 2 ".i1";
createNode unitConversion -n "unitConversion14";
	rename -uid "D6CD5902-426A-8256-7BC4-20832C69E2D3";
	setAttr ".cf" 0.017453292519943295;
createNode clamp -n "bankBallRoll_00_clp";
	rename -uid "86FB773B-4EF1-F25C-3E54-8AA7CE9055DC";
createNode unitConversion -n "unitConversion16";
	rename -uid "D33B0D5C-4156-4711-EE9D-D6A585B1FF6E";
	setAttr ".cf" 0.017453292519943295;
createNode multDoubleLinear -n "bankBallRoll_00_mdbl";
	rename -uid "00899F2B-413A-2497-E35A-CC942770826C";
	setAttr ".i2" -1;
createNode unitConversion -n "unitConversion17";
	rename -uid "5C2AA0BC-4A9B-4CE8-0494-3CA71912EB36";
	setAttr ".cf" 0.017453292519943295;
createNode reverse -n "Ball_00_rev";
	rename -uid "707CEB74-45A8-2200-25A7-7C80BE32E85E";
createNode controller -n "BallMain_00_tag";
	rename -uid "344C0354-4015-8BD7-9063-8D8064FDAE5F";
createNode controller -n "BankToe_00_tag";
	rename -uid "1AACB508-4E12-7904-FA1E-27AD2F51561B";
	setAttr -s 2 ".child";
createNode controller -n "BankHeel_00_tag";
	rename -uid "A3B444A6-47D0-A81F-5F39-A5BE68DCDEB5";
createNode controller -n "RollMain_00_tag";
	rename -uid "7B8A2E77-4EB6-9D79-2F6E-67A872CCF921";
createNode controller -n "BallRoll_00_tag";
	rename -uid "F8C178C0-45F7-7A82-4B2E-AFB1B91E9A39";
createNode controller -n "Config_00_tag";
	rename -uid "D3D17858-413E-C122-2BCA-688E722176C6";
createNode controller -n "Ball_00_tag";
	rename -uid "6EE86862-45BA-7301-38CC-F9845E92EE68";
createNode script -n "MetadataTemplate";
	rename -uid "E69973AC-4851-4983-7EA2-DDAFF937C337";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_extendBehaviour" -ln "_extendBehaviour" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" (
		"import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#RollMain_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BankIn_00_footroll\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BankExt_00_footroll\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[2]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BankHeel_00_footroll\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[3]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\n"
		+ "del template, this\n#BallMain_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[4]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BankToe_00_footroll\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[5]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BankBall_00_footroll\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[6]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#FootIk_00_mstc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[7]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n"
		+ "#Fk_00_mstc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[8]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#BallFk_00_mstc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[9]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#_00_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[10]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#_01_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[11]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo[0]\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n# Mirror\n#BankFootRoll_00_clp\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[12]\")[0]\n"
		+ "if cmds.getAttr( template + \".mirror\" ):\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".min\", -999,0,-999 )\n    cmds.setAttr( cmds.listConnections(template + \"._relatedTo[0]\")[0] + \".max\", 0,999,0 )\ndel template");
	setAttr -l on ".stp" 1;
	setAttr -s 13 "._inputTemplate";
createNode multiplyDivide -n "RollMainNeg_00_mdv";
	rename -uid "270AE67C-43C6-DB07-5C8F-6EA84C9B07CE";
	setAttr ".i2" -type "float3" -1 -1 -1 ;
createNode unitConversion -n "unitConversion18";
	rename -uid "58FE16B9-40D9-CCEA-0892-798F343B4DBE";
	setAttr ".cf" 57.295779513082323;
createNode unitConversion -n "unitConversion19";
	rename -uid "6EC396AA-4369-B7A2-BAB2-CD82BAB3C63B";
	setAttr ".cf" 0.017453292519943295;
createNode objectSet -n "ControlsSet";
	rename -uid "D088C8E8-40AD-9F68-77BE-A7AA2F325D54";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "E431B871-4D58-74CF-A5A1-68A40059A30E";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "DE45C6F6-44BE-8E01-5CE8-618328A113D7";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" -419.82299819116167 -508.20017998323516 ;
	setAttr ".tgi[0].vh" -type "double2" 368.27667075142716 125.63763631679642 ;
createNode objectSet -n "LinkSet";
	rename -uid "9424C67A-4127-0950-6D87-0289BC9B72FE";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "Secondaries";
	rename -uid "2E1BC725-42CF-B92E-F1C5-39BE68EA0186";
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
select -ne :defaultRenderUtilityList1;
	setAttr -k on ".cch";
	setAttr -cb on ".ihi";
	setAttr -av -k on ".nds";
	setAttr -cb on ".bnm";
	setAttr -s 7 ".u";
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
connectAttr "Jnt_00_prcn.crx" "_00_jnt.rx";
connectAttr "Jnt_00_prcn.cry" "_00_jnt.ry";
connectAttr "Jnt_00_prcn.crz" "_00_jnt.rz";
connectAttr "Jnt_00_prcn.cty" "_00_jnt.ty";
connectAttr "Jnt_00_prcn.ctz" "_00_jnt.tz";
connectAttr "Jnt_00_prcn.ctx" "_00_jnt.tx";
connectAttr "_00_jnt.s" "_01_jnt.is";
connectAttr "_01_jnt_orientConstraint1.crx" "_01_jnt.rx";
connectAttr "_01_jnt_orientConstraint1.cry" "_01_jnt.ry";
connectAttr "_01_jnt_orientConstraint1.crz" "_01_jnt.rz";
connectAttr "_00_jnt.msg" "_01_jnt.parent";
connectAttr "_01_jnt.ro" "_01_jnt_orientConstraint1.cro";
connectAttr "_01_jnt.pim" "_01_jnt_orientConstraint1.cpim";
connectAttr "_01_jnt.jo" "_01_jnt_orientConstraint1.cjo";
connectAttr "_01_jnt.is" "_01_jnt_orientConstraint1.is";
connectAttr "Ball_00_ctr.r" "_01_jnt_orientConstraint1.tg[0].tr";
connectAttr "Ball_00_ctr.ro" "_01_jnt_orientConstraint1.tg[0].tro";
connectAttr "Ball_00_ctr.pm" "_01_jnt_orientConstraint1.tg[0].tpm";
connectAttr "_01_jnt_orientConstraint1.w0" "_01_jnt_orientConstraint1.tg[0].tw";
connectAttr "Ik_00_mstc.wm" "Jnt_00_prcn.tg[0].tpm";
connectAttr "Config_00_ctr.fkik" "Jnt_00_prcn.tg[0].tw";
connectAttr "Fk_00_mstc.wm" "Jnt_00_prcn.tg[1].tpm";
connectAttr "Ball_00_rev.ox" "Jnt_00_prcn.tg[1].tw";
connectAttr "_00_jnt.pim" "Jnt_00_prcn.cpim";
connectAttr "BallRoot_00_prc.cty" "Ball_00_root.ty";
connectAttr "BallRoot_00_prc.ctz" "Ball_00_root.tz";
connectAttr "BallRoot_00_prc.ctx" "Ball_00_root.tx";
connectAttr "BallRoot_00_prc.cry" "Ball_00_root.ry";
connectAttr "BallRoot_00_prc.crz" "Ball_00_root.rz";
connectAttr "BallRoot_00_prc.crx" "Ball_00_root.rx";
connectAttr "BallIk_00_mstc.wm" "BallRoot_00_prc.tg[0].tpm";
connectAttr "Config_00_ctr.fkik" "BallRoot_00_prc.tg[0].tw";
connectAttr "BallFk_00_mstc.wm" "BallRoot_00_prc.tg[1].tpm";
connectAttr "Ball_00_rev.ox" "BallRoot_00_prc.tg[1].tw";
connectAttr "Ball_00_root.pim" "BallRoot_00_prc.cpim";
connectAttr "MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "input_00_link.msg" "RollMainTpl_00_root._relatedTo[0]";
connectAttr "Config_00_tpl.mirror" "RollMainTpl_00_root.mirror";
connectAttr "BankIn_00_footroll.msg" "BankInTpl_00_footroll._relatedTo[0]";
connectAttr "BankExt_00_footroll.msg" "BankExtTpl_00_footroll._relatedTo[0]";
connectAttr "BankHeel_00_footroll.msg" "BankHeelTpl_00_footroll._relatedTo[0]";
connectAttr "BankToe_00_footroll.msg" "BankToeTpl_00_footroll._relatedTo[0]";
connectAttr "BallMain_00_root.msg" "BallMainTpl_00_root._relatedTo[0]";
connectAttr "BallFk_00_mstc.msg" "BallFkTpl_00_mstc._relatedTo[0]";
connectAttr "_01_jnt.msg" "Tpl_01_jnt._relatedTo[0]";
connectAttr "BankBall_00_footroll.msg" "BankBallTpl_00_footroll._relatedTo[0]";
connectAttr "Ik_00_mstc.msg" "IkTpl_00_mstc._relatedTo[0]";
connectAttr "input_01_link.msg" "FkTpl_00_mstc._relatedTo[0]";
connectAttr "_00_jnt.msg" "Tpl_00_jnt._relatedTo[0]";
connectAttr "BankFootRoll_00_clp.msg" "Config_00_tpl._relatedTo[0]";
connectAttr "Config_00_ctr.fkik" "RollMain_00_root.v";
connectAttr "unitConversion2.o" "BankIn_00_footroll.rz";
connectAttr "unitConversion3.o" "BankExt_00_footroll.rz";
connectAttr "unitConversion12.o" "BankHeel_00_footroll.rx";
connectAttr "unitConversion14.o" "BankToe_00_footroll.rx";
connectAttr "unitConversion16.o" "BankBall_00_footroll.rx";
connectAttr "RollMain_00_ctr.ry" "BankBall_00_footroll.ry";
connectAttr "unitConversion17.o" "BallIk_00_mstc.rx";
connectAttr "unitConversion19.o" "RollMainCtr_00_root.r";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "unitConversion1.o" "BankFootRoll_00_clp.ipr";
connectAttr "unitConversion1.o" "BankFootRoll_00_clp.ipg";
connectAttr "RollMain_00_ctr.rz" "unitConversion1.i";
connectAttr "BankFootRoll_00_clp.opr" "unitConversion2.i";
connectAttr "BankFootRoll_00_clp.opg" "unitConversion3.i";
connectAttr "RollMain_00_ctr.rx" "unitConversion4.i";
connectAttr "unitConversion4.o" "BankFootRoll_01_clp.ipr";
connectAttr "BankFootRoll_01_pma.o1" "BankFootRoll_01_clp.ipg";
connectAttr "BankFootRoll_01_clp.opr" "unitConversion12.i";
connectAttr "unitConversion4.o" "BankFootRoll_01_pma.i1[0]";
connectAttr "RollMain_00_ctr.ballBreak" "BankFootRoll_01_pma.i1[1]";
connectAttr "BankFootRoll_01_clp.opg" "unitConversion14.i";
connectAttr "unitConversion4.o" "bankBallRoll_00_clp.ipr";
connectAttr "RollMain_00_ctr.ballBreak" "bankBallRoll_00_clp.mxr";
connectAttr "bankBallRoll_00_clp.opr" "unitConversion16.i";
connectAttr "bankBallRoll_00_clp.opr" "bankBallRoll_00_mdbl.i1";
connectAttr "bankBallRoll_00_mdbl.o" "unitConversion17.i";
connectAttr "Config_00_ctr.fkik" "Ball_00_rev.ix";
connectAttr "BallMain_00_ctr.msg" "BallMain_00_tag.act";
connectAttr "BankToe_00_tag.pare" "BallMain_00_tag.child[0]";
connectAttr "BankToe_00_ctr.msg" "BankToe_00_tag.act";
connectAttr "BallRoll_00_tag.pare" "BankToe_00_tag.child[0]";
connectAttr "Ball_00_tag.pare" "BankToe_00_tag.child[1]";
connectAttr "BankHeel_00_ctr.msg" "BankHeel_00_tag.act";
connectAttr "BallMain_00_tag.pare" "BankHeel_00_tag.child[0]";
connectAttr "RollMain_00_ctr.msg" "RollMain_00_tag.act";
connectAttr "RollMain_00_tag.msg" "RollMain_00_tag.child[0]";
connectAttr "BallRoll_00_ctr.msg" "BallRoll_00_tag.act";
connectAttr "RollMain_00_tag.pare" "BallRoll_00_tag.child[0]";
connectAttr "Config_00_ctr.msg" "Config_00_tag.act";
connectAttr "Config_00_tag.msg" "Config_00_tag.child[0]";
connectAttr "Ball_00_ctr.msg" "Ball_00_tag.act";
connectAttr "Ball_00_tag.msg" "Ball_00_tag.child[0]";
connectAttr "RollMainTpl_00_root.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "BankInTpl_00_footroll.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "BankExtTpl_00_footroll.msg" "MetadataTemplate._inputTemplate[2]";
connectAttr "BankHeelTpl_00_footroll.msg" "MetadataTemplate._inputTemplate[3]";
connectAttr "BallMainTpl_00_root.msg" "MetadataTemplate._inputTemplate[4]";
connectAttr "BankToeTpl_00_footroll.msg" "MetadataTemplate._inputTemplate[5]";
connectAttr "BankBallTpl_00_footroll.msg" "MetadataTemplate._inputTemplate[6]";
connectAttr "IkTpl_00_mstc.msg" "MetadataTemplate._inputTemplate[7]";
connectAttr "FkTpl_00_mstc.msg" "MetadataTemplate._inputTemplate[8]";
connectAttr "BallFkTpl_00_mstc.msg" "MetadataTemplate._inputTemplate[9]";
connectAttr "Tpl_00_jnt.msg" "MetadataTemplate._inputTemplate[10]";
connectAttr "Tpl_01_jnt.msg" "MetadataTemplate._inputTemplate[11]";
connectAttr "Config_00_tpl.msg" "MetadataTemplate._inputTemplate[12]";
connectAttr "unitConversion18.o" "RollMainNeg_00_mdv.i1";
connectAttr "RollMain_00_ctr.r" "unitConversion18.i";
connectAttr "RollMainNeg_00_mdv.o" "unitConversion19.i";
connectAttr "RollMain_00_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "Ball_00_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "_00_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "_01_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "input_00_link.iog" "LinkSet.dsm" -na;
connectAttr "input_01_link.iog" "LinkSet.dsm" -na;
connectAttr "output_00_link.iog" "LinkSet.dsm" -na;
connectAttr "BankHeel_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "BallRoll_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "BallMain_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "BankToe_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "BankFootRoll_00_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "BankFootRoll_01_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "BankFootRoll_01_pma.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "bankBallRoll_00_clp.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "bankBallRoll_00_mdbl.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "Ball_00_rev.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "RollMainNeg_00_mdv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
// End of footRoll.ma
