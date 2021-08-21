#include <iostream>
using namespace std;

char strings[101];

int main() {
	cin >> strings;
	for (int i=0;strings[i];i++) {
		if (strings[i] >= 'a' && strings[i] <= 'z')
			strings[i] -= 32;
	}
	cout << strings;
}