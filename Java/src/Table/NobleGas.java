package Table;

/**
 * Created by Thomas on 1/31/14.
 */
public class NobleGas extends NonMetal{

    int atomicNumber;
    double atomicMass;

    NobleGas(int aN, double aM){
        int atomicNumber = aN ;
        double atomicMass = aM;
    }

    NobleGas helium = new NobleGas(2, 4.0026);
    NobleGas neon = new NobleGas(10, 20.179);
    NobleGas argon = new NobleGas(18, 39.948);
    NobleGas krypton = new NobleGas(36, 83.8);
    NobleGas radon = new NobleGas(86, 222);

}
