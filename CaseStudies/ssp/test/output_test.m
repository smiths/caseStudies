function tests = verify_output_test
    tests = functiontests(localfunctions);
end

function test_output_file(testCase)
    verifyEqual(testCase, exist('outputtest.out', 'file'), 2)
end

function test_output_inputXEtrMin(testCase)
    global params_search;
    xEtrMin = dlmread('outputtest.out', ' ', [13 0 14 1]);
    verifyEqual(testCase, xEtrMin, params_search.XEtr(1))
end

function test_output_inputXEtrMax(testCase)
    global params_search;
    xEtrMax = dlmread('outputtest.out', ' ', [14 0 15 1]);
    verifyEqual(testCase, xEtrMax, params_search.XEtr(2))
end

function test_output_inputXExtMin(testCase)
    global params_search;
    xExtMin = dlmread('outputtest.out', ' ', [13 1 14 2]);
    verifyEqual(testCase, xExtMin, params_search.XExt(1))
end

function test_output_inputXExtMax(testCase)
    global params_search;
    xExtMax = dlmread('outputtest.out', ' ', [14 1 15 2]);
    verifyEqual(testCase, xExtMax, params_search.XExt(2))
end

function test_output_inputYlimMin(testCase)
    global params_search;
    yLimMin = dlmread('outputtest.out', ' ', [13 2 14 3]);
    verifyEqual(testCase, yLimMin, params_search.YLim(1))
end

function test_output_inputYlimMax(testCase)
    global params_search;
    yLimMax = dlmread('outputtest.out', ' ', [14 2 15 3]);
    verifyEqual(testCase, yLimMax, params_search.YLim(2))
end

function test_output_inputFtype(testCase)
    global params_soln;
    outputText = fileread('outputtest.out');
    if params_soln.ftype
        textToSearchFor = 'constant (Spencer)';
    else
        textToSearchFor = 'half-sine (Morgenstern-Price)';
    end
    verifyEqual(testCase, isempty(strfind(outputText, textToSearchFor)), false)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_search params_soln
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInput.txt');
    cslip = [10 20 30 40 50; 25 20 10 15 20];
    F = 1;
    Nint = [20 30 40; 50 100 75];
    Tint = [20 30 40; -25 -75 -50];
    output(cslip, F, Nint, Tint, params_layers, params_piez, params_search, ...
        params_soln, params_load, 'outputtest.dat');
end

function teardownOnce(testCase)
    delete 'outputtest.out';
end