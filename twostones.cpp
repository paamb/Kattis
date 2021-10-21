#include <iostream>

using namespace std;
int main(){
    int stones;
    scanf("%d", &stones);

    if(stones%2 == 1){
        printf("%s", "Alice");
    }
    else{
        printf("%s","Bob");
    }
}
