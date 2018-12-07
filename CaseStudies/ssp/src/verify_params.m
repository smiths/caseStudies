function verify_params(params_layers, params_piez, params_search,...
    params_soln, params_load)

% Slope Stability Analysis Program
% Input.m
%
% 20 August 2015
% 
%  - For a description of the module interface refer to the MIS.
% (../Documentation Files/MIS_SSP.pdf)
%
%  - For a description of the module secrets and services refer to the MG.
% (../Documentation Files/MG_SSP.pdf)
%
% ---------------------
%
% Recieves data input from an input file and the keyboard environment.
%
% -------------------------------------------------------------------------

nlayer = length(params_layers); % strat extraction
strat = cell(nlayer,1);
for i = 1:nlayer
    strat{i} = params_layers(i).strat;
end

phi = params_layers.phi; % soil property extraction
coh = params_layers.coh;
gam = params_layers.gam;
gams = params_layers.gams;

piez = params_piez.piez; % piez extraction

Xetr = params_search.Xetr; % search extraction
Xext = params_search.Xext;
Ylim = params_search.Ylim;

for ilayer=1:nlayer     % loop through layers
    
    if phi(ilayer) <= 0 || phi(ilayer) >= 90*(pi/180)
        error('badEffAngleFriction','Input Error : Effective angle of friction of layer %d does not meet physical constraints, must be between 0 and 90 degrees, given %0.1f', ilayer, phi(ilayer))
    end
    if coh(ilayer) <= 0 
        error('badCohesion','Input Error : cohesion of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, coh(ilayer))
    end
    if gam(ilayer) <= 0 
        error('badDryUnitWeight','Input Error : Soil weight of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, gam(ilayer) )
    end
    if gams(ilayer) <= 0 
        error('badSatUnitWeight','Input Error : Saturated soil weight of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, gams(ilayer))
    end

    if length(strat{ilayer}) < 2
        error('NotEnoughSlopeVertices','Input Error : Each slope layer must be described by at least 2 vertices')
    end
    
    for c = 1 : length(strat{ilayer}) - 1
        if strat{ilayer}(1,c+1) < strat{ilayer}(1,c)
            error('NonMonotonicLayer','Input Error : Given x-ordinates describing layer %d are not in an increasing order', ilayer)
        end
    end
end

strat_init = strat{1}(1,1);
strat_fin = strat{1}(1,end);
for c = 2:length(nlayer)
    if strat{c}(1,1) ~= strat_init || strat{c}(1,end) ~= strat_fin
        error('DiffLayerStartEnd','Input Error : Given initial x-ordinate of %0.1f, and final x-ordinate of %0.1f, of layer %d, do not match those given in the first layer with an initial x of %0.1f and final x of %0.1f', strat{c}(1,1), strat{c}(1,end), c, strat_init, strat_fin)
    end
end

if length(piez) > 0

    if length(piez) < 2
        error('NotEnoughPiezVertices','Input Error : Piezometric surface must be described by at least 2 vertices')
    end
    
    for c = 1 : length(piez) - 1
        if piez(1,c+1) < piez(1,c)
            error('NonMonotonicPiez','Input Error : Given x-ordinates describing the piezometric surface are not in an increasing order')
        end
    end

    if piez(1,1) ~= strat_init || piez(1,end) ~= strat_fin
        error('DiffPiezStartEnd','Input Error : Given initial x-ordinate of %0.1f, and final x-ordinate of %0.1f, of the piezometric surface, do not match those given in the first layer with an initial x of %0.1f and final x of %0.1f', piez(1,1), piez(1,end), strat_init, strat_fin)
    end
    
end

for i = 1:2
    if Xetr(i) < strat_init || Xetr(i) > strat_fin
        error('XEtrGuessOutOfBounds','Input Error : Given bound on x of slip surface entry %0.1f is not between minimum slope x of %0.1f and maximum slope x of %0.1f', Xetr(i), strat_init, strat_fin)
    end
    if Xext(i) < strat_init || Xext(i) > strat_fin
        error('XExtGuessOutOfBounds','Input Error : Given bound on x of slip surface exit %0.1f is not between minimum slope x of %0.1f and maximum slope x of %0.1f', Xext(i), strat_init, strat_fin)
    end
end

end     