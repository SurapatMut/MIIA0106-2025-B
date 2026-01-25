// TODO 1) เติม field ใน class Student ให้ครบ: id, nickname, lineId, phone 
// TODO 2) เขียน method input() รับค่าจากผู้ใช้ 
// TODO 3) เขียน method print() แสดงข้อมูล
#include <iostream>
#include <string>  
using namespace std;
class Student {
public:
	// TODO 
	//propeties
	string id;
	string nickname;
	string lineId;
	string phone;

	//methods
	void input() {
		cout << "Enter ID: ";
		cin >> id;
		cout << "Enter Nickname: ";
		cin >> nickname;
		cout << "Enter Line ID: ";
		cin >> lineId;
		cout << "Enter Phone: ";
		cin >> phone;
	}

	void print() {
		cout << "ID: " << id << endl;
		cout << "Nickname: " << nickname << endl;
		cout << "Line ID: " << lineId << endl;
		cout << "Phone: " << phone << endl;
	}
};

int main()
{
	Student s1;
	cout << "=== Input Student 1 ===\n";
	// TODO: s1.input();
	s1.input();

	cout << "\n=== Output Student 1 ===\n";
	// TODO: s1.print();
	s1.print(); 
	return 0;
}
