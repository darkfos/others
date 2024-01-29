package example;

import org.example.Main;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

public class MainTest {

    @Test
    void HeapSort() {
        // Создаём экземпляр класса Main

        Main maintest = new Main();

        //Тестовые массивы для сортировки
        int[] test_arr = {90, 9, 2, 3, 4, 12, 44};
        int[] test_arr_2 = {2394, 12392, 0, 213};
        int[] test_arr_3 = {904, 93, 22, 11, 323, 54355, 3};

        int[] result1 = maintest.main(test_arr);
        int[] result2 = maintest.main(test_arr_2);
        int[] result3 = maintest.main(test_arr_3);

        Assertions.assertArrayEquals(new int[]{2, 3, 4, 9, 12, 44, 90}, result1);
        Assertions.assertArrayEquals(new int[]{0, 213, 2394, 12392}, result2);
        Assertions.assertArrayEquals(new int[]{3, 11, 22, 93, 323, 904, 54355}, result3);
    }

    @Test
    void sortZero() {
        Main maintest = new Main();

        int[] number = {0};
        Assertions.assertArrayEquals(number, maintest.main(number));
    }
}
