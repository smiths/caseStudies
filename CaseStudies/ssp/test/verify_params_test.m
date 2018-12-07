function tests = verify_params_test
    tests = functiontests(localfunctions);
end

function test_invalid_input_slopeNonMono(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_nonmotonic_layer.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:NonMonotonicLayer')
end

function test_invalid_input_slopeOnePt(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_layer_onePt.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:NotEnoughLayerVertices')
end

function test_invalid_input_slopeHighStartWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_xrange_piezstarthigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:DiffPiezStartEnd')
end

function test_invalid_input_slopeLowStartWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_xrange_piezstartlow.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:DiffPiezStartEnd')
end

function test_invalid_input_slopeHighEndWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_xrange_piezendhigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:DiffPiezStartEnd')
end

function test_invalid_input_slopeLowEndWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_xrange_piezendlow.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:DiffPiezStartEnd')
end

function test_invalid_input_slopeNonMonoWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_nonmotonic_piez.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:NonMonotonicPiez')
end

function test_invalid_input_slopeOnePtWT(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Error_piez_onePt.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:NotEnoughPiezVertices')
end

function test_invalid_input_slipxMinEtr(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMinEtr.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XEtrGuessOutOfBounds')
end

function test_invalid_input_slipxMaxEtr(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMaxEtr.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XEtrGuessOutOfBounds')
end

function test_invalid_input_slipxMinExt(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMinExt.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XExtGuessOutOfBounds')
end

function test_invalid_input_slipxMaxExt(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMaxExt.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XExtGuessOutOfBounds')
end

function test_invalid_input_slipxMinEtrHigh(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMinEtrHigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XEtrGuessOutOfBounds')
end

function test_invalid_input_slipxMaxEtrHigh(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMaxEtrHigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XEtrGuessOutOfBounds')
end

function test_invalid_input_slipxMinExtHigh(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMinExtHigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XExtGuessOutOfBounds')
end

function test_invalid_input_slipxMaxExtHigh(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_XMaxExtHigh.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:XExtGuessOutOfBounds')
end

function test_invalid_input_slipYMin(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_yMin.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:YMinGuessOutOfBounds')
end

function test_invalid_input_slipYMax(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_yMax.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:YMaxGuessOutOfBounds')
end

function test_invalid_input_cohesion0(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_coh_zero.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badCohesion')
end

function test_invalid_input_cohesionNegative(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_coh_negative.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badCohesion')
end

function test_invalid_input_angFric0(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_philow_zero.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badEffAngleFriction')
end

function test_invalid_input_angFricNegative(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_philow_negative.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badEffAngleFriction')
end

function test_invalid_input_angFric90(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_phihigh90.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badEffAngleFriction')
end

function test_invalid_input_angFric100(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_phihigh100.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badEffAngleFriction')
end

function test_invalid_input_unitWt0(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gam_zero.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badDryUnitWeight')
end

function test_invalid_input_unitWtNegative(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gam_negative.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badDryUnitWeight')
end

function test_invalid_input_unitWtSat0(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gams_zero.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badSatUnitWeight')
end

function test_invalid_input_unitWtSatNegative(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gams_negative.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badSatUnitWeight')
end

function test_invalid_input_unitWtWater0(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gamw_zero.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badWatUnitWeight')
end

function test_invalid_input_unitWtWaterNegative(testCase)
    [params_layers, params_piez, params_search, params_soln, params_load] = ...
        load_params('Constraint_gamw_negative.dat');
    verifyError(testCase, @() verify_params(params_layers, params_piez, ...
        params_search, params_soln, params_load), 'verify_params:badWatUnitWeight')
end

function setupOnce(testCase)
    addpath(genpath('dataFiles/'), '../src/');
end