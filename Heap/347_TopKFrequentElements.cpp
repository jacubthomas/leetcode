#include <map>
#include <utility>
#include <vector>

class Solution {
public:
  vector<int> topKFrequent(vector<int>& nums, int k) {
      //! Sum num element counts in a map
      map<int, int> mapNumCounts;
      for (int num: nums)
          mapNumCounts[num]++;
  
      //! Comparator, comparing second value with greater - min heap
      auto comp = [](const pair<int,int>& a, const pair<int,int>& b) {
          return a.second > b.second;
      };
      //! Establish a min-heap storing tuple<int,int>, comparing by second value
      priority_queue<pair<int,int>, vector<pair<int,int>>, decltype(comp)> pq(comp);
  
      //! Push k-first elements onto min heap
      //! Push remaining elements onto heap if value is greater than heap.top()
      int i = 0;
      for (auto it = mapNumCounts.begin(); it != mapNumCounts.end(); ++it, i++) {
          if (i < k)
              pq.push(make_pair(it->first, it->second));
          else if (it->second > pq.top().second) {
              pq.pop();
              pq.push(make_pair(it->first, it->second));
          }
      }
      
      //! Unload heap onto our solution output
      vector<int> vecResult;
      while (pq.empty() == false) {
          vecResult.push_back(pq.top().first);
          pq.pop();
      }
      
      return vecResult;
  }
};
