package apt;

import java.io.ByteArrayInputStream;
import java.io.UnsupportedEncodingException;

public class Main {

    public static void main(String[] args) {
        String str = "I know the Decorator Pattern therefore I RULE!";
        ByteArrayInputStream inputStream;
        try {
            inputStream = new ByteArrayInputStream(str.getBytes("UTF-8"));
            System.out.println(new LowerCaseStream(inputStream).toLowerCase());
        } catch (UnsupportedEncodingException e) {
            e.printStackTrace();
        }
    }
}


