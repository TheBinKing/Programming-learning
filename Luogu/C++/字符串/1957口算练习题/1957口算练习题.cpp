#include <iostream>
#include <string>
#include <sstream>
using namespace std;
int main() {
	int line=0;
	cin >> line;
	char op = {};
	int n=0, m=0;
	string form;
	for (int i = 0;i < line;i++) {
		if (!(cin >>n)) {
			cin.clear();
			cin >>op>> n ;
		}
		cin >>m;
		if (op == 'a') {
			form = to_string(n) + "+" +  to_string(m) + "=" + to_string(n + m);
			cout << form<<"\n";
			cout << form.length() << "\n";
		}
		if (op == 'b') {
			form = to_string(n) + "-" + to_string(m) + "=" + to_string(n - m);
			cout << form << "\n";
			cout << form.length() << "\n";
		}
		if (op == 'c') {
			form = to_string(n) + "*" + to_string(m) + "=" + to_string(n * m);
			cout << form << "\n";
			cout << form.length()<<"\n";
		}

	}
	return 0;
}