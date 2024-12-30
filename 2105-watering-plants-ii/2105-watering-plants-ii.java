class Solution {
    public int minimumRefill(int[] plants, int capacityA, int capacityB) {
    /* 
        plants = [2,2,3,3], capacityA = 5, capacityB = 5 
                  a     b 
        a<b
        if(capacityA  or capacityB ==0 ) -> reset it to "5" -> cnt=cnt+1;
            1. a=0, b=plants.length-1 = 3 -> plants[0] = 2 , plants[3]= 3 
            capacityA = 5-2 =3 > 0, capacityB = 5-3 =2 >0 a++,b--

            2. a=1, b=plants.length-1 = 2 -> plants[1] = 2 , plants[2]= 3 
            capacityA = 3-2 =1 > 0, capacityB = 3-3 =0 >0 a++,b--
        a==b 
           if(capacityA>)
           capacityA-plant[i]
    */
    int a= 0; int b= plants.length-1; int cnt =0; int remainingA = capacityA; int remainingB  = capacityB;

        while (a <= b) {
            if (a == b) {
                // If both are at the same plant
                if (remainingA >= plants[a] || remainingB >= plants[a]) {
                    // Only one needs to water the plant
                    if (remainingA >= remainingB) {
                        remainingA -= plants[a];
                    } else {
                        remainingB -= plants[a];
                    }
                } else {
                    // If neither has enough capacity, refill once
                    cnt++;
                }
                break;
            }

            // Alice waters her current plant
            if (remainingA >= plants[a]) {
                remainingA -= plants[a];
            } else {
                // Refill and water
                cnt++;
                remainingA = capacityA - plants[a];
            }

            // Bob waters his current plant
            if (remainingB >= plants[b]) {
                remainingB -= plants[b];
            } else {
                // Refill and water
                cnt++;
                remainingB = capacityB - plants[b];
            }

            a++;
            b--;
        }

        return cnt;
    }
}

    