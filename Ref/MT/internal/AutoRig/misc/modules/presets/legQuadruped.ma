//Maya ASCII 2020 scene
//Name: legQuadruped.ma
//Last modified: Thu, May 19, 2022 10:29:41 AM
//Codeset: 1252
file -rdi 1 -ns "Foot" -rfn "FootRN" -typ "mayaAscii" "C:/Perforcelocal/[ws00]/PRJ_05/GAME/Tools/MayaTools/internal/AutoRig/misc/modules/presets/footRoll.ma";
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
fileInfo "UUID" "E00044E1-403D-8DF4-40D1-99A598C1D571";
createNode transform -s -n "persp";
	rename -uid "5FA6472C-4139-4B89-7BB1-C6B65C9425F5";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 9.9647199751610334 7.6988375709021106 15.516953110995491 ;
	setAttr ".r" -type "double3" -12.938352729707374 38.600000000015463 1.017425260665384e-15 ;
createNode camera -s -n "perspShape" -p "persp";
	rename -uid "5E52EEFD-45D1-8BD5-6B49-5DA961D7AB4D";
	setAttr -k off ".v" no;
	setAttr ".fl" 34.999999999999993;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 18.365207245466834;
	setAttr ".imn" -type "string" "persp";
	setAttr ".den" -type "string" "persp_depth";
	setAttr ".man" -type "string" "persp_mask";
	setAttr ".tp" -type "double3" 0 2.0000000183600921 -0.99999996327981044 ;
	setAttr ".hc" -type "string" "viewSet -p %camera";
createNode transform -s -n "top";
	rename -uid "5B1DF43B-4C13-D640-AF38-1EA3C80C693B";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.0714285714285725 1000.1 0.068389057750759985 ;
	setAttr ".r" -type "double3" -90 0 0 ;
createNode camera -s -n "topShape" -p "top";
	rename -uid "765AB593-4FD9-DA56-93CE-A48EFDB0B3B7";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1;
	setAttr ".ow" 20.334346504559253;
	setAttr ".imn" -type "string" "top";
	setAttr ".den" -type "string" "top_depth";
	setAttr ".man" -type "string" "top_mask";
	setAttr ".hc" -type "string" "viewSet -t %camera";
	setAttr ".o" yes;
createNode transform -s -n "front";
	rename -uid "F4D8FA7F-4FFC-8E94-05AF-04968DFBC739";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 0.98406498212856797 6.0954531876059583 1000.1063699740992 ;
createNode camera -s -n "frontShape" -p "front";
	rename -uid "EABE833F-407A-EEA8-DB5F-BA88264D06DA";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 999.90893132942676;
	setAttr ".ow" 3.6432069465701109;
	setAttr ".imn" -type "string" "front";
	setAttr ".den" -type "string" "front_depth";
	setAttr ".man" -type "string" "front_mask";
	setAttr ".tp" -type "double3" 0.97434314098707631 6.0986938013197882 0.19743864467242234 ;
	setAttr ".hc" -type "string" "viewSet -f %camera";
	setAttr ".o" yes;
createNode transform -s -n "side";
	rename -uid "FB89E91F-4861-8F86-FB32-969EC6927ABB";
	setAttr ".v" no;
	setAttr ".t" -type "double3" 1000.1431606617211 0.98469252968406296 0.98418638205640119 ;
	setAttr ".r" -type "double3" 0 90 0 ;
createNode camera -s -n "sideShape" -p "side";
	rename -uid "8F9FEF21-40BB-7DBC-1BD8-ACAFE630D580";
	setAttr -k off ".v" no;
	setAttr ".rnd" no;
	setAttr ".ncp" 0.01;
	setAttr ".coi" 1000.1431606617211;
	setAttr ".ow" 7.7526315789475984;
	setAttr ".imn" -type "string" "side";
	setAttr ".den" -type "string" "side_depth";
	setAttr ".man" -type "string" "side_mask";
	setAttr ".tp" -type "double3" 2.8477220581635265e-14 0.99971819853501986 0.87817194071909366 ;
	setAttr ".hc" -type "string" "viewSet -s %camera";
	setAttr ".o" yes;
createNode joint -n "Leg:qdrp_00_jnt";
	rename -uid "8960C8AF-4C8F-039C-19C8-79847DE846C8";
createNode joint -n "Leg:qdrp_01_jnt" -p "Leg:qdrp_00_jnt";
	rename -uid "D47AF83A-4985-FEF6-2F3B-768E6D6C4535";
createNode joint -n "Leg:qdrp_02_jnt" -p "Leg:qdrp_01_jnt";
	rename -uid "6D2AB5CA-4510-6C96-86ED-249B49CE6699";
createNode joint -n "Leg:qdrp_03_jnt" -p "Leg:qdrp_02_jnt";
	rename -uid "0A396BEE-4039-D378-6224-99B2416716AD";
createNode parentConstraint -n "Leg:qdrpJnt_03_prc" -p "Leg:qdrp_03_jnt";
	rename -uid "032D577B-427D-F6D8-09EC-578580755840";
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 2.339992988114361e-05 ;
createNode parentConstraint -n "Leg:qdrpJnt_02_prc" -p "Leg:qdrp_02_jnt";
	rename -uid "FA5176CD-4678-17B7-2903-1FB9CA2BD11A";
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 71.555333286079929 ;
createNode parentConstraint -n "Leg:qdrpJnt_01_prc" -p "Leg:qdrp_01_jnt";
	rename -uid "8986442B-44C1-53EC-3B56-54B32B021D10";
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 0 0 -71.561063815509243 ;
createNode parentConstraint -n "Leg:qdrpJnt_00_prc" -p "Leg:qdrp_00_jnt";
	rename -uid "21E8E162-45D1-186E-B333-CCBD4EA649C9";
	setAttr -s 2 ".tg";
	setAttr ".lr" -type "double3" 90.000000000006963 -26.563913890631582 -89.999999999923062 ;
createNode transform -n "Leg:Tpl_00_root";
	rename -uid "02C6C4C3-49E9-9AF6-082F-32A431330AAF";
	setAttr ".v" no;
createNode transform -n "Leg:qdrpAuxIkTpl_00_jnt" -p "Leg:Tpl_00_root";
	rename -uid "9FC2416F-4AC5-637D-3537-6B92DB14466F";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr ".t" -type "double3" 0 7 0 ;
	setAttr ".r" -type "double3" 89.999999999997783 -26.564250123491792 -89.999999999986571 ;
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999978 1 ;
createNode locator -n "Leg:qdrpAuxIkTpl_00_jntShape" -p "Leg:qdrpAuxIkTpl_00_jnt";
	rename -uid "9E0D3174-4EF4-DB6F-9987-DC8A194A5BAA";
	setAttr -k off ".v";
createNode transform -n "Leg:qdrpAuxIkTpl_01_jnt" -p "Leg:qdrpAuxIkTpl_00_jnt";
	rename -uid "DB898E43-42FF-91D3-5BF6-E092E2D1FD3B";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -ci true -sn "factor" -ln "factor" -at "double";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" 2.2360877166971069 -4.4408920985006262e-16 7.2919867937189511e-13 ;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999967 1 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -k on ".factor";
createNode locator -n "Leg:qdrpAuxIkTpl_01_jntShape" -p "Leg:qdrpAuxIkTpl_01_jnt";
	rename -uid "D8502E88-441D-4967-477F-EDB861C4A57A";
	setAttr -k off ".v";
createNode transform -n "Leg:FkTpl_00_root" -p "Leg:qdrpAuxIkTpl_00_jnt";
	rename -uid "D782A469-4054-E443-E30A-A88DD9BFA9C5";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v" no;
	setAttr ".t" -type "double3" 0 0 2.0194839173657902e-28 ;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "Leg:FkTpl_00_rootShape" -p "Leg:FkTpl_00_root";
	rename -uid "3CC434D4-48C8-542B-2B13-70AAB5676653";
	setAttr -k off ".v";
createNode transform -n "Leg:qdrpTpl_00_loc" -p "Leg:qdrpAuxIkTpl_00_jnt";
	rename -uid "02520396-4F5E-8D9A-B8D6-369C5C01E291";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2.2360877166971069 0 7.2919867937189501e-13 ;
	setAttr -l on ".tz";
	setAttr -l on ".ty";
	setAttr ".r" -type "double3" 0 0 -71.562242926365116 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr ".s" -type "double3" 0.99999999999999967 0.99999999999999978 1 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Leg:qdrpTpl_00_locShape" -p "Leg:qdrpTpl_00_loc";
	rename -uid "99B922E9-40A9-4671-21D5-ACAD8CDFC629";
	setAttr -k off ".v";
createNode transform -n "Leg:qdrpAuxIkTpl_02_jnt" -p "Leg:qdrpTpl_00_loc";
	rename -uid "A7340522-4DDB-3C91-5CB3-9D98C245D30F";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -ci true -sn "factor" -ln "factor" -at "double";
	setAttr -l on ".v" no;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -k on ".factor";
createNode locator -n "Leg:qdrpAuxIkTpl_02_jntShape" -p "Leg:qdrpAuxIkTpl_02_jnt";
	rename -uid "E2B235B4-423F-D325-2A46-0BB1B89B44E4";
	setAttr -k off ".v";
createNode transform -n "Leg:FkTpl_01_root" -p "Leg:qdrpTpl_00_loc";
	rename -uid "75D09B13-41BA-6EBD-1A43-129366D3E302";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1.0000000000000007 1.0000000000000004 1 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "Leg:FkTpl_01_rootShape" -p "Leg:FkTpl_01_root";
	rename -uid "EE084CF5-4621-8F38-B709-93B013DFF1E4";
	setAttr -k off ".v";
createNode transform -n "Leg:ikPoleTpl_00_root" -p "Leg:qdrpTpl_00_loc";
	rename -uid "BD62AE8C-411E-A066-3B3E-67A06D4E68F9";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" -1.6690003918925291 2.5736356670937548 -1.7669017145434607e-14 ;
	setAttr ".r" -type "double3" -134.99799280287331 89.999999999987409 0 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000007 ;
createNode locator -n "Leg:ikPoleTpl_00_rootShape" -p "Leg:ikPoleTpl_00_root";
	rename -uid "34CB567A-49B1-17DD-CB66-4794EE8F1D19";
	setAttr -k off ".v";
createNode transform -n "Leg:qdrpTpl_01_loc" -p "Leg:qdrpTpl_00_loc";
	rename -uid "3E9A8790-4B83-E444-234D-A29C3EF2463A";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2.8283810098779378 0 1.0337990564284161e-13 ;
	setAttr -l on ".tz";
	setAttr -l on ".ty";
	setAttr ".r" -type "double3" 0 0 71.557321594853619 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000004 0.99999999999999978 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Leg:qdrpTpl_01_locShape" -p "Leg:qdrpTpl_01_loc";
	rename -uid "A090717E-4AFF-67FC-CD79-FE8AB7E0241B";
	setAttr -k off ".v";
createNode transform -n "Leg:FkTpl_02_root" -p "Leg:qdrpTpl_01_loc";
	rename -uid "F470D34B-4E35-0A6E-0FFF-09AB410455C0";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on -k off ".v" no;
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr ".s" -type "double3" 1 1 1.0000000000000004 ;
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode locator -n "Leg:FkTpl_02_rootShape" -p "Leg:FkTpl_02_root";
	rename -uid "8F593589-4B4D-288E-BE19-DDA34C018785";
	setAttr -k off ".v";
createNode transform -n "Leg:ikTpl_01_off" -p "Leg:qdrpTpl_01_loc";
	rename -uid "73FE3A8F-4C3A-F242-1B02-88A009B6A52C";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".s" -type "double3" 1.0000000000000004 1.0000000000000004 1.0000000000000004 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Leg:ikTpl_01_offShape" -p "Leg:ikTpl_01_off";
	rename -uid "5A43DAE3-40D9-E030-37B2-D8B496B0CA63";
	setAttr -k off ".v";
createNode aimConstraint -n "Leg:ikTpl_01_off_aimConstraint1" -p "Leg:ikTpl_01_off";
	rename -uid "D8041C31-4BEC-0CDB-4C37-8AAB9773AC29";
	addAttr -dcb 0 -ci true -sn "w0" -ln "ikTpl_01_dkUAW0" -dv 1 -at "double";
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
	setAttr ".a" -type "double3" 0 0 1 ;
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" -3.4603555814952426e-07 89.999999653964437 0 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:ikTpl_00_root" -p "Leg:qdrpTpl_01_loc";
	rename -uid "DD2795A5-4810-A0EF-B674-36BB645AFCA6";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v";
	setAttr ".t" -type "double3" 2.2361941445787537 1.3505404805803272e-08 4.7206404121531789e-13 ;
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" -63.440671208019708 89.999999999987395 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 0.99999999999999978 1.0000000000000004 ;
createNode locator -n "Leg:ikTpl_00_rootShape" -p "Leg:ikTpl_00_root";
	rename -uid "4999BB51-4343-208F-B56C-D6BCA0C81D9E";
	setAttr -k off ".v";
createNode transform -n "Leg:ikTpl_01_rmv" -p "Leg:ikTpl_00_root";
	rename -uid "FC0E87D6-43FF-80DD-4EDA-6CB023BC653A";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	addAttr -ci true -k true -sn "difference" -ln "difference" -at "doubleAngle";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".s" -type "double3" 1 1.0000000000000004 0.99999999999999989 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -k on ".difference";
createNode locator -n "Leg:ikTpl_01_rmvShape" -p "Leg:ikTpl_01_rmv";
	rename -uid "1A477975-4F73-15FE-964A-C3A513185D7C";
	setAttr -k off ".v";
createNode aimConstraint -n "Leg:ikTpl_01_dkUA_aimConstraint1" -p "Leg:ikTpl_01_rmv";
	rename -uid "BA50B157-42DC-1AAE-2181-FEB9D16894DA";
	addAttr -dcb 0 -ci true -sn "w0" -ln "ikTpl_01_offW0" -dv 1 -at "double";
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
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" -26.55932913801583 1.2103182727178257e-13 5.1281356413424318e-13 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:FkTpl_03_root" -p "Leg:ikTpl_00_root";
	rename -uid "4E5A00DE-4A9E-EB09-5675-50BED02C8267";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr -l on ".v" no;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr ".r" -type "double3" 0 -89.999999999994344 0 ;
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr ".s" -type "double3" 0.99999999999999956 1.0000000000000004 1.0000000000000002 ;
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
createNode locator -n "Leg:FkTpl_03_rootShape" -p "Leg:FkTpl_03_root";
	rename -uid "E2A4F92A-4DEA-B135-C995-BEB6436CF3EF";
	setAttr -k off ".v";
createNode transform -n "Leg:qdrpDwIkTplJnt_01_grp" -p "Leg:ikTpl_00_root";
	rename -uid "7699FC1D-413E-28E8-F385-A481A009C7BC";
	setAttr ".v" no;
	setAttr ".t" -type "double3" -1.9634090941556706e-20 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000009 1.0000000000000002 1 ;
createNode aimConstraint -n "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1" -p "Leg:qdrpDwIkTplJnt_01_grp";
	rename -uid "8B575C62-4144-149C-61D7-A5B1B935EBB5";
	addAttr -dcb 0 -ci true -sn "w0" -ln "ikTpl_01_offW0" -dv 1 -at "double";
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
	setAttr ".u" -type "double3" 0 -1 0 ;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" -90 26.565049999999989 90 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:qdrpDwIkTpl_01_jnt" -p "Leg:qdrpDwIkTplJnt_01_grp";
	rename -uid "67DEE9DA-4D9E-E51E-8643-DA97FDF3E4FC";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000004 ;
createNode locator -n "Leg:qdrpDwIkTpl_01_jntShape" -p "Leg:qdrpDwIkTpl_01_jnt";
	rename -uid "9446EA20-479B-FE0E-837D-90BEC6566E80";
	setAttr -k off ".v";
createNode pointConstraint -n "Leg:qdrpDwIkTplJnt_01_pnc" -p "Leg:qdrpDwIkTpl_01_jnt";
	rename -uid "B7D682D9-490C-3BD4-76E5-56A8B0A66E26";
	setAttr ".s" -type "double3" 1 0.99999999999999978 0.99999999999999933 ;
createNode transform -n "Leg:qdrpUpIkTplJnt_01_grp" -p "Leg:qdrpDwIkTpl_01_jnt";
	rename -uid "E8EB9A8D-48CB-4834-8D79-D2B95AC5ABDC";
createNode aimConstraint -n "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1" -p "Leg:qdrpUpIkTplJnt_01_grp";
	rename -uid "DFD66932-4DFF-ED26-5EC1-4996BB12142E";
	addAttr -dcb 0 -ci true -sn "w0" -ln "locator1W0" -dv 1 -at "double";
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
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" 1.0759831769765112e-12 -1.4929821955889411e-12 -71.560125756906558 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:qdrpUpIkTpl_01_jnt" -p "Leg:qdrpUpIkTplJnt_01_grp";
	rename -uid "31246497-4CD3-09F3-C434-CAB8682F4EFA";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
createNode locator -n "Leg:qdrpUpIkTpl_01_jntShape" -p "Leg:qdrpUpIkTpl_01_jnt";
	rename -uid "C3706D14-4BB3-5344-297B-F78AC4D99DCC";
	setAttr -k off ".v";
createNode pointConstraint -n "Leg:qdrpUpIkTplJnt_01_pnc" -p "Leg:qdrpUpIkTpl_01_jnt";
	rename -uid "E39BEB1F-4523-DF10-726E-1D9A012AAF98";
	setAttr ".s" -type "double3" 1 0.99999999999999944 0.999999999999999 ;
createNode aimConstraint -n "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1" -p "Leg:qdrpUpIkTpl_01_jnt";
	rename -uid "0993EB52-4EC0-B9C5-0A44-869261A911D5";
	addAttr -dcb 0 -ci true -sn "w0" -ln "qdrpAuxIkTpl_00_jntW0" -dv 1 -at "double";
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
	setAttr ".u" -type "double3" 0 -1 0 ;
	setAttr ".wu" -type "double3" 0 0 1 ;
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" 4.7458559994730692e-12 6.5844037035663704e-12 71.566039852616044 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:qdrpUpIkTpl_02_jnt" -p "Leg:qdrpUpIkTpl_01_jnt";
	rename -uid "9E7E6A61-4359-7896-E337-31B19BF53934";
	addAttr -s false -ci true -h true -sn "_relatedTo" -ln "_relatedTo" -at "message";
	setAttr ".s" -type "double3" 0.99999999999999989 0.99999999999999989 1 ;
createNode locator -n "Leg:qdrpUpIkTpl_02_jntShape" -p "Leg:qdrpUpIkTpl_02_jnt";
	rename -uid "FD435172-485C-4A5A-40FB-73B65F0B5EE5";
	setAttr -k off ".v";
createNode pointConstraint -n "Leg:qdrpUpIkTplJnt_02_pnc" -p "Leg:qdrpUpIkTpl_02_jnt";
	rename -uid "FD2C0635-4124-9CE8-956F-1B9685630C0A";
	setAttr ".s" -type "double3" 0.99999999999999956 0.99999999999999944 0.999999999999999 ;
createNode transform -n "Leg:qdrpAux_00_grp";
	rename -uid "3DD288E9-4B3B-D01B-E96B-D38776C15F5F";
	setAttr ".v" no;
createNode joint -n "Leg:qdrpAuxIk_00_jnt" -p "Leg:qdrpAux_00_grp";
	rename -uid "0AABEF99-4F84-28DC-908A-09845661D50A";
	setAttr ".t" -type "double3" 0 7 0 ;
	setAttr ".r" -type "double3" 90 -38.096956652962369 -90 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.75 0.25 0.25 ;
createNode joint -n "Leg:qdrpAuxIk_01_jnt" -p "Leg:qdrpAuxIk_00_jnt";
	rename -uid "A1D2D274-48EB-3CA3-DB1E-59A607CF2603";
	setAttr ".t" -type "double3" 3.3541847889864838 0 0 ;
	setAttr ".r" -type "double3" 0 0 -69.724459516824325 ;
	setAttr ".pa" -type "double3" 0 0 -90 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.75 0.25 0.25 ;
createNode joint -n "Leg:qdrpAuxIk_02_jnt" -p "Leg:qdrpAuxIk_01_jnt";
	rename -uid "706B38ED-4EF6-5694-64EE-5DBDDB8326B4";
	setAttr ".t" -type "double3" 3.9464780821673147 0 0 ;
	setAttr ".r" -type "double3" 0 0 71.56505117707799 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.75 0.25 0.25 ;
createNode transform -n "Leg:qdrpDwIk_00_tr" -p "Leg:qdrpAuxIk_02_jnt";
	rename -uid "5EA79159-4C5B-7358-F701-ACA410F50EEC";
	setAttr ".t" -type "double3" 0.00020524421105624408 -0.00024983035520112582 1.8459821006316067e-15 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000002 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.70200002 0.70200002 0 ;
createNode transform -n "Leg:qdrpDwIk_01_tr" -p "Leg:qdrpDwIk_00_tr";
	rename -uid "3A82DB3E-442F-ADB4-DDAE-42813DD537F0";
	setAttr ".t" -type "double3" 2.2361941445787519 0 -3.4337306505277848e-16 ;
	setAttr ".s" -type "double3" 0.99999999999999989 1 0.99999999999999989 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0.70200002 0.70200002 0 ;
createNode joint -n "Leg:qdrpUpIk_00_jnt" -p "Leg:qdrpDwIk_01_tr";
	rename -uid "CC4B887B-4F35-304F-A6F0-84A951188268";
	setAttr ".t" -type "double3" 8.6691799872085085e-05 -2.5845948372744832e-15 -2.7779794020959137e-09 ;
	setAttr ".r" -type "double3" -89.999999999558355 81.87036711197662 -89.999999999595161 ;
	setAttr ".jo" -type "double3" -153.42996099652478 0 90.000000000005343 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 0.75 0.75 ;
createNode joint -n "Leg:qdrpUpIk_01_jnt" -p "Leg:qdrpUpIk_00_jnt";
	rename -uid "CD04B54A-4A55-3295-A004-DF8908DA7FB3";
	setAttr ".t" -type "double3" 2.8283810098779334 -4.4408920985006262e-16 2.6268733301341168e-13 ;
	setAttr ".r" -type "double3" -2.1229192719290459e-12 2.8620531061650459e-11 71.565858032444012 ;
	setAttr ".pa" -type "double3" 0 0 90 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 0.75 0.75 ;
createNode joint -n "Leg:qdrpUpIk_02_jnt" -p "Leg:qdrpUpIk_01_jnt";
	rename -uid "DBD54B4C-414F-CC4E-AD27-E88DEF984FA3";
	setAttr ".t" -type "double3" 2.2360877166971056 0 -2.5751313599813149e-13 ;
	setAttr ".uocol" yes;
	setAttr ".oclr" -type "float3" 0 0.75 0.75 ;
createNode joint -n "Leg:qdrpJntIk_00_mstc" -p "Leg:qdrpUpIk_02_jnt";
	rename -uid "F130CAD1-4086-456C-9DB2-F5A6C7BADC09";
	setAttr ".r" -type "double3" 90 -26.565051177077994 -90 ;
	setAttr ".jo" -type "double3" 116.56673012812182 89.999999999993378 0 ;
createNode ikEffector -n "Leg:effector3" -p "Leg:qdrpUpIk_01_jnt";
	rename -uid "4B2AB608-41E0-F530-39EB-EAB346F7F351";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode joint -n "Leg:qdrpJntIk_01_mstc" -p "Leg:qdrpUpIk_00_jnt";
	rename -uid "C63ACB2E-4A17-0C2F-F2F9-F296FD63E583";
	setAttr ".r" -type "double3" 0 0 -71.56505117707799 ;
	setAttr ".jo" -type "double3" 0 0 -108.43183355703107 ;
createNode pointConstraint -n "Leg:qdrpJnt_01_mstc_pointConstraint1" -p "Leg:qdrpJntIk_01_mstc";
	rename -uid "619CDDE2-4B7C-4D19-D3D7-A8BC70A5A903";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "qdrpUpIk_01_jntW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 2.8284271247461898 4.4408920985006262e-16 1.5146129380243427e-28 ;
	setAttr -k on ".w0";
createNode joint -n "Leg:qdrpJntIk_02_mstc" -p "Leg:qdrpDwIk_01_tr";
	rename -uid "8962664F-4462-1E32-F74B-00AC0CBF06D4";
	setAttr ".t" -type "double3" 8.6691799872085085e-05 -2.805611682941469e-15 -2.7779748501815128e-09 ;
	setAttr ".r" -type "double3" 0 0 71.56505117707799 ;
	setAttr ".jo" -type "double3" 90.000000000003936 71.566196509655299 -179.99999999999625 ;
createNode aimConstraint -n "Leg:qdrpDwIk_00_tr_aimConstraint1" -p "Leg:qdrpDwIk_00_tr";
	rename -uid "29A9571E-4ED5-FB89-A1BB-2F8B4B0D57E9";
	addAttr -dcb 0 -ci true -sn "w0" -ln "ik_01_ctrW0" -dv 1 -at "double";
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
	setAttr ".u" -type "double3" 0 0 1 ;
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" 90.000000000000014 5.8045122936709188e-14 166.62155091458743 ;
	setAttr -k on ".w0";
createNode joint -n "Leg:qdrpJntIk_03_mstc" -p "Leg:qdrpDwIk_00_tr";
	rename -uid "E3AF52A8-4E4B-0848-57DF-76A93518BFDE";
	setAttr ".t" -type "double3" 0.00013130553734876205 -5.5741352532769073e-16 -4.3785329888498912e-05 ;
	setAttr ".jo" -type "double3" 90.000000000001265 0.0011219326474207671 -180 ;
createNode ikEffector -n "Leg:effector1" -p "Leg:qdrpAuxIk_01_jnt";
	rename -uid "C97684F8-410A-A77B-18EF-55A844488952";
	setAttr ".v" no;
	setAttr ".hd" yes;
createNode ikHandle -n "Leg:qdrpUpIk_00_ikrp" -p "Leg:qdrpAuxIk_00_jnt";
	rename -uid "69AC801B-45EC-344D-C7B0-C9A86362A43C";
	setAttr ".t" -type "double3" 7.982363894321054e-06 -1.026394853420598e-05 8.6790214511398104e-14 ;
	setAttr ".r" -type "double3" -51.908767314510918 90 0 ;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1" -p
		 "Leg:qdrpUpIk_00_ikrp";
	rename -uid "B02A9A6F-46E0-54A8-3038-8A84A361D1D9";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ikPole_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" -9.8607613152626476e-32 1.9999999999999996 4.0127726168849245 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:Config_00_root";
	rename -uid "2164EE14-46DE-EE9C-C58A-27957367A59E";
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Leg:Config_00_ctr" -p "Leg:Config_00_root";
	rename -uid "0ADD76F7-48AD-C51C-04AB-7FBA68C361EB";
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
	setAttr -k on ".fkIk" 1;
createNode nurbsCurve -n "Leg:Config_00_ctrShape" -p "Leg:Config_00_ctr";
	rename -uid "A4FDE4B7-4591-3B19-B4B7-9B8073ECD631";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-0.50754647857757385 0.25419990378570528 -0.50365936256114197
		-0.50754647857757385 0.25419990378570528 -0.42810164846872401
		-8.5637699810786345e-16 -1.7040707585512525e-16 -0.42810164846872401
		-8.6880761133796366e-16 -1.9522657372879512e-16 -0.50365936256114197
		-0.25720416068109514 0.12881829676299131 -0.50365936256114197
		-9.1853006425835907e-16 -2.9450456522347544e-16 -0.75181606784027055
		-9.1853006425835907e-16 -2.9450456522347544e-16 -0.85361746887853784
		-0.26537940088541162 0.13291278930914485 -0.59201294018284345
		-0.50754647857757396 0.25419990378570528 -0.8143579797112086
		-0.50754647857757396 0.25419990378570528 -0.73340385955741116
		-0.25788543714491435 0.12915950770398679 -0.50365936256114197
		-0.50754647857757385 0.25419990378570528 -0.50365936256114197
		;
createNode nurbsCurve -n "Leg:Config_00_ctrShape5" -p "Leg:Config_00_ctr";
	rename -uid "7D480FE5-42B8-3076-C93B-0C833DC62A7B";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-0.50754647857757396 0.25419990378570528 -1.1922015781073059
		-0.50754647857757396 0.25419990378570528 -1.152313593794364
		0.10150929571551377 -0.050839980757141127 -0.95056450630975253
		0.10150929571551373 -0.05083998075714128 -0.99045242140516521
		-0.50754647857757396 0.25419990378570528 -1.1922015781073059
		;
createNode nurbsCurve -n "Leg:Config_00_ctrShape6" -p "Leg:Config_00_ctr";
	rename -uid "3257E850-47EF-FC16-1763-B791BD47F119";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 10 2 no 3
		11 0 1 2 3 4 5 6 7 8 9 10
		11
		-0.50754647857757385 0.25419990378570528 -0.32112374545251798
		-0.50754647857757362 0.25419990378570534 -0.0039290201278821303
		-7.9480661695253232e-16 -4.7473000449604746e-17 -0.0039290201278821303
		-8.0354689187994525e-16 -6.4924209892028136e-17 -0.084474696306748434
		-0.23045199107951653 0.11541972298539646 -0.084474696306748434
		-0.23045199107951661 0.11541972298539643 -0.28315242907234722
		-0.28360512446753289 0.14204097239492744 -0.28315242907234722
		-0.283605124467533 0.14204097239492752 -0.084474696306748434
		-0.45370502882768421 0.22723391756812358 -0.084474696306748434
		-0.45370502882768415 0.22723391756812353 -0.32112374545251798
		-0.50754647857757385 0.25419990378570528 -0.32112374545251798
		;
createNode nurbsCurve -n "Leg:Config_00_ctrShape7" -p "Leg:Config_00_ctr";
	rename -uid "6618C7F1-4A9A-84E1-6787-2DA7710B58AF";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 4 2 no 3
		5 0 1 2 3 4
		5
		-0.50754647857757396 0.25419990378570506 -1.4273030617832974
		-0.50754647857757396 0.25419990378570506 -1.3467573942566222
		-9.9311374363895185e-16 -4.4342155246549476e-16 -1.3467573942566222
		-9.9311374363895185e-16 -4.4342155246549476e-16 -1.4273030617832974
		-0.50754647857757396 0.25419990378570506 -1.4273030617832974
		;
createNode nurbsCurve -n "Leg:Config_00_ctrShape8" -p "Leg:Config_00_ctr";
	rename -uid "E3335A88-4F24-65BA-7D70-30AACA30FFE6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 11 2 no 3
		12 0 1 2 3 4 5 6 7 8 9 10 11
		12
		-0.50754647857757396 0.25419990378570501 -1.6504965005407113
		-0.50754647857757396 0.25419990378570501 -1.5749387864482933
		-1.0428361965593462e-15 -5.4269954396017405e-16 -1.5749387864482933
		-1.0428361965593462e-15 -5.4269954396017405e-16 -1.6504965005407113
		-0.2572041606810952 0.12881829676299081 -1.6504965005407113
		-1.0428361965593462e-15 -5.4269954396017405e-16 -1.8986532404286036
		-1.0925586494797423e-15 -6.4197753545485412e-16 -2.0004546414668707
		-0.26537940088541184 0.13291278930914446 -1.7388500435536485
		-0.50754647857757407 0.25419990378570495 -1.9611951522995381
		-0.50754647857757407 0.25419990378570495 -1.880240962928218
		-0.25788543714491441 0.12915950770398643 -1.6504965005407113
		-0.50754647857757396 0.25419990378570501 -1.6504965005407113
		;
createNode parentConstraint -n "Leg:ConfigRoot_00_prc" -p "Leg:Config_00_root";
	rename -uid "FA684E73-4D7D-38ED-76F8-5DA4BAE2E487";
	setAttr ".s" -type "double3" 1 0.99999999999999989 0.99999999999999978 ;
	setAttr ".lr" -type "double3" 90.000000000006963 -26.563913890631582 -89.999999999923062 ;
createNode transform -n "Leg:Fk_00_root";
	rename -uid "563EF43D-4ACE-AA5B-AECE-5E9ADBC71BC9";
	setAttr ".t" -type "double3" -2.0194839173657902e-28 7 6.9952819339094868e-42 ;
	setAttr ".r" -type "double3" 89.999999999997783 -26.564250123491792 -89.999999999986571 ;
	setAttr ".s" -type "double3" 1 1.0000000000000002 1 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".rpt" -type "double3" 2.2044709673953989e-29 1.8411902321118976e-16 -2.9790618086251792e-16 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 -9.8607613152626498e-32 0 ;
createNode transform -n "Leg:Fk_00_ctr" -p "Leg:Fk_00_root";
	rename -uid "AD01AE8B-44E4-F254-11B0-18AB4614648E";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "Leg:qdrpJntFk_00_mstc" -p "Leg:Fk_00_ctr";
	rename -uid "10AF6954-467D-FF4C-DF41-C9AC1D5354BB";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" -8.8817841970012523e-16 -8.8817841970012523e-16 -2.0194839173657902e-28 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -l on ".radi";
createNode transform -n "Leg:Fk_01_root" -p "Leg:Fk_00_ctr";
	rename -uid "17207F23-4A72-B96E-5658-CCAC0C4AE1C3";
	setAttr ".t" -type "double3" 2.2360877166971074 0 7.2919867937189491e-13 ;
	setAttr ".r" -type "double3" 0 0 -71.562242926365116 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1 1 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754681e-16 0 ;
	setAttr ".rpt" -type "double3" -3.1596984947465454e-16 2.2772641650360992e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Leg:Fk_01_ctr" -p "Leg:Fk_01_root";
	rename -uid "D422E852-459B-ADC7-827A-C395B064AD53";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "Leg:qdrpJntFk_01_mstc" -p "Leg:Fk_01_ctr";
	rename -uid "86F418B7-4059-7B76-AA2B-37915B76C3FE";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" -4.4408920985006262e-16 0 1.0097419586828951e-28 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -l on ".radi";
createNode transform -n "Leg:Fk_02_root" -p "Leg:Fk_01_ctr";
	rename -uid "B7945C0B-46D3-A5CA-11D2-64849AC75C30";
	setAttr ".t" -type "double3" 2.8283810098779352 0 1.0382674720381562e-13 ;
	setAttr ".r" -type "double3" 0 0 71.557321594853633 ;
	setAttr ".s" -type "double3" 1 0.99999999999999978 1.0000000000000002 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".rpt" -type "double3" 3.1596080025213243e-16 2.2769927715540753e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 9.8607613152626454e-32 0 ;
createNode transform -n "Leg:Fk_02_ctr" -p "Leg:Fk_02_root";
	rename -uid "442EF112-4D39-5E47-310C-A3B1196A554D";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".tx";
	setAttr -l on -k off ".ty";
	setAttr -l on -k off ".tz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode joint -n "Leg:qdrpJntFk_02_mstc" -p "Leg:Fk_02_ctr";
	rename -uid "DE8CD069-4D13-22F7-2618-D4B9557083E4";
	setAttr -l on ".v" no;
	setAttr ".t" -type "double3" -4.4408920985006262e-16 2.2193618470778276e-16 -2.0194839173657902e-28 ;
	setAttr -l on ".tx";
	setAttr -l on ".ty";
	setAttr -l on ".tz";
	setAttr -l on ".rx";
	setAttr -l on ".ry";
	setAttr -l on ".rz";
	setAttr -l on ".sx";
	setAttr -l on ".sy";
	setAttr -l on ".sz";
	setAttr -l on ".radi";
createNode nurbsCurve -n "Leg:Fk_02_ctrShape" -p "Leg:Fk_02_ctr";
	rename -uid "F53CCE8B-4C5C-802E-D4B5-9793026DBC33";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-06 0.5 -0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 0.5 0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 0.5 -0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 0.5 0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 0.5
		;
createNode transform -n "Leg:Fk_03_root" -p "Leg:Fk_02_ctr";
	rename -uid "626EFC27-4E4E-CCD0-C5C9-F2867209FE3F";
	setAttr ".t" -type "double3" 2.2361941445787528 1.350540462796701e-08 4.7206407319988246e-13 ;
	setAttr ".r" -type "double3" 0 0 63.44067120801968 ;
	setAttr ".s" -type "double3" 1 0.99999999999999989 1 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754686e-16 0 ;
	setAttr ".rpt" -type "double3" 2.9791897340949633e-16 1.8414461194681531e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 9.8607613152626465e-32 0 ;
createNode transform -n "Leg:Fk_03_ctr" -p "Leg:Fk_03_root";
	rename -uid "38C9B550-4A0F-9769-56B3-C690331741EF";
createNode nurbsCurve -n "Leg:Fk_03_ctrShape" -p "Leg:Fk_03_ctr";
	rename -uid "54FA9F0D-4546-7D45-9525-A1B227D428C2";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-06 0.5 -0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		0.87823173232003982 -0.5 0.5
		0.87823173232003982 0.5 0.5
		0.87823173232003982 0.5 -0.5
		0.87823173232003982 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 0.5 -0.5
		0.87823173232003982 0.5 -0.5
		0.87823173232003982 0.5 0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		0.87823173232003982 -0.5 0.5
		0.87823173232003982 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 0.5
		;
createNode joint -n "Leg:qdrpJntFk_03_mstc" -p "Leg:Fk_03_ctr";
	rename -uid "AEB249C8-4120-6129-4F92-988429496A1F";
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
	setAttr ".jo" -type "double3" 0 0 -63.440671082895818 ;
createNode nurbsCurve -n "Leg:Fk_01_ctrShape" -p "Leg:Fk_01_ctr";
	rename -uid "63B4A9A0-4FDD-428F-4A0D-21A19F8459D8";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-06 0.5 -0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 0.5 0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 0.5 -0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 0.5 0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 0.5
		;
createNode nurbsCurve -n "Leg:Fk_00_ctrShape" -p "Leg:Fk_00_ctr";
	rename -uid "722B5B19-4BB4-C2F8-9BF3-B38282A67CEE";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-4.9999998736893758e-06 0.5 -0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 0.5 0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 0.5 -0.5
		1.7840255808801397 0.5 -0.5
		1.7840255808801397 0.5 0.5
		-4.9999998736893758e-06 0.5 0.5
		-4.9999998736893758e-06 -0.5 0.5
		1.7840255808801397 -0.5 0.5
		1.7840255808801397 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 -0.5
		-4.9999998736893758e-06 -0.5 0.5
		;
createNode transform -n "Leg:ik_00_grp";
	rename -uid "911A4C96-432B-D105-F452-62A70F266581";
createNode transform -n "Leg:ikPole_00_root" -p "Leg:ik_00_grp";
	rename -uid "951630F3-4D56-0860-3558-7FBDAD5B4F7F";
	setAttr ".t" -type "double3" 3.9923092356379255e-16 4.3603997230529794 4 ;
	setAttr ".s" -type "double3" 1 1.0000000000000004 1.0000000000000002 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 -1.4791141972893978e-31 0 ;
createNode transform -n "Leg:ikPole_00_ctr" -p "Leg:ikPole_00_root";
	rename -uid "68838504-4CF2-8463-D725-6AA03C467037";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".rx";
	setAttr -l on -k off ".ry";
	setAttr -l on -k off ".rz";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Leg:ikPole_00_ctrShape" -p "Leg:ikPole_00_ctr";
	rename -uid "30A28AED-42DE-8F41-F5D0-57B91472EB7D";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 20 2 no 3
		21 0 1 2 5 8 9 10 13 16 17 18 21 24 25 26 27 28 29 30 31 32
		21
		-5.5511151231257827e-17 -0.21994586017864298 -0.098359980527570778
		-1.1102230246251565e-16 -0.35883451011432171 -0.17941719077053508
		-1.1102230246251565e-16 -0.44966709222076767 -0.33296889850143707
		-1.6653345369377348e-16 -0.50000000000000011 -0.53825170088485663
		-1.1102230246251565e-16 -0.44966709222076767 -0.7435345032682763
		-1.1102230246251565e-16 -0.35883451011432171 -0.89708621099917818
		-5.5511151231257827e-17 -0.21994586017864298 -0.97814342124214249
		0 0 -1.0382517008848566
		5.5511151231257827e-17 0.21994586017864298 -0.97814342124214249
		1.1102230246251565e-16 0.35883451011432171 -0.89708621099917818
		1.1102230246251565e-16 0.44966709222076767 -0.7435345032682763
		1.6653345369377348e-16 0.50000000000000011 -0.53825170088485663
		1.1102230246251565e-16 0.44966709222076767 -0.33296889850143707
		1.1102230246251565e-16 0.35883451011432171 -0.17941719077053508
		5.5511151231257827e-17 0.21994586017864298 -0.098359980527570778
		5.5511151231257827e-17 0.17941725505716086 6.42866261335584e-08
		1.1102230246251565e-16 0.35883451011432171 6.42866261335584e-08
		0 0 0.35883457440094757
		-1.1102230246251565e-16 -0.35883451011432171 6.42866261335584e-08
		-5.5511151231257827e-17 -0.17941725505716086 6.42866261335584e-08
		-5.5511151231257827e-17 -0.21994586017864298 -0.098359980527570778
		;
createNode nurbsCurve -n "Leg:ikPole_00_ctrShape1" -p "Leg:ikPole_00_ctr";
	rename -uid "ADB9DF2C-47AA-37CF-3A20-BE830CFB61A6";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 20 2 no 3
		21 0 1 2 5 8 9 10 13 16 17 18 21 24 25 26 27 28 29 30 31 32
		21
		0.21994586017864295 0 -0.098359980527570778
		0.3588345101143216 0 -0.17941719077053508
		0.43989172035728591 0 -0.33296889850143707
		0.5 0 -0.53825170088485663
		0.43989172035728591 0 -0.7435345032682763
		0.3588345101143216 0 -0.89708621099917818
		0.21994586017864295 0 -0.97814342124214249
		0 0 -1.0382517008848566
		-0.21994586017864295 0 -0.97814342124214249
		-0.3588345101143216 0 -0.89708621099917818
		-0.43989172035728591 0 -0.7435345032682763
		-0.5 0 -0.53825170088485663
		-0.43989172035728591 0 -0.33296889850143707
		-0.3588345101143216 0 -0.17941719077053508
		-0.21994586017864295 0 -0.098359980527570778
		-0.1794172550571608 0 6.42866261335584e-08
		-0.3588345101143216 0 6.42866261335584e-08
		0 0 0.35883457440094757
		0.3588345101143216 0 6.42866261335584e-08
		0.1794172550571608 0 6.42866261335584e-08
		0.21994586017864295 0 -0.098359980527570778
		;
createNode transform -n "Leg:ik_00_root" -p "Leg:ik_00_grp";
	rename -uid "1028C0D0-4B55-46C6-16D9-DCBE28C3C353";
	setAttr ".t" -type "double3" -1.8459821395099538e-15 0.9997181985350192 -5.9791600945824364e-05 ;
	setAttr ".s" -type "double3" 1 0.99999999999999967 1.0000000000000004 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 1.4791141972893967e-31 0 ;
createNode transform -n "Leg:ik_00_ctr" -p "Leg:ik_00_root";
	rename -uid "35DF4094-4B09-B46E-ACB8-34B3AE7C6E63";
	addAttr -ci true -sn "SpaceSwitch" -ln "SpaceSwitch" -min 0 -max 1 -en "world:hips" 
		-at "enum";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
	setAttr -l on ".SpaceSwitch";
createNode ikHandle -n "Leg:qdrpAuxIk_00_ikrp" -p "Leg:ik_00_ctr";
	rename -uid "1108D4E8-4700-044A-595B-C197372A6F14";
	setAttr ".v" no;
	setAttr ".roc" yes;
createNode poleVectorConstraint -n "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1" 
		-p "Leg:qdrpAuxIk_00_ikrp";
	rename -uid "C41A84BC-4BC0-C526-B452-73910027D18C";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "ikPole_00_ctrW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 0 -2 3.0127726168849245 ;
	setAttr -k on ".w0";
createNode pointConstraint -n "Leg:qdrpAuxIk_00_ikrp_pointConstraint1" -p "Leg:qdrpAuxIk_00_ikrp";
	rename -uid "13E38344-4891-0741-49E3-D8AE58DD5D41";
	addAttr -dcb 0 -ci true -k true -sn "w0" -ln "FootIk_00_mstcW0" -dv 1 -min 0 -at "double";
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
	setAttr ".rst" -type "double3" 1.8459821395099538e-15 0.00028180146498058001 5.9791600945824343e-05 ;
	setAttr -k on ".w0";
createNode transform -n "Leg:ik_01_root" -p "Leg:ik_00_ctr";
	rename -uid "79150FFA-41AB-9282-EA91-9F939A01C337";
	setAttr ".t" -type "double3" 0 3.3306690738754696e-16 0 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
createNode transform -n "Leg:ik_01_off" -p "Leg:ik_01_root";
	rename -uid "5C6E4FDA-4B75-E77C-1A61-27B1E274C4F9";
	setAttr ".t" -type "double3" 3.0741942836771039e-15 2.2361941334304678 -0.00022329232770107454 ;
	setAttr ".r" -type "double3" 89.99427914869355 0 0 ;
	setAttr ".s" -type "double3" 1.0000000000000002 1.0000000000000002 1.0000000000000007 ;
	setAttr ".rp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".rpt" -type "double3" 0 3.3303365142584616e-16 -3.3306690572728146e-16 ;
	setAttr ".sp" -type "double3" 0 -3.3306690738754696e-16 0 ;
	setAttr ".spt" -type "double3" 0 -9.8607613152626498e-32 0 ;
createNode transform -n "Leg:ik_01_ctr" -p "Leg:ik_01_off";
	rename -uid "22F0BEE1-4E8E-BB0F-5611-18BBFC3C08F9";
	setAttr -l on -k off ".v";
	setAttr -l on -k off ".sx";
	setAttr -l on -k off ".sy";
	setAttr -l on -k off ".sz";
createNode nurbsCurve -n "Leg:ik_01_ctrShape" -p "Leg:ik_01_ctr";
	rename -uid "2CEA9502-4F7B-9537-F033-66BD77BE9B63";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 32 2 no 3
		33 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32
		33
		0.21994586017864295 2.4651903288156619e-32 0.43989172035728591
		0.3588345101143216 2.4651903288156619e-32 0.3588345101143216
		0.43989172035728591 2.4651903288156619e-32 0.21994586017864295
		0.53825176517148277 2.4651903288156619e-32 0.1794172550571608
		0.53825176517148277 2.4651903288156619e-32 0.3588345101143216
		0.89708627528580431 2.4651903288156619e-32 0
		0.53825176517148277 2.4651903288156619e-32 -0.3588345101143216
		0.53825176517148277 2.4651903288156619e-32 -0.1794172550571608
		0.43989172035728591 2.4651903288156619e-32 -0.21994586017864295
		0.3588345101143216 2.4651903288156619e-32 -0.3588345101143216
		0.21994586017864295 2.4651903288156619e-32 -0.43989172035728591
		0.1794172550571608 2.4651903288156619e-32 -0.53825176517148277
		0.3588345101143216 2.4651903288156619e-32 -0.53825176517148277
		0 2.4651903288156619e-32 -0.89708627528580431
		-0.3588345101143216 2.4651903288156619e-32 -0.53825176517148277
		-0.1794172550571608 2.4651903288156619e-32 -0.53825176517148277
		-0.21994586017864295 2.4651903288156619e-32 -0.43989172035728591
		-0.3588345101143216 2.4651903288156619e-32 -0.3588345101143216
		-0.43989172035728591 2.4651903288156619e-32 -0.21994586017864295
		-0.53825176517148277 2.4651903288156619e-32 -0.1794172550571608
		-0.53825176517148277 2.4651903288156619e-32 -0.3588345101143216
		-0.89708627528580431 2.4651903288156619e-32 0
		-0.53825176517148277 2.4651903288156619e-32 0.3588345101143216
		-0.53825176517148277 2.4651903288156619e-32 0.1794172550571608
		-0.43989172035728591 2.4651903288156619e-32 0.21994586017864295
		-0.3588345101143216 2.4651903288156619e-32 0.3588345101143216
		-0.21994586017864295 2.4651903288156619e-32 0.43989172035728591
		-0.1794172550571608 2.4651903288156619e-32 0.53825176517148277
		-0.3588345101143216 2.4651903288156619e-32 0.53825176517148277
		0 2.4651903288156619e-32 0.89708627528580431
		0.3588345101143216 2.4651903288156619e-32 0.53825176517148277
		0.1794172550571608 2.4651903288156619e-32 0.53825176517148277
		0.21994586017864295 2.4651903288156619e-32 0.43989172035728591
		;
createNode aimConstraint -n "Leg:ik_01_root_aimConstraint1" -p "Leg:ik_01_root";
	rename -uid "978F4D65-4AAD-D2DC-F661-5E891B86FD41";
	addAttr -dcb 0 -ci true -sn "w0" -ln "qdrpAuxIk_00_jntW0" -dv 1 -at "double";
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
	setAttr ".wut" 1;
	setAttr ".rsrr" -type "double3" -26.565050000000003 0 0 ;
	setAttr -k on ".w0";
createNode nurbsCurve -n "Leg:ik_00_ctrShape" -p "Leg:ik_00_ctr";
	rename -uid "09DD4BDC-404F-4D05-DB5B-6CAC75CDD3D0";
	setAttr -k off ".v";
	setAttr ".cc" -type "nurbsCurve" 
		1 16 0 no 3
		17 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
		17
		-0.5 0.5 -0.5
		-0.5 0.5 0.5
		-0.5 -0.5 0.5
		0.5 -0.5 0.5
		0.5 0.5 0.5
		0.5 0.5 -0.5
		0.5 -0.5 -0.5
		-0.5 -0.5 -0.5
		-0.5 0.5 -0.5
		0.5 0.5 -0.5
		0.5 0.5 0.5
		-0.5 0.5 0.5
		-0.5 -0.5 0.5
		0.5 -0.5 0.5
		0.5 -0.5 -0.5
		-0.5 -0.5 -0.5
		-0.5 -0.5 0.5
		;
createNode lightLinker -s -n "lightLinker1";
	rename -uid "9BB00E90-4092-B582-780D-A2935BD5AEF2";
	setAttr -s 2 ".lnk";
	setAttr -s 2 ".slnk";
createNode shapeEditorManager -n "shapeEditorManager";
	rename -uid "C91E4C32-4872-F383-A107-94AAA217ACDB";
createNode poseInterpolatorManager -n "poseInterpolatorManager";
	rename -uid "029A25E8-49AF-AE97-8244-7AAD95B3D6AE";
createNode displayLayerManager -n "layerManager";
	rename -uid "7D3DD5C9-4430-EAD5-E5BA-22A9886DC0EB";
createNode displayLayer -n "defaultLayer";
	rename -uid "78C033BE-4958-77CD-C65B-2180EE9662EB";
createNode renderLayerManager -n "renderLayerManager";
	rename -uid "CCE5405C-4129-6486-E7A4-70832A80EB59";
createNode renderLayer -n "defaultRenderLayer";
	rename -uid "EF6D0C8B-4C67-8B6F-F969-F9AD64E5B794";
	setAttr ".g" yes;
createNode script -n "uiConfigurationScriptNode";
	rename -uid "F74812F0-42D6-09A6-1DA5-04B75A3AE3E7";
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
		+ "            -nCloths 1\n            -nParticles 1\n            -nRigids 1\n            -dynamicConstraints 1\n            -locators 1\n            -manipulators 1\n            -pluginShapes 1\n            -dimensions 1\n            -handles 1\n            -pivots 1\n            -textures 1\n            -strokes 1\n            -motionTrails 1\n            -clipGhosts 1\n            -greasePencils 1\n            -shadows 0\n            -captureSequenceNumber -1\n            -width 1261\n            -height 708\n            -sceneRenderFilter 0\n            $editorName;\n        modelEditor -e -viewSelected 0 $editorName;\n        modelEditor -e \n            -pluginObjects \"gpuCacheDisplayFilter\" 1 \n            $editorName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextPanel \"outlinerPanel\" (localizedPanelLabel(\"ToggledOutliner\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\toutlinerPanel -edit -l (localizedPanelLabel(\"ToggledOutliner\")) -mbv $menusOkayInPanels  $panelName;\n"
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
		+ "\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"contentBrowserPanel\" (localizedPanelLabel(\"Content Browser\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Content Browser\")) -mbv $menusOkayInPanels  $panelName;\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\t$panelName = `sceneUIReplacement -getNextScriptedPanel \"Stereo\" (localizedPanelLabel(\"Stereo\")) `;\n\tif (\"\" != $panelName) {\n\t\t$label = `panel -q -label $panelName`;\n\t\tscriptedPanel -edit -l (localizedPanelLabel(\"Stereo\")) -mbv $menusOkayInPanels  $panelName;\n{ string $editorName = ($panelName+\"Editor\");\n            stereoCameraView -e \n                -camera \"persp\" \n                -useInteractiveMode 0\n                -displayLights \"default\" \n                -displayAppearance \"smoothShaded\" \n                -activeOnly 0\n                -ignorePanZoom 0\n                -wireframeOnShaded 0\n"
		+ "                -headsUpDisplay 1\n                -holdOuts 1\n                -selectionHiliteDisplay 1\n                -useDefaultMaterial 0\n                -bufferMode \"double\" \n                -twoSidedLighting 0\n                -backfaceCulling 0\n                -xray 0\n                -jointXray 0\n                -activeComponentsXray 0\n                -displayTextures 0\n                -smoothWireframe 0\n                -lineWidth 1\n                -textureAnisotropic 0\n                -textureHilight 1\n                -textureSampling 2\n                -textureDisplay \"modulate\" \n                -textureMaxSize 32768\n                -fogging 0\n                -fogSource \"fragment\" \n                -fogMode \"linear\" \n                -fogStart 0\n                -fogEnd 100\n                -fogDensity 0.1\n                -fogColor 0.5 0.5 0.5 1 \n                -depthOfFieldPreview 1\n                -maxConstantTransparency 1\n                -objectFilterShowInHUD 1\n                -isFiltered 0\n                -colorResolution 4 4 \n"
		+ "                -bumpResolution 4 4 \n                -textureCompression 0\n                -transparencyAlgorithm \"frontAndBackCull\" \n                -transpInShadows 0\n                -cullingOverride \"none\" \n                -lowQualityLighting 0\n                -maximumNumHardwareLights 0\n                -occlusionCulling 0\n                -shadingModel 0\n                -useBaseRenderer 0\n                -useReducedRenderer 0\n                -smallObjectCulling 0\n                -smallObjectThreshold -1 \n                -interactiveDisableShadows 0\n                -interactiveBackFaceCull 0\n                -sortTransparent 1\n                -controllers 1\n                -nurbsCurves 1\n                -nurbsSurfaces 1\n                -polymeshes 1\n                -subdivSurfaces 1\n                -planes 1\n                -lights 1\n                -cameras 1\n                -controlVertices 1\n                -hulls 1\n                -grid 1\n                -imagePlane 1\n                -joints 1\n                -ikHandles 1\n"
		+ "                -deformers 1\n                -dynamics 1\n                -particleInstancers 1\n                -fluids 1\n                -hairSystems 1\n                -follicles 1\n                -nCloths 1\n                -nParticles 1\n                -nRigids 1\n                -dynamicConstraints 1\n                -locators 1\n                -manipulators 1\n                -pluginShapes 1\n                -dimensions 1\n                -handles 1\n                -pivots 1\n                -textures 1\n                -strokes 1\n                -motionTrails 1\n                -clipGhosts 1\n                -greasePencils 1\n                -shadows 0\n                -captureSequenceNumber -1\n                -width 0\n                -height 0\n                -sceneRenderFilter 0\n                -displayMode \"centerEye\" \n                -viewColor 0 0 0 1 \n                -useCustomBackground 1\n                $editorName;\n            stereoCameraView -e -viewSelected 0 $editorName;\n            stereoCameraView -e \n"
		+ "                -pluginObjects \"gpuCacheDisplayFilter\" 1 \n                $editorName; };\n\t\tif (!$useSceneConfig) {\n\t\t\tpanel -e -l $label $panelName;\n\t\t}\n\t}\n\n\n\tif ($useSceneConfig) {\n        string $configName = `getPanel -cwl (localizedPanelLabel(\"Current Layout\"))`;\n        if (\"\" != $configName) {\n\t\t\tpanelConfiguration -edit -label (localizedPanelLabel(\"Current Layout\")) \n\t\t\t\t-userCreated false\n\t\t\t\t-defaultImage \"vacantCell.xP:/\"\n\t\t\t\t-image \"\"\n\t\t\t\t-sc false\n\t\t\t\t-configString \"global string $gMainPane; paneLayout -e -cn \\\"single\\\" -ps 1 100 100 $gMainPane;\"\n\t\t\t\t-removeAllPanels\n\t\t\t\t-ap false\n\t\t\t\t\t(localizedPanelLabel(\"Persp View\")) \n\t\t\t\t\t\"modelPanel\"\n"
		+ "\t\t\t\t\t\"$panelName = `modelPanel -unParent -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels `;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1261\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t\t\"modelPanel -edit -l (localizedPanelLabel(\\\"Persp View\\\")) -mbv $menusOkayInPanels  $panelName;\\n$editorName = $panelName;\\nmodelEditor -e \\n    -cam `findStartUpCamera persp` \\n    -useInteractiveMode 0\\n    -displayLights \\\"default\\\" \\n    -displayAppearance \\\"smoothShaded\\\" \\n    -activeOnly 0\\n    -ignorePanZoom 0\\n    -wireframeOnShaded 0\\n    -headsUpDisplay 1\\n    -holdOuts 1\\n    -selectionHiliteDisplay 1\\n    -useDefaultMaterial 0\\n    -bufferMode \\\"double\\\" \\n    -twoSidedLighting 0\\n    -backfaceCulling 0\\n    -xray 0\\n    -jointXray 0\\n    -activeComponentsXray 0\\n    -displayTextures 0\\n    -smoothWireframe 0\\n    -lineWidth 1\\n    -textureAnisotropic 0\\n    -textureHilight 1\\n    -textureSampling 2\\n    -textureDisplay \\\"modulate\\\" \\n    -textureMaxSize 32768\\n    -fogging 0\\n    -fogSource \\\"fragment\\\" \\n    -fogMode \\\"linear\\\" \\n    -fogStart 0\\n    -fogEnd 100\\n    -fogDensity 0.1\\n    -fogColor 0.5 0.5 0.5 1 \\n    -depthOfFieldPreview 1\\n    -maxConstantTransparency 1\\n    -rendererName \\\"vp2Renderer\\\" \\n    -objectFilterShowInHUD 1\\n    -isFiltered 0\\n    -colorResolution 256 256 \\n    -bumpResolution 512 512 \\n    -textureCompression 0\\n    -transparencyAlgorithm \\\"frontAndBackCull\\\" \\n    -transpInShadows 0\\n    -cullingOverride \\\"none\\\" \\n    -lowQualityLighting 0\\n    -maximumNumHardwareLights 1\\n    -occlusionCulling 0\\n    -shadingModel 0\\n    -useBaseRenderer 0\\n    -useReducedRenderer 0\\n    -smallObjectCulling 0\\n    -smallObjectThreshold -1 \\n    -interactiveDisableShadows 0\\n    -interactiveBackFaceCull 0\\n    -sortTransparent 1\\n    -controllers 1\\n    -nurbsCurves 1\\n    -nurbsSurfaces 1\\n    -polymeshes 1\\n    -subdivSurfaces 1\\n    -planes 1\\n    -lights 1\\n    -cameras 1\\n    -controlVertices 1\\n    -hulls 1\\n    -grid 1\\n    -imagePlane 1\\n    -joints 1\\n    -ikHandles 1\\n    -deformers 1\\n    -dynamics 1\\n    -particleInstancers 1\\n    -fluids 1\\n    -hairSystems 1\\n    -follicles 1\\n    -nCloths 1\\n    -nParticles 1\\n    -nRigids 1\\n    -dynamicConstraints 1\\n    -locators 1\\n    -manipulators 1\\n    -pluginShapes 1\\n    -dimensions 1\\n    -handles 1\\n    -pivots 1\\n    -textures 1\\n    -strokes 1\\n    -motionTrails 1\\n    -clipGhosts 1\\n    -greasePencils 1\\n    -shadows 0\\n    -captureSequenceNumber -1\\n    -width 1261\\n    -height 708\\n    -sceneRenderFilter 0\\n    $editorName;\\nmodelEditor -e -viewSelected 0 $editorName;\\nmodelEditor -e \\n    -pluginObjects \\\"gpuCacheDisplayFilter\\\" 1 \\n    $editorName\"\n"
		+ "\t\t\t\t$configName;\n\n            setNamedPanelLayout (localizedPanelLabel(\"Current Layout\"));\n        }\n\n        panelHistory -e -clear mainPanelHistory;\n        sceneUIReplacement -clear;\n\t}\n\n\ngrid -spacing 5 -size 12 -divisions 5 -displayAxes yes -displayGridLines yes -displayDivisionLines yes -displayPerspectiveLabels no -displayOrthographicLabels no -displayAxesBold yes -perspectiveLabelPosition axis -orthographicLabelPosition edge;\nviewManip -drawCompass 0 -compassAngle 0 -frontParameters \"\" -homeParameters \"\" -selectionLockParameters \"\";\n}\n");
	setAttr ".st" 3;
createNode script -n "sceneConfigurationScriptNode";
	rename -uid "32E3B5E5-43ED-B89B-AD4D-44BFEF997FB1";
	setAttr ".b" -type "string" "playbackOptions -min 1 -max 120 -ast 1 -aet 200 ";
	setAttr ".st" 6;
createNode ikRPsolver -n "ikRPsolver";
	rename -uid "BC81278B-4737-E341-79E6-87A40EF7D9E0";
createNode unitConversion -n "unitConversion1";
	rename -uid "EE64BD82-40A8-D536-ECEB-A1869864EEDC";
	setAttr ".cf" 57.295779513082323;
createNode script -n "MetadataTemplate";
	rename -uid "2350CCAE-4E0E-17A4-E0CA-B9841B4A0DE0";
	addAttr -s false -ci true -m -sn "_inputTemplate" -ln "_inputTemplate" -at "message";
	addAttr -s false -ci true -m -sn "_extendBehaviour" -ln "_extendBehaviour" -at "message";
	setAttr ".ihi" 0;
	setAttr ".nds" 1;
	setAttr ".b" -type "string" (
		"import maya.cmds as cmds\n_METADATA_TEMPLATE_ = cmds.ls(sl=True)\nif not _METADATA_TEMPLATE_:\n    raise ValueError(\"This is not MetadataTemplate\")\n_METADATA_TEMPLATE_ = _METADATA_TEMPLATE_[0].rpartition(\":\")[0] + \":MetadataTemplate\"\n#ik_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[0]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#ikPole_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[1]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#qdrpAuxIk_00_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[3]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, t=cmds.xform(template, t=True, ws=True, q=True))\ndel template, this\n#qdrpUpIk_02_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[4]\")[0]\n"
		+ "this = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.setAttr( this + \".t\", *cmds.getAttr( template + \".t\" )[0] )\ndel template, this\n#qdrpUpIk_01_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[5]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.setAttr( this + \".t\", *cmds.getAttr( template + \".t\" )[0] )\ndel template, this\n#qdrpDwIk_01_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[6]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.setAttr( this + \".t\", *cmds.getAttr( template + \".t\" )[0] )\ndel template, this\n#qdrpAuxIk_01_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[7]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.setAttr( this + \".tx\", cmds.getAttr( template + \".tx\") + (cmds.getAttr( template + \".factor\" )/2.0) )\ndel template, this\n#qdrpAuxIk_02_jnt\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[8]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\n"
		+ "cmds.setAttr( this + \".tx\", cmds.getAttr( template + \".tx\") + (cmds.getAttr( template + \".factor\" )/2.0) )\ndel template, this\n#ik_01_rmv\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[9]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ndifference = cmds.getAttr( template + \".rx\" ) - cmds.getAttr( template + \".difference\" )\ncmds.setAttr( this + \".value[0].value_Position\", cmds.getAttr( this + \".inputValue\") )\ncmds.setAttr( this + \".value[0].value_FloatValue\", cmds.getAttr( template + \".rx\" ) + difference)\ndel difference\ndel template, this\n#ik_01_off\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[2]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_00_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[10]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\n"
		+ "del template, this\n#Fk_01_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[11]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_02_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[12]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this\n#Fk_03_root\ntemplate = cmds.listConnections(_METADATA_TEMPLATE_ + \"._inputTemplate[13]\")[0]\nthis = cmds.listConnections(template + \"._relatedTo\")[0]\ncmds.xform(this, ws=True, m=cmds.xform(template, m=True, ws=True, q=True))\ndel template, this");
	setAttr -l on ".stp" 1;
	setAttr -s 14 "._inputTemplate";
createNode remapValue -n "ik_01_rmv";
	rename -uid "6165EBDE-410B-7C9C-FF6B-6F898412BFB5";
	setAttr -s 2 ".vl[0:1]"  -69.71665955 -26.55360794 1 0 0 1;
	setAttr -s 2 ".cl";
	setAttr ".cl[0].clp" 0;
	setAttr ".cl[0].clc" -type "float3" 0 0 0 ;
	setAttr ".cl[0].cli" 1;
	setAttr ".cl[1].clp" 1;
	setAttr ".cl[1].clc" -type "float3" 1 1 1 ;
	setAttr ".cl[1].cli" 1;
createNode unitConversion -n "unitConversion2";
	rename -uid "7D34B7F3-4F79-CCDC-9BDB-CAB148E53258";
	setAttr ".cf" 0.017453292519943295;
createNode reverse -n "LegConfig_00_rev";
	rename -uid "6E2EDFAA-41BB-FD66-C790-898425FDAD55";
createNode controller -n "Leg:Fk_01_tag";
	rename -uid "5804889C-4D0A-C4C3-C51D-9D820AFC6EB2";
createNode controller -n "Leg:Fk_02_tag";
	rename -uid "45BE30C6-4A4E-8CB7-51CF-B283F9C51E2A";
createNode controller -n "Leg:Fk_00_tag";
	rename -uid "41DA4698-40C4-C90E-AD4B-A684841AF2D3";
createNode controller -n "Leg:Fk_03_tag";
	rename -uid "B6B21492-4D9B-DE1D-C35C-2187B32F4A43";
createNode controller -n "LegConfig_00_tag";
	rename -uid "127209FE-450C-A73B-CDBB-1CA6510EEFC4";
	setAttr -s 3 ".child";
createNode controller -n "ik_00_tag";
	rename -uid "E7FA1354-478A-CCDA-30BA-9880A417A9A6";
	setAttr -s 2 ".child";
createNode controller -n "ik_01_tag";
	rename -uid "247692AF-4F0F-968A-71D1-35AC15EC374C";
createNode controller -n "ikPole_00_tag";
	rename -uid "EC21186D-4B65-BC5F-8D4E-7183E648DCD4";
createNode reference -n "FootRN";
	rename -uid "EEBA26EF-43AD-F8F8-B201-3B8B25C905EA";
	setAttr -s 15 ".phl";
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
	setAttr ".ed" -type "dataReferenceEdits" 
		"FootRN"
		"FootRN" 0
		"FootRN" 33
		0 "|Foot:Foot_00_jnt" "|Leg:qdrp_00_jnt|Leg:qdrp_01_jnt|Leg:qdrp_02_jnt|Leg:qdrp_03_jnt" 
		"-s -r "
		0 "|Foot:FootFk_00_mstc" "|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr|Leg:Fk_03_root|Leg:Fk_03_ctr" 
		"-s -r "
		0 "|Foot:FootRoll_00_root" "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr" 
		"-s -r "
		2 "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root" "translate" 
		" -type \"double3\" 0 -0.99971819853501964 5.9791600945824343e-05"
		2 "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root" "scale" 
		" -type \"double3\" 1 1.00000000000000044 0.99999999999999967"
		2 "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:FootRollCtr_00_root|Foot:FootRoll_00_ctr" 
		"rotate" " -type \"double3\" 0 0 0"
		2 "|Leg:qdrp_00_jnt|Leg:qdrp_01_jnt|Leg:qdrp_02_jnt|Leg:qdrp_03_jnt|Foot:Foot_00_jnt" 
		"translate" " -type \"double3\" -9.4045956619992488e-05 0.00022328300238100285 0"
		
		2 "|Leg:qdrp_00_jnt|Leg:qdrp_01_jnt|Leg:qdrp_02_jnt|Leg:qdrp_03_jnt|Foot:Foot_00_jnt" 
		"jointOrient" " -type \"double3\" -63.44179323886785227 89.99999999991970867 0"
		2 "|Leg:qdrp_00_jnt|Leg:qdrp_01_jnt|Leg:qdrp_02_jnt|Leg:qdrp_03_jnt|Foot:Foot_00_jnt" 
		"segmentScaleCompensate" " 1"
		2 "|Foot:Ball_00_root|Foot:Ball_00_ctr" "rotate" " -type \"double3\" 0 0 0"
		
		2 "|Foot:Tpl_00_root" "visibility" " 0"
		2 "|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr|Leg:Fk_03_root|Leg:Fk_03_ctr|Foot:FootFk_00_mstc" 
		"translate" " -type \"double3\" 0 0 0"
		2 "|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr|Leg:Fk_03_root|Leg:Fk_03_ctr|Foot:FootFk_00_mstc" 
		"rotate" " -type \"double3\" 0 89.99999999998740918 0"
		2 "|Leg:Fk_00_root|Leg:Fk_00_ctr|Leg:Fk_01_root|Leg:Fk_01_ctr|Leg:Fk_02_root|Leg:Fk_02_ctr|Leg:Fk_03_root|Leg:Fk_03_ctr|Foot:FootFk_00_mstc" 
		"scale" " -type \"double3\" 0.99999999999999978 1 1"
		2 "|Foot:Config_00_root" "visibility" " 0"
		3 "|Foot:Config_00_root|Foot:Config_00_ctr.instObjGroups" "Foot:ControlsSet.dagSetMembers" 
		"-na"
		3 "Foot:BankHeel_00_tag.parent" "Foot:Config_00_tag.children[0]" ""
		5 4 "FootRN" "|Leg:qdrp_00_jnt|Leg:qdrp_01_jnt|Leg:qdrp_02_jnt|Leg:qdrp_03_jnt|Foot:Foot_00_jnt.inverseScale" 
		"FootRN.placeHolderList[1]" ""
		5 3 "FootRN" "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:FootIk_00_mstc.parentMatrix" 
		"FootRN.placeHolderList[2]" ""
		5 3 "FootRN" "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:FootIk_00_mstc.translate" 
		"FootRN.placeHolderList[3]" ""
		5 3 "FootRN" "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:FootIk_00_mstc.rotatePivot" 
		"FootRN.placeHolderList[4]" ""
		5 3 "FootRN" "|Leg:ik_00_grp|Leg:ik_00_root|Leg:ik_00_ctr|Foot:FootRoll_00_root|Foot:BankIn_00_footroll|Foot:BankExt_00_footroll|Foot:BankHeel_00_footroll|Foot:BankHeel_00_root|Foot:BankHeel_00_ctr|Foot:BallMain_00_root|Foot:BallMain_00_ctr|Foot:BankToe_00_footroll|Foot:BankToe_00_root|Foot:BankToe_00_ctr|Foot:BankBall_00_footroll|Foot:BallRoll_00_root|Foot:BallRoll_00_ctr|Foot:FootIk_00_mstc.rotatePivotTranslate" 
		"FootRN.placeHolderList[5]" ""
		5 4 "FootRN" "|Foot:Config_00_root|Foot:Config_00_ctr.fkik" "FootRN.placeHolderList[6]" 
		""
		5 3 "FootRN" "Foot:MetadataTemplate.message" "FootRN.placeHolderList[7]" 
		""
		5 3 "FootRN" "Foot:SkinJointsSet.message" "FootRN.placeHolderList[8]" 
		""
		5 3 "FootRN" "Foot:ControlsSet.message" "FootRN.placeHolderList[9]" 
		""
		5 3 "FootRN" "Foot:TemplateSet.message" "FootRN.placeHolderList[10]" 
		""
		5 3 "FootRN" "Foot:BankHeel_00_tag.parent" "FootRN.placeHolderList[11]" 
		"Foot:Config_00_tag.child[0]"
		5 0 "FootRN" "Foot:Config_00_tag.message" "Foot:Config_00_tag.children[0]" 
		"FootRN.placeHolderList[12]" "FootRN.placeHolderList[13]" ""
		5 3 "FootRN" "Foot:Ball_00_tag.parent" "FootRN.placeHolderList[14]" 
		""
		5 3 "FootRN" "Foot:Ball_00_tag.parent" "FootRN.placeHolderList[15]" 
		"";
lockNode -l 1 ;
createNode objectSet -n "ControlsSet";
	rename -uid "5B88DE27-4B48-88D1-B849-F0B9A1EA8AC7";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dnsm";
createNode objectSet -n "SkinJointsSet";
	rename -uid "92DB5D8A-4A53-A0CD-73F8-928588A3A550";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode objectSet -n "TemplateSet";
	rename -uid "42155615-4D34-9771-D5FC-08A889E66962";
	setAttr ".ihi" 0;
	setAttr -s 5 ".dsm";
createNode objectSet -n "Fk";
	rename -uid "0EBCAA31-4E43-DA65-59A5-1B884BFBEC16";
	setAttr ".ihi" 0;
	setAttr -s 4 ".dsm";
createNode objectSet -n "Ik";
	rename -uid "3C9F5224-46F6-5950-8E05-8F8A2D14E578";
	setAttr ".ihi" 0;
	setAttr -s 3 ".dsm";
createNode nodeGraphEditorInfo -n "MayaNodeEditorSavedTabsInfo";
	rename -uid "62732735-4A43-94C2-69B1-09B7DC780AF7";
	setAttr ".tgi[0].tn" -type "string" "Untitled_1";
	setAttr ".tgi[0].vl" -type "double2" 2913.1370310669445 816.21056448152888 ;
	setAttr ".tgi[0].vh" -type "double2" 3565.2027517484103 1135.9389219979935 ;
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
	setAttr -s 8 ".u";
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
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
connectAttr "Leg:qdrp_03_jnt.s" "FootRN.phl[1]";
connectAttr "FootRN.phl[2]" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.tg[0].tpm";
connectAttr "FootRN.phl[3]" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.tg[0].tt";
connectAttr "FootRN.phl[4]" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.tg[0].trp";
connectAttr "FootRN.phl[5]" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.tg[0].trt";
connectAttr "Leg:Config_00_ctr.fkIk" "FootRN.phl[6]";
connectAttr "FootRN.phl[7]" "MetadataTemplate._extendBehaviour[0]";
connectAttr "FootRN.phl[8]" "SkinJointsSet.dnsm" -na;
connectAttr "FootRN.phl[9]" "ControlsSet.dnsm" -na;
connectAttr "FootRN.phl[10]" "TemplateSet.dnsm" -na;
connectAttr "FootRN.phl[11]" "ik_00_tag.child[1]";
connectAttr "FootRN.phl[12]" "FootRN.phl[13]";
connectAttr "FootRN.phl[14]" "ik_01_tag.child[0]";
connectAttr "FootRN.phl[15]" "Leg:Fk_03_tag.child[0]";
connectAttr "Leg:qdrpJnt_00_prc.ctx" "Leg:qdrp_00_jnt.tx";
connectAttr "Leg:qdrpJnt_00_prc.cty" "Leg:qdrp_00_jnt.ty";
connectAttr "Leg:qdrpJnt_00_prc.ctz" "Leg:qdrp_00_jnt.tz";
connectAttr "Leg:qdrpJnt_00_prc.crx" "Leg:qdrp_00_jnt.rx";
connectAttr "Leg:qdrpJnt_00_prc.cry" "Leg:qdrp_00_jnt.ry";
connectAttr "Leg:qdrpJnt_00_prc.crz" "Leg:qdrp_00_jnt.rz";
connectAttr "Leg:qdrp_00_jnt.s" "Leg:qdrp_01_jnt.is";
connectAttr "Leg:qdrpJnt_01_prc.ctx" "Leg:qdrp_01_jnt.tx";
connectAttr "Leg:qdrpJnt_01_prc.cty" "Leg:qdrp_01_jnt.ty";
connectAttr "Leg:qdrpJnt_01_prc.ctz" "Leg:qdrp_01_jnt.tz";
connectAttr "Leg:qdrpJnt_01_prc.crx" "Leg:qdrp_01_jnt.rx";
connectAttr "Leg:qdrpJnt_01_prc.cry" "Leg:qdrp_01_jnt.ry";
connectAttr "Leg:qdrpJnt_01_prc.crz" "Leg:qdrp_01_jnt.rz";
connectAttr "Leg:qdrp_01_jnt.s" "Leg:qdrp_02_jnt.is";
connectAttr "Leg:qdrpJnt_02_prc.ctx" "Leg:qdrp_02_jnt.tx";
connectAttr "Leg:qdrpJnt_02_prc.cty" "Leg:qdrp_02_jnt.ty";
connectAttr "Leg:qdrpJnt_02_prc.ctz" "Leg:qdrp_02_jnt.tz";
connectAttr "Leg:qdrpJnt_02_prc.crx" "Leg:qdrp_02_jnt.rx";
connectAttr "Leg:qdrpJnt_02_prc.cry" "Leg:qdrp_02_jnt.ry";
connectAttr "Leg:qdrpJnt_02_prc.crz" "Leg:qdrp_02_jnt.rz";
connectAttr "Leg:qdrp_02_jnt.s" "Leg:qdrp_03_jnt.is";
connectAttr "Leg:qdrpJnt_03_prc.ctx" "Leg:qdrp_03_jnt.tx";
connectAttr "Leg:qdrpJnt_03_prc.cty" "Leg:qdrp_03_jnt.ty";
connectAttr "Leg:qdrpJnt_03_prc.ctz" "Leg:qdrp_03_jnt.tz";
connectAttr "Leg:qdrpJnt_03_prc.crx" "Leg:qdrp_03_jnt.rx";
connectAttr "Leg:qdrpJnt_03_prc.cry" "Leg:qdrp_03_jnt.ry";
connectAttr "Leg:qdrpJnt_03_prc.crz" "Leg:qdrp_03_jnt.rz";
connectAttr "Leg:qdrpJntIk_03_mstc.wm" "Leg:qdrpJnt_03_prc.tg[0].tpm";
connectAttr "Leg:Config_00_ctr.fkIk" "Leg:qdrpJnt_03_prc.tg[0].tw";
connectAttr "Leg:qdrpJntFk_03_mstc.wm" "Leg:qdrpJnt_03_prc.tg[1].tpm";
connectAttr "LegConfig_00_rev.ox" "Leg:qdrpJnt_03_prc.tg[1].tw";
connectAttr "Leg:qdrp_03_jnt.pim" "Leg:qdrpJnt_03_prc.cpim";
connectAttr "Leg:qdrpJntIk_02_mstc.wm" "Leg:qdrpJnt_02_prc.tg[0].tpm";
connectAttr "Leg:Config_00_ctr.fkIk" "Leg:qdrpJnt_02_prc.tg[0].tw";
connectAttr "Leg:qdrpJntFk_02_mstc.wm" "Leg:qdrpJnt_02_prc.tg[1].tpm";
connectAttr "LegConfig_00_rev.ox" "Leg:qdrpJnt_02_prc.tg[1].tw";
connectAttr "Leg:qdrp_02_jnt.pim" "Leg:qdrpJnt_02_prc.cpim";
connectAttr "Leg:qdrpJntIk_01_mstc.wm" "Leg:qdrpJnt_01_prc.tg[0].tpm";
connectAttr "Leg:Config_00_ctr.fkIk" "Leg:qdrpJnt_01_prc.tg[0].tw";
connectAttr "Leg:qdrpJntFk_01_mstc.wm" "Leg:qdrpJnt_01_prc.tg[1].tpm";
connectAttr "LegConfig_00_rev.ox" "Leg:qdrpJnt_01_prc.tg[1].tw";
connectAttr "Leg:qdrp_01_jnt.pim" "Leg:qdrpJnt_01_prc.cpim";
connectAttr "Leg:qdrpJntIk_00_mstc.wm" "Leg:qdrpJnt_00_prc.tg[0].tpm";
connectAttr "Leg:Config_00_ctr.fkIk" "Leg:qdrpJnt_00_prc.tg[0].tw";
connectAttr "Leg:qdrpJntFk_00_mstc.wm" "Leg:qdrpJnt_00_prc.tg[1].tpm";
connectAttr "LegConfig_00_rev.ox" "Leg:qdrpJnt_00_prc.tg[1].tw";
connectAttr "Leg:qdrp_00_jnt.pim" "Leg:qdrpJnt_00_prc.cpim";
connectAttr "Leg:qdrpAuxIk_00_jnt.msg" "Leg:qdrpAuxIkTpl_00_jnt._relatedTo";
connectAttr "Leg:qdrpTpl_00_loc.tx" "Leg:qdrpAuxIkTpl_01_jnt.tx" -l on;
connectAttr "Leg:ikTpl_00_root.tx" "Leg:qdrpAuxIkTpl_01_jnt.factor" -l on;
connectAttr "Leg:qdrpAuxIk_01_jnt.msg" "Leg:qdrpAuxIkTpl_01_jnt._relatedTo";
connectAttr "Leg:Fk_00_root.msg" "Leg:FkTpl_00_root._relatedTo";
connectAttr "Leg:qdrpTpl_01_loc.tx" "Leg:qdrpAuxIkTpl_02_jnt.tx" -l on;
connectAttr "Leg:ikTpl_00_root.tx" "Leg:qdrpAuxIkTpl_02_jnt.factor" -l on;
connectAttr "Leg:qdrpAuxIk_02_jnt.msg" "Leg:qdrpAuxIkTpl_02_jnt._relatedTo";
connectAttr "Leg:Fk_01_root.msg" "Leg:FkTpl_01_root._relatedTo";
connectAttr "Leg:ikPole_00_root.msg" "Leg:ikPoleTpl_00_root._relatedTo";
connectAttr "Leg:Fk_02_root.msg" "Leg:FkTpl_02_root._relatedTo";
connectAttr "Leg:ik_01_off.msg" "Leg:ikTpl_01_off._relatedTo";
connectAttr "Leg:ikTpl_01_off_aimConstraint1.crx" "Leg:ikTpl_01_off.rx" -l on;
connectAttr "Leg:ikTpl_01_off_aimConstraint1.cry" "Leg:ikTpl_01_off.ry" -l on;
connectAttr "Leg:ikTpl_01_off_aimConstraint1.crz" "Leg:ikTpl_01_off.rz" -l on;
connectAttr "Leg:ikTpl_01_off.pim" "Leg:ikTpl_01_off_aimConstraint1.cpim";
connectAttr "Leg:ikTpl_01_off.t" "Leg:ikTpl_01_off_aimConstraint1.ct";
connectAttr "Leg:ikTpl_01_off.rp" "Leg:ikTpl_01_off_aimConstraint1.crp";
connectAttr "Leg:ikTpl_01_off.rpt" "Leg:ikTpl_01_off_aimConstraint1.crt";
connectAttr "Leg:ikTpl_01_off.ro" "Leg:ikTpl_01_off_aimConstraint1.cro";
connectAttr "Leg:ikTpl_01_rmv.t" "Leg:ikTpl_01_off_aimConstraint1.tg[0].tt";
connectAttr "Leg:ikTpl_01_rmv.rp" "Leg:ikTpl_01_off_aimConstraint1.tg[0].trp";
connectAttr "Leg:ikTpl_01_rmv.rpt" "Leg:ikTpl_01_off_aimConstraint1.tg[0].trt";
connectAttr "Leg:ikTpl_01_rmv.pm" "Leg:ikTpl_01_off_aimConstraint1.tg[0].tpm";
connectAttr "Leg:ikTpl_01_off_aimConstraint1.w0" "Leg:ikTpl_01_off_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPoleTpl_00_root.wm" "Leg:ikTpl_01_off_aimConstraint1.wum";
connectAttr "Leg:ik_00_root.msg" "Leg:ikTpl_00_root._relatedTo";
connectAttr "Leg:ikTpl_01_dkUA_aimConstraint1.cry" "Leg:ikTpl_01_rmv.ry" -l on;
connectAttr "Leg:ikTpl_01_dkUA_aimConstraint1.crz" "Leg:ikTpl_01_rmv.rz" -l on;
connectAttr "Leg:ikTpl_01_dkUA_aimConstraint1.crx" "Leg:ikTpl_01_rmv.rx" -l on;
connectAttr "ik_01_rmv.msg" "Leg:ikTpl_01_rmv._relatedTo";
connectAttr "Leg:ik_01_root.rx" "Leg:ikTpl_01_rmv.difference" -l on;
connectAttr "Leg:ikTpl_01_rmv.pim" "Leg:ikTpl_01_dkUA_aimConstraint1.cpim";
connectAttr "Leg:ikTpl_01_rmv.t" "Leg:ikTpl_01_dkUA_aimConstraint1.ct";
connectAttr "Leg:ikTpl_01_rmv.rp" "Leg:ikTpl_01_dkUA_aimConstraint1.crp";
connectAttr "Leg:ikTpl_01_rmv.rpt" "Leg:ikTpl_01_dkUA_aimConstraint1.crt";
connectAttr "Leg:ikTpl_01_rmv.ro" "Leg:ikTpl_01_dkUA_aimConstraint1.cro";
connectAttr "Leg:ikTpl_01_off.t" "Leg:ikTpl_01_dkUA_aimConstraint1.tg[0].tt";
connectAttr "Leg:ikTpl_01_off.rp" "Leg:ikTpl_01_dkUA_aimConstraint1.tg[0].trp";
connectAttr "Leg:ikTpl_01_off.rpt" "Leg:ikTpl_01_dkUA_aimConstraint1.tg[0].trt";
connectAttr "Leg:ikTpl_01_off.pm" "Leg:ikTpl_01_dkUA_aimConstraint1.tg[0].tpm";
connectAttr "Leg:ikTpl_01_dkUA_aimConstraint1.w0" "Leg:ikTpl_01_dkUA_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPoleTpl_00_root.wm" "Leg:ikTpl_01_dkUA_aimConstraint1.wum";
connectAttr "Leg:Fk_03_root.msg" "Leg:FkTpl_03_root._relatedTo";
connectAttr "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.cry" "Leg:qdrpDwIkTplJnt_01_grp.ry"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.crx" "Leg:qdrpDwIkTplJnt_01_grp.rx"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.crz" "Leg:qdrpDwIkTplJnt_01_grp.rz"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp.pim" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.cpim"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp.t" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.ct"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp.rp" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.crp"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp.rpt" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.crt"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp.ro" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.cro"
		;
connectAttr "Leg:ikTpl_01_off.t" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.tg[0].tt"
		;
connectAttr "Leg:ikTpl_01_off.rp" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.tg[0].trp"
		;
connectAttr "Leg:ikTpl_01_off.rpt" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.tg[0].trt"
		;
connectAttr "Leg:ikTpl_01_off.pm" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.w0" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPoleTpl_00_root.wm" "Leg:qdrpDwIkTplJnt_01_grp_aimConstraint1.wum"
		;
connectAttr "Leg:qdrpDwIkTplJnt_01_pnc.ct" "Leg:qdrpDwIkTpl_01_jnt.t";
connectAttr "Leg:qdrpDwIk_01_tr.msg" "Leg:qdrpDwIkTpl_01_jnt._relatedTo";
connectAttr "Leg:qdrpTpl_01_loc.wm" "Leg:qdrpDwIkTplJnt_01_pnc.tg[0].tpm";
connectAttr "Leg:qdrpDwIkTpl_01_jnt.pim" "Leg:qdrpDwIkTplJnt_01_pnc.cpim";
connectAttr "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.crx" "Leg:qdrpUpIkTplJnt_01_grp.rx"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.cry" "Leg:qdrpUpIkTplJnt_01_grp.ry"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.crz" "Leg:qdrpUpIkTplJnt_01_grp.rz"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp.pim" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.cpim"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp.t" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.ct"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp.rp" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.crp"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp.rpt" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.crt"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp.ro" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.cro"
		;
connectAttr "Leg:qdrpTpl_00_loc.t" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.tg[0].tt"
		;
connectAttr "Leg:qdrpTpl_00_loc.rp" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.tg[0].trp"
		;
connectAttr "Leg:qdrpTpl_00_loc.rpt" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.tg[0].trt"
		;
connectAttr "Leg:qdrpTpl_00_loc.pm" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.w0" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.wm" "Leg:qdrpUpIkTplJnt_01_grp_aimConstraint1.wum"
		;
connectAttr "Leg:qdrpUpIk_01_jnt.msg" "Leg:qdrpUpIkTpl_01_jnt._relatedTo";
connectAttr "Leg:qdrpUpIkTplJnt_01_pnc.ct" "Leg:qdrpUpIkTpl_01_jnt.t";
connectAttr "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.crx" "Leg:qdrpUpIkTpl_01_jnt.rx"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.cry" "Leg:qdrpUpIkTpl_01_jnt.ry"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.crz" "Leg:qdrpUpIkTpl_01_jnt.rz"
		;
connectAttr "Leg:qdrpTpl_00_loc.wm" "Leg:qdrpUpIkTplJnt_01_pnc.tg[0].tpm";
connectAttr "Leg:qdrpUpIkTpl_01_jnt.pim" "Leg:qdrpUpIkTplJnt_01_pnc.cpim";
connectAttr "Leg:qdrpUpIkTpl_01_jnt.pim" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.cpim"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt.t" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.ct"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt.rp" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.crp"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt.rpt" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.crt"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt.ro" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.cro"
		;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.t" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.tg[0].tt"
		;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.rp" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.tg[0].trp"
		;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.rpt" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.tg[0].trt"
		;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.pm" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.w0" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPoleTpl_00_root.wm" "Leg:qdrpUpIkTpl_01_jnt_aimConstraint1.wum"
		;
connectAttr "Leg:qdrpUpIk_02_jnt.msg" "Leg:qdrpUpIkTpl_02_jnt._relatedTo";
connectAttr "Leg:qdrpUpIkTplJnt_02_pnc.ct" "Leg:qdrpUpIkTpl_02_jnt.t";
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.wm" "Leg:qdrpUpIkTplJnt_02_pnc.tg[0].tpm";
connectAttr "Leg:qdrpUpIkTpl_02_jnt.pim" "Leg:qdrpUpIkTplJnt_02_pnc.cpim";
connectAttr "Leg:qdrpAuxIk_00_jnt.s" "Leg:qdrpAuxIk_01_jnt.is";
connectAttr "Leg:qdrpAuxIk_01_jnt.s" "Leg:qdrpAuxIk_02_jnt.is";
connectAttr "Leg:qdrpDwIk_00_tr_aimConstraint1.crx" "Leg:qdrpDwIk_00_tr.rx";
connectAttr "Leg:qdrpDwIk_00_tr_aimConstraint1.cry" "Leg:qdrpDwIk_00_tr.ry";
connectAttr "Leg:qdrpDwIk_00_tr_aimConstraint1.crz" "Leg:qdrpDwIk_00_tr.rz";
connectAttr "Leg:qdrpUpIk_00_jnt.s" "Leg:qdrpUpIk_01_jnt.is";
connectAttr "Leg:qdrpUpIk_01_jnt.s" "Leg:qdrpUpIk_02_jnt.is";
connectAttr "Leg:qdrpUpIk_02_jnt.s" "Leg:qdrpJntIk_00_mstc.is";
connectAttr "Leg:qdrpUpIk_02_jnt.tx" "Leg:effector3.tx";
connectAttr "Leg:qdrpUpIk_02_jnt.ty" "Leg:effector3.ty";
connectAttr "Leg:qdrpUpIk_02_jnt.tz" "Leg:effector3.tz";
connectAttr "Leg:qdrpUpIk_02_jnt.opm" "Leg:effector3.opm";
connectAttr "Leg:qdrpUpIk_00_jnt.s" "Leg:qdrpJntIk_01_mstc.is";
connectAttr "Leg:qdrpJnt_01_mstc_pointConstraint1.ctx" "Leg:qdrpJntIk_01_mstc.tx"
		;
connectAttr "Leg:qdrpJnt_01_mstc_pointConstraint1.cty" "Leg:qdrpJntIk_01_mstc.ty"
		;
connectAttr "Leg:qdrpJnt_01_mstc_pointConstraint1.ctz" "Leg:qdrpJntIk_01_mstc.tz"
		;
connectAttr "Leg:qdrpJntIk_01_mstc.pim" "Leg:qdrpJnt_01_mstc_pointConstraint1.cpim"
		;
connectAttr "Leg:qdrpJntIk_01_mstc.rp" "Leg:qdrpJnt_01_mstc_pointConstraint1.crp"
		;
connectAttr "Leg:qdrpJntIk_01_mstc.rpt" "Leg:qdrpJnt_01_mstc_pointConstraint1.crt"
		;
connectAttr "Leg:qdrpUpIk_01_jnt.t" "Leg:qdrpJnt_01_mstc_pointConstraint1.tg[0].tt"
		;
connectAttr "Leg:qdrpUpIk_01_jnt.rp" "Leg:qdrpJnt_01_mstc_pointConstraint1.tg[0].trp"
		;
connectAttr "Leg:qdrpUpIk_01_jnt.rpt" "Leg:qdrpJnt_01_mstc_pointConstraint1.tg[0].trt"
		;
connectAttr "Leg:qdrpUpIk_01_jnt.pm" "Leg:qdrpJnt_01_mstc_pointConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpJnt_01_mstc_pointConstraint1.w0" "Leg:qdrpJnt_01_mstc_pointConstraint1.tg[0].tw"
		;
connectAttr "Leg:qdrpDwIk_00_tr.pim" "Leg:qdrpDwIk_00_tr_aimConstraint1.cpim";
connectAttr "Leg:qdrpDwIk_00_tr.t" "Leg:qdrpDwIk_00_tr_aimConstraint1.ct";
connectAttr "Leg:qdrpDwIk_00_tr.rp" "Leg:qdrpDwIk_00_tr_aimConstraint1.crp";
connectAttr "Leg:qdrpDwIk_00_tr.rpt" "Leg:qdrpDwIk_00_tr_aimConstraint1.crt";
connectAttr "Leg:qdrpDwIk_00_tr.ro" "Leg:qdrpDwIk_00_tr_aimConstraint1.cro";
connectAttr "Leg:ik_01_ctr.t" "Leg:qdrpDwIk_00_tr_aimConstraint1.tg[0].tt";
connectAttr "Leg:ik_01_ctr.rp" "Leg:qdrpDwIk_00_tr_aimConstraint1.tg[0].trp";
connectAttr "Leg:ik_01_ctr.rpt" "Leg:qdrpDwIk_00_tr_aimConstraint1.tg[0].trt";
connectAttr "Leg:ik_01_ctr.pm" "Leg:qdrpDwIk_00_tr_aimConstraint1.tg[0].tpm";
connectAttr "Leg:qdrpDwIk_00_tr_aimConstraint1.w0" "Leg:qdrpDwIk_00_tr_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPole_00_ctr.wm" "Leg:qdrpDwIk_00_tr_aimConstraint1.wum";
connectAttr "Leg:qdrpAuxIk_02_jnt.tx" "Leg:effector1.tx";
connectAttr "Leg:qdrpAuxIk_02_jnt.ty" "Leg:effector1.ty";
connectAttr "Leg:qdrpAuxIk_02_jnt.tz" "Leg:effector1.tz";
connectAttr "Leg:qdrpAuxIk_02_jnt.opm" "Leg:effector1.opm";
connectAttr "Leg:qdrpUpIk_00_jnt.msg" "Leg:qdrpUpIk_00_ikrp.hsj";
connectAttr "Leg:effector3.hp" "Leg:qdrpUpIk_00_ikrp.hee";
connectAttr "ikRPsolver.msg" "Leg:qdrpUpIk_00_ikrp.hsv";
connectAttr "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.ctx" "Leg:qdrpUpIk_00_ikrp.pvx"
		;
connectAttr "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.cty" "Leg:qdrpUpIk_00_ikrp.pvy"
		;
connectAttr "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.ctz" "Leg:qdrpUpIk_00_ikrp.pvz"
		;
connectAttr "Leg:qdrpUpIk_00_ikrp.pim" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.cpim"
		;
connectAttr "Leg:qdrpUpIk_00_jnt.pm" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.ps"
		;
connectAttr "Leg:qdrpUpIk_00_jnt.t" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.crp"
		;
connectAttr "Leg:ikPole_00_ctr.t" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "Leg:ikPole_00_ctr.rp" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "Leg:ikPole_00_ctr.rpt" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "Leg:ikPole_00_ctr.pm" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.w0" "Leg:qdrpUpIk_00_ikrp_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "Leg:ConfigRoot_00_prc.ct" "Leg:Config_00_root.t";
connectAttr "Leg:ConfigRoot_00_prc.cr" "Leg:Config_00_root.r";
connectAttr "Leg:qdrp_00_jnt.wm" "Leg:ConfigRoot_00_prc.tg[0].tpm";
connectAttr "Leg:Config_00_root.pim" "Leg:ConfigRoot_00_prc.cpim";
connectAttr "LegConfig_00_rev.ox" "Leg:Fk_00_root.v";
connectAttr "Leg:Config_00_ctr.fkIk" "Leg:ik_00_grp.v";
connectAttr "Leg:qdrpAuxIk_00_jnt.msg" "Leg:qdrpAuxIk_00_ikrp.hsj";
connectAttr "Leg:effector1.hp" "Leg:qdrpAuxIk_00_ikrp.hee";
connectAttr "ikRPsolver.msg" "Leg:qdrpAuxIk_00_ikrp.hsv";
connectAttr "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.ctx" "Leg:qdrpAuxIk_00_ikrp.pvx"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.cty" "Leg:qdrpAuxIk_00_ikrp.pvy"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.ctz" "Leg:qdrpAuxIk_00_ikrp.pvz"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.ctx" "Leg:qdrpAuxIk_00_ikrp.tx"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.cty" "Leg:qdrpAuxIk_00_ikrp.ty"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.ctz" "Leg:qdrpAuxIk_00_ikrp.tz"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp.pim" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.cpim"
		;
connectAttr "Leg:qdrpAuxIk_00_jnt.pm" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.ps"
		;
connectAttr "Leg:qdrpAuxIk_00_jnt.t" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.crp"
		;
connectAttr "Leg:ikPole_00_ctr.t" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.tg[0].tt"
		;
connectAttr "Leg:ikPole_00_ctr.rp" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.tg[0].trp"
		;
connectAttr "Leg:ikPole_00_ctr.rpt" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.tg[0].trt"
		;
connectAttr "Leg:ikPole_00_ctr.pm" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.tg[0].tpm"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.w0" "Leg:qdrpAuxIk_00_ikrp_poleVectorConstraint1.tg[0].tw"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp.pim" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.cpim"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp.rp" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.crp"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp.rpt" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.crt"
		;
connectAttr "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.w0" "Leg:qdrpAuxIk_00_ikrp_pointConstraint1.tg[0].tw"
		;
connectAttr "Leg:ik_01_root_aimConstraint1.crx" "Leg:ik_01_root.rx";
connectAttr "Leg:ik_01_root_aimConstraint1.cry" "Leg:ik_01_root.ry";
connectAttr "Leg:ik_01_root_aimConstraint1.crz" "Leg:ik_01_root.rz";
connectAttr "Leg:ik_01_root.pim" "Leg:ik_01_root_aimConstraint1.cpim";
connectAttr "Leg:ik_01_root.t" "Leg:ik_01_root_aimConstraint1.ct";
connectAttr "Leg:ik_01_root.rp" "Leg:ik_01_root_aimConstraint1.crp";
connectAttr "Leg:ik_01_root.rpt" "Leg:ik_01_root_aimConstraint1.crt";
connectAttr "Leg:ik_01_root.ro" "Leg:ik_01_root_aimConstraint1.cro";
connectAttr "Leg:qdrpAuxIk_00_jnt.t" "Leg:ik_01_root_aimConstraint1.tg[0].tt";
connectAttr "Leg:qdrpAuxIk_00_jnt.rp" "Leg:ik_01_root_aimConstraint1.tg[0].trp";
connectAttr "Leg:qdrpAuxIk_00_jnt.rpt" "Leg:ik_01_root_aimConstraint1.tg[0].trt"
		;
connectAttr "Leg:qdrpAuxIk_00_jnt.pm" "Leg:ik_01_root_aimConstraint1.tg[0].tpm";
connectAttr "Leg:ik_01_root_aimConstraint1.w0" "Leg:ik_01_root_aimConstraint1.tg[0].tw"
		;
connectAttr "Leg:ikPole_00_ctr.wm" "Leg:ik_01_root_aimConstraint1.wum";
connectAttr "unitConversion2.o" "Leg:ik_01_root_aimConstraint1.ox";
relationship "link" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "link" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialShadingGroup.message" ":defaultLightSet.message";
relationship "shadowLink" ":lightLinker1" ":initialParticleSE.message" ":defaultLightSet.message";
connectAttr "layerManager.dli[0]" "defaultLayer.id";
connectAttr "renderLayerManager.rlmi[0]" "defaultRenderLayer.rlid";
connectAttr "Leg:qdrpAuxIk_01_jnt.rz" "unitConversion1.i";
connectAttr "Leg:ikTpl_00_root.msg" "MetadataTemplate._inputTemplate[0]";
connectAttr "Leg:ikPoleTpl_00_root.msg" "MetadataTemplate._inputTemplate[1]";
connectAttr "Leg:ikTpl_01_off.msg" "MetadataTemplate._inputTemplate[2]";
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.msg" "MetadataTemplate._inputTemplate[3]";
connectAttr "Leg:qdrpUpIkTpl_02_jnt.msg" "MetadataTemplate._inputTemplate[4]";
connectAttr "Leg:qdrpUpIkTpl_01_jnt.msg" "MetadataTemplate._inputTemplate[5]";
connectAttr "Leg:qdrpDwIkTpl_01_jnt.msg" "MetadataTemplate._inputTemplate[6]";
connectAttr "Leg:qdrpAuxIkTpl_01_jnt.msg" "MetadataTemplate._inputTemplate[7]";
connectAttr "Leg:qdrpAuxIkTpl_02_jnt.msg" "MetadataTemplate._inputTemplate[8]";
connectAttr "Leg:ikTpl_01_rmv.msg" "MetadataTemplate._inputTemplate[9]";
connectAttr "Leg:FkTpl_00_root.msg" "MetadataTemplate._inputTemplate[10]";
connectAttr "Leg:FkTpl_01_root.msg" "MetadataTemplate._inputTemplate[11]";
connectAttr "Leg:FkTpl_02_root.msg" "MetadataTemplate._inputTemplate[12]";
connectAttr "Leg:FkTpl_03_root.msg" "MetadataTemplate._inputTemplate[13]";
connectAttr "unitConversion1.o" "ik_01_rmv.i";
connectAttr "ik_01_rmv.ov" "unitConversion2.i";
connectAttr "Leg:Config_00_ctr.fkIk" "LegConfig_00_rev.ix";
connectAttr "Leg:Fk_01_ctr.msg" "Leg:Fk_01_tag.act";
connectAttr "Leg:Fk_02_tag.pare" "Leg:Fk_01_tag.child[0]";
connectAttr "Leg:Fk_02_ctr.msg" "Leg:Fk_02_tag.act";
connectAttr "Leg:Fk_03_tag.pare" "Leg:Fk_02_tag.child[0]";
connectAttr "Leg:Fk_00_ctr.msg" "Leg:Fk_00_tag.act";
connectAttr "Leg:Fk_01_tag.pare" "Leg:Fk_00_tag.child[0]";
connectAttr "Leg:Fk_03_ctr.msg" "Leg:Fk_03_tag.act";
connectAttr "Leg:Config_00_ctr.msg" "LegConfig_00_tag.act";
connectAttr "Leg:Fk_00_tag.pare" "LegConfig_00_tag.child[0]";
connectAttr "ik_00_tag.pare" "LegConfig_00_tag.child[1]";
connectAttr "ikPole_00_tag.pare" "LegConfig_00_tag.child[2]";
connectAttr "Leg:ik_00_ctr.msg" "ik_00_tag.act";
connectAttr "ik_01_tag.pare" "ik_00_tag.child[0]";
connectAttr "Leg:ik_01_ctr.msg" "ik_01_tag.act";
connectAttr "Leg:ikPole_00_ctr.msg" "ikPole_00_tag.act";
connectAttr "ikPole_00_tag.msg" "ikPole_00_tag.child[0]";
connectAttr "Leg:Config_00_ctr.iog" "ControlsSet.dsm" -na;
connectAttr "Fk.msg" "ControlsSet.dnsm" -na;
connectAttr "Ik.msg" "ControlsSet.dnsm" -na;
connectAttr "Leg:qdrp_00_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "Leg:qdrp_01_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "Leg:qdrp_02_jnt.iog" "SkinJointsSet.dsm" -na;
connectAttr "Leg:qdrpAuxIkTpl_00_jnt.iog" "TemplateSet.dsm" -na;
connectAttr "Leg:qdrpTpl_00_loc.iog" "TemplateSet.dsm" -na;
connectAttr "Leg:ikPoleTpl_00_root.iog" "TemplateSet.dsm" -na;
connectAttr "Leg:qdrpTpl_01_loc.iog" "TemplateSet.dsm" -na;
connectAttr "Leg:ikTpl_00_root.iog" "TemplateSet.dsm" -na;
connectAttr "Leg:Fk_00_ctr.iog" "Fk.dsm" -na;
connectAttr "Leg:Fk_01_ctr.iog" "Fk.dsm" -na;
connectAttr "Leg:Fk_02_ctr.iog" "Fk.dsm" -na;
connectAttr "Leg:Fk_03_ctr.iog" "Fk.dsm" -na;
connectAttr "Leg:ik_00_ctr.iog" "Ik.dsm" -na;
connectAttr "Leg:ik_01_ctr.iog" "Ik.dsm" -na;
connectAttr "Leg:ikPole_00_ctr.iog" "Ik.dsm" -na;
connectAttr "ik_01_rmv.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "LegConfig_00_rev.msg" ":defaultRenderUtilityList1.u" -na;
connectAttr "defaultRenderLayer.msg" ":defaultRenderingList1.r" -na;
connectAttr "ikRPsolver.msg" ":ikSystem.sol" -na;
// End of legQuadruped.ma
