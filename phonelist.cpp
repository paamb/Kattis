#include <iostream>
#include <queue>
#include <cstdio>
using namespace std;
string check_test_cases(){
    priority_queue<string> numbers;
    int num_numbers;
    scanf("%d", &num_numbers);

    for(int i = 0; i < num_numbers; i++){
        string number;
        scanf("%s", number);
        numbers.push(number);
    }
    string num_1;
    string num_2;
    for(int i = 0; i < num_numbers - 1; i++){

        if (i == 0){
            num_1 = numbers.top();
            num_2 = numbers.top();
            numbers.pop();
            numbers.pop();
        }

        else{
            num_1 = num_2;
            num_2 = numbers.top();
            numbers.pop();
        }
        if(num_1 == num_2.substr(0,num_1.length())){
            cout << "hei" << endl;
            return "NO";
        }
    }
    return "YES";
}

int main(){
    int testcases;
    scanf("%d", &testcases);

    for(int i = 0; i < testcases; i++){
        printf("%s", check_test_cases());
    }
}

