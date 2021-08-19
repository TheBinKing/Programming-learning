#include <iostream>
#include <stack>
using namespace std;
stack<int> a;
int c;
int main() {
	while (1) {
		cin >> c;
		if (c == 0) break;
		a.push(c);
	}
	while (!a.empty())
	{
		cout << a.top() << " ";
		a.pop();
	}
	return 0;
}