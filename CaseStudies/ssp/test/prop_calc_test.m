function tests = prop_calc_test
    tests = functiontests(localfunctions);
end

function test_prop_calc_wWet(testCase)
    global params_layers params_piez;
    slip = [0 10; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.W(1), 1500000)
end

function test_prop_calc_wWetDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 5 0];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.W(1), 3000000)
end

function test_prop_calc_wDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.W(1), 1125000)
end

function test_prop_calc_ubWet(testCase)
    global params_layers params_piez;
    slip = [0 10; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.Ub(1), 1397542.4859, 'RelTol', 1e-12)
end

function test_prop_calc_ubDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.Ub(1), 0)
end

function test_prop_calc_utWet(testCase)
    global params_layers params_piez;
    slip = [-10 0; 5 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.Ut(1), 1414213.5624, 'RelTol', 1e-12)
end

function test_prop_calc_utDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.Ut(1), 0)
end

function test_prop_calc_hWet(testCase)
    global params_layers params_piez;
    slip = [0 10; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.H(1), 375000)
end

function test_prop_calc_hWetDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 5 0];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.H(1), 125000)
end

function test_prop_calc_hDry(testCase)
    global params_layers params_piez;
    slip = [20 30; 15 10];
    params_internalForce = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_internalForce.H(1), 0)
end

function test_prop_calc_alpha(testCase)
    global params_layers params_piez;
    slip = [20 30; 15 10];
    [~, params_angles] = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_angles.Alpha(1), -0.46364760900, 'RelTol', 1e-12)
end

function test_prop_calc_alpha(testCase)
    global params_layers params_piez;
    slip = [-10 0; 10 10];
    [~, params_angles] = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, params_angles.Beta(1), -0.78539816340, 'RelTol', 1e-12)
end

function test_prop_calc_height(testCase)
    global params_layers params_piez;
    slip = [0 10; 15 10];
    [~, ~, ~, ~, ~, h] = prop_calc(slip, params_layers, params_piez);
    verifyEqual(testCase, h(1), 7.5)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers params_piez;
    [params_layers, params_piez] = ...
        load_params('ValidInputPropCalc.txt');
end