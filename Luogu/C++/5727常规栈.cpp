#include <iostream>
#include <stack>
using namespace std;
stack<int>a;
int temp;
int input;
int main() {
	cin >> input;
	a.push(input);
	while (input != 1) {
		if (input % 2 != 0) {
			input = input * 3 + 1;
			a.push(input);
			continue;
		}
		input = input / 2;
		a.push(input);
	}
	while (!a.empty()) {
		cout << a.top() << " ";
		a.pop();
	}
	return 0;
}