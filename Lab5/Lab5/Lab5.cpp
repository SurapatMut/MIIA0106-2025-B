#include <iostream>
#include <string>

using namespace std;

double calculateArea(double radius)
{
	return 3.14159 * radius * radius;
}

double rectangleArea(double width, double height)
{
	double result = width * height;
	return result;
}
int main()
{
	double radins; // declare radius variable
	double result; // declare result variable

	cout << "Enter the radius the : "; // prompt user for radius
	cin >> radins; // read radius from user

	//result = 3.14159 * radins * radins; // calculate area
	//cout << "The area of the circle is: " << result << endl; // display area

	result = calculateArea(radins); // call function to calculate area
	cout << "The area of the circle is: " << result << endl; // display result

	//width, height
	double width, height;
	cout << "Enter width "; // declare radius variable
	cin >> width; // read radius from user
	cout << "Enter height "; // declare radius variable
	cin >> height; // read radius from user

	result = rectangleArea(width, height); // call function to calculate area
	cout << "The area of the rectangle is: " << result << endl; // display result


	return 1;
}