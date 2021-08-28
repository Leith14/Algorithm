public class _0004_Median_of_Two_Sorted_Arrays {
    public double findMedianSortedArrays(int[] inuput1, int[] inuput2) {
        // if input1 length is greater than switch them so that input1 is smaller than input2.
        if (inuput1.length > inuput2.length) {
            return findMedianSortedArrays(inuput2, inuput1);
        }
        int x = inuput1.length;
        int y = inuput2.length;

        int low = 0;
        int high = x;
        while (low <= high) {
            int partitionX = (low + high) / 2;
            int partitionY = (x + y + 1) / 2 - partitionX;

            // if partitionX is 0 it means nothing is there on left side. Use -INF for maxLeftX
            // if partitionX is length of input then there is nothing on right side. Use +INF for maxRightX
            int maxLeftX = (partitionX == 0) ? Integer.MIN_VALUE : inuput1[partitionX - 1];
            int minRightX = (partitionX == x) ? Integer.MAX_VALUE : inuput1[partitionX];

            int maxLeftY = (partitionY == 0) ? Integer.MIN_VALUE : inuput2[partitionY - 1];
            int minRightY = (partitionY == y) ? Integer.MAX_VALUE : inuput2[partitionY];

            if (maxLeftX <= minRightY && maxLeftY <= minRightX) {
                if ((x + y) % 2 == 0) {
                    return ((double) Math.max(maxLeftX, maxLeftY) + Math.min(minRightX, minRightY)) / 2;
                } else {
                    return Math.max(maxLeftX, maxLeftY);
                }
            } else if (maxLeftX > minRightY) high = partitionX - 1; // we are too far on right side for partitionX.Go on left side
            else low = partitionX + 1;// we are too far on left side for partitionX. Go on right side.
        }

        // Only we can come here is if input arrays were not sorted. Throw in that scenario.
        throw new IllegalArgumentException();
    }


}
