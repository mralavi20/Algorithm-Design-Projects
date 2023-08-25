#include <iostream>
#include <vector>

using namespace std;

void merge (vector<int> &nums, vector<int> &result, int left, int right, int mid) {
    int n1 = mid - left + 1;
    int n2 = right - mid;
    int i = left;
    int j = mid + 1;
    vector<int> temp;


    while (i < mid + 1 && j < right + 1) {
        if (nums[i] > 2 * nums[j]) {
            result[0] = result[0] + n1 - i + left;
            j = j + 1;
        }
        else {
            i = i + 1;
        }
    }
    
    i = left;
    j = mid + 1;

    while (i < mid + 1 && j < right + 1) {
        if (nums[i] <= nums[j]) {
            temp.push_back (nums[i]);
            i = i + 1;
        }
        else {
            temp.push_back (nums[j]);
            j = j + 1;
        }
    }
    
    while (i < mid + 1) {
        temp.push_back (nums[i]);
        i = i + 1;
    }

    while (j < right + 1) {
        temp.push_back (nums[j]);
        j = j + 1;
    }

    for (i = left; i < right + 1; i++) {
        nums[i] = temp[i - left];
    }
}

void merge_sort (vector<int> &nums, vector<int> &result, int left, int right) {
    if (left < right) {
        int mid = (right + left) / 2;

        merge_sort (nums, result, left, mid);
        merge_sort (nums, result, mid + 1, right);
        merge (nums, result, left, right, mid);
    }
}
int main () {
    int n;
    int i;
    int num;
    vector<int> nums;
    vector<int> result;

    cin >> n;

    for (i = 0; i < n; i++) {
        cin >> num;
        nums.push_back (num);
    }

    result.push_back (0);
    
    merge_sort (nums, result, 0, n - 1);
    
    cout << result[0] << endl;

    return 0;
}