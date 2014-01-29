package Table;

/**
 * Created by Thomas on 1/28/14.
 */
public class Halogen extends NonMetal {

    public int atomicNumber;
    public double atomicMass;

    public Halogen(int aN, double aM){
        int atomicNumber = aN;
        double atomicMass = aM;
    }

    Halogen fluorine = new Halogen(9, 18.998403);
    Halogen chlorine = new Halogen(17, 35.453);
    Halogen bromine = new Halogen(35,79.904);
    Halogen iodine = new Halogen(53, 126.905);
    Halogen astatine = new Halogen(85, 210);
}