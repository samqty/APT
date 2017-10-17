package apt;

import java.io.InputStream;
import java.util.Scanner;

public class LowerCaseStream {
    private InputStream _inputStream;
    public LowerCaseStream(InputStream inputStream)
    {
        _inputStream = inputStream;
    }

    public String toLowerCase()
    {
        Scanner s = new Scanner(_inputStream).useDelimiter("\\A");
        String result = s.hasNext() ? s.next() : "";

        return result.toLowerCase();
    }
}
