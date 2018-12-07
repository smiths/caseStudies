function [params_layers, params_piez, params_search,...
    params_soln, params_load]=...
    load_params(fname)

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

sepind = find(fname=='.',1,'last');

nfile = length(fname);
if ~isempty(sepind) && (    strcmp(fname(sepind+1:nfile),'out') ...
                            || strcmp(fname(sepind+1:nfile),'OUT')  )
	error('Cannot use extension ''.out'' for input file.');
end

data = dlmread(fname);% read in slope geometry, stratigraphy, and piezometric surface
[A1, A2] = size(data);

if A2 > 5
    error('Input Error : An extra soil data input has been given')
end

layer_checkA = data(:,3); layersindexA = find(layer_checkA);
layer_checkB = data(:,4); layersindexB = find(layer_checkB); %This is a workaround to allow for one 0 value for one material property
layer_checkC = data(:,5); layersindexC = find(layer_checkC);

if ~isequal(layersindexA,layersindexB) && ~isequal(layersindexC,layersindexB) && ~isequal(layersindexA,layersindexC)
    error('Input Error : Stratigraphic soil properties not fully defined')
end

[numlayer, maxIndex] = max([length(layersindexA), length(layersindexB), length(layersindexC)]);

switch maxIndex
    case 1
        layersindex = layersindexA;
    case 2
        layersindex = layersindexB;
    case 3
        layersindex = layersindexC;
end

i = 1;
nlayer = data(i,1);         % number of stratigraphic layers
if nlayer ~= numlayer
    error('Input Error : Expected %d and  detected %d stratigraphic layers', nlayer, numlayer)
end

for c = 1 : numlayer - 1
   layer_vertlengths = layersindex(c+1) - layersindex(c) - 1;
   if layer_vertlengths ~= data(layersindex(c),1)
       error('Input Error : Expected %d and detected %d vertex sets describing stratigraphic layer %d', data(layersindex(c),1), layer_vertlengths, i )
   end
end
exp_rng = 3;
exp_laststrat = data(layersindex(end),1);
exp_piez = data(layersindex(end) + data(layersindex(end),1) + 1,1);
if exp_piez > 0
    string_gamw = ' and 1 line describing the weight of water';
    add_gamw = 1;
else
    string_gamw = '';
    add_gamw = 0;
end
lengthtoend_Vals = exp_laststrat + exp_piez + exp_rng + 2 + add_gamw; % + 2 for the line with the number of vertices for water table and the line with the value for ftype
lengthtoend_Size = A1 - layersindex(end);
if lengthtoend_Vals ~= lengthtoend_Size
    error('Input Error : Expected %d vertex sets describing the last stratigraphic layer, %d vertex set describing the piezometric surface%s, and %d vertex sets describing the search range do not match the detected', exp_laststrat, exp_piez, string_gamw, exp_rng)
end

ltor = data(i,2);           % is slope movement left-to-right?

strat = cell(nlayer,1);     % array for strat data
phi = zeros(nlayer,1);      % effective angle of friction
coh = zeros(nlayer,1);      % effective cohesion
gam = zeros(nlayer,1);      % dry unit weight
gams = zeros(nlayer,1);     % sat unit weight

i = i+1;
for ilayer=1:nlayer     % loop through layers
    
    npts = data(i,1);           % number of points in strat geom
    
    phi(ilayer) = data(i,2);
    coh(ilayer) = data(i,3);
    gam(ilayer) = data(i,4);
    gams(ilayer) = data(i,5);
    
    i = i+1;
    
    strat{ilayer} = data(i:i+npts-1,1:2)';   % read strat geom
    
    if ilayer == 1
        Y_start = strat{1}(2,1);
        Y_end = strat{1}(2,end);
        if Y_start > Y_end
            if ~ltor
                error('Input Error : Detected soil motion direction (left to right), does not match given soil motion')
            end
        elseif Y_start < Y_end
            if ltor
                error('Input Error : Detected soil motion direction (right to left), does not match given soil motion')
            end
        end
    end
    
    i = i+npts;
    
end
phi = phi*(pi/180);

params_layers = struct('strat',strat, 'phi',phi, 'coh',coh,...
    'gam',gam, 'gams',gams);

nwpts = data(i,1);  % number of points in piez data (0 if dry)
if nwpts > 0
    
    i = i+1;
    gamw = data(i,1);   % unit weight of water
    
    i = i+1;
    piez = data(i:i+nwpts-1,1:2)';   % piez surface data
    
    i=i+nwpts; % jump for entrance/exit input
    
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

params_search = struct('Xext',Xext, 'Xetr',Xetr,'Ylim',Ylim);

cncvu = 1; % slopes must be concave (Kin Adm)
obtu = 1; % slopes must be obtuse (Kin Adm)
evnslc = 1; % Slice evenly

i = i+1;
ftype = data(i,1);

params_soln = struct('ltor',ltor, 'ftype',ftype,...
    'evnslc',evnslc, 'cncvu',cncvu, 'obtu',obtu);

end     



   