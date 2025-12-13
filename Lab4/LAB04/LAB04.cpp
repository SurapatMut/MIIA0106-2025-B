#include <iostream>
#include <string>

using namespace std;

int main() 
{
	string name = "Surapat Krutta";

	//cout แสดงข้อมูลออกหน้าจอ
	cout << " Test Lab 04 \n";
	cout << " Test Lab 04-1 " << endl;
	cout << "Please enter Your Name ";

	//cin ใช้ในการเกฌบข้อมูลไวในตัวแปล
	//cin >> name; //เจอช่องว่างจะไม่รับข้อมูล
	cin > name;
	cin.ignore(); //clear buffer
	getline(cin, name);

	cout << "My name is " << name << "----" << endl;



	return 1;
}