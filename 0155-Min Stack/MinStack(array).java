class MinStack {
    int [] array =new int [9999];
    int stackLength = 0;
    /** initialize your data structure here. */
    public MinStack() {
        
    }
    
    public void push(int x) {
        array[stackLength++] = x;
    }
    
    public void pop() {
        array[stackLength-1] = 0;
        stackLength--;
    }
    
    public int top() {
        return array[stackLength-1];
    }
    
    public int getMin() {
        int min = array[0];
        for(int i = 0;i<stackLength;i++){
            if(array[i]<min)  min = array[i];
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
