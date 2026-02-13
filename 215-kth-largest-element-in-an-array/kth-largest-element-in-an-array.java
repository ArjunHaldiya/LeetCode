import java.util.*;


class Solution {
    public int findKthLargest(int[] nums, int k) {
       PriorityQueue<Integer> heap = new PriorityQueue<>(Collections.reverseOrder());
       for(int num : nums){
        heap.add(num);
       }

       int result = 0;

       for(int i = 0; i < k; i++){
        result = heap.poll();
       }

       return result;
    }
}