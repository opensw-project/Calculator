public class Div
{
    private int a;
    private int b;
    /**
     * Div 클래스의 객체 생성자
     */
    public Div(int a, int b)
    {

        this.a = a;
        this.b = b;
    }
    public double calculate(){  //나누가는 실수형으로 연산함
        return (double)this.a / this.b;
    }
    public void sefValue(int a, int b){
        this.a = a;
        this.b = b;
    }
}
