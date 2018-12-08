function tests = prop_calc_test
    tests = functiontests(localfunctions);
end

function test_prop_calc_wWet(testCase)
    global params_layers params_piez;
    slip = [0 10; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.W(1), 1500000)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers params_piez;
    [params_layers, params_piez] = ...
        load_params('ValidInputPropCalc.txt');
end