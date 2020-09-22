function [ind] = LPM(X,Y)
%LPM Summary of this function goes here
%   Detailed explanation goes here
x1 = X; y1 = Y;
[numx1,~] = size(x1);
p1 = ones(1,numx1);
Xt = X';Yt = Y';
lambda1 = 6;lambda2 = 6;
numNeigh1 = 4; numNeigh2 = 4;
kdtreeX = vl_kdtreebuild(Xt);
kdtreeY = vl_kdtreebuild(Yt);
[neighborX, ~] =vl_kdtreequery(kdtreeX, Xt, Xt, 'NumNeighbors', numNeigh1+1) ;
[neighborY, ~] =vl_kdtreequery(kdtreeY, Yt, Yt, 'NumNeighbors', numNeigh1+1) ;
p2 = ffm2(X, Y, lambda1, numNeigh1, neighborX(1:end,:),neighborY(1:end,:),p1);
idx = find(p2 == 1);
kdtreeX = vl_kdtreebuild(Xt(:,idx));
kdtreeY = vl_kdtreebuild(Yt(:,idx));
[neighborX, ~] =vl_kdtreequery(kdtreeX, Xt(:,idx), Xt, 'NumNeighbors', numNeigh2+1) ;
[neighborY, ~] =vl_kdtreequery(kdtreeY, Yt(:,idx), Yt, 'NumNeighbors', numNeigh2+1) ;
p2 = ffm2(X, Y, lambda2, numNeigh2, neighborX(1:end,:),neighborY(1:end,:),p2);
ind = find(p2 == 1);
end

