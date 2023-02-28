#include <iostream>
using namespace std;
struct Grade
{
	int C;
	int M;
	int E;
};
bool Compare_grade(Grade a,Grade b) {
	if (abs(a.C - b.C) > 5)
		return 0;
	if (abs(a.M - b.M) > 5)
		return 0;
	if (abs(a.E - b.E) > 5)
		return 0;
	return 1;
}
bool Compare_all(Grade a, Grade b) {
	int a_all = a.M + a.C + a.E;
	int b_all = b.C + b.E + b.M;
	if (abs(a_all - b_all) > 10)
		return 0;
	return 1;
}
int main() {
	int num;
	int flag=0;
	cin >> num;
	if (num == 0 || num == 1) {
		cout << 0;
		return 1;
	}
	Grade a[1000];
	for (int i = 0;i < num;i++) {
		cin >> a[i].C >> a[i].M >> a[i].E;
	}
	for (int i = 0;i < num;i++) {
		for (int j = 1;(i + j) < num;j++)
			if (Compare_all(a[i], a[i + j]) && Compare_grade(a[i], a[i + j]))
				flag++;

	}
	cout << flag;
}