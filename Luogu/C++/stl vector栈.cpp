#include <iostream>
#include <vector> //stl vector 
using namespace std;
vector<int> a;
int c;
int main() {
	while (1) {
		cin >> c;
		if (c == 0)break;
		a.push_back(c);
	}
	while (!a.empty())
	{
		cout << a.back() << " ";
		a.pop_back();
	}
	return 0;
}