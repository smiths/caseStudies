function tests = control_test
    tests = functiontests(localfunctions);
end

function test_control_Ex1Fs(testCase)
    F1_grec = 1.327; % reported values of Fs
    F1_malk = 1.238;
    F1_cheng = 1.325;
    F1_li = 1.327;

    F_ssp = dlmread('Ex1.out', ' ', [64 0 64 0]);
    rel_err_grec = abs(F1_grec - F_ssp) / F1_grec
    rel_err_malk = abs(F1_malk - F_ssp) / F1_malk
    rel_err_cheng = abs(F1_cheng - F_ssp) / F1_cheng
    rel_err_li = abs(F1_li - F_ssp) / F1_li

    rel_tol = 0.1;
    verifyEqual(testCase, rel_err_grec < rel_tol && rel_err_malk < rel_tol && ...
        rel_err_cheng < rel_tol && rel_err_li < rel_tol, true)
end

function test_control_Ex1Slip(testCase)
    data = dlmread('./dataFiles/Ex1_Greco1996.surf')'; 
    slip1_grec = data(1:2,:);
    slip1_grecVert = MatchSlice (slip1_grec, 10); %Reslices slip surface into 10 slices
    slip1_grecNorm = norm(slip1_grecVert);

    data = dlmread('./dataFiles/Ex1_MalkawiEtAl2001.surf')'; 
    slip1_malk = data(1:2,:);
    slip1_malkVert = MatchSlice (slip1_malk, 10);
    slip1_malkNorm = norm(slip1_malkVert);

    data = dlmread('./dataFiles/Ex1_ChengEtAl2007.surf')'; 
    slip1_cheng = data(1:2,:);
    slip1_chengVert = MatchSlice (slip1_cheng, 10);
    slip1_chengNorm = norm(slip1_chengVert);

    data = dlmread('./dataFiles/Ex1_LiEtAl2010.surf')'; 
    slip1_li = data(1:2,:);
    slip1_liVert = MatchSlice (slip1_li, 10);
    slip1_liNorm = norm(slip1_liVert);

    slipX_ssp = sum(dlmread('Ex1.out', ' ', [23 2 59 3]), 2);
    slipY_ssp = sum(dlmread('Ex1.out', ' ', [23 6 59 8]), 2);
    slip_ssp = [slipX_ssp'; slipY_ssp'];
    slip_sspVert = MatchSlice(slip_ssp, 10);

    diffNorm_grec = norm(slip1_grecVert - slip_sspVert);
    diffNorm_malk = norm(slip1_malkVert - slip_sspVert);
    diffNorm_cheng = norm(slip1_chengVert - slip_sspVert);
    diffNorm_li = norm(slip1_liVert - slip_sspVert);

    rel_err_grec = diffNorm_grec / slip1_grecNorm
    rel_err_malk = diffNorm_grec / slip1_grecNorm
    rel_err_cheng = diffNorm_grec / slip1_grecNorm
    rel_err_li = diffNorm_grec / slip1_grecNorm

    rel_tol = 0.1;
    verifyEqual(testCase, rel_err_grec < rel_tol && rel_err_malk < rel_tol && ...
        rel_err_cheng < rel_tol && rel_err_li < rel_tol, true)
end

function test_control_OrigFs(testCase)
    F_orig = 0.9835; % Fs from original program

    F_ssp = dlmread('ValidInput.out', ' ', [64 0 64 0]);

    rel_err_orig = abs(F_orig - F_ssp) / F_orig

    rel_tol = 0.1;
    verifyEqual(testCase, rel_err_orig < rel_tol, true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    control('Ex1.dat');
    control('ValidInput.txt');
end

function teardownOnce(testCase)
    % delete 'ValidInput.out';
    % delete 'Ex1.out';
end