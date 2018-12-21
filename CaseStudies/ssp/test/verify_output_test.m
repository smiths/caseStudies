function tests = verify_output_test
    tests = functiontests(localfunctions);
end

function test_verify_output_FsNegative(testCase)
    F = -1;
    verifyError(testCase, @() verify_output(F), 'verify_output:badFactorOfSafety')
end

function test_verify_output_Fs0(testCase)
    F = 0;
    verifyError(testCase, @() verify_output(F), 'verify_output:badFactorOfSafety')
end

function test_verify_output_Fs(testCase)
    F = 1;
    verify_output(F);
    verifyEqual(testCase, true, true) %Only passes if verify_output doesn't throw an exception
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
end