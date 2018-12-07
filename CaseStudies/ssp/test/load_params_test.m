function tests = load_params_test
    tests = functiontests(localfunctions);
end

function test_input_slope(testCase)
    global params_layers;
    expStrat = [0 20 30 40 70; 25 25 20 15 15];
    verifyEqual(testCase, params_layers.strat, expStrat)
end

function test_input_phi(testCase)
    global params_layers;
    expPhi = 0.34906585040;
    verifyEqual(testCase, params_layers.phi, expPhi, 'RelTol', 1e-10)
end

function test_input_coh(testCase)
    global params_layers;
    expCoh = 5000;
    verifyEqual(testCase, params_layers.coh, expCoh)
end

function test_input_gam(testCase)
    global params_layers;
    expGam = 15000;
    verifyEqual(testCase, params_layers.gam, expGam)
end

function test_input_gams(testCase)
    global params_layers;
    expGams = 15000;
    verifyEqual(testCase, params_layers.gams, expGams)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers params_piez params_search params_soln;
    [params_layers, params_piez, params_search, params_soln] = load_params('ValidInput.txt');
end


