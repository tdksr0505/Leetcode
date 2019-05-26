class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> list = new ArrayList<>();
        List<Integer> preList = new ArrayList<>();
        List<Integer> subList;
        
        for(int layer=0;layer<numRows;layer++){
        	subList = new ArrayList<>();
            if(layer!=0) {
                subList.add(1);   
                preList = list.get(layer-1);
                for(int i=0;i<preList.size()-1;i++){
                    subList.add(preList.get(i) + preList.get(i+1));
                }
            }
            subList.add(1);
            list.add(subList);
        }
        return list;
    }
}