#include <thread>
#include <vector>
#include <random>
#include <iostream>



bool INJECTIVE;

int getRandom(int n) {
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dis(0, n); //specify your interval here
    return dis(gen);
}

void check(std::vector<std::vector<int>> fDict, int n) {
    for (int i=n; i < fDict.size() && INJECTIVE; i++) {
        if (fDict.at(n).at(1) == fDict.at(i).at(1) && fDict.at(n).at(0) != fDict.at(i).at(0)) {
            INJECTIVE = false;
        }
    }
}

class randInjective {
public:
    bool injective(int maxDomain, int maxCodomain) {

        INJECTIVE = true;
        std::vector<std::vector<int>> domain(maxDomain);
        for (int i = 0; i < maxDomain; i++) {
            domain.at(i).push_back(i);
            domain.at(i).push_back(getRandom(maxCodomain));
        }

        std::vector<std::thread> threads;
        for (int i = 0; i < maxDomain && INJECTIVE; i++) {  // removed && INJECTIVE
            threads.push_back(std::thread(check, domain, i));
        }

        // previously had all threads joined above -- that was causing lockup
        // now all threads are made, but any after INJECTIVE = false will just end immediately
        for (int i = 0; i < threads.size(); i++) {
            threads.at(i).join();
        }

        return INJECTIVE;

    }
};

extern "C" {
    randInjective* randInjective_new(){ return new randInjective(); }
    int randInjective_injective(randInjective* randInjective1, int domain, int codomain) {return randInjective1->injective(domain, codomain);}
}


