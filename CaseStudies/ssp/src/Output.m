function Output(cslip, F, Nint, Tint, params_layers, params_piez,...
    params_soln, params_load, params_search, fname)

% Slope Stability Analysis Program
% Output.m
%
% 20 August 2015
% 
%  - For a description of the module interface refer to the MIS.
% (../Documentation Files/MIS_SSP.pdf)
%
%  - For a description of the module secrets and services refer to the MG.
% (../Documentation Files/MG_SSP.pdf)
%
% -------------------------------------------------------------------------

% -------------------------------------------------------------------------
% PREPARE VALUES (FOR PLOTTING)
% -------------------------------------------------------------------------

sepind = find(fname=='.',1,'last'); % find separator (for creating output file later)

nlayer = length(params_layers); % strat extraction
strat = cell(nlayer,1);
for i = 1:nlayer
    strat{i} = params_layers(i).strat;
end

piez = params_piez.piez; % piez extraction

ftype = params_soln.ftype; % soln method extraction

Xetr = params_search.Xetr; %search range extraction
Xext = params_search.Xext;
Ylim = params_search.Ylim;


% -------------------------------------------------------------------------
% PLOT RESULTS
% -------------------------------------------------------------------------

figure;

% plot stratigraphy and critical slip surface
hgeom = subplot(211);
nlayer = size(strat,1);
if size(piez,1),    plot(piez(1,:),piez(2,:),'--b');
else plot(strat{1}(1,1),strat{1}(2,1));
end
hold on;
for i = 1:nlayer
    h = plot(strat{i}(1,:),strat{i}(2,:),'-k');
    if i==1,	set(h,'linewidth',2);   end
end
h = plot(cslip(1,:),cslip(2,:),'--r');
set(h,'linewidth',2)
xlabel('x','fontweight','bold');
ylabel('y','fontweight','bold');
title(sprintf('Critical slip surface, Fs = %5.4f', ...
                F), 'fontweight', 'bold');

minx = min(strat{1}(1,:));
maxx = max(strat{1}(1,:));
miny = min([min(cslip(2,:)) min(strat{nlayer}(2,:))]);
maxy = max(strat{1}(2,:));
hslp = max(strat{1}(2,:)) - min(strat{1}(2,:));

set(hgeom, 'xlim', [minx maxx]);
set(hgeom, 'ylim', [miny-0.2*hslp maxy+0.2*hslp]);
hold off;

% plot interslice forces
hfrc = subplot(212);
plot(cslip(1,2:nslice),Nint,'-k');
hold on;
plot(cslip(1,2:nslice),Tint,'-r');
hold off;

set(hfrc, 'xlim', [minx maxx]);
xlabel('x','fontweight','bold');
ylabel('G, X','fontweight','bold');
title('Interslice forces','fontweight','bold');
legend('G','X');



% -------------------------------------------------------------------------
% GENERATE OUTPUT FILE
% -------------------------------------------------------------------------

foutname = fname;

% strip file extension
if ~isempty(sepind),    foutname = foutname(1:sepind-1);    end

% check for existing output file and set output filename
if exist([foutname '.OUT'],'file')
    foutname = [foutname '.OUT'];
else
    foutname = [foutname '.out'];
end

fout = fopen(foutname,'a');

fprintf(fout, '\r\n\r\n');
fprintf(fout, '-----------------------------------------\r\n');
fprintf(fout, 'Slope Stability Analysis\r\n\r\n');
fprintf(fout, 'Input File:\t\t%s\r\n', fname);
fprintf(fout, 'Date:\t\t\t%s\r\n', datestr(now));
fprintf(fout, '-----------------------------------------\r\n');

fprintf(fout, '\r\n\r\n');
fprintf(fout, 'Slip Surface Search Ranges\r\n');
fprintf(fout, '\r\n');
fprintf(fout, '   Xenter      Xexit     Yrange\r\n');
fprintf(fout, '%9.4f  %9.4f  %9.4f\r\n', [Xetr; Xext; Ylim]);

fprintf(fout, '\r\n\r\n');
if ftype,   ftype = 'constant (Spencer)';
else        ftype = 'half-sine (Morgenstern-Price)';
end
fprintf(fout, 'Interslice force relation:\t%s\r\n', ftype);

fprintf(fout, '\r\n\r\n');
fprintf(fout, 'Critical Surface\r\n');
fprintf(fout, '\r\n');
fprintf(fout, '        x          y\r\n');
fprintf(fout, '%9.4f  %9.4f\r\n', cslip);

fprintf(fout, '\r\n\r\n');
fprintf(fout, 'Factor of Safety\r\n');
fprintf(fout, '\r\n');
fprintf(fout, 'Fs =\t\t%5.4f\r\n', F);


fprintf(fout, '\r\n\r\n');
fprintf(fout, 'Interslice Forces\r\n');
fprintf(fout, '\r\n');
fprintf(fout, '        x         N_mp         T_mp\r\n');
fprintf(fout, '%9.4f  %11.3f  %11.3f\r\n', ...
                    [   cslip(1,2:nslice);
                        Nint;
                        Tint]     );

fprintf(fout, '\r\n\r\n');

fclose(fout);
end