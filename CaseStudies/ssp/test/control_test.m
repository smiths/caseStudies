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

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    control('Ex1.dat');
end

function teardownOnce(testCase)
    % delete 'ValidInput.out';
    % delete 'Ex1.out';
end