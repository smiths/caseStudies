function tests = genetic_alg_test
    tests = functiontests(localfunctions);
end

function test_genetic_alg_xExtMin(testCase)
    global cslip, params_search;
    verifyEqual(testCase, cslip(end) >= params_search.Xext(1), true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global cslip, params_search;
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInput.txt');
    cslip = genetic_alg(params_layers, params_piez, params_search, ...
        params_soln, params_load)
end