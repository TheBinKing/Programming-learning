/*使用栈进行逆序输出*/
#include <iostream>
using namespace std;
int a[101],top=0,flag;

int main() {
	while (true)
	{
		cin >> flag;
		if (flag == 0) break;
		a[++top] = flag;
	}
	while (top != 0) {
		flag = a[top--];
		cout << flag << " ";
	}
	return 0;
}
