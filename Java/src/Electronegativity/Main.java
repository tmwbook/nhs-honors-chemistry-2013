package Electronegativity;

/**
 * Created by Thomas on 2/6/14.
 */
public class Main {

    private int electroNegMath(double a, double b){

        a += .5;
        b += .5;
        this.a = int a;
        this.b = int b;
        if (a > b){
            return a - b;
        }
        else {
            return b - a;
        }

    }

    public String electroNegTypeOfBond(String atomA, String atomB){
        atomAData = Table.Table.loc[atomA];
        atomBData = Table.Table.loc[atomB];
        if (electroNegMath(atomA, atomB) >= 1.7){
            return "Ionic Compound";
        }
        else {
            if (electroNegMath(atomA,atomB) >= .3){
                return "Non - Polar Covalent";
            }
            else{
                return "Polar Covalent";
            }
        }
    }
    private boolean electroNegCheckIfPossible(String atomA, String atomB){
        if (atomA == )
    }

}
