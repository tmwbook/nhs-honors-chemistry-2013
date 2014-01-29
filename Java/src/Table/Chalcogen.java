package Table;

/**
 * Created by Thomas on 1/29/14.
 */
public class Chalcogen {

    public int atomicNumber;
    public double atomicMass;

    public Chalcogen(int aN, double aM){
        int atomicNumber = aN;
        double atomicMass = aM;
    }

    Chalcogen oxygen = new Chalcogen(8, 15.9994);
    Chalcogen sulfur = new Chalcogen(16, 31.06);
    Chalcogen selenium = new Chalcogen(34, 78.96);
    Chalcogen tellurium = new Chalcogen(52, 127.6);
    Chalcogen poloium = new Chalcogen(84, 127.6);

}