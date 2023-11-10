//Maya ASCII 2020 scene
//Name: spineIkFk3Bones.ma
//Last modified: Tue, Jul 19, 2022 11:02:36 AM
//Codeset: 1252
file -rdi 1 -ns "SpineIk" -rfn "SpineIkRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/curve/3Ik2Bezier.ma";
file -rdi 1 -ns "SpineFk" -rfn "SpineFkRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/curve/3Controls.ma";
file -r -ns "SpineIk" -dr 1 -rfn "SpineIkRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/curve/3Ik2Bezier.ma";
file -r -ns "SpineFk" -dr 1 -rfn "SpineFkRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/curve/3Controls.ma";
requires maya "2020";
requires "stereoCamera" "10.0";
requires "mtoa" "4.1.1";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2020";
fileInfo "version" "2020";
fileInfo "cutIdentifier" "202011110415-b1e20b88e2";
fileInfo "osv" "Microsoft Windows 10 Technical Preview  (Build 19043)\n";
fileInfo "UUID" "FC1C60D9-4973-31ED-1369-069326EA387D";
createNode transform -s -n "persp";
	rename -uid "8523C6E0-4607-D599-114E-AC86C600FA3D";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 23.749426572540614 29.259926884973535 65.426805437079864 ;
	setAttr ".r" -type "double3" -15.938352729614911 21.800000000012162 4.2819106514370627e-16 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "39AA19EE-4FED-F4DF-ED2E-7FBB74E3A891";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".coi" 76.843017131218289;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "1D1BB94D-4664-4613-03E6-44935A9A7C15";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 1000.1 0 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "F4CD52C3-43A6-1E4C-C18A-A6B4CE82E163";
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
	rename -uid "97DCDBF2-4890-14B6-E48F-FD8CE27D9A0B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0 0 1000.1 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "D8EDC6A1-450E-C9E0-88D1-C5981222146F";
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
	rename -uid "AF28C0A7-48BA-AC32-DBF1-B99CB229C739";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1 0 0 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "99655BA1-443D-8E3E-53A8-3A87137E2215";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 30;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "Hips_00_jnt";
	rename -uid "F384F189-4611-1C8A-6FA5-0680A4303832";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
createNode parentConstraint -n "Hips_00_jnt_parentConstraint1" -p "Hips_00_jnt";
	rename -uid "75C63AA6-4867-CFED-227B-0588FEB9AB99";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Hips_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 180 0 ;
	setAttr -k on ".w0";
createNode joint -n "Chest_00_jnt";
	rename -uid "084F84B3-4F12-6B97-5A1E-5FBE947723BD";
	addAttr -s false -ci true -sn "parent" -ln "parent" -at "message";
	setAttr ".mnrl" -type "double3" -360 -360 -360 ;
	setAttr ".mxrl" -type "double3" 360 360 360 ;
	setAttr ".jo" -type "double3" 0 0 -38.034700230458498 ;
createNode parentConstraint -n "ChestJnt_00_jnt_prc" -p "Chest_00_jnt";
	rename -uid "13841EA5-4803-13C5-0475-52B76A7698E2";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Chest_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".lr" -type "double3" 0 0 38.03470023045849 ;
	setAttr ".rst" -type "double3" 0 4.025001 0 ;
	setAttr -k on ".w0";
createNode transform -n "Spine:Sys_00_grp";
	rename -uid "9CFC6D4A-42AC-FC58-D8F1-589980A34958";
	setAttr ".v" no;
createNode transform -n "Spine:FinalSpl_00_crv" -p "Spine:Sys_00_grp";
	rename -uid "3BE3A4D6-4244-0703-2301-34AB1BA30B99";
createNode nurbsCurve -n "Spine:FinalSpl_00_crvShape" -p "Spine:FinalSpl_00_crv";
	rename -uid "F3D2F4E1-4EBC-2CF2-4F35-B6950FDE9686";
	setAttr -k off ".v";
	setAttr ".tw" yes;
createNode transform -n "Tpl_00_tpl";
	rename -uid "71335D63-401C-41E0-D792-4AA6EEE708A5";
	addAttr -s false -ci true -h true -sn "metadataTemplate" -ln "metadataTemplate" 
		-at "message";
	setAttr ".v" no;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 1 1 0.3882353 ;
createNode transform -n "SpineTpl_02_tr" -p "Tpl_00_tpl";
	rename -uid "94C44BE1-478C-AAA2-8BB0-B0B2633B87CD";
	addAttr -ci true -sn "uValue" -ln "uValue" -at "double";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
	setAttr -k on ".uValue" 1;
createNode locator -n "SpineTpl_02_trShape" -p "SpineTpl_02_tr";
	rename -uid "79E08078-43F8-9C9C-E60C-D28572F2B497";
	setAttr -k off ".v";
createNode aimConstraint -n "SpineTpl_02_tr_aimConstraint1" -p "SpineTpl_02_tr";
	rename -uid "E90F53BB-4136-225B-5F80-C38B9584E01D";
	addAttr -dcb 0 -ci true -sn "w0" -ln "SplPosTpl_00_rootW0" -dv 1 -at "double";
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
	setAttr ".a" -type "double3" 0 1 0 ;
	setAttr ".u" -type "double3" 0 0 1 ;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".wut" 2;
	setAttr -k on ".w0";
createNode transform -n "SpineTpl_01_tr" -p "Tpl_00_tpl";
	rename -uid "40225551-4BC7-728C-28AB-10902126F6E8";
	addAttr -ci true -sn "uValue" -ln "uValue" -at "double";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -k off ".rx";
	setAttr -k off ".ry";
	setAttr -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr ".it" no;
	setAttr -k on ".uValue" 0.5;
createNode locator -n "SpineTpl_01_trShape" -p "SpineTpl_01_tr";
	rename -uid "2914F910-4129-AEEA-E55B-01BB0F340EA4";
	setAttr -k off ".v";
createNode aimConstraint -n "SpineTpl_01_mp_aimConstraint1" -p "SpineTpl_01_tr";
	rename -uid "7BA78EC5-44DD-35E2-0F6B-6580233C2E93";
	addAttr -dcb 0 -ci true -sn "w0" -ln "SpineIkTpl_02_mpW0" -dv 1 -at "double";
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
	setAttr ".a" -type "double3" 0 1 0 ;
	setAttr ".u" -type "double3" 1 0 0 ;
	setAttr ".wu" -type "double3" 1 0 0 ;
	setAttr ".wut" 2;
	setAttr -k on ".w0";
createNode transform -n "Controls_00_grp";
	rename -uid "A1266BFE-47BE-DE4D-435D-028925B0A764";
createNode transform -n "Spine:Config_00_root" -p "Controls_00_grp";
	rename -uid "49D7009B-4CCE-B726-AA8D-1688E6B8A982";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Spine:Config_00_ctr" -p "Spine:Config_00_root";
	rename -uid "BC5D14A6-4390-717E-C661-3FAF61C1ADCA";
	addAttr -ci true -k true -sn "fkIk" -ln "fkIk" -min 0 -max 1 -at "double";
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
	setAttr -k on ".fkIk";
createNode nurbsCurve -n "Spine:Config_00_ctrShape" -p "Spine:Config_00_ctr";
	rename -uid "37CFBFA0-44E3-DBD6-6747-8088AA0516D8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 10 2 no 3
		11 0 1 2 3 4 5 6 7 8 9 10
		11
		-5.5511151231257827e-16 2.8379390945597356 -1.6054565561205578
		-5.2041704279304213e-18 2.8379390945597356 -0.01964311643958043
		-5.2041704279304213e-18 0 -0.01964311643958043
		-1.1102230246251565e-16 0 -0.42233082085178753
		-1.1102230246251565e-16 1.2885691114173157 -0.42233082085178753
		-3.3306690738754696e-16 1.2885691114173157 -1.415619150166139
		-3.3306690738754696e-16 1.5857741194452566 -1.415619150166139
		-1.1102230246251565e-16 1.5857741194452566 -0.42233082085178753
		-1.1102230246251565e-16 2.5368853751423321 -0.42233082085178753
		-5.5511151231257827e-16 2.5368853751423321 -1.6054565561205578
		-5.5511151231257827e-16 2.8379390945597356 -1.6054565561205578
		;
createNode nurbsCurve -n "Spine:Config_00_ctrShape1" -p "Spine:Config_00_ctr";
	rename -uid "D0E665D5-4A15-4C5A-FFD0-4486E75E186E";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-6.6613381477509392e-16 2.8379390945597356 -2.5180424591019475
		-6.6613381477509392e-16 2.8379390945597356 -2.1402920461444253
		-6.6613381477509392e-16 0 -2.1402920461444253
		-6.6613381477509392e-16 0 -2.5180424591019475
		-6.6613381477509392e-16 1.4381534966530989 -2.5180424591019475
		-1.1102230246251565e-15 0 -3.7587006635403477
		-1.3322676295501878e-15 0 -4.267656257866868
		-6.6613381477509392e-16 1.4838652388530824 -2.9597657276493399
		-1.3322676295501878e-15 2.8379390945597356 -4.0713786385185529
		-1.1102230246251565e-15 2.8379390945597356 -3.6666489205005481
		-6.6613381477509392e-16 1.441962844550249 -2.5180424591019475
		-6.6613381477509392e-16 2.8379390945597356 -2.5180424591019475
		;
createNode nurbsCurve -n "Spine:Config_00_ctrShape2" -p "Spine:Config_00_ctr";
	rename -uid "DF4B1FE6-4A06-8DCE-B8CD-B4B05BF1B993";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-2.2204460492503131e-15 2.8379390945597356 -5.9604058151864754
		-2.2204460492503131e-15 2.8379390945597356 -5.7609860375072959
		-1.3322676295501878e-15 -0.56758781891194632 -4.7523424856669294
		-1.3322676295501878e-15 -0.56758781891194632 -4.951761917293422
		-2.2204460492503131e-15 2.8379390945597356 -5.9604058151864754
		;
createNode nurbsCurve -n "Spine:Config_00_ctrShape3" -p "Spine:Config_00_ctr";
	rename -uid "B4B87D4A-4043-0A4C-F13D-10A5313E04C0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-2.6645352591003757e-15 2.8379390945597356 -8.2516489832077085
		-2.6645352591003757e-15 2.8379390945597356 -7.8738985702501845
		-2.6645352591003757e-15 0 -7.8738985702501845
		-2.6645352591003757e-15 0 -8.2516489832077085
		-2.6645352591003757e-15 1.4381534966530989 -8.2516489832077085
		-3.5527136788005009e-15 0 -9.4923073606724486
		-2.6645352591003757e-15 0 -10.001262954998968
		-2.6645352591003757e-15 1.4838652388530824 -8.6933720787287641
		-3.5527136788005009e-15 2.8379390945597356 -9.8049853356506436
		-2.6645352591003757e-15 2.8379390945597356 -9.4002552715799759
		-2.6645352591003757e-15 1.441962844550249 -8.2516489832077085
		-2.6645352591003757e-15 2.8379390945597356 -8.2516489832077085
		;
createNode nurbsCurve -n "Spine:Config_00_ctrShape4" -p "Spine:Config_00_ctr";
	rename -uid "9512FFD6-41D7-7849-67C9-979771C49EC5";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-2.6645352591003757e-15 2.8379390945597356 -7.1357945046445108
		-2.2204460492503131e-15 2.8379390945597356 -6.7331068434888923
		-2.2204460492503131e-15 0 -6.7331068434888923
		-2.6645352591003757e-15 0 -7.1357945046445108
		-2.6645352591003757e-15 2.8379390945597356 -7.1357945046445108
		;
createNode parentConstraint -n "Spine:ConfigRoot_00_prc" -p "Spine:Config_00_root";
	rename -uid "AFF42AD2-461D-A801-10CE-B19BEF5D0DFA";
createNode transform -n "Hips_00_root" -p "Controls_00_grp";
	rename -uid "11032908-4E55-8053-0BAF-198DABCC5956";
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Hips_00_ctr" -p "Hips_00_root";
	rename -uid "07012CC0-4538-27E9-DEEA-42ACBD7716FC";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Hips_00_ctrShape" -p "Hips_00_ctr";
	rename -uid "B5571ECB-4E11-A028-9D1D-138880529DD3";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-3.75 3.75 -3.75
		-3.75 3.75 3.75
		-3.75 -3.75 3.75
		3.75 -3.75 3.75
		3.75 3.75 3.75
		3.75 3.75 -3.75
		3.75 -3.75 -3.75
		-3.75 -3.75 -3.75
		-3.75 3.75 -3.75
		3.75 3.75 -3.75
		3.75 3.75 3.75
		-3.75 3.75 3.75
		-3.75 -3.75 3.75
		3.75 -3.75 3.75
		3.75 -3.75 -3.75
		-3.75 -3.75 -3.75
		-3.75 -3.75 3.75
		;
createNode transform -n "output_01_link" -p "Hips_00_ctr";
	rename -uid "99DB5D65-4AF8-05A4-22B1-A5B586F40F47";
	setAttr ".t" -type "double3" -3.3306690738754696e-16 -3.3306690738754696e-16 4.0788932203406729e-32 ;
	setAttr ".r" -type "double3" 0 180 0 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.40392157 0.63137257 ;
createNode pointConstraint -n "Hips_00_root_pointConstraint1" -p "Hips_00_root";
	rename -uid "A19A1A8E-4167-63B3-9FD7-7A91C8DBDDE4";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "Spl_00_ctrW0" -dv 1 -min 0 -at "double";
	addAttr -dcb 0 -ci true -k true -sn "w1" -ln "_00_ctrW1" -dv 1 -min 0 -at "double";
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
	setAttr ".o" -type "double3" -1.6653345369377348e-16 0 0 ;
	setAttr ".rst" -type "double3" -1.6653345369377348e-16 3.3306690738754696e-16 0 ;
	setAttr -k on ".w0";
	setAttr -k on ".w1";
createNode transform -n "Chest_00_root" -p "Controls_00_grp";
	rename -uid "64D24DF0-401A-A2E0-AB64-2F9FAF2A989B";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Chest_00_ctr" -p "Chest_00_root";
	rename -uid "1FAB95F5-4217-C260-E3A6-30AA04828515";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Chest_00_ctrShape" -p "Chest_00_ctr";
	rename -uid "09888DF6-4332-A359-0467-4E936D7F6714";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-3.75 3.75 -3.75
		-3.75 3.75 3.75
		-3.75 -3.75 3.75
		3.75 -3.75 3.75
		3.75 3.75 3.75
		3.75 3.75 -3.75
		3.75 -3.75 -3.75
		-3.75 -3.75 -3.75
		-3.75 3.75 -3.75
		3.75 3.75 -3.75
		3.75 3.75 3.75
		-3.75 3.75 3.75
		-3.75 -3.75 3.75
		3.75 -3.75 3.75
		3.75 -3.75 -3.75
		-3.75 -3.75 -3.75
		-3.75 -3.75 3.75
		;
createNode transform -n "output_00_link" -p "Chest_00_ctr";
	rename -uid "F01999CA-458F-1EC5-096E-EBAE29D7F21A";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.40392157 0.63137257 ;
createNode parentConstraint -n "ChestRoot_00_prc" -p "Chest_00_root";
	rename -uid "4E08F641-4621-BD9F-5C90-F09ABA32C17C";
	setAttr -s 2 ".tg";
createNode transform -n "input_01_link";
	rename -uid "2865EB45-4DA0-D1F6-6C3F-71B9CE381BE0";
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.1882353 0.63137257 0.63137257 ;
createNode fosterParent -n "SpineIkRNfosterParent1";
	rename -uid "0CEE677F-4FFA-D04B-296D-B1851718A65A";
createNode transform -n "ChestRootIk_00_mstc" -p "SpineIkRNfosterParent1";
	rename -uid "EEA4BB13-4187-AA9D-ECAB-4493DDAF0B2E";
	setAttr ".t" -type "double3" 0 -10 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "ChestRootTpl_00_mstc" -p "SpineIkRNfosterParent1";
	rename -uid "24C19092-4613-52B1-EAF3-23B3AD81709C";
	addAttr -s false -ci true -h true -m -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -s 2 "._relatedTo";
createNode locator -n "ChestRootTpl_00_mstcShape" -p "ChestRootTpl_00_mstc";
	rename -uid "13CBD9AF-4E91-3810-DFFA-2DA5E323B737";
	setAttr -k off ".v";
	setAttr ".los" -type "double3" 0.5 0.5 0.5 ;
createNode orientConstraint -n "ChestRootTpl_00_mstc_orientConstraint1" -p "ChestRootTpl_00_mstc";
	rename -uid "163AB941-481D-3E31-C894-BCB626D0A8CE";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SpineTpl_02_trW0" -dv 1 -min 0 -at "double";
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
createNode fosterParent -n "SpineFkRNfosterParent1";
	rename -uid "02CECC37-4471-021F-EE58-84A964E0B78F";
createNode transform -n "ChestRootFk_00_mstc" -p "SpineFkRNfosterParent1";
	rename -uid "41967C95-4554-B799-A1B9-DCA64FD61940";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode pointConstraint -n "Tpl_00_root_pointConstraint1" -p "SpineFkRNfosterParent1";
	rename -uid "951E83CA-4AAA-E0CF-060A-E68F581E8989";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "OrigPosTpl_00_trW0" -dv 1 -min 0 
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
	setAttr -k on ".w0";
createNode aimConstraint -n "Tpl_00_root_aimConstraint1" -p "SpineFkRNfosterParent1";
	rename -uid "9ECB485A-4940-C96F-9C9E-65A4D223A938";
	addAttr -dcb 0 -ci true -sn "w0" -ln "SpineTpl_01_trW0" -dv 1 -at "double";
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
	setAttr ".a" -type "double3" 0 1 0 ;
	setAttr ".u" -type "double3" 0 0 1 ;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".wut" 2;
	setAttr -k on ".w0";
createNode parentConstraint -n "Tpl_01_root_parentConstraint1" -p "SpineFkRNfosterParent1";
	rename -uid "EC2E2387-459C-3D50-5D4A-6D93EDF14A20";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SpineTpl_01_trW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode parentConstraint -n "Tpl_02_root_parentConstraint1" -p "SpineFkRNfosterParent1";
	rename -uid "045FF12C-4F2D-B90A-9300-ECA543E41B59";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "SpineTpl_02_trW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 10 0 ;
	setAttr -k on ".w0";
createNode lightLinker -s -n "lightLinker1";
	rename -uid "E7D6F5A0-4673-C294-ECD3-788F526122EC";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "1883A7BA-4953-4CA7-29FC-F28E59019D0D";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "4504E102-4A65-0801-AA72-9BA61927790D";
createNode displayLayerManager -n "layerManager";
	rename -uid "5D077CD1-4E2D-B6DB-F910-449DDD497D22";
createNode displayLayer -n "defaultLayer";
	rename -uid "5657BDAD-45F5-EE29-D414-5EA42CCA62A4";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "6E4C1791-45B2-02C5-7E70-D88D730B5A1C";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "4792283D-46C0-95E1-DA0D-3F99C7871690";
	setAttr ".g" yes;
createNode renderLayer -n "spineIkFk3Bones_defaultRenderLayer";
	rename -uid "03048DB8-4656-038C-2E52-788B07ACD1A0";
	setAttr ".g" yes;
createNode reference -n "SpineIkRN";
	rename -uid "8803A3E4-4AB3-C961-6706-BCAD4F114599";
	setAttr -s 2 ".fn";
	setAttr ".fn[0]" -type "string" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/curve/3Ik2Bezier.ma";
	setAttr ".fn[1]" -type "string" "C:/Users/dricobarral/Desktop/d_module/AutoRig/misc/modules/spline3IkCtr2BezierCtr.ma";
	setAttr -s 31 ".phl";
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
	setAttr ".ed" -type "dataReferenceEdits" 
		"SpineIkRN"
		"SpineIkRN" 3
		2 "|SpineIk:SplPosCOG_00_spc" "translate" " -type \"double3\" 0 30 0"
		5 2 "SpineIkRN" "SpineIk:MetadataTemplate._extendBehaviour[0]" "SpineIkRN.placeHolderList[46]" 
		""
		5 3 "SpineIkRN" "SpineIk:TemplateSet.message" "SpineIkRN.placeHolderList[69]" 
		""
		"SpineIkRN" 61
		0 "|SpineIk:Sys_00_grp" "|Spine:Sys_00_grp" "-s -r "
		0 "|SpineIk:Tpl_00_tpl" "|Tpl_00_tpl" "-s -r "
		0 "|SpineIk:SplControls_00_grp" "|Controls_00_grp" "-s -r "
		0 "|SpineIk:input_00_link" "|input_01_link" "-s -r "
		0 "|SpineIkRNfosterParent1|ChestRootTpl_00_mstc" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root|SpineIk:SplTplTop_03_off|SpineIk:SplTpl_03_loc" 
		"-s -r "
		0 "|SpineIkRNfosterParent1|ChestRootIk_00_mstc" "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr" 
		"-s -r "
		2 "|Spine:Sys_00_grp|SpineIk:Sys_00_grp|SpineIk:OrigPos_00_tr|SpineIk:PosAux_00_jnt|SpineIk:PosAux_01_jnt" 
		"translate" " -type \"double3\" 10 0 0"
		2 "|Spine:Sys_00_grp|SpineIk:Sys_00_grp|SpineIk:OrigPos_00_tr|SpineIk:PosAux_00_jnt|SpineIk:PosAux_01_jnt|SpineIk:PosAux_02_jnt" 
		"translate" " -type \"double3\" 10 0 0"
		2 "|Spine:Sys_00_grp|SpineIk:Sys_00_grp|SpineIk:OrigPos_00_tr|SpineIk:PosAux_00_jnt|SpineIk:PosAux_01_jnt|SpineIk:PosAux_02_jnt|SpineIk:PosAux_03_jnt" 
		"translate" " -type \"double3\" 10 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:SplPos_01_root|SpineIk:SplPos_01_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr|SpineIk:Spl_03_loc|SpineIk:Spl_03_locShape" 
		"localPosition" " -type \"double3\" 0 -10 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr|SpineIk:SplBezier_01_root" 
		"translate" " -type \"double3\" 0 -14 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_02_root|SpineIk:Spl_02_aux|SpineIk:Spl_02_ctr|SpineIk:SplBezier_01_root|SpineIk:SplBezier_01_off|SpineIk:SplBezier_01_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr|SpineIk:SplBezier_00_root" 
		"translate" " -type \"double3\" 0 4 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr|SpineIk:SplBezier_00_root|SpineIk:SplBezier_00_off|SpineIk:SplBezier_00_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_01_root|SpineIk:Spl_01_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_01_root|SpineIk:Spl_01_root_pointConstraint1" 
		"Spl_00_ctrW0" " -k 1 0.6666"
		2 "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_01_root|SpineIk:Spl_01_root_pointConstraint1" 
		"Spl_02_ctrW1" " -k 1 0.3333"
		2 "|Tpl_00_tpl|SpineIk:Tpl_00_tpl" "visibility" " 0"
		2 "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplBezierTpl_00_root" 
		"translate" " -type \"double3\" 0 4 0"
		2 "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root" 
		"translate" " -type \"double3\" 0 30 0"
		2 "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root|SpineIk:SplTplTop_03_off|SpineIk:SplTpl_03_loc" 
		"translate" " -type \"double3\" 0 -10 0"
		2 "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root|SpineIk:SplTplTop_03_off|SpineIk:SplBezierTpl_01_root" 
		"translate" " -type \"double3\" 0 -14 0"
		2 "|SpineIk:SplPosWorld_00_spc" "translate" " -type \"double3\" 0 30 0"
		2 "|input_01_link|SpineIk:input_00_link" "translate" " -type \"double3\" 0 0 0"
		
		2 "|input_01_link|SpineIk:input_00_link|SpineIk:SplPos_00_root" "translate" 
		" -type \"double3\" 0 0 0"
		2 "|input_01_link|SpineIk:input_00_link|SpineIk:SplPos_00_root|SpineIk:SplPos_00_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		5 3 "SpineIkRN" "|Spine:Sys_00_grp|SpineIk:Sys_00_grp|SpineIk:Spl_00_crv|SpineIk:Spl_00_crvShape.worldSpace" 
		"SpineIkRN.placeHolderList[70]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.translate" 
		"SpineIkRN.placeHolderList[71]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.rotatePivot" 
		"SpineIkRN.placeHolderList[72]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.rotatePivotTranslate" 
		"SpineIkRN.placeHolderList[73]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.parentMatrix" 
		"SpineIkRN.placeHolderList[74]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.worldMatrix" 
		"SpineIkRN.placeHolderList[75]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.worldMatrix" 
		"SpineIkRN.placeHolderList[76]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr.worldMatrix" 
		"SpineIkRN.placeHolderList[77]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.worldMatrix" 
		"SpineIkRN.placeHolderList[78]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.worldMatrix" 
		"SpineIkRN.placeHolderList[79]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.translate" 
		"SpineIkRN.placeHolderList[80]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.rotatePivot" 
		"SpineIkRN.placeHolderList[81]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.rotatePivotTranslate" 
		"SpineIkRN.placeHolderList[82]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:SplPosTpl_00_root.parentMatrix" 
		"SpineIkRN.placeHolderList[83]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:referenceTpl_00_crv|SpineIk:referenceTpl_00_crvShape.worldSpace" 
		"SpineIkRN.placeHolderList[84]" ""
		5 3 "SpineIkRN" "|Tpl_00_tpl|SpineIk:Tpl_00_tpl|SpineIk:OrigPosTpl_00_tr|SpineIk:referenceTpl_00_crv|SpineIk:referenceTpl_00_crvShape.worldSpace" 
		"SpineIkRN.placeHolderList[85]" ""
		5 4 "SpineIkRN" "|Controls_00_grp|SpineIk:SplControls_00_grp.visibility" 
		"SpineIkRN.placeHolderList[86]" ""
		5 3 "SpineIkRN" "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr.translate" 
		"SpineIkRN.placeHolderList[87]" ""
		5 3 "SpineIkRN" "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr.rotatePivot" 
		"SpineIkRN.placeHolderList[88]" ""
		5 3 "SpineIkRN" "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr.rotatePivotTranslate" 
		"SpineIkRN.placeHolderList[89]" ""
		5 3 "SpineIkRN" "|Controls_00_grp|SpineIk:SplControls_00_grp|SpineIk:Spl_00_root|SpineIk:Spl_00_aux|SpineIk:Spl_00_ctr.parentMatrix" 
		"SpineIkRN.placeHolderList[90]" ""
		5 4 "SpineIkRN" "|input_01_link|SpineIk:input_00_link|SpineIk:SplPos_00_root.visibility" 
		"SpineIkRN.placeHolderList[91]" ""
		5 3 "SpineIkRN" "SpineIk:ControlsSet.message" "SpineIkRN.placeHolderList[92]" 
		""
		5 3 "SpineIkRN" "SpineIk:SkinJointsSet.message" "SpineIkRN.placeHolderList[93]" 
		""
		5 4 "SpineIkRN" "SpineIk:Spl_00_tag.children[1]" "SpineIkRN.placeHolderList[94]" 
		""
		5 4 "SpineIkRN" "SpineIk:Spl_02_tag.children[1]" "SpineIkRN.placeHolderList[95]" 
		""
		5 3 "SpineIkRN" "SpineIk:MetadataTemplate.message" "SpineIkRN.placeHolderList[96]" 
		""
		5 2 "SpineIkRN" "SpineIk:MetadataTemplate._postExecution[0]" "SpineIkRN.placeHolderList[97]" 
		""
		5 4 "SpineIkRN" "SpineIk:MetadataTemplate._postExecution[1]" "SpineIkRN.placeHolderList[98]" 
		""
		5 3 "SpineIkRN" "SpineIk:LinkSet.message" "SpineIkRN.placeHolderList[99]" 
		"";
lockNode -l 1 ;
createNode reverse -n "FkIk_00_rev";
	rename -uid "6028C9C7-450A-C94F-94F8-C4AC684DA312";
createNode objectSet -n "ControlsSet";
	rename -uid "882C3E9C-4B85-6313-CC39-1CB73E5C83C4";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "90C78442-410D-07C6-EE6F-06B81C387529";
	setAttr ".ihi" 0;
	setAttr -s 2 ".dsm";
	setAttr -s 2 ".dnsm";
createNode motionPath -n "SpineIk:FkTplTr_01_mp";
	rename -uid "78DA2FC6-4CEC-1E93-540F-DDA73F068E53";
	setAttr ".wut" 2;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".fm" yes;
createNode motionPath -n "SpineIk:TplTr_02_mp";
	rename -uid "C4619D4B-41E6-6C3C-6348-E4AD9A5BBF8F";
	setAttr ".wut" 2;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".fm" yes;
createNode controller -n "Chest_00_tag";
	rename -uid "A73EAB0C-4C47-D19C-CE17-19BD1F61840F";
createNode controller -n "Hips_00_tag";
	rename -uid "7EF9E78E-4057-ACA6-E58D-00A156772089";
createNode controller -n "Config_00_tag";
	rename -uid "68F32881-4329-24AC-0B09-288372690280";
createNode reference -n "sharedReferenceNode";
	rename -uid "10344FDA-4F35-C1EB-47EB-F6B53234BF08";
	setAttr ".ed" -type "dataReferenceEdits" 
		"sharedReferenceNode";
createNode script -n "uiConfigurationScriptNode";
	rename -uid "C7DFE7AE-4406-E18E-7E2A-D186FAEF726E";
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
	rename -uid "9AD9D27C-4D84-B6C0-5118-E9A6954AF70F";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode script -n "Spine:MetadataTemplate";
	rename -uid "23F62779-461C-9DA1-AC70-49A8B5FF64CE";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_postExecution" -ln "_postExecution" -at "message";
	addAttr -s false -ci true -m -sn "_preExecution" -ln "_preExecution" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" "import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)[0]\n#ChestRoot_01_mstc\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nfor this in cmds.listConnections(template + \"._relatedTo\"):\n    cmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this";
	setAttr -l on ".stp" 1;
	setAttr -s 2 "._preExecution";
createNode reference -n "SpineFkRN";
	rename -uid "63DB1BA8-4752-E5A0-C53A-62939941A137";
	setAttr -s 47 ".phl";
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
	setAttr ".phl[88]" 0;
	setAttr ".phl[89]" 0;
	setAttr ".ed" -type "dataReferenceEdits" 
		"SpineFkRN"
		"SpineFkRN" 1
		5 3 "SpineFkRN" "SpineFk:TemplateSet.message" "SpineFkRN.placeHolderList[43]" 
		""
		"SpineFkRN" 65
		0 "|SpineFk:Sys_00_grp" "|Spine:Sys_00_grp" "-s -r "
		0 "|SpineFk:Tpl_00_tpl" "|Tpl_00_tpl" "-s -r "
		0 "|SpineFk:input_00_link" "|input_01_link" "-s -r "
		0 "|SpineFkRNfosterParent1|Tpl_02_root_parentConstraint1" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root" 
		"-s -r "
		0 "|SpineFkRNfosterParent1|Tpl_01_root_parentConstraint1" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root" 
		"-s -r "
		0 "|SpineFkRNfosterParent1|Tpl_00_root_aimConstraint1" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root" 
		"-s -r "
		0 "|SpineFkRNfosterParent1|Tpl_00_root_pointConstraint1" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root" 
		"-s -r "
		0 "|SpineFkRNfosterParent1|ChestRootFk_00_mstc" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr|SpineFk:_02_root|SpineFk:_02_ctr|SpineFk:Crv_03_loc|SpineFk:output_00_link" 
		"-s -r "
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl" "visibility" " 0"
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_00_rootShape" 
		"visibility" " -k 0 0"
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_01_rootShape" 
		"visibility" " -k 0 0"
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root|SpineFk:Tpl_02_rootShape" 
		"visibility" " -k 0 0"
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root|SpineFk:CrvTpl_03_loc" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root|SpineFk:CrvTpl_03_loc|SpineFk:CrvTpl_03_locShape" 
		"visibility" " -k 0 0"
		2 "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr|SpineFk:_02_root|SpineFk:_02_ctr" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr|SpineFk:_02_root|SpineFk:_02_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr|SpineFk:_02_root|SpineFk:_02_ctr|SpineFk:Crv_03_loc" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr|SpineFk:_01_root|SpineFk:_01_ctr|SpineFk:_02_root|SpineFk:_02_ctr|SpineFk:Crv_03_loc|SpineFk:output_00_link" 
		"translate" " -type \"double3\" 0 0 0"
		5 1 "SpineFkRN" "SpineFk:MetadataTemplate.message" "SpineFkRN.placeHolderList[44]" 
		""
		5 3 "SpineFkRN" "|Spine:Sys_00_grp|SpineFk:Sys_00_grp|SpineFk:Quadratic_00_crv|SpineFk:Quadratic_00_crvShape.worldSpace" 
		"SpineFkRN.placeHolderList[45]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.translate" 
		"SpineFkRN.placeHolderList[46]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.translateX" 
		"SpineFkRN.placeHolderList[47]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.translateY" 
		"SpineFkRN.placeHolderList[48]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.translateZ" 
		"SpineFkRN.placeHolderList[49]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.parentInverseMatrix" 
		"SpineFkRN.placeHolderList[50]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.parentInverseMatrix" 
		"SpineFkRN.placeHolderList[51]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotatePivot" 
		"SpineFkRN.placeHolderList[52]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotatePivot" 
		"SpineFkRN.placeHolderList[53]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotatePivotTranslate" 
		"SpineFkRN.placeHolderList[54]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotatePivotTranslate" 
		"SpineFkRN.placeHolderList[55]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotateX" 
		"SpineFkRN.placeHolderList[56]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotateY" 
		"SpineFkRN.placeHolderList[57]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotateZ" 
		"SpineFkRN.placeHolderList[58]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root.rotateOrder" 
		"SpineFkRN.placeHolderList[59]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.translateX" 
		"SpineFkRN.placeHolderList[60]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.translateY" 
		"SpineFkRN.placeHolderList[61]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.translateZ" 
		"SpineFkRN.placeHolderList[62]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotateX" 
		"SpineFkRN.placeHolderList[63]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotateY" 
		"SpineFkRN.placeHolderList[64]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotateZ" 
		"SpineFkRN.placeHolderList[65]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotateOrder" 
		"SpineFkRN.placeHolderList[66]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.parentInverseMatrix" 
		"SpineFkRN.placeHolderList[67]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotatePivot" 
		"SpineFkRN.placeHolderList[68]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root.rotatePivotTranslate" 
		"SpineFkRN.placeHolderList[69]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.translateX" 
		"SpineFkRN.placeHolderList[70]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.translateY" 
		"SpineFkRN.placeHolderList[71]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.translateZ" 
		"SpineFkRN.placeHolderList[72]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotateX" 
		"SpineFkRN.placeHolderList[73]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotateY" 
		"SpineFkRN.placeHolderList[74]" ""
		5 4 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotateZ" 
		"SpineFkRN.placeHolderList[75]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotateOrder" 
		"SpineFkRN.placeHolderList[76]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.parentInverseMatrix" 
		"SpineFkRN.placeHolderList[77]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotatePivot" 
		"SpineFkRN.placeHolderList[78]" ""
		5 3 "SpineFkRN" "|Tpl_00_tpl|SpineFk:Tpl_00_tpl|SpineFk:Tpl_00_root|SpineFk:Tpl_01_root|SpineFk:Tpl_02_root.rotatePivotTranslate" 
		"SpineFkRN.placeHolderList[79]" ""
		5 4 "SpineFkRN" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root.visibility" 
		"SpineFkRN.placeHolderList[80]" ""
		5 3 "SpineFkRN" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr.translate" 
		"SpineFkRN.placeHolderList[81]" ""
		5 3 "SpineFkRN" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr.rotatePivot" 
		"SpineFkRN.placeHolderList[82]" ""
		5 3 "SpineFkRN" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr.rotatePivotTranslate" 
		"SpineFkRN.placeHolderList[83]" ""
		5 3 "SpineFkRN" "|input_01_link|SpineFk:input_00_link|SpineFk:_00_root|SpineFk:_00_ctr.parentMatrix" 
		"SpineFkRN.placeHolderList[84]" ""
		5 3 "SpineFkRN" "SpineFk:MetadataTemplate.message" "SpineFkRN.placeHolderList[85]" 
		""
		5 4 "SpineFkRN" "SpineFk:MetadataTemplate._postExecution[0]" "SpineFkRN.placeHolderList[86]" 
		""
		5 3 "SpineFkRN" "SpineFk:ControlsSet.message" "SpineFkRN.placeHolderList[87]" 
		""
		5 3 "SpineFkRN" "SpineFk:SkinJointsSet.message" "SpineFkRN.placeHolderList[88]" 
		""
		5 3 "SpineFkRN" "SpineFk:LinkSet.message" "SpineFkRN.placeHolderList[89]" 
		"";
lockNode -l 1 ;
createNode avgCurves -n "Spine:FinalSpl_00_crvAvg";
	rename -uid "3122C43A-4D1D-2081-76E6-5A9009B98523";
	setAttr ".aw" no;
createNode objectSet -n "LinkSet";
	rename -uid "877389FF-4ED0-3114-A51E-6082395B9ACA";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
	setAttr -s 2 ".dnsm";
createNode objectSet -n "Secondaries";
	rename -uid "94BAE703-48A6-0CB4-6828-1B90D26C0D19";
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
select -ne :defaultRenderingList1;
	setAttr -k on ".ihi";
	setAttr -s 4 ".r";
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
connectAttr "SpineIkRN.phl[70]" "Spine:FinalSpl_00_crvAvg.ic1";
connectAttr "SpineIkRN.phl[71]" "Tpl_00_root_pointConstraint1.tg[0].tt";
connectAttr "SpineIkRN.phl[72]" "Tpl_00_root_pointConstraint1.tg[0].trp";
connectAttr "SpineIkRN.phl[73]" "Tpl_00_root_pointConstraint1.tg[0].trt";
connectAttr "SpineIkRN.phl[74]" "Tpl_00_root_pointConstraint1.tg[0].tpm";
connectAttr "SpineIkRN.phl[75]" "SpineIk:FkTplTr_01_mp.wum";
connectAttr "SpineIkRN.phl[76]" "SpineTpl_01_mp_aimConstraint1.wum";
connectAttr "SpineIkRN.phl[77]" "Tpl_00_root_aimConstraint1.wum";
connectAttr "SpineIkRN.phl[78]" "SpineTpl_02_tr_aimConstraint1.wum";
connectAttr "SpineIkRN.phl[79]" "SpineIk:TplTr_02_mp.wum";
connectAttr "SpineIkRN.phl[80]" "SpineTpl_02_tr_aimConstraint1.tg[0].tt";
connectAttr "SpineIkRN.phl[81]" "SpineTpl_02_tr_aimConstraint1.tg[0].trp";
connectAttr "SpineIkRN.phl[82]" "SpineTpl_02_tr_aimConstraint1.tg[0].trt";
connectAttr "SpineIkRN.phl[83]" "SpineTpl_02_tr_aimConstraint1.tg[0].tpm";
connectAttr "SpineIkRN.phl[84]" "SpineIk:TplTr_02_mp.gp";
connectAttr "SpineIkRN.phl[85]" "SpineIk:FkTplTr_01_mp.gp";
connectAttr "Spine:Config_00_ctr.fkIk" "SpineIkRN.phl[86]";
connectAttr "SpineIkRN.phl[87]" "Hips_00_root_pointConstraint1.tg[0].tt";
connectAttr "SpineIkRN.phl[88]" "Hips_00_root_pointConstraint1.tg[0].trp";
connectAttr "SpineIkRN.phl[89]" "Hips_00_root_pointConstraint1.tg[0].trt";
connectAttr "SpineIkRN.phl[90]" "Hips_00_root_pointConstraint1.tg[0].tpm";
connectAttr "Spine:Config_00_ctr.fkIk" "SpineIkRN.phl[91]";
connectAttr "SpineIkRN.phl[92]" "ControlsSet.dnsm" -na;
connectAttr "SpineIkRN.phl[93]" "SkinJointsSet.dnsm" -na;
connectAttr "Hips_00_tag.pare" "SpineIkRN.phl[94]";
connectAttr "Chest_00_tag.pare" "SpineIkRN.phl[95]";
connectAttr "SpineIkRN.phl[96]" "Spine:MetadataTemplate._preExecution[0]";
connectAttr "SpineFkRN.phl[44]" "SpineIkRN.phl[97]";
connectAttr "Spine:MetadataTemplate.msg" "SpineIkRN.phl[98]";
connectAttr "SpineIkRN.phl[99]" "LinkSet.dnsm" -na;
connectAttr "SpineFkRN.phl[45]" "Spine:FinalSpl_00_crvAvg.ic2";
connectAttr "SpineFkRN.phl[46]" "Tpl_00_root_aimConstraint1.ct";
connectAttr "Tpl_00_root_pointConstraint1.ctx" "SpineFkRN.phl[47]";
connectAttr "Tpl_00_root_pointConstraint1.cty" "SpineFkRN.phl[48]";
connectAttr "Tpl_00_root_pointConstraint1.ctz" "SpineFkRN.phl[49]";
connectAttr "SpineFkRN.phl[50]" "Tpl_00_root_pointConstraint1.cpim";
connectAttr "SpineFkRN.phl[51]" "Tpl_00_root_aimConstraint1.cpim";
connectAttr "SpineFkRN.phl[52]" "Tpl_00_root_pointConstraint1.crp";
connectAttr "SpineFkRN.phl[53]" "Tpl_00_root_aimConstraint1.crp";
connectAttr "SpineFkRN.phl[54]" "Tpl_00_root_pointConstraint1.crt";
connectAttr "SpineFkRN.phl[55]" "Tpl_00_root_aimConstraint1.crt";
connectAttr "Tpl_00_root_aimConstraint1.crx" "SpineFkRN.phl[56]";
connectAttr "Tpl_00_root_aimConstraint1.cry" "SpineFkRN.phl[57]";
connectAttr "Tpl_00_root_aimConstraint1.crz" "SpineFkRN.phl[58]";
connectAttr "SpineFkRN.phl[59]" "Tpl_00_root_aimConstraint1.cro";
connectAttr "Tpl_01_root_parentConstraint1.ctx" "SpineFkRN.phl[60]";
connectAttr "Tpl_01_root_parentConstraint1.cty" "SpineFkRN.phl[61]";
connectAttr "Tpl_01_root_parentConstraint1.ctz" "SpineFkRN.phl[62]";
connectAttr "Tpl_01_root_parentConstraint1.crx" "SpineFkRN.phl[63]";
connectAttr "Tpl_01_root_parentConstraint1.cry" "SpineFkRN.phl[64]";
connectAttr "Tpl_01_root_parentConstraint1.crz" "SpineFkRN.phl[65]";
connectAttr "SpineFkRN.phl[66]" "Tpl_01_root_parentConstraint1.cro";
connectAttr "SpineFkRN.phl[67]" "Tpl_01_root_parentConstraint1.cpim";
connectAttr "SpineFkRN.phl[68]" "Tpl_01_root_parentConstraint1.crp";
connectAttr "SpineFkRN.phl[69]" "Tpl_01_root_parentConstraint1.crt";
connectAttr "Tpl_02_root_parentConstraint1.ctx" "SpineFkRN.phl[70]";
connectAttr "Tpl_02_root_parentConstraint1.cty" "SpineFkRN.phl[71]";
connectAttr "Tpl_02_root_parentConstraint1.ctz" "SpineFkRN.phl[72]";
connectAttr "Tpl_02_root_parentConstraint1.crx" "SpineFkRN.phl[73]";
connectAttr "Tpl_02_root_parentConstraint1.cry" "SpineFkRN.phl[74]";
connectAttr "Tpl_02_root_parentConstraint1.crz" "SpineFkRN.phl[75]";
connectAttr "SpineFkRN.phl[76]" "Tpl_02_root_parentConstraint1.cro";
connectAttr "SpineFkRN.phl[77]" "Tpl_02_root_parentConstraint1.cpim";
connectAttr "SpineFkRN.phl[78]" "Tpl_02_root_parentConstraint1.crp";
connectAttr "SpineFkRN.phl[79]" "Tpl_02_root_parentConstraint1.crt";
connectAttr "FkIk_00_rev.ox" "SpineFkRN.phl[80]";
connectAttr "SpineFkRN.phl[81]" "Hips_00_root_pointConstraint1.tg[1].tt";
connectAttr "SpineFkRN.phl[82]" "Hips_00_root_pointConstraint1.tg[1].trp";
connectAttr "SpineFkRN.phl[83]" "Hips_00_root_pointConstraint1.tg[1].trt";
connectAttr "SpineFkRN.phl[84]" "Hips_00_root_pointConstraint1.tg[1].tpm";
connectAttr "SpineFkRN.phl[85]" "Spine:MetadataTemplate._preExecution[1]";
connectAttr "Spine:MetadataTemplate.msg" "SpineFkRN.phl[86]";
connectAttr "SpineFkRN.phl[87]" "ControlsSet.dnsm" -na;
connectAttr "SpineFkRN.phl[88]" "SkinJointsSet.dnsm" -na;
connectAttr "SpineFkRN.phl[89]" "LinkSet.dnsm" -na;
connectAttr "Hips_00_jnt_parentConstraint1.ctx" "Hips_00_jnt.tx";
connectAttr "Hips_00_jnt_parentConstraint1.cty" "Hips_00_jnt.ty";
connectAttr "Hips_00_jnt_parentConstraint1.ctz" "Hips_00_jnt.tz";
connectAttr "Hips_00_jnt_parentConstraint1.crx" "Hips_00_jnt.rx";
connectAttr "Hips_00_jnt_parentConstraint1.cry" "Hips_00_jnt.ry";
connectAttr "Hips_00_jnt_parentConstraint1.crz" "Hips_00_jnt.rz";
connectAttr "Hips_00_jnt.ro" "Hips_00_jnt_parentConstraint1.cro";
connectAttr "Hips_00_jnt.pim" "Hips_00_jnt_parentConstraint1.cpim";
connectAttr "Hips_00_jnt.rp" "Hips_00_jnt_parentConstraint1.crp";
connectAttr "Hips_00_jnt.rpt" "Hips_00_jnt_parentConstraint1.crt";
connectAttr "Hips_00_jnt.jo" "Hips_00_jnt_parentConstraint1.cjo";
connectAttr "Hips_00_ctr.t" "Hips_00_jnt_parentConstraint1.tg[0].tt";
connectAttr "Hips_00_ctr.rp" "Hips_00_jnt_parentConstraint1.tg[0].trp";
connectAttr "Hips_00_ctr.rpt" "Hips_00_jnt_parentConstraint1.tg[0].trt";
connectAttr "Hips_00_ctr.r" "Hips_00_jnt_parentConstraint1.tg[0].tr";
connectAttr "Hips_00_ctr.ro" "Hips_00_jnt_parentConstraint1.tg[0].tro";
connectAttr "Hips_00_ctr.s" "Hips_00_jnt_parentConstraint1.tg[0].ts";
connectAttr "Hips_00_ctr.pm" "Hips_00_jnt_parentConstraint1.tg[0].tpm";
connectAttr "Hips_00_jnt_parentConstraint1.w0" "Hips_00_jnt_parentConstraint1.tg[0].tw"
		;
connectAttr "ChestJnt_00_jnt_prc.ctx" "Chest_00_jnt.tx";
connectAttr "ChestJnt_00_jnt_prc.cty" "Chest_00_jnt.ty";
connectAttr "ChestJnt_00_jnt_prc.ctz" "Chest_00_jnt.tz";
connectAttr "ChestJnt_00_jnt_prc.crx" "Chest_00_jnt.rx";
connectAttr "ChestJnt_00_jnt_prc.cry" "Chest_00_jnt.ry";
connectAttr "ChestJnt_00_jnt_prc.crz" "Chest_00_jnt.rz";
connectAttr "Chest_00_jnt.ro" "ChestJnt_00_jnt_prc.cro";
connectAttr "Chest_00_jnt.pim" "ChestJnt_00_jnt_prc.cpim";
connectAttr "Chest_00_jnt.rp" "ChestJnt_00_jnt_prc.crp";
connectAttr "Chest_00_jnt.rpt" "ChestJnt_00_jnt_prc.crt";
connectAttr "Chest_00_jnt.jo" "ChestJnt_00_jnt_prc.cjo";
connectAttr "Chest_00_ctr.t" "ChestJnt_00_jnt_prc.tg[0].tt";
connectAttr "Chest_00_ctr.rp" "ChestJnt_00_jnt_prc.tg[0].trp";
connectAttr "Chest_00_ctr.rpt" "ChestJnt_00_jnt_prc.tg[0].trt";
connectAttr "Chest_00_ctr.r" "ChestJnt_00_jnt_prc.tg[0].tr";
connectAttr "Chest_00_ctr.ro" "ChestJnt_00_jnt_prc.tg[0].tro";
connectAttr "Chest_00_ctr.s" "ChestJnt_00_jnt_prc.tg[0].ts";
connectAttr "Chest_00_ctr.pm" "ChestJnt_00_jnt_prc.tg[0].tpm";
connectAttr "ChestJnt_00_jnt_prc.w0" "ChestJnt_00_jnt_prc.tg[0].tw";
connectAttr "Spine:FinalSpl_00_crvAvg.oc" "Spine:FinalSpl_00_crvShape.cr";
connectAttr "Spine:MetadataTemplate.msg" "Tpl_00_tpl.metadataTemplate";
connectAttr "SpineIk:TplTr_02_mp.ac" "SpineTpl_02_tr.t";
connectAttr "SpineTpl_02_tr_aimConstraint1.crx" "SpineTpl_02_tr.rx" -l on;
connectAttr "SpineTpl_02_tr_aimConstraint1.cry" "SpineTpl_02_tr.ry" -l on;
connectAttr "SpineTpl_02_tr_aimConstraint1.crz" "SpineTpl_02_tr.rz" -l on;
connectAttr "SpineTpl_02_tr_aimConstraint1.w0" "SpineTpl_02_tr_aimConstraint1.tg[0].tw"
		;
connectAttr "SpineTpl_02_tr.pim" "SpineTpl_02_tr_aimConstraint1.cpim";
connectAttr "SpineTpl_02_tr.t" "SpineTpl_02_tr_aimConstraint1.ct";
connectAttr "SpineTpl_02_tr.rp" "SpineTpl_02_tr_aimConstraint1.crp";
connectAttr "SpineTpl_02_tr.rpt" "SpineTpl_02_tr_aimConstraint1.crt";
connectAttr "SpineTpl_02_tr.ro" "SpineTpl_02_tr_aimConstraint1.cro";
connectAttr "SpineIk:FkTplTr_01_mp.ac" "SpineTpl_01_tr.t";
connectAttr "SpineTpl_01_mp_aimConstraint1.crx" "SpineTpl_01_tr.rx" -l on;
connectAttr "SpineTpl_01_mp_aimConstraint1.cry" "SpineTpl_01_tr.ry" -l on;
connectAttr "SpineTpl_01_mp_aimConstraint1.crz" "SpineTpl_01_tr.rz" -l on;
connectAttr "SpineTpl_01_tr.pim" "SpineTpl_01_mp_aimConstraint1.cpim";
connectAttr "SpineTpl_01_tr.t" "SpineTpl_01_mp_aimConstraint1.ct";
connectAttr "SpineTpl_01_tr.rp" "SpineTpl_01_mp_aimConstraint1.crp";
connectAttr "SpineTpl_01_tr.rpt" "SpineTpl_01_mp_aimConstraint1.crt";
connectAttr "SpineTpl_01_tr.ro" "SpineTpl_01_mp_aimConstraint1.cro";
connectAttr "SpineTpl_02_tr.t" "SpineTpl_01_mp_aimConstraint1.tg[0].tt";
connectAttr "SpineTpl_02_tr.rp" "SpineTpl_01_mp_aimConstraint1.tg[0].trp";
connectAttr "SpineTpl_02_tr.rpt" "SpineTpl_01_mp_aimConstraint1.tg[0].trt";
connectAttr "SpineTpl_02_tr.pm" "SpineTpl_01_mp_aimConstraint1.tg[0].tpm";
connectAttr "SpineTpl_01_mp_aimConstraint1.w0" "SpineTpl_01_mp_aimConstraint1.tg[0].tw"
		;
connectAttr "Spine:ConfigRoot_00_prc.ctx" "Spine:Config_00_root.tx";
connectAttr "Spine:ConfigRoot_00_prc.cty" "Spine:Config_00_root.ty";
connectAttr "Spine:ConfigRoot_00_prc.ctz" "Spine:Config_00_root.tz";
connectAttr "Spine:ConfigRoot_00_prc.crx" "Spine:Config_00_root.rx";
connectAttr "Spine:ConfigRoot_00_prc.cry" "Spine:Config_00_root.ry";
connectAttr "Spine:ConfigRoot_00_prc.crz" "Spine:Config_00_root.rz";
connectAttr "output_01_link.wm" "Spine:ConfigRoot_00_prc.tg[0].tpm";
connectAttr "Spine:Config_00_root.pim" "Spine:ConfigRoot_00_prc.cpim";
connectAttr "Hips_00_root_pointConstraint1.ctx" "Hips_00_root.tx";
connectAttr "Hips_00_root_pointConstraint1.cty" "Hips_00_root.ty";
connectAttr "Hips_00_root_pointConstraint1.ctz" "Hips_00_root.tz";
connectAttr "Hips_00_root_pointConstraint1.w0" "Hips_00_root_pointConstraint1.tg[0].tw"
		;
connectAttr "Hips_00_root_pointConstraint1.w1" "Hips_00_root_pointConstraint1.tg[1].tw"
		;
connectAttr "Spine:Config_00_ctr.fkIk" "Hips_00_root_pointConstraint1.w0";
connectAttr "FkIk_00_rev.ox" "Hips_00_root_pointConstraint1.w1";
connectAttr "Hips_00_root.pim" "Hips_00_root_pointConstraint1.cpim";
connectAttr "Hips_00_root.rp" "Hips_00_root_pointConstraint1.crp";
connectAttr "Hips_00_root.rpt" "Hips_00_root_pointConstraint1.crt";
connectAttr "ChestRoot_00_prc.ctx" "Chest_00_root.tx";
connectAttr "ChestRoot_00_prc.cty" "Chest_00_root.ty";
connectAttr "ChestRoot_00_prc.ctz" "Chest_00_root.tz";
connectAttr "ChestRoot_00_prc.crx" "Chest_00_root.rx";
connectAttr "ChestRoot_00_prc.cry" "Chest_00_root.ry";
connectAttr "ChestRoot_00_prc.crz" "Chest_00_root.rz";
connectAttr "ChestRootIk_00_mstc.wm" "ChestRoot_00_prc.tg[0].tpm";
connectAttr "Spine:Config_00_ctr.fkIk" "ChestRoot_00_prc.tg[0].tw";
connectAttr "ChestRootFk_00_mstc.wm" "ChestRoot_00_prc.tg[1].tpm";
connectAttr "FkIk_00_rev.ox" "ChestRoot_00_prc.tg[1].tw";
connectAttr "Chest_00_root.pim" "ChestRoot_00_prc.cpim";
connectAttr "ChestRootIk_00_mstc.msg" "ChestRootTpl_00_mstc._relatedTo[0]";
connectAttr "ChestRootFk_00_mstc.msg" "ChestRootTpl_00_mstc._relatedTo[1]";
connectAttr "ChestRootTpl_00_mstc_orientConstraint1.crx" "ChestRootTpl_00_mstc.rx"
		 -l on;
connectAttr "ChestRootTpl_00_mstc_orientConstraint1.cry" "ChestRootTpl_00_mstc.ry"
		 -l on;
connectAttr "ChestRootTpl_00_mstc_orientConstraint1.crz" "ChestRootTpl_00_mstc.rz"
		 -l on;
connectAttr "ChestRootTpl_00_mstc.ro" "ChestRootTpl_00_mstc_orientConstraint1.cro"
		;
connectAttr "ChestRootTpl_00_mstc.pim" "ChestRootTpl_00_mstc_orientConstraint1.cpim"
		;
connectAttr "SpineTpl_02_tr.r" "ChestRootTpl_00_mstc_orientConstraint1.tg[0].tr"
		;
connectAttr "SpineTpl_02_tr.ro" "ChestRootTpl_00_mstc_orientConstraint1.tg[0].tro"
		;
connectAttr "SpineTpl_02_tr.pm" "ChestRootTpl_00_mstc_orientConstraint1.tg[0].tpm"
		;
connectAttr "ChestRootTpl_00_mstc_orientConstraint1.w0" "ChestRootTpl_00_mstc_orientConstraint1.tg[0].tw"
		;
connectAttr "Tpl_00_root_pointConstraint1.w0" "Tpl_00_root_pointConstraint1.tg[0].tw"
		;
connectAttr "SpineTpl_01_tr.t" "Tpl_00_root_aimConstraint1.tg[0].tt";
connectAttr "SpineTpl_01_tr.rp" "Tpl_00_root_aimConstraint1.tg[0].trp";
connectAttr "SpineTpl_01_tr.rpt" "Tpl_00_root_aimConstraint1.tg[0].trt";
connectAttr "SpineTpl_01_tr.pm" "Tpl_00_root_aimConstraint1.tg[0].tpm";
connectAttr "Tpl_00_root_aimConstraint1.w0" "Tpl_00_root_aimConstraint1.tg[0].tw"
		;
connectAttr "SpineTpl_01_tr.t" "Tpl_01_root_parentConstraint1.tg[0].tt";
connectAttr "SpineTpl_01_tr.rp" "Tpl_01_root_parentConstraint1.tg[0].trp";
connectAttr "SpineTpl_01_tr.rpt" "Tpl_01_root_parentConstraint1.tg[0].trt";
connectAttr "SpineTpl_01_tr.r" "Tpl_01_root_parentConstraint1.tg[0].tr";
connectAttr "SpineTpl_01_tr.ro" "Tpl_01_root_parentConstraint1.tg[0].tro";
connectAttr "SpineTpl_01_tr.s" "Tpl_01_root_parentConstraint1.tg[0].ts";
connectAttr "SpineTpl_01_tr.pm" "Tpl_01_root_parentConstraint1.tg[0].tpm";
connectAttr "Tpl_01_root_parentConstraint1.w0" "Tpl_01_root_parentConstraint1.tg[0].tw"
		;
connectAttr "SpineTpl_02_tr.t" "Tpl_02_root_parentConstraint1.tg[0].tt";
connectAttr "SpineTpl_02_tr.rp" "Tpl_02_root_parentConstraint1.tg[0].trp";
connectAttr "SpineTpl_02_tr.rpt" "Tpl_02_root_parentConstraint1.tg[0].trt";
connectAttr "SpineTpl_02_tr.r" "Tpl_02_root_parentConstraint1.tg[0].tr";
connectAttr "SpineTpl_02_tr.ro" "Tpl_02_root_parentConstraint1.tg[0].tro";
connectAttr "SpineTpl_02_tr.s" "Tpl_02_root_parentConstraint1.tg[0].ts";
connectAttr "SpineTpl_02_tr.pm" "Tpl_02_root_parentConstraint1.tg[0].tpm";
connectAttr "Tpl_02_root_parentConstraint1.w0" "Tpl_02_root_parentConstraint1.tg[0].tw"
		;
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "SpineIkRNfosterParent1.msg" "SpineIkRN.fp";
connectAttr "sharedReferenceNode.sr" "SpineIkRN.sr";
connectAttr "Spine:Config_00_ctr.fkIk" "FkIk_00_rev.ix";
connectAttr "Secondaries.msg" "ControlsSet.dnsm" -na;
connectAttr "Hips_00_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "Chest_00_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "SpineTpl_01_tr.uValue" "SpineIk:FkTplTr_01_mp.u";
connectAttr "SpineTpl_02_tr.uValue" "SpineIk:TplTr_02_mp.u";
connectAttr "Chest_00_ctr.msg" "Chest_00_tag.act";
connectAttr "Chest_00_tag.msg" "Chest_00_tag.child[0]";
connectAttr "Hips_00_ctr.msg" "Hips_00_tag.act";
connectAttr "Hips_00_tag.msg" "Hips_00_tag.child[0]";
connectAttr "Config_00_tag.msg" "Config_00_tag.child[0]";
connectAttr "Spine:Config_00_ctr.msg" "Config_00_tag.act";
connectAttr "ChestRootTpl_00_mstc.msg" "Spine:MetadataTemplate._inputTemplate[0]"
		;
connectAttr "SpineFkRNfosterParent1.msg" "SpineFkRN.fp";
connectAttr "Spine:Config_00_ctr.fkIk" "Spine:FinalSpl_00_crvAvg.w1";
connectAttr "FkIk_00_rev.ox" "Spine:FinalSpl_00_crvAvg.w2";
connectAttr "input_01_link.iog" "LinkSet.dsm" -na;
connectAttr "output_00_link.iog" "LinkSet.dsm" -na;
connectAttr "output_01_link.iog" "LinkSet.dsm" -na;
connectAttr "Spine:Config_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Hips_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "Chest_00_ctr.iog" "Secondaries.dsm" -na;
connectAttr "FkIk_00_rev.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "spineIkFk3Bones_defaultRenderLayer.msg" ":defaultRenderingList1.r" 
		-na;
// End of spineIkFk3Bones.ma
