bool graph_valid_tree(int n, vector<vector<int>> edges) {
        if (n < 2) return true;

        //! Building an adjacency list
        map<int, vector<int>> adjacencyList;
        for (int i=0; i < n; i++)
            adjacencyList[i] = {};
        for (vector<int> edge: edges) {
            adjacencyList[edge[0]].push_back(edge[1]);
            adjacencyList[edge[1]].push_back(edge[0]);
        }

        //! DFS
        set<int> visited;
        bool cycleDetected = false;
        dfs(0,-1, adjacencyList, visited, cycleDetected);
        
        //! Valid trees mean all components are connected and no cycles exist
        return (!cycleDetected) && visited.size() == n;
    }

    void dfs(int currentNode, 
             int fromNode,
             map<int, 
             vector<int>>& adjacencyList, 
             set<int>& visited,
             bool& cycleDetected) {
        //! We should never revisit a node, given we don't call DFS on neighbors equal to fromNode
        if (visited.find(currentNode) != visited.end()) {
            cycleDetected = true;
            return;
        }
        //! Track that we have been here
        visited.insert(currentNode);

        //! Shouldn't run into segfault here... 
        //! given it's undirected graph and we built the list
        for (int neighbor: adjacencyList[currentNode]) {
            if (neighbor != fromNode) //! Make cycle detection easy, don't go back to where we came from
                dfs(neighbor, currentNode, adjacencyList, visited, cycleDetected);
        }
    }
