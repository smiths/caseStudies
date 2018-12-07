function tests = genetic_alg_test
    tests = functiontests(localfunctions);
end

function test_genetic_alg_xExtMin(testCase)
    global cslip params_search;
    verifyEqual(testCase, cslip(1,end) >= params_search.Xext(1), true)
end

function test_genetic_alg_xExtMax(testCase)
    global cslip params_search;
    verifyEqual(testCase, cslip(1,end) <= params_search.Xext(2), true)
end

function test_genetic_alg_xEtrMin(testCase)
    global cslip params_search;
    verifyEqual(testCase, cslip(1,1) >= params_search.Xetr(1), true)
end

function test_genetic_alg_xEtrMax(testCase)
    global cslip params_search;
    verifyEqual(testCase, cslip(1,1) <= params_search.Xetr(2), true)
end

function test_genetic_alg_yLimMin(testCase)
    global cslip params_search;
    aboveMin = true;
    for i = 1:length(cslip(2,:))
        if cslip(2,i) < params_search.Ylim(1)
            aboveMin = false;
            break
        end
    end
    verifyEqual(testCase, aboveMin, true)
end

function test_genetic_alg_yLimMax(testCase)
    global cslip params_search;
    belowMax = true;
    for i = 1:length(cslip(2,:))
        if cslip(2,i) > params_search.Ylim(2)
            belowMax = false;
            break
        end
    end
    verifyEqual(testCase, belowMax, true)
end

function test_genetic_alg_vertices(testCase)
    global cslip;
    init_num_vertices = 4;
    num_adds = 2;
    num_vertices = (init_num_vertices * 2 ^ num_adds) - (2 ^ num_adds - 1);
    verifyEqual(testCase, length(cslip(1,:)), num_vertices)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global cslip params_search;
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('ValidInput.txt');
    cslip = genetic_alg(params_layers, params_piez, params_search, ...
        params_soln, params_load);
end