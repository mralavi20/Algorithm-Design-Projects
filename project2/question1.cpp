#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int n;
	int m;
	int num;
	int status;
	int i;
	int j;
	vector<vector<int>> table;
	vector<vector<int>> c1;
	vector<vector<int>> c2;
	vector<int> temp1;
	vector<int> temp2;

	cin >> n;
	cin >> m;

	status = 0;

	for (i = 0; i < n; i++) {
		for (j = 0; j < m; j++) {
			cin >> num;
			temp1.push_back(num);

			if (status == 0) {
				temp2.push_back(0);
			}
		}

		table.push_back(temp1);
		temp1.clear();

		c1.push_back(temp2);
		c2.push_back(temp2);

		status = 1;
		
	}

	for (i = 1; i < m; i++) {
		c1[0][i] = c1[0][i - 1] + table[0][i];
		c2[0][i] = -1;
	}

	for (i = 1; i < n; i++) {
		for (j = 0; j < m; j++) {
			if (i == 1) {
				if (j == 0) {
					c1[i][j] = c1[i - 1][j] + table[i][j];
					c2[i][m - j - 1] = c1[i - 1][m - j - 1] + table[i][m - j - 1];
				}

				else {
					c1[i][j] = min(c1[i - 1][j], c1[i][j - 1]) + table[i][j];
					c2[i][m - j - 1] = min(c1[i - 1][m - j - 1], c2[i][m - j]) + table[i][m - j - 1];
				}
			}
				
			else {
				if (j == 0) {
					c1[i][j] = min(c1[i - 1][j], c2[i - 1][j]) + table[i][j];
					c2[i][m - j - 1] = min(c1[i - 1][m - j - 1], c2[i - 1][m - j - 1]) + table[i][m - j - 1];
				}
				else {
					c1[i][j] = min({ c1[i - 1][j], c2[i - 1][j], c1[i][j - 1] }) + table[i][j];
					c2[i][m - j - 1] = min({ c1[i - 1][m - j - 1], c2[i - 1][m - j - 1], c2[i][m - j] }) + table[i][m - j - 1];
				}
			}
		}
	}

	cout << (c1[n - 1][m - 1] + table[0][0]) << endl;

	return 0;
}