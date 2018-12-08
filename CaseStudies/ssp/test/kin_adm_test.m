function tests = kin_adm_test
    tests = functiontests(localfunctions);
end

function test_kin_adm_xDec(testCase)
    global strat params_soln;
    slip = [20 30 25 40; 25 15 15 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_xEq(testCase)
    global strat params_soln;
    slip = [20 30 30 40; 25 14 14 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_xEtrOnSlope(testCase)
    global strat params_soln;
    slip = [-10 30 35 40; 25 15 12 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_xEtrOnEdge(testCase)
    global strat params_soln;
    slip = [0 30 35 40; 25 15 14 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_xExtOnSlope(testCase)
    global strat params_soln;
    slip = [20 30 35 80; 25 15 12 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_xExtOnEdge(testCase)
    global strat params_soln;
    slip = [20 30 35 70; 25 15 14 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_inSlope(testCase)
    global strat params_soln;
    slip = [20 30 35 40; 25 25 12 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_onSlope(testCase)
    global strat;
    params_soln = struct('cncvu', 0, 'obtu', 0);
    slip = [20 30 34 38 40; 25 15 18 15 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_cncvUp(testCase)
    global strat params_soln;
    slip = [20 30 32 35 40; 25 15 15 12 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_cncvUpOff(testCase)
    global strat;
    params_soln = struct('cncvu', 0, 'obtu', 0);
    slip = [20 30 32 35 40; 25 15 15 12 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_cncvUpEq(testCase)
    global strat params_soln;
    slip = [20 30 35 40; 25 15 15 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function test_kin_adm_obtu(testCase)
    global strat;
    params_soln = struct('cncvu', 0, 'obtu', 1);
    slip = [20 30 31 40; 25 15 5 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, false)
end

function test_kin_adm_obtuOff(testCase)
    global strat;
    params_soln = struct('cncvu', 0, 'obtu', 0);
    slip = [20 30 31 40; 25 15 5 15];
    pass = kin_adm(slip, strat, params_soln);
    verifyEqual(testCase, pass, true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global strat params_soln;
    [params_layer, ~, ~, params_soln] = ...
        load_params('ValidInput.txt');
    strat = params_layer.strat;
end