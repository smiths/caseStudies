function tests = weighter_test
    tests = functiontests(localfunctions);
end

function test_weighter_sort(testCase)
    global slipsurfs
    slipsurfs{1, 2} = 1.0;
    slipsurfs{2, 2} = 0.8;
    slipsurfs{3, 2} = 1.5;
    newslips = weighter(3, slipsurfs);
    verifyEqual(testCase, newslips{1,2} == 0.8 && newslips{2,2} == 1.0 && ...
        newslips{3,2} == 1.5, true)
end

function test_weighter_size(testCase)
    global slipsurfs
    slipsurfs{1, 2} = 1.0;
    slipsurfs{2, 2} = 0.8;
    slipsurfs{3, 2} = 1.5;
    newslips = weighter(3, slipsurfs);
    verifyEqual(testCase, length(newslips), 3)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global slipsurfs;
    slipsurfs = cell(3, 6);
end