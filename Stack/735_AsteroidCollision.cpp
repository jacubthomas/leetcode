class Solution {
public:
    //! Kind of like merge intervals, we add these asteroids into new vec one-by-one
    //! Then we assess
    vector<int> asteroidCollision(vector<int>& asteroids) {
        vector<int> result = {asteroids[0]};

        for (int i=1; i < asteroids.size(); i++) {
            int currAsteroid = asteroids[i];
            if (result.size() == 0) { //! No Collision
                result.push_back(currAsteroid);
                continue;
            }
            //! Get prev asteroid
            int prevAsteroid = result.back();
            if (prevAsteroid < 0) { //! No Collision
                result.push_back(currAsteroid);
                continue;
            } else if (prevAsteroid > 0 && currAsteroid < 0) { //! Collision: 2 cases
                //! Case 1: equal, neither exist in final result
                if (prevAsteroid == currAsteroid) {
                    result.pop_back();
                    continue;
                //! Case 2: Inequal we set off (a possible chain) collision(s)
                } else {

                    if (prevAsteroid > abs(currAsteroid)) continue;
                    while (prevAsteroid > 0 && currAsteroid < 0 && abs(currAsteroid) > prevAsteroid) {
                        if (result.size() > 0) {
                            result.pop_back();
                            if (result.size() > 0)
                                prevAsteroid = result.back();
                        }
                        else  {
                            prevAsteroid = 0;
                            break;
                        }
                    }
                    if (prevAsteroid == 0) {
                        result.push_back(currAsteroid);
                        continue;
                    } 
                    else if (prevAsteroid > 0 && currAsteroid < 0 && abs(currAsteroid) < prevAsteroid)
                        continue;
                    else if (prevAsteroid > 0 && currAsteroid < 0 && abs(currAsteroid) == prevAsteroid)
                        result.pop_back();
                    else result.push_back(currAsteroid);
                }
            } else //! No Collision
                result.push_back(currAsteroid);
        }

        return result;
    }
};



/*
//! Print
        while (!pq.empty()) {
            pair<int,int> p = pq.top();
            pq.pop();
            cout << "[" << p.first << "," << p.second << "], ";
        }
*/
