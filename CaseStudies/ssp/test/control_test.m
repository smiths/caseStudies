function tests = control_test
    tests = functiontests(localfunctions);
end

function test_control_Ex1Fs(testCase)
    F1_grec = 1.327; % reported values of Fs
    F1_malk = 1.238;
    F1_cheng = 1.325;
    F1_li = 1.327;

    F_ssp = dlmread('Ex1.out', ' ', [64 0 64 0]);
    rel_err_grec = abs(F1_grec - F_ssp) / F1_grec;
    rel_err_malk = abs(F1_malk - F_ssp) / F1_malk;
    rel_err_cheng = abs(F1_cheng - F_ssp) / F1_cheng;
    rel_err_li = abs(F1_li - F_ssp) / F1_li;

    rel_tol = 0.1;
    verifyEqual(testCase, rel_err_grec < rel_tol && rel_err_malk < rel_tol && ...
        rel_err_cheng < rel_tol && rel_err_li < rel_tol, true)
end

function test_control_Ex1Slip(testCase)
    data = dlmread('./dataFiles/Ex1_Greco1996.surf')'; 
    slip1_grec = data(1:2,:);
    slip1_grecVert = match_slice(slip1_grec, 10); %Reslices slip surface into 10 slices
    slip1_grecNorm = norm(slip1_grecVert);

    data = dlmread('./dataFiles/Ex1_MalkawiEtAl2001.surf')'; 
    slip1_malk = data(1:2,:);
    slip1_malkVert = match_slice(slip1_malk, 10);
    slip1_malkNorm = norm(slip1_malkVert);

    data = dlmread('./dataFiles/Ex1_ChengEtAl2007.surf')'; 
    slip1_cheng = data(1:2,:);
    slip1_chengVert = match_slice(slip1_cheng, 10);
    slip1_chengNorm = norm(slip1_chengVert);

    data = dlmread('./dataFiles/Ex1_LiEtAl2010.surf')'; 
    slip1_li = data(1:2,:);
    slip1_liVert = match_slice(slip1_li, 10);
    slip1_liNorm = norm(slip1_liVert);

    slipX_ssp = sum(dlmread('Ex1.out', ' ', [23 2 59 3]), 2);
    slipY_ssp = sum(dlmread('Ex1.out', ' ', [23 6 59 8]), 2);
    slip_ssp = [slipX_ssp'; slipY_ssp'];
    slip_sspVert = match_slice(slip_ssp, 10);

    diffNorm_grec = norm(slip1_grecVert - slip_sspVert);
    diffNorm_malk = norm(slip1_malkVert - slip_sspVert);
    diffNorm_cheng = norm(slip1_chengVert - slip_sspVert);
    diffNorm_li = norm(slip1_liVert - slip_sspVert);

    rel_err_grec = diffNorm_grec / slip1_grecNorm;
    rel_err_malk = diffNorm_malk / slip1_malkNorm;
    rel_err_cheng = diffNorm_cheng / slip1_chengNorm;
    rel_err_li = diffNorm_li / slip1_liNorm;

    rel_tol = 0.1;
    verifyEqual(testCase, rel_err_grec < rel_tol && rel_err_malk < rel_tol && ...
        rel_err_cheng < rel_tol && rel_err_li < rel_tol, true)
end

function test_control_OrigFs(testCase)
    F_orig = 0.9835; % Fs from original program

    F_ssp = dlmread('ValidInput.out', ' ', [64 0 64 0]);

    rel_err_orig = abs(F_orig - F_ssp) / F_orig;

    rel_tol = 0.01;
    verifyEqual(testCase, rel_err_orig < rel_tol, true)
end

function test_control_OrigSlip(testCase)
    slipX_orig = dlmread('./dataFiles/OrigProg.out', ' ', [23 2 59 2]);
    slipY_orig = dlmread('./dataFiles/OrigProg.out', ' ', [23 6 59 6]);
    slip_orig = [slipX_orig'; slipY_orig'];
    slip_origVert = match_slice(slip_orig, 10); %Reslices slip surface into 10 slices
    slip_origNorm = norm(slip_origVert);

    slipX_ssp = dlmread('ValidInput.out', ' ', [23 2 59 2]);
    slipY_ssp = dlmread('ValidInput.out', ' ', [23 6 59 6]);
    slip_ssp = [slipX_ssp'; slipY_ssp'];
    slip_sspVert = match_slice(slip_ssp, 10);

    diffNorm_orig = norm(slip_origVert - slip_sspVert);

    rel_err_orig = diffNorm_orig / slip_origNorm;

    rel_tol = 0.05;
    verifyEqual(testCase, rel_err_orig < rel_tol, true)
end

function test_control_OrigNormal(testCase)
    normalX_orig = dlmread('./dataFiles/OrigProg.out', ' ', [153 2 187 2]);
    normalY_orig = sum(dlmread('./dataFiles/OrigProg.out', ' ', [153 8 187 10]), 2);
    normal_orig = [normalX_orig'; normalY_orig'];
    normal_origVert = match_slice(normal_orig, 10); %Reslices slip surface into 10 slices
    normal_origNorm = norm(normal_origVert);

    normalX_orig2 = dlmread('./dataFiles/OrigProg2.out', ' ', [153 2 187 2]);
    normalY_orig2 = sum(dlmread('./dataFiles/OrigProg2.out', ' ', [153 8 187 10]), 2);
    normal_orig2 = [normalX_orig2'; normalY_orig2'];
    normal_origVert2 = match_slice(normal_orig2, 10); %Reslices slip surface into 10 slices
    normal_origNorm2 = norm(normal_origVert2);

    normalX_orig3 = dlmread('./dataFiles/OrigProg3.out', ' ', [153 2 187 2]);
    normalY_orig3 = sum(dlmread('./dataFiles/OrigProg3.out', ' ', [153 8 187 10]), 2);
    normal_orig3 = [normalX_orig3'; normalY_orig3'];
    normal_origVert3 = match_slice(normal_orig3, 10); %Reslices slip surface into 10 slices
    normal_origNorm3 = norm(normal_origVert3);

    normalX_orig4 = dlmread('./dataFiles/OrigProg4.out', ' ', [153 2 187 2]);
    normalY_orig4 = sum(dlmread('./dataFiles/OrigProg4.out', ' ', [153 8 187 10]), 2);
    normal_orig4 = [normalX_orig4'; normalY_orig4'];
    normal_origVert4 = match_slice(normal_orig4, 10); %Reslices slip surface into 10 slices
    normal_origNorm4 = norm(normal_origVert4);

    normalX_ssp = sum(dlmread('ValidInput.out', ' ', [70 2 104 2]), 2);
    normalY_ssp = sum(dlmread('ValidInput.out', ' ', [70 8 104 10]), 2);
    normal_ssp = [normalX_ssp'; normalY_ssp'];
    normal_sspVert = match_slice(normal_ssp, 10);

    diffNorm_orig = norm(normal_origVert - normal_sspVert);
    diffNorm_orig2 = norm(normal_origVert2 - normal_sspVert);
    diffNorm_orig3 = norm(normal_origVert3 - normal_sspVert);
    diffNorm_orig4 = norm(normal_origVert4 - normal_sspVert);

    rel_err_orig = diffNorm_orig / normal_origNorm;
    rel_err_orig2 = diffNorm_orig2 / normal_origNorm2;
    rel_err_orig3 = diffNorm_orig3 / normal_origNorm3;
    rel_err_orig4 = diffNorm_orig4 / normal_origNorm4;

    rel_tol = 0.15;
    verifyEqual(testCase, rel_err_orig < rel_tol || rel_err_orig2 < rel_tol || ...
        rel_err_orig3 < rel_tol || rel_err_orig4 < rel_tol, true)
end

function test_control_OrigShear(testCase)
    shearX_orig = dlmread('./dataFiles/OrigProg.out', ' ', [153 2 187 2]);
    shearY_orig = sum(dlmread('./dataFiles/OrigProg.out', ' ', [153 14 187 17]), 2);
    shear_orig = [shearX_orig'; shearY_orig'];
    shear_origVert = match_slice(shear_orig, 10); %Reslices slip surface into 10 slices
    shear_origNorm = norm(shear_origVert);

    shearX_orig2 = dlmread('./dataFiles/OrigProg2.out', ' ', [153 2 187 2]);
    shearY_orig2 = sum(dlmread('./dataFiles/OrigProg2.out', ' ', [153 14 187 17]), 2);
    shear_orig2 = [shearX_orig2'; shearY_orig2'];
    shear_origVert2 = match_slice(shear_orig2, 10); %Reslices slip surface into 10 slices
    shear_origNorm2 = norm(shear_origVert2);

    shearX_orig3 = dlmread('./dataFiles/OrigProg3.out', ' ', [153 2 187 2]);
    shearY_orig3 = sum(dlmread('./dataFiles/OrigProg3.out', ' ', [153 14 187 17]), 2);
    shear_orig3 = [shearX_orig3'; shearY_orig3'];
    shear_origVert3 = match_slice(shear_orig3, 10); %Reslices slip surface into 10 slices
    shear_origNorm3 = norm(shear_origVert3);

    shearX_orig4 = dlmread('./dataFiles/OrigProg4.out', ' ', [153 2 187 2]);
    shearY_orig4 = sum(dlmread('./dataFiles/OrigProg4.out', ' ', [153 14 187 17]), 2);
    shear_orig4 = [shearX_orig4'; shearY_orig4'];
    shear_origVert4 = match_slice(shear_orig4, 10); %Reslices slip surface into 10 slices
    shear_origNorm4 = norm(shear_origVert4);

    shearX_ssp = sum(dlmread('ValidInput.out', ' ', [70 2 104 2]), 2);
    shearY_ssp = sum(dlmread('ValidInput.out', ' ', [70 14 104 17]), 2);
    shear_ssp = [shearX_ssp'; shearY_ssp'];
    shear_sspVert = match_slice(shear_ssp, 10);

    diffNorm_orig = norm(shear_origVert - shear_sspVert);
    diffNorm_orig2 = norm(shear_origVert2 - shear_sspVert);
    diffNorm_orig3 = norm(shear_origVert3 - shear_sspVert);
    diffNorm_orig4 = norm(shear_origVert4 - shear_sspVert);

    rel_err_orig = diffNorm_orig / shear_origNorm;
    rel_err_orig2 = diffNorm_orig2 / shear_origNorm2;
    rel_err_orig3 = diffNorm_orig3 / shear_origNorm3;
    rel_err_orig4 = diffNorm_orig4 / shear_origNorm4;

    rel_tol = 0.15;
    verifyEqual(testCase, rel_err_orig < rel_tol || rel_err_orig2 < rel_tol || ...
    rel_err_orig3 < rel_tol || rel_err_orig4 < rel_tol, true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    control('Ex1.dat');
    control('ValidInput.txt');
end

function teardownOnce(testCase)
    delete 'ValidInput.out';
    delete 'ValidInput.png';
    delete 'Ex1.out';
    delete 'Ex1.png';
end