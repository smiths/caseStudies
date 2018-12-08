function verify_output(F)

if F <= 0
    error('verify_output:badFactorOfSafety','Output Error : The computed factor of safety, %0.1f, was negative', F);
end