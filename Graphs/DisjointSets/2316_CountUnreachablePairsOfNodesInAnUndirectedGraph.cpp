class UnionFind {
    public:
        UnionFind(const int n, const vector<vector<int>> edges) {
            this->m_iNumNodes = n;

            //! Every node will initially be it's own root
            for (int i=0; i < n; i++)
                m_vecNodeToRoot.push_back(i);

            //! Now nodes will be connected under clusters identified by a root node
            for (vector<int> edge: edges)
                this->unionize(edge[0], edge[1]);
        }

        //! Find the root of a given node
        //! All connected components will share a common root node
        int find(const int iNode) {
            //! Root of a union of connected components is itself
            if (iNode == m_vecNodeToRoot[iNode])
                return iNode;
            //! Path compress - update node roots to point directly to root node
            m_vecNodeToRoot[iNode] = find(m_vecNodeToRoot[iNode]);
            return m_vecNodeToRoot[iNode];
        }
        
        //! Connected components share a common root
        void unionize(const int iNodeLeft, const int iNodeRight) {
            const int iRootLeft = find(iNodeLeft);
            const int iRootRight = find(iNodeRight);
            if (iRootLeft != iRootRight) //! Simple union, we can also union by rank for performance
                m_vecNodeToRoot[iRootRight] = iRootLeft;
        }

        bool connected (const int iNodeLeft, const int iNodeRight) {
            const int iRootLeft = find(iNodeLeft);
            const int iRootRight = find(iNodeRight);
            return iRootLeft == iRootRight;
        }
        

        //! Generate a list summing connected nodes attached to each root
        vector<int> gatherSetNodeCounts() {
            map<int,int> mapRootToNodeCounts;
            for (int i=0; i < m_iNumNodes; i++) {
                const int iRoot = find(m_vecNodeToRoot[i]);
                mapRootToNodeCounts[iRoot]++;
            }

            vector<int> vecRootNodeCounts;
            for (auto it = mapRootToNodeCounts.begin(); it != mapRootToNodeCounts.end(); ++it)
                vecRootNodeCounts.push_back(it->second);
            
            return vecRootNodeCounts;
        }
    private:
        vector<int> m_vecNodeToRoot;
        int m_iNumNodes;
};

class Solution {
public:
    long long countPairs(int n, vector<vector<int>>& edges) {
        //! Leverage Union-Find to discern which nodes are connected
        UnionFind uf(n, edges);

        //! Let's gather all the disjoint set roots, along with set size
       vector<int> vecRootNodeCounts = uf.gatherSetNodeCounts();
    
        /*! 
         * Given each cluster of nodes, we ask ourselves
         * How many nodes does my cluster contain
         * How many nodes does it not - this is how many nodes it can't reach
         * So a cluster's_node_count * all_other_nodes
         * And we must sum these products for every cluster
         */
        long long llSumMissingConnections = 0;
        long long llRemainingNodes = n;
        for (int i=0; i<vecRootNodeCounts.size()-1; i++) {
            const long long llNodesInCluster = vecRootNodeCounts[i];
            llSumMissingConnections += llNodesInCluster * (llRemainingNodes - llNodesInCluster);
            //! We've accounted for these nodes, remove from remaining calculations
            llRemainingNodes -= llNodesInCluster;
        }
        return llSumMissingConnections;
    }
};
