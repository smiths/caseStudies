function tests = load_params_test
    tests = functiontests(localfunctions)
end

function test_input_slope(testCase)
    global params_layers
    expStrat = cell(1,1);
    expStrat{1} = [0 20 30 40 70; 25 25 20 15 15]
    verifyEqual(testCase, params_layers.strat, expStrat)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers, params_piez, params_search, params_soln
    [params_layers, params_piez, params_search, params_soln] = load_params('ValidInput.txt')
end


