// TODO: แสดงค่า score, address และ pointer
#include <iostream>
#include <string>
using namespace std;

int main() {
    int score = 50;
    int* ptr = &score;
	
    // TODO
	cout << "Value of score: " << score << endl;
	cout << "Address of score: " << &score << endl;
	cout << "Value of *ptr: " << *ptr << endl;
    return 0;
}