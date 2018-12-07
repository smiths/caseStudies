function tests = load_params_test
    tests = functiontests(localfunctions);
end

function test_input_slope(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_nonmotonic_layer.dat');
    verifyError(testCase, @verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'NonMonotonicLayer')
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
end


