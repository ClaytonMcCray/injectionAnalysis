#include <random>
#include <stdio.h>



int getRandom(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, n);
    return dis(gen);
}

__global__
void check(int *fDictX, int *fDictY, int sizeOfFDict, int currInjective) {
    int idx = blockIdx.x * blockDim.x + threadIdx.x;
    if (idx < sizeOfFDict) {
        for (int i=idx; i < sizeOfFDict && currInjective; i++) {
            if (fDictY[idx] == fDictY[i] && fDictX[idx] != fDictX[i]) {
                currInjective = 0;
            }
        }
    }
}


int injective(int maxDomain, int maxCodomain) {
    int INJECTIVE = 1;
    // get a device copy of INJECTIVE
    //int d_INJECTIVE;
    //cudaMalloc(&d_INJECTIVE, sizeof(int));
    //cudaMemcpy(d_INJECTIVE, INJECTIVE, sizeof(int), cudaMemcpyHostToDevice);
    // ****

    int *domainX, *domainY, *d_domainX, *d_domainY;  // host, device
    domainX = (int*)malloc(maxDomain * sizeof(int));
    domainY = (int*)malloc(maxDomain * sizeof(int));

    cudaMalloc(&d_domainX, maxDomain*sizeof(int));
    cudaMalloc(&d_domainY, maxDomain*sizeof(int));

    for (int i = 0; i < maxDomain; i++) {
        domainX[i] = i;
        domainY[i] = getRandom(maxCodomain);
    }

    cudaMemcpy(d_domainX, domainX, maxDomain*sizeof(int), cudaMemcpyHostToDevice);
    cudaMemcpy(d_domainY, domainY, maxDomain*sizeof(int), cudaMemcpyHostToDevice);

    check<<<(maxDomain+255)/256, 256>>>(d_domainX, d_domainY, maxDomain, INJECTIVE);

    //cudaMemcpy(INJECTIVE, d_INJECTIVE, sizeof(int), cudaMemcpyDeviceToHost);
    
    cudaFree(d_domainX);
    cudaFree(d_domainY);
    free(domainX);
    free(domainY);

    return INJECTIVE;

}
    

int main() {
    int test = injective(2560, 10240);
    printf("%s\n", test);
    
    return 0;
}

    


    

