
#include <iostream>
using namespace std;
int num[100], c = 0;
int main() {
	for (int i = 0;;i++) {
		cin >> num[i];
		if (num[i] == 0)
			break;
		c = i;
	}
	for (int i = 0;i <= c;i++) {
		cout << num[c-i] << " ";
	}
	return 0;

}
