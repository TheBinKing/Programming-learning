#include <iostream>
using namespace std;
void write(int n) {
	if (n == 1) {
		cout << "1"<<" ";
		return;
	}
	if (n & 1) write(n * 3 + 1);
	else write(n >> 1); //二进制中程序右移动一位，相当于乘两倍
	cout << n<< " ";
}
int main() {
	int n;
	cin >> n;
	write(n);
	return 0;
}