def output(params, time, tempW, eW, eTot, filename):
    outputFilename = filename + 'out'
    f = open(outputFilename, 'w')
    f.write('\tL\t\t\t\t' + str(params.L) + '\n')
    f.write('\tdiam\t\t\t' + str(params.diam) + '\n')
    f.write('\tAc\t\t\t\t' + str(params.Ac) + '\n')
    f.write('\tTc\t\t\t\t' + str(params.Tc) + '\n')
    f.write('\trho_w\t\t\t' + str(params.rho_w) + '\n')
    f.write('\tC_w\t\t\t\t' + str(params.C_w) + '\n')
    f.write('\thc\t\t\t\t' + str(params.hc) + '\n')
    f.write('\tTinit\t\t\t' + str(params.Tinit) + '\n')
    f.write('\ttstep\t\t\t' + str(params.tstep) + '\n')
    f.write('\ttfinal\t\t\t' + str(params.tfinal) + '\n')
    f.write('\tAbsTol\t\t\t' + str(params.AbsTol) + '\n')
    f.write('\tRelTol\t\t\t' + str(params.RelTol) + '\n')
    f.write('\tConsTol\t\t\t' + str(params.ConsTol) + '\n')
    f.write('\tVt\t\t\t\t' + str(params.Vt) + '\n')
    f.write('\tMw\t\t\t\t' + str(params.Mw) + '\n')
    f.write('\ttau_w\t\t\t' + str(params.tau_w) + '\n')
    f.write('\tMw_noPCM\t\t' + str(params.Mw_noPCM) + '\n')
    f.write('\ttau_w_noPCM\t\t' + str(params.tau_w_noPCM) + '\n')
    results = zip(time, tempW, eW, eTot)
    max_width = max(len(str(result)) for category in results for result in category)
    f.write('\n' + 'Time'.ljust(max_width+1) + 'Twater'.ljust(max_width+1) +
            'Ewater'.ljust(max_width+1) + 'Etotal'.ljust(max_width+1) + '\n')
    for t, Tw, Ew, Et in zip(time, tempW, eW, eTot):
        f.write(str(t).ljust(max_width+1) + str(Tw).ljust(max_width+1) +
                str(Ew).ljust(max_width+1) + str(Et).ljust(max_width+1) + '\n')
    f.close()
