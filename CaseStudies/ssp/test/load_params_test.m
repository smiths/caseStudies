function tests = load_params_test
    tests = functiontests(localfunctions);
end

function test_input_badFilename
    verifyError(testCase, @() load_params('ValidInput.out'), 'load_params:badFilename');
end

function test_input_unexpected
    verifyError(testCase, @() load_params('UnexpectedInput.txt'), 'load_params:unexpectedInput');
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

function test_input_piez(testCase)
    global params_piez;
    expPiez = [0 10.87 21.14 31.21 38.69 40 70; 22 21.28 19.68 17.17 14.56 14 14];
    verifyEqual(testCase, params_piez.piez, expPiez)
end

function test_input_gamw(testCase)
    global params_piez;
    expGamw = 9800;
    verifyEqual(testCase, params_piez.gamw, expGamw)
end

function test_input_xExtMin(testCase)
    global params_search;
    expXExtMin = 34;
    verifyEqual(testCase, params_search.Xext(1), expXExtMin)
end

function test_input_xExtMax(testCase)
    global params_search;
    expXExtMax = 53;
    verifyEqual(testCase, params_search.Xext(2), expXExtMax)
end

function test_input_xEtrMin(testCase)
    global params_search;
    expXEtrMin = 10;
    verifyEqual(testCase, params_search.Xetr(1), expXEtrMin)
end

function test_input_xEtrMax(testCase)
    global params_search;
    expXEtrMax = 24;
    verifyEqual(testCase, params_search.Xetr(2), expXEtrMax)
end

function test_input_yLimMin(testCase)
    global params_search;
    expYLimMin = 5;
    verifyEqual(testCase, params_search.Ylim(1), expYLimMin)
end

function test_input_yLimMax(testCase)
    global params_search;
    expYLimMax = 26;
    verifyEqual(testCase, params_search.Ylim(2), expYLimMax)
end

function test_input_ltor(testCase)
    global params_soln;
    expLtor = 1;
    verifyEqual(testCase, params_soln.ltor, expLtor)
end

function test_input_ftype(testCase)
    global params_soln;
    expFtype = 0;
    verifyEqual(testCase, params_soln.ftype, expFtype)
end

function test_input_evnslc(testCase)
    global params_soln;
    expEvnslc = 1;
    verifyEqual(testCase, params_soln.evnslc, expEvnslc)
end

function test_input_cncvu(testCase)
    global params_soln;
    expCncvu = 1;
    verifyEqual(testCase, params_soln.cncvu, expCncvu)
end

function test_input_obtu(testCase)
    global params_soln;
    expObtu = 1;
    verifyEqual(testCase, params_soln.obtu, expObtu)
end

function test_input_rtol(testCase)
    [~, ~, ~, params_soln] = load_params('ValidInputRtol.txt');
    expLtor = 0;
    verifyEqual(testCase, params_soln.ltor, expLtor)
end

function test_input_noWTpiez(testCase)
    [~, params_piez] = load_params('ValidInputNoWT.txt');
    expPiez = [];
    verifyEqual(testCase, params_piez.piez, expPiez)
end

function test_input_noWTgamw(testCase)
    [~, params_piez] = load_params('ValidInputNoWT.txt');
    expGamw = 0;
    verifyEqual(testCase, params_piez.gamw, expGamw)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global params_layers params_piez params_search params_soln;
    [params_layers, params_piez, params_search, params_soln] = load_params('ValidInput.txt');
end


