#include <iostream>

using namespace std;
int a;
char s[999];
int main() {
	cin >> a;
	cin >> s;
	for (int i = 0;s[i];i++) {
		s[i] = (s[i] + a - 'a') % 26 + 'a';
	}
	cout << s;
}