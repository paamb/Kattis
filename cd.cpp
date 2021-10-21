#include <iostream>
#include <unordered_set>

using namespace std;

int main(){
    while (true){
        int N;
        int M;
        scanf("%d", &N);
        scanf("%d", &M);

        if(N == 0 && M == 0){
            break;
        }
        unordered_set<int> set;
        for(int i = 0; i < N; i++){
            int cd;
            scanf("%d",&cd);
            set.insert(cd);
        }
        int count = 0;
        for(int i = 0; i < M; i++){
            int cd;
            scanf("%d", &cd);
            if(set.count(cd)){
                count++;
            }
        }
        printf("%d\n", count);
    }
}