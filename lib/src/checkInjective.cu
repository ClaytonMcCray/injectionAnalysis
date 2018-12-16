#include <random>



int getRandom(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, n);
    return dis(gen);
}

__global__
void check(int *fDictX, int *fDictY, int sizeOfFDict, int *currInjective) {
    int idxInit = blockIdx.x * blockDim.x + threadIdx.x;  // this is the initial global index

    if (idxInit < sizeOfFDict) {  // make sure we're not out of bounds
        // grid-stride loop 
        for (int idx = idxInit; idx <= sizeOfFDict; idx += blockDim.x * gridDim.x) {
            // this inner loop will do the work for a thread in each grid
            for (int i=idx; i < sizeOfFDict; i++) {
                if (fDictY[idx] == fDictY[i] && fDictX[idx] != fDictX[i]) {
                    currInjective[idx] = 0;  // this will insert a zero into INJECTIVE
                    break;
                }
            }
        }
    }
}


extern "C" {
    int injective(int maxDomain, int maxCodomain) {

        // declare the arrays
        int *domainX, *domainY, *INJECTIVE;

        // allocated Unified Memory
        cudaMallocManaged(&domainX, maxDomain*sizeof(int));
        cudaMallocManaged(&domainY, maxDomain*sizeof(int));
        cudaMallocManaged(&INJECTIVE, maxDomain*sizeof(int));


        // initialize function
        for (int i = 0; i < maxDomain; i++) {
            domainX[i] = i;
            domainY[i] = getRandom(maxCodomain);
            INJECTIVE[i] = 1;  // here we assume that the function is injective
        }


        // actually make the kernel call
        // this is currently running with thread blocks of size 256. I may find a better number
        // to tune that too. It's <<< numBlocks, numThreads >>>
        check<<<(maxDomain+255)/256, 256>>>(domainX, domainY, maxDomain, INJECTIVE);
        cudaDeviceSynchronize();  // sync the host and device

        // error checking
        if (cudaSuccess != cudaGetLastError()) {
            cudaFree(domainX);
            cudaFree(domainY);
            cudaFree(INJECTIVE);
            return -1;  // this will be used to raise a RuntimeError 
        }

        // free the unified memory
        cudaFree(domainX);
        cudaFree(domainY);

        for (int i = 0; i < maxDomain; i++) {
            if (INJECTIVE[i] == 0) {  // 0 => false so the function is not injective
                cudaFree(INJECTIVE);
                return 0;
            }
        }

        cudaFree(INJECTIVE);
        return 1;  // the function is injective

    }
}
    
    
