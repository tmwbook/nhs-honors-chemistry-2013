package Table;

/**
 * Created by Thomas on 1/31/14.
 */
public class Pnictogen extends NonMetal {

    public int atomicNumber;
    public double atomicMass;

    public Pnictogen(int aN, double aM){
        int atomicNumber = aN;
        double atomicMass = aM;
    }

    Pnictogen nitrogen = new Pnictogen(7, 14.0067);
    Pnictogen phosphorus = new Pnictogen(15, 30.97376);
    Pnictogen arsenic = new Pnictogen(33, 749216);
    Pnictogen antimony = new Pnictogen(51, 121.75);
    Pnictogen bismuth = new Pnictogen(83, 209);
}