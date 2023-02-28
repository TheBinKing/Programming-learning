#include <iostream>
using namespace std;

int main() {
	int A[500][500] = { 0};
	int num;
	cin >> num;
	int h = 0, l = (num - 1) / 2;
	A[h][l] = 1;
	for (int i = 2;i <= num * num;i++) {
		if (A[(h - 1 + num) % num][(l + 1) % num]== 0) {
			h = (h - 1 + num) % num;
			l = (l + 1) % num;
		}
		else {
			h = (h + 1) % num;
		}
		A[h][l] = i;
	}
	for (int i = 0;i < num ;i++) {
		for (int j =0;j < num;j++) {
			cout << A[i][j] << ' ';
		}
		cout << '\n';
	}
}