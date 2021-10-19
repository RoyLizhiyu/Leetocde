class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int up = 0;
        int left = 0;
        int right = matrix[0].length-1;
        int down = matrix.length-1;
        ArrayList<Integer> result = new ArrayList<Integer>();
        
        while (result.size() != matrix[0].length * matrix.length) {
            
            // go to right
            for (int l = left; l< right+1; l++){
                result.add(matrix[up][l]);
            }
            
            // go to down
            
            for (int u = up+1; u < down+1; u++){
                result.add(matrix[u][right]);
            }
            
            if (down != up){
                for (int r = right-1; r>left-1; r--){
                    result.add(matrix[down][r]);
                }
            }
            
            if (left != right){
                
                for (int d = down-1; d > up; d--){
                    result.add(matrix[d][left]);
                }
            }
            up++;
            down--;
            left++;
            right--;
            
            
        }
        return result;
        
    }
}
