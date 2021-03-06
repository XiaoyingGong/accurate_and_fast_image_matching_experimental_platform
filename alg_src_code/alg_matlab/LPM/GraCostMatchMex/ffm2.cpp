#include "mex.h" 
#include "float.h"
#include<iostream>
void GraCostMatch(float* X, float* Y, int* neighborX, int* neighborY, float lambda, int numNeigh,
	int numPoint, double* Prob, double*p)
{
	int numNeighCands;
	numNeighCands = numPoint;

		if (numNeighCands > numNeigh+1){
		for (int i = 0; i < numPoint; i++){
			int cost = 0;
			int ad = 0;
			if(p[i] > 0.5) ad = 1;
		
			for (int m = 0; m < numNeigh; m++){
				int  num = numNeigh+1;
				int tmp = neighborX[num*i+m+ad];
				bool isMember = false;
				for (int n = 0; n < numNeigh; n++){
					if (neighborY[num*i+n+ad] == tmp){
						isMember = true;
						break;
					}
				}
				if (!isMember)
					cost++;
			}
			cost *= 2;

			if (cost <= lambda){
				Prob[i] = 1.0f;
			}
			else{
				Prob[i] = 0.0f;
			}

		}
		}
}

void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[]) 
{
	/*nlhs：num of output para
		plhs：output para
		nrhs：num of input para
		prhs：input para */ 
	double *X;
	double *Y;
	int *neighborX;
	int *neighborY;
	double *Prob;
	double *p;
	float lambda1, lambda2;
	int numNeigh1, numNeigh2;
	int M, N, numPoint;

	X = (double *)mxGetData(prhs[0]);
	Y = (double *)mxGetData(prhs[1]);
	lambda1 = static_cast<float>(mxGetScalar(prhs[2]));
	numNeigh1 = static_cast<int>(mxGetScalar(prhs[3]));

	neighborX = (int *)mxGetData(prhs[4]);
	neighborY = (int *)mxGetData(prhs[5]);
	
	p = (double *)mxGetData(prhs[6]);
	
	M = static_cast<int>(mxGetM(prhs[0]));
	N = static_cast<int>(mxGetN(prhs[0]));
	if (M==2){
		numPoint = N;
	}
	else if (N==2){
		numPoint = M;
	}

	float* new_X = new float[numPoint*2];
	float* new_Y = new float[numPoint*2];
	if (M==2){
		for (int i = 0; i < M*N; i++){
			new_X[i] = static_cast<float>(X[i]);
			new_Y[i] = static_cast<float>(Y[i]);
		}
	}
	else if (N==2){
		for (int i = 0; i < M; i++){
			new_X[i*2] = static_cast<float>(X[i]);
			new_X[i*2+1] = static_cast<float>(X[i+M]);
			new_Y[i*2] = static_cast<float>(Y[i]);
			new_Y[i*2+1] = static_cast<float>(Y[i+M]);
		}
	}

	plhs[0] = mxCreateDoubleMatrix(1, numPoint,mxREAL);
	Prob = mxGetPr(plhs[0]);

	GraCostMatch(new_X, new_Y, neighborX, neighborY,lambda1, numNeigh1, numPoint, Prob,p);
	delete[] new_X;
	delete[] new_Y;
}
