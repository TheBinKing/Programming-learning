#include <iostream>
using namespace std;
int a[101], c;
int* p = a;//定义一个int类型的指针,指向数组不用取址符
int main() {
	while (true)
	{
		cin >> c;
		if (c == 0) break;
		p++;
		*p = c;
	}
	while (p!=a)
	{
		cout << *p << " ";
		p--;
	}
	return 0;
}