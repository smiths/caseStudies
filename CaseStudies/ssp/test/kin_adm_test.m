function tests = kin_adm_test
    tests = functiontests(localfunctions);
end

function test_kin_adm_xDec(testCase)
    global strat params_soln;
    slip = [20 30 25 40; 25 15 15 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global strat params_soln;
    [params_layer, ~, ~, params_soln] = ...
        load_params('ValidInput.txt');
    strat = params_layer.strat{1};
end