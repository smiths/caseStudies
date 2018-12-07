function tests = verify_params_test
    tests = functiontests(localfunctions);
end

function test_invalid_input_slopeNonMono(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_nonmotonic_layer.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:NonMonotonicLayer')
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
end


