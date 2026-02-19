#include <iostream>
#include <queue>
#include <vector>

using namespace std;

class Solution {
public:
    vector<int> getOrder(vector<vector<int>>& tasks) {
        vector<int> order;
        
        //! We need to append the original index to each task before we arrange them
        //! So we return the correct index-based ordering 
        for (int i=0; i < tasks.size(); i++) {
            tasks[i].push_back(i);
        }

        //! First we'll sort tasks by starting time - tiebreak on smaller processing time
        std::sort(tasks.begin(), tasks.end(), [](const vector<int>& a, const vector<int>& b){
            if (a[0] < b[0]) return true;
            else if(a[0] > b[0]) return false; 
            else return a[1] < b[1];
        });

        //! We'll also need a priority queue with a custom comparator
        auto comp = [](const vector<int>&a, const vector<int>&b) {
            //! Prioritize minimum processing time
            if (a[1] < b[1]) return false;
            else if (a[1] > b[1]) return true;
            //! Then tiebreak on minimum index
            else return a[2] > b[2];
        };
        priority_queue<vector<int>, vector<vector<int>>, decltype(comp)> pqAvailableTasks(comp);

        //! Start order with first sorted task
        int64_t currentTaskEnd = tasks[0][0] + tasks[0][1];
        int currentTaskIndex = tasks[0][2];

        int tasksEnqueued = 1;
        int tasksCompleted = 0;
        int64_t timeIndex = 1;
        while (tasksCompleted < tasks.size()) {
            //! Continously add all newly available tasks to the pq
            while (tasksEnqueued < tasks.size() && 
                   tasks[tasksEnqueued][0] <= timeIndex) {
                pqAvailableTasks.push(tasks[tasksEnqueued++]);
            }

            //! Check if current task is completed
            if (currentTaskEnd == timeIndex) {
                tasksCompleted++;
                order.push_back(currentTaskIndex);
                if (!pqAvailableTasks.empty()) {
                    vector<int> nextTask = pqAvailableTasks.top();
                    pqAvailableTasks.pop();
                    currentTaskIndex = nextTask[2];
                    currentTaskEnd = nextTask[1] + timeIndex;
                }
            }
            //! We are beyond the last completed task but have not queued another
            else if (currentTaskEnd < timeIndex){
                //! Pull of the queue if it has any
                if (!pqAvailableTasks.empty()) {
                    vector<int> nextTask = pqAvailableTasks.top();
                    pqAvailableTasks.pop();
                    currentTaskIndex = nextTask[2];
                    currentTaskEnd = nextTask[1] + timeIndex;
                }
                //! Jump ahead to the next enqueue time if our queue is empty
                else if (pqAvailableTasks.empty() && tasksEnqueued < tasks.size())
                    timeIndex = tasks[tasksEnqueued][0]-1;
            }

            timeIndex = max(timeIndex + 1, currentTaskEnd);
        }

        return order;
    }
};
