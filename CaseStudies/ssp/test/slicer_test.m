function tests = slicer_test
    tests = functiontests(localfunctions);
end

function test_slicer_evnslcSize(testCase)
    global slip;
    newSlip = slicer(true, slip, 6);
    verifyEqual(testCase, length(newSlip(1,:)), 7)
end

function test_slicer_evnslcVals(testCase)
    global slip;
    newSlip = slicer(true, slip, 6);
    expSlip = [0 2 4 8 10 13 16; 10 8 6 2 3 4 5];
    verifyEqual(testCase, newSlip, expSlip)
end

function test_slicer_notEvnslcSize(testCase)
    global slip;
    newSlip = slicer(false, slip, 6);
    verifyEqual(testCase, length(newSlip(1,:)), 7)
end

function test_slicer_notEvnslcVals(testCase)
    global slip;
    newSlip = slicer(false, slip, 6);
    expSlip = [0 4 8 9 10 13 16; 10 6 2 2.5 3 4 5];
    verifyEqual(testCase, newSlip, expSlip)
end

function test_slicer_notEvnslcIndivisible(testCase)
    slip = [0 8 10; 10 2 3];
    newSlip = slicer(false, slip, 5);
    verifyEqual(testCase, length(newSlip(1,:)), 5)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global slip;
    slip = [0 8 10 16; 10 2 3 5];
end