function tests = verify_output_test
    tests = functiontests(localfunctions);
end

function test_output_file(testCase)
    verifyEqual(testCase, isfile('outputtest.out'), true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInput.txt');
    cslip = [10 20 30 40 50; 25 20 10 15 20];
    F = 1;
    Nint = [20 30 40; 50 100 75];
    Tint = [20 30 40; -25 -75 -50];
    output(cslip, F, Nint, Tint, params_layers, params_piez, params_search, ...
        params_soln, params_load, 'outputtest.dat');
end