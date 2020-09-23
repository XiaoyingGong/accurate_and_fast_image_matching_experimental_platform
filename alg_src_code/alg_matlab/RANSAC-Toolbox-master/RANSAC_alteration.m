function [indexRANSAC] = RANSAC_alteration(X, Y)
    input_data = [X; Y];

    sigma=1;
    options.epsilon = 1e-6;
    options.P_inlier = 1-1e-4;
    options.sigma = sigma;
    options.validateMSS_fun = @validateMSS_homography;
    options.est_fun = @estimate_homography;
    options.man_fun = @error_homography;
    options.mode = 'RANSAC';
    options.Ps = [];
    options.notify_iters = [];
    options.min_iters = 1000;
    options.fix_seed = false;
    options.reestimate = true;
    options.stabilize = false;
    
    [results, options] = RANSAC(input_data, options);
    index=results.CS;
    [junk,index]=find(index~=0);
    indexRANSAC = index';
end