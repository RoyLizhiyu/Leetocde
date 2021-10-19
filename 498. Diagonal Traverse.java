class Solution {
    public int[] findDiagonalOrder(int[][] mat) {
        int m = mat.length;
        int n = mat[0].length;
        int[] result = new int[m*n];
        int k = 0;
        ArrayList<Integer> intermediate = new ArrayList<Integer>();
        for (int i = 0; i < m + n - 1; i++){
            int x;
            int y;
            intermediate.clear();
            if (i < n){
                x = 0;
                y = i;
                
            }
            else{
                x = i - n + 1;
                y = n - 1;
            }
            
            while (x< m && y>-1) {
                intermediate.add(mat[x][y]);
                x++;
                y--;
            }
            if (i % 2 == 0) {
                Collections.reverse(intermediate);
                
            }
            for (int t = 0; t < intermediate.size(); t++) {
                result[k++] = intermediate.get(t);
            }
            
            
        }
        return result;
        
    }
}
