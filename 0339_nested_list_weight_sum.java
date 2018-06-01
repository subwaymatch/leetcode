/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * public interface NestedInteger {
 *
 *     // @return true if this NestedInteger holds a single integer, rather than a nested list.
 *     public boolean isInteger();
 *
 *     // @return the single integer that this NestedInteger holds, if it holds a single integer
 *     // Return null if this NestedInteger holds a nested list
 *     public Integer getInteger();
 *
 *     // @return the nested list that this NestedInteger holds, if it holds a nested list
 *     // Return null if this NestedInteger holds a single integer
 *     public List<NestedInteger> getList();
 * }
 */
public class Solution {
    public int add(List<NestedInteger> nestedList, int depth) {
        int sum = 0; 
        
        for (NestedInteger nestedInt : nestedList) {
            if (nestedInt.isInteger()) sum += (nestedInt.getInteger() * depth); 
            else sum += add(nestedInt.getList(), depth + 1); 
        }
        
        return sum; 
    }
    
    public int depthSum(List<NestedInteger> nestedList) {
        return add(nestedList, 1); 
    }
}
