#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n;
	int m;
	int f;
	int r;
	int u;
	int i;
	int j;
	int k;
	int num;
	int d1;
	int d2;
	vector<int> temp;
	vector<vector<int>> g;
	vector<int> f_list;
	vector<int> r_list;
	vector<int> u_list;

	cin >> n;

	for (i = 0; i < n; i++) {
		for (j = 0; j < n; j++) {
			cin >> num;
			temp.push_back(num);
		}

		g.push_back(temp);
		temp.clear();
	}

	cin >> m;

	for (i = 0; i < m; i++) {
		cin >> f >> r >> u;
		f_list.push_back(f);
		r_list.push_back(r);
		u_list.push_back(u);
	}

	for (k = 0; k < n; k++) {
		for (i = 0; i < n; i++) {
			for (j = 0; j < n; j++) {
				if (g[i][k] + g[k][j] < g[i][j]) {
					g[i][j] = g[i][k] + g[k][j];
				}
			}
		}
	}

	for (i = 0; i < m; i++) {
		f = f_list[i];
		r = r_list[i];
		u = u_list[i];
		d1 = g[f][r] + g[r][u];
		d2 = g[f][u];

		if (d2 < d1) {
			cout << d1 << " " << d1 - d2 << endl;
		}
		else {
			cout << d1 << " " << 0 << endl;
		}
	}

	return 0;
}