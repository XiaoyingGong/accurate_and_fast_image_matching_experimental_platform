
clear all;
close all;
initialization;  %run it only at the first time

fn_l = '1.bmp';
fn_r = '2.bmp';
Ia = imread(fn_l);
Ib = imread(fn_r);
if size(Ia,3)==1
    Ia = repmat(Ia,[1,1,3]);
end
if size(Ib,3)==1
    Ib = repmat(Ib,[1,1,3]);
end
%%
load putative_match.mat;

tic;
[wa,ha,~] = size(Ia);
[wb,hb,~] = size(Ib);
maxw = max(wa,wb);maxh = max(ha,hb);
Ib(wb+1:maxw, :,:) = 0;
Ia(wa+1:maxw, :,:) = 0;
ind  = LPM(X, Y);
toc

[FP,FN] = plot_matches(Ia, Ib, X, Y, ind, CorrectIndex);
plot_4c(Ia,Ib,X,Y,ind,CorrectIndex);












