#include <iostream>
#include <vector>

// mine
// class Solution {
// public:
//     int removeElement(std::vector<int>& nums, int val) {
//         int count = 0;
//         for(int i = nums.size() - 1; i >= 0; i--){
//             if(nums[i] == val){
//                 nums.erase(nums.begin() + i);
//             }
//             else{
//                 count++;
//             }
//         }
//         return count;
//     }
// };

// 0 ms leet code
class Solution {
public:
    int removeElement(std::vector<int>& nums, int val) {
        int index = 0;
        for(int i = 0; i< nums.size(); i++){
            if(nums[i] != val){
                nums[index] = nums[i];
                index++;
            }
        }
        return index;
    }
};

int main() {
    Solution s;
    std::vector<int> nums = {3, 2, 2, 3};
    int val = 3;
    int result = s.removeElement(nums, val);
    std::cout << result << std::endl;
    for(int j = 0; j < nums.size(); j++){
        std::cout << nums[j];
    }
    return 0;
}