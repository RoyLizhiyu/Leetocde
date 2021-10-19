class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        if (numRows == 1){
            result.add(new ArrayList<>());
            result.get(0).add(1);
            return result;
        }
        
        List<List<Integer>> prev = generate(numRows-1);
        result.addAll(prev);
        List<Integer> last = result.get(result.size()-1);
        int i = 0;
        int j = 0;
        List<Integer> newL = new ArrayList<Integer> ();
        while (i <= last.size()){
            if (i == 0 ){
                newL.add(last.get(i));
            }
            else if (i == last.size()){
                newL.add(last.get(i-1));
            }
            
            else{
                newL.add(last.get(i)+last.get(j));
                j++;
            }
            i++;
               
        }
        result.add(newL);
        return result;
    }
}
