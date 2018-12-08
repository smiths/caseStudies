function tests = morg_price_test
    tests = functiontests(localfunctions);
end

function test_morg_price_nonConvergingFs(testCase)
    global params_layers params_piez params_soln params_load;
    slip = [20 30 40; 25 10 15];
    Fs = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, Fs, 1000)
end

function test_morg_price_nonConvergingG(testCase)
    global params_layers params_piez params_soln params_load;
    slip = [20 30 40; 25 10 15];
    [~, ~, G, ~] = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, G, [])
end

function test_morg_price_nonConvergingX(testCase)
    global params_layers params_piez params_soln params_load;
    slip = [20 30 40; 25 10 15];
    [~, ~, ~, X] = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, X, [])
end

function test_morg_price_spuriousFs(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInputSpurious.txt');
    slip = [20 25 30 35 40; 25 20 15 14 15];
    Fs = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, Fs, 1000)
end

function test_morg_price_spuriousG(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInputSpurious.txt');
    slip = [20 25 30 35 40; 25 20 15 14 15];
    [~, ~, G, ~] = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, G, [])
end

function test_morg_price_spuriousX(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInputSpurious.txt');
    slip = [20 25 30 35 40; 25 20 15 14 15];
    [~, ~, ~, X] = morg_price(slip, params_layers, params_piez, params_soln, params_load);
    verifyEqual(testCase, X, [])
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers params_piez params_soln params_load;
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInput.txt');
end