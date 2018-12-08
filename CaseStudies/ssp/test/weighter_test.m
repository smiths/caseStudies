function tests = weighter_test
    tests = functiontests(localfunctions);
end

function test_weighter_sort(testCase)
    slipsurfs = cell(3,6);
    slipsurfs{1,2} = 1.0;
    slipsurfs{2,2} = 0.8;
    slipsurfs{3,2} = 1.5;
    newslips = weighter(3, slipsurfs);
    verifyEqual(testCase, newslips{1,2} == 0.8 && newslips{2,2} == 1.0 && ...
        newslips{3,2} == 1.5, true)
end

function test_weighter_size(testCase)
    slipsurfs = cell(3,6);
    slipsurfs{1,2} = 1.0;
    slipsurfs{2,2} = 0.8;
    slipsurfs{3,2} = 1.5;
    newslips = weighter(3, slipsurfs);
    verifyEqual(testCase, length(newslips(:,2)), 3)
end

function test_weighter_first(testCase)
    global slipsurfs
    slipsurfs{1,2} = 0.8;
    slipsurfs{2,2} = 1.4;
    slipsurfs{3,2} = 1.8;
    slipsurfs{4,2} = 2.0;
    newslips = weighter(4, slipsurfs);
    verifyEqual(testCase, newslips{1,5}, 0.6)
end

function test_weighter_mid(testCase)
    global slipsurfs
    slipsurfs{1,2} = 0.8;
    slipsurfs{2,2} = 1.4;
    slipsurfs{3,2} = 1.8;
    slipsurfs{4,2} = 2.0;
    newslips = weighter(4, slipsurfs);
    verifyEqual(testCase, newslips{2,5}, 0.9)
end

function test_weighter_secondLast(testCase)
    global slipsurfs
    slipsurfs{1,2} = 0.8;
    slipsurfs{2,2} = 1.4;
    slipsurfs{3,2} = 1.8;
    slipsurfs{4,2} = 2.0;
    newslips = weighter(4, slipsurfs);
    verifyEqual(testCase, newslips{3,5}, 1.0)
end

function test_weighter_last(testCase)
    global slipsurfs
    slipsurfs{1,2} = 0.8;
    slipsurfs{2,2} = 1.4;
    slipsurfs{3,2} = 1.8;
    slipsurfs{4,2} = 2.0;
    newslips = weighter(4, slipsurfs);
    verifyEqual(testCase, newslips{4,5}, 1.0)
end

function test_weighter_NaN(testCase)
    slipsurfs = cell(3,6);
    slipsurfs{1,2} = 1.0;
    slipsurfs{2,2} = 1.0;
    slipsurfs{3,2} = 1.0;
    newslips = weighter(3, slipsurfs);
    verifyEqual(testCase, isnan(newslips{1,5}) && isnan(newslips{2,5}) && ...
    isnan(newslips{3,5}), true)
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
    global slipsurfs;
    slipsurfs = cell(4,6);
end