function [params_layers, params_piez, params_search,...
    params_soln, params_load, fnameout, sepind]=...
    SSA_InputSpecial ( fname, rngInFile )

fnameout = strcat(fname,'_output');
sepind = find(fname=='.',1,'last');

data = dlmread(fname);% read in slope geometry, stratigraphy, and piezometric surface
[A1, A2] = size(data);

if A2 > 7
    fprintf('Input Error : An extra soil data input has been given')
    return;
end

% rngInFile= input(['\nSelect input file type,\n'...
%     '0 => Entrance/Exit range not included in file\n'...
%     '1 => Entrance/Exit range included in file: ']); %Input file type

layer_checkA = data(:,3); layersindexA = find(layer_checkA);
layer_checkB = data(:,7); layersindexB = find(layer_checkB);

if ~isequal(layersindexA,layersindexB)
    fprintf('Input Error : Stratigraphic soil properties not fully defined')
    return;
end

numlayer = length(layersindexA);

i = 1;
nlayer = data(i,1);         % number of stratigraphic layers
if nlayer ~= numlayer
    fprintf('Input Error : Expected %d and  detected %d stratigraphic layers', nlayer, numlayer)
    return;
end

for c = 1 : numlayer - 1
   layer_vertlengths = layersindexA(c+1) - layersindexA(c) - 1;
   if layer_vertlengths ~= data(layersindexA(c),1)
       fprintf('Input Error : Expected %d and detected %d vertex sets describing stratigraphic layer %d', data(layersindexA(c),1), layer_vertlengths, i )
       return;
   end
end
if rngInFile
    exp_rng = 3;
else
    exp_rng = 0;
end
exp_laststrat = data(layersindexA(end),1);
exp_piez = data(layersindexA(end) + data(layersindexA(end),1) + 1,1);
if exp_piez > 0
    string_gamw = ' and 1 line describing the weight of water';
    add_gamw = 1;
else
    string_gamw = '';
    add_gamw = 0;
end
lengthtoend_Vals = exp_laststrat + exp_piez + exp_rng + 1 + add_gamw;
lengthtoend_Size = A1 - layersindexA(end);
if lengthtoend_Vals ~= lengthtoend_Size
    fprintf('Input Error : Expected %d vertex sets describing the last stratigraphic layer, %d vertex set describing the piezometric surface%s, and %d vertex sets describing the search range do not match the detected', exp_laststrat, exp_piez, string_gamw, exp_rng)
    return;
end


ltor = data(i,2);           % is slope movement left-to-right?

strat = cell(nlayer,1);     % array for strat data
phi = zeros(nlayer,1);      % effective angle of friction
coh = zeros(nlayer,1);      % effective cohesion
gam = zeros(nlayer,1);      % dry unit weight
gams = zeros(nlayer,1);     % sat unit weight
E = zeros(nlayer,1);        % elastic modulus
nu = zeros(nlayer,1);       % Poisson's ratio

i = i+1;
for ilayer=1:nlayer     % loop through layers
    
    npts = data(i,1);           % number of points in strat geom
    
    phi(ilayer) = data(i,2);
    if phi(ilayer) <= 0 || phi(ilayer) >= 90
        fprintf('Input Error : Effective angle of friction of layer %d does not meet physical constraints, must be between 0 and 90 degrees, given %0.1f', ilayer, phi(ilayer))
        return;
    end
    coh(ilayer) = data(i,3);
    if coh(ilayer) < 0 
        fprintf('Input Error : cohesion of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, coh(ilayer))
        return;
    end
    gam(ilayer) = data(i,4);
    if gam(ilayer) <= 0 
        fprintf('Input Error : Soil weight of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, gam(ilayer) )
        return;
    end
    gams(ilayer) = data(i,5);
    if gams(ilayer) <= 0 
        fprintf('Input Error : Saturated soil weight of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, gams(ilayer))
        return;
    end
    E(ilayer) = data(i,6);
    if E(ilayer) <= 0 
        fprintf('Input Error : Youngs modulus of layer %d does not meet physical constraints, must be greater than 0, given %0.1f', ilayer, E(ilayer))
        return;
    end
    nu(ilayer) = data(i,7);
    if nu(ilayer) <= 0 
        fprintf('Input Error : Poissons ratio of layer %d does not meet physical constraints, must be greater than 0 and less than 1, given %0.1f', ilayer, nu(ilayer))
        return;
    end
    
    i = i+1;
    
    strat{ilayer} = data(i:i+npts-1,1:2)';   % read strat geom
    
    for c = 1 : length(strat{ilayer}) - 1
        if strat{ilayer}(1,c+1) < strat{ilayer}(1,c)
            fprintf('Input Error : Given x-ordinates describing layer %d are not in an increasing order', ilayer)
            return;
        end
    end
    
    if ilayer == 1
        Y_start = strat{1}(2,1);
        Y_end = strat{1}(2,end);
        if Y_start > Y_end
            if ~ltor
                fprintf('Input Error : Detected soil motion direction (left to right), does not match given soil motion')
                return;
            end
        elseif Y_start < Y_end
            if ltor
                fprintf('Input Error : Detected soil motion direction (right to left), does not match given soil motion')
                return;
            end
        end
    else
        strat_init = strat{1}(1,1);
        strat_fin = strat{1}(1,end);
        if strat{ilayer}(1,1) ~= strat_init || strat{ilayer}(1,end) ~= strat_fin
            fprintf('Input Error : Given initial x-ordinate of %0.1f, and final x-ordinate of %0.1f, of layer %d, do not match those given in the first layer with an initial x of %0.1f and final x of %0.1f', strat{ilayer}(1,1), strat{ilayer}(1,end), ilayer, strat_init, strat_fin)
            return;
        end
    end
    
    i = i+npts;
    
end
phi = phi*(pi/180);

strat_init = strat{1}(1,1);
strat_fin = strat{1}(1,end);
for c = 2:length(nlayer)
    if strat{c}(1,1) ~= strat_init || strat{c}(1,end) ~= strat_fin
        fprintf('Input Error : Given initial x-ordinate of %0.1f, and final x-ordinate of %0.1f, of layer %d, do not match those given in the first layer with an initial x of %0.1f and final x of %0.1f', strat{c}(1,1), strat{c}(1,end), c, strat_init, strat_fin)
        return;
    end
end

params_layers = struct('strat',strat, 'phi',phi, 'coh',coh,...
    'gam',gam, 'gams',gams, 'E',E, 'nu',nu);

nwpts = data(i,1);  % number of points in piez data (0 if dry)
if nwpts > 0
    
    i = i+1;
    gamw = data(i,1);   % unit weight of water
    
    i = i+1;
    piez = data(i:i+nwpts-1,1:2)';   % piez surface data
    
    i=i+nwpts; % jump for entrance/exit input
    
    for c = 1 : length(piez) - 1
        if piez(1,c+1) < piez(1,c)
            fprintf('Input Error : Given x-ordinates describing the piezometric surface are not in an increasing order')
            return;
        end
    end
    
    strat_init = strat{1}(1,1);
    strat_fin = strat{1}(1,end);
    if piez(1,1) ~= strat_init || piez(1,end) ~= strat_fin
        fprintf('Input Error : Given initial x-ordinate of %0.1f, and final x-ordinate of %0.1f, of the piezometric surface, do not match those given in the first layer with an initial x of %0.1f and final x of %0.1f', piez(1,1), piez(1,end), strat_init, strat_fin)
        return;
    end
    
else
    
    piez = [];
    gamw = 0;
    
    i=i+1; % jump for entrance/exit input
    
end
params_piez = struct('piez',piez, 'gamw',gamw);

Q = [];
omega = [];
Kc = 0;

params_load = struct('Kc',Kc, 'Q',Q, 'omega',omega);

if  rngInFile % set up genetic algorithm search data file read
    x1 = data(i,1);
    x2 = data(i,2);
    Xetr = [min(x1,x2),max(x1,x2)];
    
    i=i+1;
    x1 = data(i,1);
    x2 = data(i,2);
    Xext = [min(x1,x2),max(x1,x2)];

    i=i+1;
    y1 = data(i,1);
    y2 = data(i,2);
    Ylim = [min(y1,y2),max(y1,y2)]; 
else % set up genetic algorithm search command prompts
    x1 = 1;
    x2 = 2;
    Xetr = [min(x1,x2),max(x1,x2)];

    x1 = 1;
    x2 = 2;
    Xext = [min(x1,x2),max(x1,x2)];

    y1 = 1;
    y2 = 2;
    Ylim = [min(y1,y2),max(y1,y2)];   
end

params_search = struct('Xext',Xext, 'Xetr',Xetr,'Ylim',Ylim);

cncvu = 1; % slopes must be concave (Kin Adm)
obtu = 1; % slopes must be obtuse (Kin Adm)
evnslc = 1; % Slice evenly
ftype = 0;

params_soln = struct('ltor',ltor, 'ftype',ftype,...
    'evnslc',evnslc, 'cncvu',cncvu, 'obtu',obtu);

end     