function slipnew = match_slice( slip, nSlices )

XMin = slip (1,1);
XMax = slip (1,length(slip));
XLine = slip (1,:);
YPoints = slip (2,:);

SliceDist = (XMax-XMin)/(nSlices);
XSlices = XMin:SliceDist:XMax;
YSlices = zeros(1,length(XSlices));

XSlices(1) = XLine(1);
XSlices(nSlices+1) = XLine(end);
YSlices(1) = YPoints(1);
YSlices(nSlices+1) = YPoints(end);
for i = 2:nSlices
    k = find(XLine<XSlices(i),1,'last');
    DeltaX = XLine(k+1)-XLine(k);
    DeltaY = YPoints(k+1) - YPoints(k);
    DeltaS = XSlices(i) - XLine(k);
    YSlices(i) = YPoints(k) + (DeltaS*DeltaY)/(DeltaX);
end

slipnew=[XSlices;YSlices];
end