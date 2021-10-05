Leetcode prb https://leetcode.com/problems/binary-search/
Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.
  
class Solution {
  public:
    int search(vector<int>& nums, int target)
    {
      int n=nums.size();
      int s=0, e=n-1;
      while(s<=e)
      {
        int m=(s+e)/2;
        if(nums[m]==target)
          return m;
        if(nums[m]<target)
        {
          s = m+1;
        }
        else
        {
          e = m-1;
        }
      }
      return -1;
    }
};
