package org.example;


//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static int[] main(int[] arr) {
        //TIP Press <shortcut actionId="ShowIntentionActions"/> with your caret at the highlighted text
        // to see how IntelliJ IDEA suggests fixing it.
        System.out.println("Heap Sort");

        heapSort(arr);

        return arr;
    }

    public static void heapSort(int[] arr) {
        int length_arr = arr.length;

        for (int i = (length_arr / 2) - 1; i >= 0; i--) {
            heapfy(arr, i, length_arr);
        }

        for (int i = length_arr-1; i >= 0; i--) {
            int temp = arr[i];
            arr[i] = arr[0];
            arr[0] = temp;

            heapfy(arr, 0, i);
        }
    }

    public static void heapfy(int[] arr, int i, int length) {
        int l = i * 2 + 1;
        int r = i * 2 + 2;
        int largest = i;

        if (l < length && arr[l] > arr[largest]) {
            largest = l;
        }
        if (r < length && arr[r] > arr[largest]) {
            largest = r;
        }

        if (i != largest) {
            int temp = arr[i];
            arr[i] = arr[largest];
            arr[largest] = temp;

            heapfy(arr, largest, length);
        }
    }
}