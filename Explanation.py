# -*- coding: utf-8 -*-
"""
This graph is limited to 3 levels. 
With 2 chosen variables CLUSTER2, CLUSTER1, and target as SCH_YR this graph can be interpret as:
Overall in test set, there are 2544 positive, 1358 negative.
For CLUSTER1 less than 294, there are 2324 positive, 1350 negative.
For CLUSTER1 less than 103.5, there are 2 positive, 24 negative. 
For CLUSTER1 more than 103.5 and less than 294, there are 2322 positive, 1326 negative. 
...
in third level, I end up with 8 node, where there is some node with high probability of positive, and with big enough size (>30) such as:
leaf 3: CLUSTER1 less than 107 and larger than 103.5
leaf 5: CLUSTER2 less than 449, CLUSTER1 less than 420.5
leaf 7: CLUSTER2 larger than 449, CLUSTER1 less than 422

"""
