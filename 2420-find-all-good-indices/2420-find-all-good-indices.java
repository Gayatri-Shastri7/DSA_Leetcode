class Solution {
    public List<Integer> goodIndices(int[] nums, int k) {
        List<Integer> nm=new ArrayList<>();
        int p=nums.length;
        int a[]=new int[p];
        a[0]=1;
        for(int i=1;i<p;i++)
        {
            if(nums[i]<=nums[i-1])
            {
                a[i]=a[i-1]+1;
            }
            else
            {
                a[i]=1;
            }
        }
        int b[]=new int[p];
        b[p-1]=1;
        for(int i=p-2;i>=0;i--)
        {
            if(nums[i+1]>=nums[i])
            {
                b[i]=b[i+1]+1;
            }
            else
            {
                b[i]=1;;
            }
        }
        for(int i=k;i<p-k;i++)
        {
            if(k<=a[i-1]&&k<=b[i+1])
                nm.add(i);
        }
        return nm;
    }
}